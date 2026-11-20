"""Sum up 20 November 2026 world news in one image.

The entry image is news.png in this repository.
This program copies it, byte for byte, to /output/entry.png.
No network, no randomness, deterministic: two runs write the same bytes.
"""
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "news.png"
OUT = Path("/output/entry.png")


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
