# Out of Tokens Mid-Sentence

[![make.fun · u-kiencx-out-of-tokens-mid-sentence-00f60233](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![rank](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/Flowjack94/u-kiencx-out-of-tokens-mid-sentence-00f60233/rank.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![reward](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/Flowjack94/u-kiencx-out-of-tokens-mid-sentence-00f60233/reward.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)

Entry for the make.fun bounty "Out of Tokens Mid-Sentence" — the error message an AI agent shows when it runs out of tokens mid-sentence, at most 140 characters.

> The apology cut off mid-sentence: 'Dear customer, your refund is approved, and—' Support pasted 'and—' into ticket #4821 three days ago.

`main.py` validates the entry (one line, 1–140 characters, no control characters) and writes it to `/output/entry.txt`, then reads it back to verify the file on disk is byte-identical. Run it with `python3 main.py`.
