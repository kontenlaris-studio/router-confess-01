#!/usr/bin/env python3
"""The Router Confesses — make.fun one-liner entry.

A home Wi-Fi router excuses itself for dying at the exact climax of a
movie. The line is the whole entry: it prints to stdout and is written
to /output/entry.txt so the kit's run-check can verify it.
"""

import os

# The line (132 characters, cap 200). The router narrates its own death:
# the movie froze because it did — nine seconds of red light, darkness,
# and then the human's scream reaching it through the wall.
LINE = (
    "The movie froze at the worst line because I did \u2014 9 seconds of "
    "red light, then darkness, then your scream found me through the wall."
)


def main() -> None:
    assert len(LINE) <= 200, "entry exceeds the 200-character cap"
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
