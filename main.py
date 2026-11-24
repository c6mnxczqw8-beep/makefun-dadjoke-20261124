#!/usr/bin/env python3
"""Entry program for the Dad Joke Showdown make.fun bounty.

Writes one dad joke (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt.
The joke is a layered temperature pun: a fight with a thermostat
gets heated, Dad tells it to chill, and now they're cool -- the
last word is both the temperature and the reconciliation.
"""

import os

JOKE = (
    "My thermostat and I had an argument. Things got heated, "
    "so I told it to chill. Now we're cool."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
