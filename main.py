#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence pitching a bizarre startup idea that sounds like a
joke yet holds together as a real business, to /output/entry.txt.

The pitch: retired librarians, leased out to shush noisy neighbours for a
monthly fee. The customers are light sleepers in apartments; the money is
the subscription; the turn is that anyone who has ever lain awake listening
to a neighbour's 2 a.m. karaoke knows exactly why they would pay.
"""

import os
from pathlib import Path

PITCH = (
    "We lease retired librarians to shush your noisy neighbours for a "
    "monthly fee, because light sleepers will pay anything for one quiet night."
)


def main() -> None:
    pitch = PITCH.strip()
    assert 1 <= len(pitch) <= 200, f"pitch must be 1-200 chars, got {len(pitch)}"
    assert pitch.count(".") == 1, "pitch must be exactly one sentence"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(pitch, encoding="utf-8")
    print(f"wrote {len(pitch)}-char pitch to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
