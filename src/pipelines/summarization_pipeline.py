"""Generate abstractive summaries for each review cluster."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd
import yaml

from src.components.summarization_engine import SummarizationEngine


def run(config_path: str = "src/config/config.yaml") -> None:
    config = yaml.safe_load(Path(config_path).read_text())
    data_cfg = config["data"]
    model_cfg = config["models"]

    df = pd.read_csv(data_cfg["cluster_assignments_path"])
    engine = SummarizationEngine(
        model_name=model_cfg["summarizer_model"],
        max_length=model_cfg.get("max_summary_length", 128),
        min_length=model_cfg.get("min_summary_length", 32),
    )

    summaries = []
    for cluster_id, group in df.groupby("cluster_id"):
        summary = engine.summarize(group["reviewText"].tolist()[:200])
        summaries.append({
            "cluster_id": int(cluster_id),
            "summary": summary,
            "size": int(len(group)),
        })
    Path(data_cfg["summaries_path"]).write_text(json.dumps(summaries, indent=2))
    print(f"Wrote {len(summaries)} cluster summaries -> {data_cfg['summaries_path']}")


def cli() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="src/config/config.yaml")
    args = parser.parse_args()
    run(args.config)


if __name__ == "__main__":
    cli()
