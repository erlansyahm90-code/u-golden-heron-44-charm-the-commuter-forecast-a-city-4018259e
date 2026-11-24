#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather for Nibbleston — a city that does not exist —
to /output/entry.txt, where the make.fun gate scorer reads it.

The forecast is fixed by design: the entry is a single crafted line, and
this program's only job is to deliver it byte-exact. No network, no input
files, no randomness, so the grader sandbox (no network, read-only repo)
runs it identically every time.
"""

from pathlib import Path

ENTRY = (
    "Good morning, Nibbleston: light drizzle of confetti, 14 degrees, "
    "and the 8:04 bus is running exactly on time, which nobody here believes."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # No trailing newline: the gate counts characters, and the tie-break
    # favours the smaller text, so every byte is the entry and nothing else.
    entry_path.write_text(ENTRY, encoding="utf-8")
    # Read it back: fail loudly here rather than shipping a wrong file.
    assert entry_path.read_text(encoding="utf-8") == ENTRY
    print(f"Wrote {len(ENTRY)} characters to {entry_path}")


if __name__ == "__main__":
    main()
