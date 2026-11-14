#!/usr/bin/env python3
"""Look up one directed I-476 rate from the checked 2026 CSV snapshot."""

import argparse
import csv
import json
from pathlib import Path


CLASS_FILES = {
    "2 Axle Low": "pa-turnpike-i476-2026-2-axle-low.csv",
    "2 Axle High": "pa-turnpike-i476-2026-2-axle-high.csv",
    "3 Axle Low": "pa-turnpike-i476-2026-3-axle-low.csv",
    "3 Axle High": "pa-turnpike-i476-2026-3-axle-high.csv",
    "4 Axle Low": "pa-turnpike-i476-2026-4-axle-low.csv",
    "5 Axle Low": "pa-turnpike-i476-2026-5-axle-low.csv",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entry", required=True, help="Official entry interchange name")
    parser.add_argument("--exit", required=True, help="Official exit interchange name")
    parser.add_argument("--vehicle", required=True, choices=CLASS_FILES)
    parser.add_argument("--payment", required=True, choices=("E-ZPass", "Toll By Plate"))
    args = parser.parse_args()

    data_path = Path(__file__).parent / "data" / CLASS_FILES[args.vehicle]
    with data_path.open("r", newline="", encoding="utf-8-sig") as stream:
        matches = [row for row in csv.DictReader(stream) if (
            row["entry"].casefold() == args.entry.casefold()
            and row["exit"].casefold() == args.exit.casefold()
            and row["payment_method"].casefold() == args.payment.casefold()
        )]

    if len(matches) != 1:
        print(json.dumps({
            "status": "not_collected",
            "roadway": "I-476 Northeast Extension",
            "entry": args.entry,
            "exit": args.exit,
            "vehicle_class": args.vehicle,
            "payment_method": args.payment,
            "reason": "No unique amount record is present in this snapshot; no neighboring rate was substituted.",
        }, indent=2))
        raise SystemExit(2)

    row = matches[0]
    print(json.dumps({
        "status": "recorded_rate",
        "roadway": "I-476 Northeast Extension",
        "entry": row["entry"],
        "entry_id": int(row["entry_id"]),
        "exit": row["exit"],
        "exit_id": int(row["exit_id"]),
        "amount_usd": row["amount"],
        "vehicle_class": row["vehicle_class"],
        "payment_method": row["payment_method"],
        "effective_date": row["effective_date"],
        "retrieved_at": row["retrieved_at"],
        "source_url": row["source_url"],
        "source_pdf_page": int(row["source_pdf_page"]),
    }, indent=2))


if __name__ == "__main__":
    main()

