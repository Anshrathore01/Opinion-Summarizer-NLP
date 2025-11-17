"""Clustering helpers for grouping similar reviews."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


@dataclass
class ClusteringEngine:
    n_clusters: int = 20
    random_state: int = 42
    use_pca: bool = True
    pca_components: Optional[int] = 50

    def fit_predict(self, embeddings: np.ndarray) -> np.ndarray:
        matrix = embeddings
        if self.use_pca and self.pca_components and matrix.shape[1] > self.pca_components:
            reducer = PCA(n_components=self.pca_components, random_state=self.random_state)
            matrix = reducer.fit_transform(matrix)
        model = KMeans(n_clusters=self.n_clusters, random_state=self.random_state, n_init="auto")
        labels = model.fit_predict(matrix)
        return labels


__all__ = ["ClusteringEngine"]
