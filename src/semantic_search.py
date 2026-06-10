from text_utils import load_documents, print_results, rank_by_similarity


def main():
    documents = load_documents()
    queries = [
        "embedding là gì",
        "xe hơi và ô tô",
        "CV phù hợp với công việc",
        "làm sao chatbot lấy kiến thức riêng để trả lời",
    ]

    for query in queries:
        keyword_results = rank_by_similarity(query, documents, semantic=False)
        semantic_results = rank_by_similarity(query, documents, semantic=True)
        print_results("Keyword Search baseline", query, keyword_results, top_k=3)
        print_results("DEMO 2: Semantic Search toy model", query, semantic_results, top_k=3)


if __name__ == "__main__":
    main()

