import json
import math
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "documents.json"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


SYNONYMS = {
    "xe": "oto",
    "xe hơi": "oto",
    "ô tô": "oto",
    "oto": "oto",
    "car": "oto",
    "cv": "resume",
    "hồ sơ": "resume",
    "resume": "resume",
    "tuyển dụng": "recruitment",
    "ứng viên": "candidate",
    "rag": "rag",
    "truy xuất": "retrieval",
    "tìm kiếm": "search",
    "ý nghĩa": "semantic",
}


STOPWORDS = {
    "là",
    "gì",
    "và",
    "có",
    "của",
    "để",
    "với",
    "the",
    "a",
    "an",
    "is",
    "are",
    "to",
    "of",
    "and",
}


def load_documents():
    with DATA_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^\w\sÀ-ỹ]", " ", text)
    return [token for token in text.split() if token and token not in STOPWORDS]


def normalize_tokens(tokens):
    normalized = []
    joined = " ".join(tokens)
    for phrase, replacement in SYNONYMS.items():
        if " " in phrase and phrase in joined:
            normalized.append(replacement)
    for token in tokens:
        normalized.append(SYNONYMS.get(token, token))
    return normalized


def build_vocabulary(texts, semantic=False):
    vocab = {}
    for text in texts:
        tokens = tokenize(text)
        if semantic:
            tokens = normalize_tokens(tokens)
        for token in tokens:
            if token not in vocab:
                vocab[token] = len(vocab)
    return vocab


def bag_of_words_vector(text, vocab, semantic=False):
    tokens = tokenize(text)
    if semantic:
        tokens = normalize_tokens(tokens)
    counts = Counter(tokens)
    vector = [0.0] * len(vocab)
    for token, count in counts.items():
        if token in vocab:
            vector[vocab[token]] = float(count)
    return vector


def cosine_similarity(vec_a, vec_b):
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def rank_by_similarity(query, documents, semantic=False):
    texts = [doc["text"] for doc in documents] + [query]
    vocab = build_vocabulary(texts, semantic=semantic)
    query_vector = bag_of_words_vector(query, vocab, semantic=semantic)

    results = []
    for doc in documents:
        doc_vector = bag_of_words_vector(doc["text"], vocab, semantic=semantic)
        score = cosine_similarity(query_vector, doc_vector)
        results.append((score, doc))
    return sorted(results, key=lambda item: item[0], reverse=True)


def print_results(title, query, results, top_k=5):
    print("=" * 80)
    print(title)
    print(f"Query: {query}")
    print("-" * 80)
    for rank, (score, doc) in enumerate(results[:top_k], start=1):
        print(f"{rank}. score={score:.3f} | {doc['title']}")
        print(f"   {doc['text']}")
    print()
