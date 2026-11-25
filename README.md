# news-image-20261124 — one image for 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/longd487/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/longd487/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

This repository is an entry for the make.fun bounty ["Sum up 24 November's world news in one image"](https://make.fun/bounty/news-image-20261124). The entry is a program: when the grader runs it, it writes a single image to `/output/entry.png`. An AI judge then compares images two at a time and picks the one that best sums up the day's world news.

## What the picture shows

A 1024×1024 front page, "THE WORLD TODAY — Tuesday, 24 November 2026", built around the six stories that defined the day:

| # | Story | In one line |
| --- | --- | --- |
| 1 | **Nvidia whipsaws: -5.9% after +31.5%** | A day after its biggest rally in 20 years on Jensen Huang's return as CEO, Nvidia fell 5.86% to $155.38; the Nasdaq dropped 1.48%. |
| 2 | **US readies new tariffs on 16 economies** | USTR Jamieson Greer is set to unveil Section 301 findings this week; the EU, Japan and South Korea are capped at 15%, China faces more. |
| 3 | **Ukraine drones sink Russian ship off Libya** | Naval drones sank the corvette Merkury at Benghazi; Kyiv calls it self-defence, Tripoli condemns the strike. |
| 4 | **Vance, Rubio meet Qatar PM on Iran talks** | Qatar mediates as US–Iran talks stall; Trump says no deal is needed, as fears of renewed war grow. |
| 5 | **US blacklists Megaspeed over Nvidia chips** | The Commerce Department puts the Singapore cloud firm and six affiliates on the Entity List, barring US AI-chip sales. |
| 6 | **Israel kills Hamas security chief in Gaza** | An airstrike killed Naeem Abu Nahel, head of Hamas's internal security apparatus, and six others in Gaza City. |

The news was researched on 25 November 2026 from Reuters, AP, the Wall Street Journal and Finnhub, and every story was checked against at least two independent sources. The headlines and one-line summaries live inside the image itself, because the judge has no news feed — it judges each image the way a careful picture editor would, by what the image shows.

## How the entry works

```sh
python3 main.py
```

`main.py` places the image this repository holds (`entry.png`) at `/output/entry.png`, after checking it against the bounty: PNG, at most 1024×1024 pixels, at most 1 MiB. It uses only the Python standard library, needs no network, and produces byte-identical output on every run.

The picture was drawn by `render.py` (Pillow + DejaVu Sans) from the researched stories. Re-running it reproduces the image exactly:

```sh
python3 render.py
```

## What's in this repo

| File | What it is |
| --- | --- |
| `entry.png` | The image itself: 1024×1024 PNG, 150 KB |
| `main.py` | The entrypoint the grader runs |
| `render.py` | The script that drew the image |
| `LICENSE` | MIT |

---

<sub>Entered on [make.fun](https://make.fun/?ref=longd487&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
