
import os
import numpy as np
import faiss
import torch
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def load_sentence_transformer(path_or_name):
    if os.path.exists(path_or_name):
        model = SentenceTransformer(path_or_name)
    else:
        model = SentenceTransformer(path_or_name)  
    return model

def load_summarizer_model(path_or_name):
    
    tokenizer = AutoTokenizer.from_pretrained(path_or_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(path_or_name)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    return model, tokenizer

def load_tokenizer(path_or_name):
    return AutoTokenizer.from_pretrained(path_or_name)

def load_faiss_index(path):
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"FAISS index not found: {path}")
    index = faiss.read_index(path)
    # load metadata if available
    meta_path = os.path.join(os.path.dirname(path), "meta.jsonl")
    meta = []
    if os.path.exists(meta_path):
        import json
        with open(meta_path) as f:
            for line in f:
                if line.strip():
                    meta.append(json.loads(line))
    else:
        np_meta = os.path.join(os.path.dirname(path), "meta.npy")
        if os.path.exists(np_meta):
            meta = np.load(np_meta, allow_pickle=True).tolist()
    return index, meta
