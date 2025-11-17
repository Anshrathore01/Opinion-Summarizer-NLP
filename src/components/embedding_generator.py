"""Sentence embedding generation utilities."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm.auto import tqdm


@dataclass
class EmbeddingGenerator:
    model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    batch_size: int = 64
    normalize: bool = True

    def __post_init__(self) -> None:
        self.model = SentenceTransformer(self.model_name)

    def encode(self, texts: Iterable[str]) -> np.ndarray:
        embeddings: List[np.ndarray] = []
        batch: List[str] = []
        for text in texts:
            batch.append(text)
            if len(batch) == self.batch_size:
                embeddings.append(self.model.encode(batch, normalize_embeddings=self.normalize))
                batch = []
        if batch:
            embeddings.append(self.model.encode(batch, normalize_embeddings=self.normalize))
        return np.vstack(embeddings)

    def save(self, embeddings: np.ndarray, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        np.save(path, embeddings)


__all__ = ["EmbeddingGenerator"]
