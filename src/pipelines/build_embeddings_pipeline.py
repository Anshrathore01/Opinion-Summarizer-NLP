"""CLI to build review embeddings from the raw dataset."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import yaml

from src.components.data_loader import ReviewDatasetLoader
from src.components.data_cleaning import ReviewCleaner
from src.components.embedding_generator import EmbeddingGenerator


def run(config_path: str = "src/config/config.yaml") -> None:
    config = yaml.safe_load(Path(config_path).read_text())
    data_cfg = config["data"]
    model_cfg = config["models"]

    loader = ReviewDatasetLoader(Path(data_cfg["raw_path"]))
    cleaner = ReviewCleaner()
    df = cleaner(loader.load())

    generator = EmbeddingGenerator(model_name=model_cfg["embedding_model"])
    embeddings = generator.encode(df["clean_text"].tolist())
    generator.save(embeddings, Path(data_cfg["embeddings_path"]))

    df[["reviewText", "clean_text"]].to_parquet(data_cfg["cleaned_path"], index=False)
    print(f"Saved {len(df)} cleaned reviews and embeddings -> {data_cfg['embeddings_path']}")


def cli() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="src/config/config.yaml")
    args = parser.parse_args()
    run(args.config)


if __name__ == "__main__":
    cli()
