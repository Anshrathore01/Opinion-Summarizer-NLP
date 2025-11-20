"""Flask entrypoint for the Opinion Summarizer demo."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd
import yaml
from flask import Flask, redirect, render_template, request, url_for

from src.components.query_engine import QueryEngine

app = Flask(__name__)
CONFIG_PATH = Path("src/config/config.yaml")


@dataclass
class QueryResult:
    text: str
    score: float


@lru_cache(maxsize=1)
def load_config():
    return yaml.safe_load(CONFIG_PATH.read_text())


@lru_cache(maxsize=1)
def load_query_engine() -> QueryEngine:
    config = load_config()
    data_cfg = config["data"]
    embeddings = np.load(data_cfg["embeddings_path"])
    df = pd.read_parquet(data_cfg["cleaned_path"])
    return QueryEngine(embeddings=embeddings, documents=df["reviewText"].tolist())


def load_cluster_summaries():
    config = load_config()
    summary_path = Path(config["data"]["summaries_path"])
    if summary_path.exists():
        return json.loads(summary_path.read_text())
    return []


@app.route("/")
def home():
    return render_template("index.html", summaries=load_cluster_summaries())


@app.route("/results", methods=["POST"])
def results():
    query = request.form.get("query", "").strip()
    if not query:
        return redirect(url_for("home"))
    try:
        engine = load_query_engine()
        matches = engine.search(query)
        results = [QueryResult(text=doc, score=score) for doc, score in matches]
        return render_template("results.html", query=query, results=results)
    except Exception as e:
        # Log error and return user-friendly message
        return render_template("results.html", query=query, results=[], error=str(e))


@app.route("/health")
def health():
    """Health check endpoint for deployment monitoring."""
    try:
        config = load_config()
        return {"status": "healthy", "config_loaded": True}, 200
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}, 500


if __name__ == "__main__":
    # For Hugging Face Spaces, use port 7860
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port, debug=False)
