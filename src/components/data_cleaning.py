"""Text cleaning routines for the review corpus."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable, List

import pandas as pd

HTML_TAG_RE = re.compile(r"<[^>]+>")
NON_ALPHA_RE = re.compile(r"[^a-zA-Z0-9\s]")
MULTISPACE_RE = re.compile(r"\s+")


@dataclass
class ReviewCleaner:
    lowercase: bool = True

    def clean(self, text: str) -> str:
        if not isinstance(text, str):
            text = ""
        if self.lowercase:
            text = text.lower()
        text = HTML_TAG_RE.sub(" ", text)
        text = NON_ALPHA_RE.sub(" ", text)
        text = MULTISPACE_RE.sub(" ", text)
        return text.strip()

    def clean_series(self, series: pd.Series) -> pd.Series:
        return series.fillna("").map(self.clean)

    def remove_short_reviews(self, df: pd.DataFrame, min_chars: int = 20) -> pd.DataFrame:
        mask = df["reviewText"].str.len() >= min_chars
        return df.loc[mask].copy()

    def __call__(self, df: pd.DataFrame, min_chars: int = 20) -> pd.DataFrame:
        df = df.copy()
        df["clean_text"] = self.clean_series(df["reviewText"])
        df = self.remove_short_reviews(df, min_chars=min_chars)
        df = df.drop_duplicates(subset=["clean_text"])
        return df.reset_index(drop=True)


__all__ = ["ReviewCleaner"]
