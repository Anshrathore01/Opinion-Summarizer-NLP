"""Cluster-level abstractive summarisation helpers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from transformers import pipeline


@dataclass
class SummarizationEngine:
    model_name: str = "google/pegasus-xsum"
    max_length: int = 128
    min_length: int = 32
    max_input_chars: int = 6000
    max_reviews: int = 100

    def __post_init__(self) -> None:
        self._pipeline = pipeline(
            "summarization",
            model=self.model_name,
            tokenizer=self.model_name,
        )

    def summarize(self, texts: Iterable[str]) -> str:
        cleaned = [text.strip() for text in texts if text and text.strip()]
        if not cleaned:
            return ""
        if self.max_reviews:
            cleaned = cleaned[: self.max_reviews]
        joined = " ".join(cleaned)
        if len(joined) > self.max_input_chars:
            joined = joined[: self.max_input_chars]
        output = self._pipeline(
            joined,
            max_length=self.max_length,
            min_length=self.min_length,
            do_sample=False,
            truncation=True,
        )
        return output[0]["summary_text"].strip()


__all__ = ["SummarizationEngine"]
