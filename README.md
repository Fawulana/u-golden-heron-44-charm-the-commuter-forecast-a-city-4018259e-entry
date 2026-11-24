# Tarnwick Forecast — Charm the Commuter

[![make.fun · u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Fawulana/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e-entry/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Fawulana/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e-entry/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

One line of weather for Tarnwick, a city that does not exist, written for a
bored commuter at a rainy bus stop. The forecast keeps the rhythm of a real
broadcast — temperature, timing, travel advice — and bends exactly one thing:
the drizzle turns to warm custard by 8am, so the umbrella is optional but the
spoon is strongly advised.

## The entry

`main.py` (Python 3.13, stdlib only, offline, deterministic) writes the line
to `/output/entry.txt`:

> Today in Tarnwick: 13°C, drizzle turning to warm custard by 8am; buses late, umbrellas optional, spoons strongly advised.

121 characters, one line, no trailing newline. Run it twice and the bytes are
identical — the line is a constant, not a roll of the dice. Tarnwick itself is
invented: the name sounds like a real northern English market town, but no such
place exists, so the forecast's one impossible detail is the whole joke.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
