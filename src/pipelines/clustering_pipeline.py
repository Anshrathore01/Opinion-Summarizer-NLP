"""Cluster review embeddings and persist cluster labels."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
import numpy as np
import yaml

from src.components.clustering_engine import ClusteringEngine


def run(config_path: str = "src/config/config.yaml") -> None:
    config = yaml.safe_load(Path(config_path).read_text())
    data_cfg = config["data"]
    cluster_cfg = config["clustering"]

    embeddings = np.load(data_cfg["embeddings_path"])
    engine = ClusteringEngine(
        n_clusters=cluster_cfg["n_clusters"],
        use_pca=cluster_cfg.get("use_pca", True),
        pca_components=cluster_cfg.get("pca_components"),
    )
    labels = engine.fit_predict(embeddings)

    df = pd.read_parquet(data_cfg["cleaned_path"])
    df["cluster_id"] = labels
    df.to_csv(data_cfg["cluster_assignments_path"], index=False)
    print(f"Clustered {len(df)} reviews into {labels.max()+1} clusters")


def cli() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="src/config/config.yaml")
    args = parser.parse_args()
    run(args.config)


if __name__ == "__main__":
    cli()
