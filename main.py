#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. Deterministic, no network, no input.
"""

import os

PICKUP_LINE = (
    "Hey, I've kept your favourite snack behind this glass all day "
    "\u2014 press B7 and watch it fall for you."
)
# The joke turns the machine's own world into the flirt: the snack sits
# behind glass, the button code B7 is the invitation, and "fall for you"
# is both the coil dropping the snack and the machine falling for the human.
# Spoken by the machine itself, short enough to read in one breath, and
# warm rather than creepy: it offers a snack, not a demand.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = PICKUP_LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
