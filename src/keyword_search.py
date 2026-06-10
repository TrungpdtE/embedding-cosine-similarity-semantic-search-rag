from text_utils import load_documents, print_results, rank_by_similarity


def main():
    documents = load_documents()
    queries = [
        "embedding là gì",
        "xe hơi và ô tô",
        "CV phù hợp với công việc",
    ]

    for query in queries:
        results = rank_by_similarity(query, documents, semantic=False)
        print_results("DEMO 1: Keyword Search", query, results)


if __name__ == "__main__":
    main()

