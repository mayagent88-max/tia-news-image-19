#!/usr/bin/env python3
"""Entry program for news-image-20261119: copy the front page to /output."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(out, "entry.png"))


if __name__ == "__main__":
    main()
