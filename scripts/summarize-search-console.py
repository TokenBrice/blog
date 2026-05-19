#!/usr/bin/env python3
"""Summarize a Google Search Console CSV export by SEO reporting buckets.

Expected columns are the usual Search Console/API names: page, query, clicks,
impressions, ctr, and position. Column matching is case-insensitive and the
script ignores extra columns, so exports can be lightly edited before use.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse


PILLAR_SLUGS = {
    "guides",
    "stablecoins-guide",
    "lending-money-markets",
    "dex-liquidity",
    "yield",
    "defi-risk",
    "governance",
}

TOPIC_KEYWORDS = {
    "stablecoins": (
        "stablecoin",
        "polaris",
        "pharos",
        "gho",
        "lusd",
        "liquity",
        "rai",
        "pegged",
    ),
    "lending": ("lending", "borrow", "aave", "euler", "morpho", "money-market"),
    "dex-liquidity": ("dex", "liquidity", "curve", "crv", "velo", "maverick", "swap"),
    "yield": ("yield", "farm", "vault", "yearn", "apy"),
    "governance": ("governance", "dao", "vote", "venft", "ve", "crv-wars"),
    "risk": ("risk", "bullshit", "security", "privacy", "depeg"),
}


@dataclass
class Bucket:
    clicks: float = 0
    impressions: float = 0
    position_weight: float = 0

    def add(self, clicks: float, impressions: float, position: float) -> None:
        self.clicks += clicks
        self.impressions += impressions
        if impressions > 0:
            self.position_weight += position * impressions

    @property
    def ctr(self) -> float:
        return self.clicks / self.impressions if self.impressions else 0

    @property
    def position(self) -> float:
        return self.position_weight / self.impressions if self.impressions else 0


def number(value: str) -> float:
    value = (value or "").strip().replace("%", "").replace(",", "")
    if not value:
        return 0
    try:
        return float(value)
    except ValueError:
        return 0


def normalized_row(row: dict[str, str]) -> dict[str, str]:
    return {key.strip().lower(): value for key, value in row.items() if key}


def page_path(page: str) -> str:
    parsed = urlparse(page)
    return parsed.path or page or "/"


def language(path: str) -> str:
    return "fr" if path == "/fr/" or path.startswith("/fr/") else "en"


def page_type(path: str) -> str:
    clean = path.strip("/")
    parts = clean.split("/") if clean else []
    if clean in ("", "fr"):
        return "home"
    if parts and parts[0] == "fr":
        parts = parts[1:]
    if not parts:
        return "home"
    if parts[0] == "glossary":
        return "glossary-term" if len(parts) > 1 else "glossary-list"
    if parts[0] == "categories":
        return "category"
    if parts[0] == "series":
        return "series"
    if parts[0] in {"search", "archives", "subscribe", "shows", "about"}:
        return "utility"
    if parts[0] in PILLAR_SLUGS:
        return "pillar"
    return "post"


def topic_cluster(path: str, query: str) -> str:
    haystack = f"{path} {query}".lower()
    for topic, keywords in TOPIC_KEYWORDS.items():
        if any(keyword in haystack for keyword in keywords):
            return topic
    if "/glossary/" in path:
        return "glossary"
    return "other"


def summarize(csv_path: Path) -> dict[tuple[str, str, str], Bucket]:
    with csv_path.open(newline="", encoding="utf-8-sig") as handle:
        try:
            reader = csv.DictReader(handle)
            fieldnames = {name.strip().lower() for name in (reader.fieldnames or [])}
        except UnicodeDecodeError as exc:
            raise ValueError("input is not a UTF-8 CSV export") from exc
        required = {"page", "clicks", "impressions"}
        missing = required - fieldnames
        if missing:
            raise ValueError(f"input is missing expected columns: {', '.join(sorted(missing))}")
        buckets: dict[tuple[str, str, str], Bucket] = defaultdict(Bucket)
        try:
            for raw in reader:
                row = normalized_row(raw)
                path = page_path(row.get("page", ""))
                query = row.get("query", "")
                clicks = number(row.get("clicks", "0"))
                impressions = number(row.get("impressions", "0"))
                position = number(row.get("position", "0"))
                key = (language(path), page_type(path), topic_cluster(path, query))
                buckets[key].add(clicks, impressions, position)
        except UnicodeDecodeError as exc:
            raise ValueError("input is not a UTF-8 CSV export") from exc
    return buckets


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path, help="Search Console CSV export")
    args = parser.parse_args()

    if not args.csv.exists():
        parser.error(f"{args.csv} does not exist")
    if args.csv.suffix.lower() == ".zip":
        parser.error("expected a Search Console performance CSV, not a Coverage ZIP")

    writer = csv.writer(sys.stdout)
    writer.writerow(["language", "page_type", "topic_cluster", "clicks", "impressions", "ctr", "position"])
    try:
        buckets = summarize(args.csv)
    except ValueError as exc:
        parser.error(str(exc))
    for key, bucket in sorted(buckets.items()):
        writer.writerow([
            *key,
            round(bucket.clicks),
            round(bucket.impressions),
            f"{bucket.ctr:.4f}",
            f"{bucket.position:.2f}",
        ])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
