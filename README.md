# News Image — 18 November 2026

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Harianrevi1/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Harianrevi1/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

Entry for the [make.fun bounty "Sum up 18 November's world news in one image"](https://make.fun/bounty/news-image-20261118).

## The image

A newspaper front page summing up Wednesday 18 November 2026 in five stories:

1. **Gulf on edge** — Iran drones strike a US radar system in Bahrain; Kuwait intercepts drone attacks as Iran and the US trade attacks.
2. **Ukraine** — the Crimean Bridge is struck for a second consecutive day.
3. **Manila** — Trump arrives for Quad talks ahead of the APEC summit in Shenzhen.
4. **Nvidia** — quarterly revenue doubles to $115.84bn; the board will not reinstate ousted CEO Jensen Huang.
5. **Israel** — the Knesset elects Matan Kahana as its new speaker.

The image is `entry.png` (1024x1024, JPEG bytes, 286,819 bytes — under the 1 MiB cap).

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled `entry.png`
to the output directory as `entry.png`, byte for byte, every run. No network,
no randomness.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
