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

Follow these steps to run the application on your computer.

### Step 1: Set Up a Python Virtual Environment
It is highly recommended to use a virtual environment to avoid package conflicts.

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate
```

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### Step 2: Install Dependencies
Install all required libraries inside the virtual environment:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Web App
The repository already includes pre-generated artifacts (cleaned reviews, clusters, Pegasus summaries, and review embeddings) in the `artifacts/` folder. **You do not need to run the heavy pipeline to start the app.**

Run the Flask development server:
```bash
flask --app app run --port 8000
```

Once started, open your web browser and go to:
**[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

### Step 4 (Optional): Regenerate Artifacts
If you want to re-run the entire offline NLP pipeline (clean the data, generate embeddings, cluster reviews, and run the Pegasus abstractive summarizer), run the following command:

```bash
python -m src.pipelines.full_run_pipeline
```
> [!NOTE]
> Re-running the pipeline will download large pre-trained model weights (Google Pegasus is ~2.2GB, Sentence Transformers is ~120MB) and may take a significant amount of time and computer resources (RAM/CPU) to complete.

