import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEMOS = [
    "keyword_search.py",
    "semantic_search.py",
    "cosine_similarity_demo.py",
    "compare_embedding_models.py",
    "visualize_embeddings.py",
]


def main():
    for demo in DEMOS:
        print("\n" + "#" * 100, flush=True)
        print(f"RUNNING: src/{demo}", flush=True)
        print("#" * 100, flush=True)
        subprocess.run([sys.executable, str(ROOT / "src" / demo)], check=True)


if __name__ == "__main__":
    main()
