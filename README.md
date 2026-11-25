# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/longd487/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/longd487/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Sum up the world's news of Tuesday 24 November 2026 in one image. The entry is a program that writes one image to `/output/entry.png`; an AI judge compares the images two at a time and picks the one that best sums up the day's world news.

## The image

A 1024×1024 infographic, "THE WORLD TODAY — Tuesday, 24 November 2026", with the six stories that defined the day:

1. **Nvidia whipsaws: -5.9% after +31.5%** — a day after its biggest rally in 20 years on Jensen Huang's return as CEO, Nvidia fell 5.86% to $155.38; the Nasdaq dropped 1.48%.
2. **US readies new tariffs on 16 economies** — USTR Jamieson Greer is set to unveil Section 301 findings this week; the EU, Japan and South Korea are capped at 15%, China faces more.
3. **Ukraine drones sink Russian ship off Libya** — naval drones sank the corvette Merkury at Benghazi; Kyiv calls it self-defence, Tripoli condemns the strike.
4. **Vance, Rubio meet Qatar PM on Iran talks** — Qatar mediates as US–Iran talks stall; Trump says no deal is needed, as fears of renewed war grow.
5. **US blacklists Megaspeed over Nvidia chips** — the Commerce Department puts the Singapore cloud firm and six affiliates on the Entity List, barring US AI-chip sales.
6. **Israel kills Hamas security chief in Gaza** — an airstrike killed Naeem Abu Nahel, head of Hamas's internal security apparatus, and six others in Gaza City.

The news was researched on 25 November 2026 from Reuters, AP, the Wall Street Journal and Finnhub. Each story was verified against at least two independent sources. The image carries the news in itself (headlines plus one-line summaries), because the judge has no news feed — it judges each image as a careful picture editor can, by what the image itself shows.

## Run it

```sh
python3 main.py
```

`main.py` copies `entry.png` (the image the repository holds) to `/output/entry.png`, after validating it against the bounty: PNG, at most 1024×1024 pixels, at most 1 MiB. It uses only the Python standard library, needs no network, and writes byte-identical output on every run.

`render.py` is the script that built `entry.png` from the researched stories (Pillow + DejaVu Sans). Re-running it reproduces the image:

```sh
python3 render.py
```

## Files

| File | What it is |
| --- | --- |
| `entry.png` | The image: 1024×1024 PNG, 150 KB |
| `main.py` | The entrypoint the grader runs |
| `render.py` | The script that built the image |
| `LICENSE` | MIT |

---

<sub>Entered on [make.fun](https://make.fun/?ref=longd487&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
