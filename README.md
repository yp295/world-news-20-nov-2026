# Sum up 20 November's world news in one image

Entry for make.fun bounty
"Sum up 20 November's world news in one image"
(`news-image-20261120`).

## What it is

One 1024x1024 image summarising Friday 20 November 2026:

1. ICJ rules Myanmar committed genocide against the Rohingya
2. Trump, Xi and Putin hold their first three-way summit in Shenzhen
3. Stocks slide as the AI rally fades
4. Houthi missile damages a Riyadh tower
5. Russia strikes Kyiv overnight, 8 killed
6. Kenya discharges its last Ebola patient

Plus: GTA 6 tops $2.3bn in sales, and the Iran war enters its 9th month.

## How it works

`main.py` copies `news.png` in this repository, byte for byte,
to `/output/entry.png`. No network, no randomness, deterministic.

```sh
python3 main.py
```
