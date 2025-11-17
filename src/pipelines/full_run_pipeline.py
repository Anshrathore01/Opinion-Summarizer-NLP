"""Execute the full offline pipeline: load -> clean -> embed -> cluster -> summarize."""

from __future__ import annotations

from pathlib import Path

from src.pipelines.build_embeddings_pipeline import run as build_embeddings
from src.pipelines.clustering_pipeline import run as cluster_reviews
from src.pipelines.summarization_pipeline import run as summarize_clusters


def run(config_path: str = "src/config/config.yaml") -> None:
    build_embeddings(config_path)
    cluster_reviews(config_path)
    summarize_clusters(config_path)


if __name__ == "__main__":
    run()
