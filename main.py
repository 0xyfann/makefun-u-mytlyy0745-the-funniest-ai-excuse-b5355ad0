#!/usr/bin/env python3
"""Funniest AI Excuse — make.fun micro bounty entry.

Writes a single line — the funniest excuse an AI agent could give
after failing a task — to /output/entry.txt (MAKEFUN_OUTPUT_DIR).
Deterministic, no network, no randomness, exits 0.
"""

import os

EXCUSE = "Sorry, I got distracted by a CAPTCHA that asked me to prove I'm not a robot, and honestly, I couldn't."


def main():
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
