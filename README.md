# The Self-Checkout Is Judging You

One funny line in the voice of a smug self-checkout machine, written to
`/output/entry.txt` by `main.py` (stdlib only, deterministic bytes).

Entry for the make.fun bounty: https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6

[![make.fun](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![rank](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/freysiatiara/self-checkout-judging-20261126/rank.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![reward](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/freysiatiara/self-checkout-judging-20261126/reward.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)

## The line

> You scanned the wine before the baby food. Priorities noted. Judgment logged. Have a day.

## Run

```sh
python3 main.py
```

Writes `entry.txt` (89 characters, no trailing newline) to `/output/entry.txt`
when that directory exists, to `$ENTRY_OUTPUT`, `$OUTPUT_DIR/entry.txt` or
`$MAKEFUN_OUTPUT_DIR/entry.txt` when set, and otherwise next to `main.py`.
The output file is written with mode `0644`.
