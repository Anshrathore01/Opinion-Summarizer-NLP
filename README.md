# Opinion-Summarizer-NLP

An end-to-end project to summarize opinions from Amazon Electronics reviews:
- sample 50k reviews from Kaggle dataset
- clean & preprocess text
- generate embeddings (SentenceTransformer)
- cluster reviews (KMeans / HDBSCAN)
- create cluster-level summaries (T5 / Pegasus)
- build FAISS vector index for retrieval
- Streamlit app for exploration and search

## Setup

1. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
