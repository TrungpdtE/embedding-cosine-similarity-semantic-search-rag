import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "embedding_visualization.png"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


POINTS = [
    ("embedding", 1.0, 4.0, "NLP"),
    ("vector", 1.3, 3.7, "NLP"),
    ("semantic search", 1.8, 4.2, "NLP"),
    ("RAG", 2.2, 3.6, "NLP"),
    ("ChatGPT", 2.4, 4.4, "NLP"),
    ("CV", 5.1, 2.4, "Recruitment"),
    ("resume", 5.4, 2.1, "Recruitment"),
    ("job matching", 5.8, 2.6, "Recruitment"),
    ("search engine", 3.6, 3.1, "Search"),
    ("keyword search", 3.2, 2.8, "Search"),
]


COLORS = {
    "NLP": "#2563eb",
    "Recruitment": "#16a34a",
    "Search": "#dc2626",
}


def main():
    plt.figure(figsize=(10, 6))
    for label, x, y, group in POINTS:
        plt.scatter(x, y, color=COLORS[group], s=120)
        plt.text(x + 0.06, y + 0.06, label, fontsize=10)

    plt.title("Embedding Visualization: từ/cụm từ gần nghĩa nằm gần nhau")
    plt.xlabel("Dimension 1 sau khi giảm chiều")
    plt.ylabel("Dimension 2 sau khi giảm chiều")
    plt.grid(True, linestyle="--", alpha=0.35)

    handles = []
    labels = []
    for group, color in COLORS.items():
        handles.append(plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=color, markersize=10))
        labels.append(group)
    plt.legend(handles, labels)
    plt.tight_layout()
    plt.savefig(OUTPUT, dpi=160)
    print(f"Đã tạo biểu đồ: {OUTPUT}")


if __name__ == "__main__":
    main()
