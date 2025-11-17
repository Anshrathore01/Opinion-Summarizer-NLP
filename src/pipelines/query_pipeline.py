"""Expose a CLI helper to run semantic search queries."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

from src.components.query_engine import QueryEngine


def run(query: str, config_path: str = "src/config/config.yaml") -> None:
    config = yaml.safe_load(Path(config_path).read_text())
    data_cfg = config["data"]
    embeddings = np.load(data_cfg["embeddings_path"])
    df = pd.read_parquet(data_cfg["cleaned_path"])

    engine = QueryEngine(embeddings=embeddings, documents=df["reviewText"].tolist())
    results = engine.search(query)

    for rank, (text, score) in enumerate(results, start=1):
        print(f"[{rank}] score={score:.3f}\n{text}\n")


def cli() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Natural language query to look up")
    parser.add_argument("--config", default="src/config/config.yaml")
    args = parser.parse_args()
    run(args.query, args.config)


if __name__ == "__main__":
    cli()
