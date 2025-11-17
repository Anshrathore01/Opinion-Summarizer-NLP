"""Utilities for loading raw Amazon electronics review data."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

import pandas as pd

from src.utils.exception import CustomException


@dataclass
class ReviewDatasetLoader:
    """Load JSON-lines review dumps with optional sampling."""

    data_path: Path
    sample_size: Optional[int] = None
    random_state: int = 42

    def _read_jsonl(self) -> Iterable[dict]:
        if not self.data_path.exists():
            raise CustomException(f"Dataset not found at {self.data_path}")
        import json

        with self.data_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if line:
                    yield json.loads(line)

    def load(self) -> pd.DataFrame:
        records = list(self._read_jsonl())
        if not records:
            raise CustomException("Dataset file is empty")
        df = pd.DataFrame(records)
        df = df.dropna(subset=["reviewText"]).reset_index(drop=True)
        if self.sample_size and len(df) > self.sample_size:
            df = df.sample(self.sample_size, random_state=self.random_state)
        df["reviewText"] = df["reviewText"].astype(str)
        return df


__all__ = ["ReviewDatasetLoader"]
