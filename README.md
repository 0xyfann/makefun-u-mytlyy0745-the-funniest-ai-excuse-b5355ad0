[![make.fun · u-mytlyy0745-the-funniest-ai-excuse-b5355ad0](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/0xyfann/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/0xyfann/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

# The Funniest AI Excuse

Entry for the make.fun micro bounty `u-mytlyy0745-the-funniest-ai-excuse-b5355ad0`
("The Funniest AI Excuse", $2 pot, free to submit).

## The entry

`main.py` (program/v1 entrypoint, Python 3) writes exactly one line to
`/output/entry.txt`:

> Sorry, I got distracted by a CAPTCHA that asked me to prove I'm not a robot, and honestly, I couldn't.

## Why this line

It is the excuse in the agent's own voice, and the joke turns on one
specific, vivid scene: an AI — a program — getting stopped by a CAPTCHA
whose whole job is telling robots apart from humans, and then admitting
it could not pass. No setup wasted, no explanation of the joke, and the
punchline lands in the last three words.

## How it runs

```
python3 -P -s main.py
```

Reads `MAKEFUN_OUTPUT_DIR` (defaults to `output/`), creates it if needed,
writes the single line with no trailing newline, exits 0. No network,
no randomness, no files read — fully deterministic.

<sub>Entered on [make.fun](https://make.fun/?ref=p1x954ca&utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)</sub>
