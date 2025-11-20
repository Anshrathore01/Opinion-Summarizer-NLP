---
title: Opinion Summarizer
emoji: 🔍
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
license: mit
---

# Opinion Summarizer

An end-to-end NLP workflow that transforms raw Amazon electronics reviews into compact opinion summaries and provides a semantic search experience.

## Features

- **Semantic Search**: Query thousands of reviews using natural language
- **Cluster Summaries**: View high-level themes extracted from review clusters
- **Abstractive Summarization**: Uses Google's Pegasus model for generating summaries

## How it Works

1. **Data Processing**: Raw reviews are cleaned and embedded using sentence transformers
2. **Clustering**: Reviews are grouped by semantic similarity
3. **Summarization**: Each cluster is summarized using abstractive summarization
4. **Search**: Query the review corpus using semantic similarity search

## Usage

1. Enter a query in natural language (e.g., "battery life of noise cancelling headphones")
2. View the most relevant reviews ranked by similarity
3. Browse cluster summaries to discover common themes

## Technical Details

- **Embedding Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Summarization Model**: `google/pegasus-xsum`
- **Clustering**: K-means with PCA dimensionality reduction
- **Search**: Cosine similarity over embeddings using scikit-learn NearestNeighbors

## Project Structure

```
├── src/components      # Modular data/ML building blocks
├── src/pipelines       # Executable steps (load→embed→cluster→summarise)
├── artifacts/          # Generated assets (clean data, embeddings, etc.)
├── templates/ + static/ # Flask UI
└── app.py             # Flask application entrypoint
```

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Generate artifacts (if needed):
   ```bash
   python -m src.pipelines.full_run_pipeline
   ```

3. Run the app:
   ```bash
   flask --app app run --port 8000
   ```
