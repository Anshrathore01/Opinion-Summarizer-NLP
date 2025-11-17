# Opinion-Summarizer-NLP

An end-to-end workflow that turns raw Amazon electronics reviews into compact opinion summaries and a lightweight semantic search experience.

## Project layout

```
├── src/components      # modular data/ML building blocks
├── src/pipelines       # executable steps (load→embed→cluster→summarise)
├── artifacts/          # generated assets (clean data, embeddings, etc.)
├── templates/ + static/ # Flask UI
└── notebooks/EDA.ipynb # exploratory analysis walkthrough
```

## Getting started

1. **Install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Place the sampled dataset** at `artifacts/raw_data/electronics_sample_50k.json`. This should be a JSONL file where each line is a review dict from the Amazon Electronics dataset.
3. **Generate assets**
   ```bash
   python -m src.pipelines.build_embeddings_pipeline
   python -m src.pipelines.clustering_pipeline
   python -m src.pipelines.summarization_pipeline
   ```
   or simply run `python -m src.pipelines.full_run_pipeline` to execute all three.
4. **Launch the app**
   ```bash
   flask --app app run --port 8000
   ```

## Pipelines

| Step | Purpose | Output |
| --- | --- | --- |
| `build_embeddings_pipeline` | load → clean → embed reviews | `artifacts/cleaned_data/*.parquet`, `artifacts/embeddings/*.npy` |
| `clustering_pipeline` | group reviews by semantic similarity | `artifacts/clustering/cluster_labels.csv` |
| `summarization_pipeline` | produce abstractive summary per cluster | `artifacts/summaries/cluster_summaries.json` |

## Web interface

The Flask app exposes:
- `/` overview page with the most recent cluster summaries
- `/results` POST route to run semantic search over the indexed reviews

Static styling lives in `static/styles.css`; HTML templates sit in `templates/`.

## Notebook

`notebooks/EDA.ipynb` reproduces the exploratory plots (length distributions, word clouds, rating histograms, etc.) over the sampled 50k reviews.

## Configuration

Tune paths and hyper-parameters inside `src/config/config.yaml`, `src/config/model_config.json`, and `src/config/cluster_config.json`.
