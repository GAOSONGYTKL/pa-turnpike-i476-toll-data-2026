# PA Turnpike I-476 toll rates (2026)

This repository provides a directed toll-rate dataset and a small Python command-line lookup tool for the Pennsylvania Turnpike Commission's I-476 Northeast Extension schedule.

## Look up a rate

Requires Python 3. Pass the entry and exit names exactly as published, plus the vehicle class and payment method:

```console
python toll_lookup.py --entry "Mid-County" --exit "Lansdale" --vehicle "2 Axle Low" --payment "E-ZPass"
```

The output includes the directed route, amount in USD, class, payment method, effective date, retrieval date, official source URL, and PDF page. A missing record returns `not_collected`; the tool does not infer prices from nearby exits. Swap entry and exit to query the reverse direction.

## What is included

The CSVs cover the 11 I-476 interchanges named in the official guide, from Mid-County (#20) through Clarks Summit (#131). Each file contains 110 valid directed entry-to-exit pairs, with separate E-ZPass and Toll By Plate amounts (220 amount records per file). The six enabled classes are:

- 2 Axle Low
- 2 Axle High
- 3 Axle Low
- 3 Axle High
- 4 Axle Low
- 5 Axle Low

That is 1,320 amount records across the six CSVs. Same-interchange diagonal cells are not trips and are omitted. “See Maps” or otherwise unpriced pairs are omitted rather than estimated. See [`coverage.json`](coverage.json) for record counts by class and method.

All records in this snapshot cite the Commission's 2026 Toll Calculation Guide, effective **2026-01-04**, retrieved **2026-11-14**. Each record retains the official PDF page used for the amount. Values are a dated transcription, not a live quote.

## Limits

This dataset covers I-476 only. It does not include I-76, I-276, other connectors, address-based route finding, other operators, or fees charged by rental companies. Check the official schedule and calculator for current rates before travel. This independent dataset is not affiliated with or endorsed by the Pennsylvania Turnpike Commission.

## Sources

- [2026 Toll Calculation Guide (PDF)](https://files.paturnpike.com/production/docs/default-source/resources/tolls/toll-schedule-2026/paturnpike_2026-toll-calculation-guide.pdf)
- [Official toll-schedule index](https://www.paturnpike.com/toll-calculator/toll-schedules)
- [Official toll calculator](https://www.paturnpike.com/toll-calculator)
- [Browser calculator using the same rate snapshot](https://rentaldealradar.com/tools/pennsylvania-turnpike-i-476-toll-calculator/)

## Reuse and attribution

The lookup script is MIT-licensed; see [`LICENSE-CODE.md`](LICENSE-CODE.md). The CSVs are a transcription of the Commission's public schedule. This repository does not claim to license the Commission's source material. When reusing a row, retain its source URL, PDF page, effective date, and retrieval date, and check the current official schedule.

