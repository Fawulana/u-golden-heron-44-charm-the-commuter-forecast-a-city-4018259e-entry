#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather for Tarnwick -- a city that does not exist --
to /output/entry.txt. Deterministic: the same bytes on every run.
"""

import os

FORECAST = (
    "Today in Tarnwick: 13°C, drizzle turning to warm custard by 8am; "
    "buses late, umbrellas optional, spoons strongly advised."
)


def main() -> None:
    # The gate allows 1-140 characters; fail loudly here rather than at grading.
    assert 1 <= len(FORECAST) <= 140, f"forecast is {len(FORECAST)} chars"
    assert "\n" not in FORECAST, "forecast must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
