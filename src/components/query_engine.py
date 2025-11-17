"""Simple semantic search over review embeddings."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence, Tuple

import numpy as np
from sklearn.neighbors import NearestNeighbors
from sentence_transformers import SentenceTransformer


@dataclass
class QueryEngine:
    embeddings: np.ndarray
    documents: Sequence[str]
    model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    top_k: int = 5

    def __post_init__(self) -> None:
        if len(self.documents) != len(self.embeddings):
            raise ValueError("Embeddings and documents must be aligned")
        self.model = SentenceTransformer(self.model_name)
        self.index = NearestNeighbors(metric="cosine")
        self.index.fit(self.embeddings)

    def search(self, query: str) -> List[Tuple[str, float]]:
        query_emb = self.model.encode([query])
        distances, indices = self.index.kneighbors(query_emb, n_neighbors=self.top_k)
        results = []
        for dist, idx in zip(distances[0], indices[0]):
            similarity = 1 - dist
            results.append((self.documents[idx], float(similarity)))
        return results


__all__ = ["QueryEngine"]
