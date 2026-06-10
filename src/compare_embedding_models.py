from text_utils import load_documents, print_results, rank_by_similarity


MODELS = [
    {
        "name": "Bag of Words Keyword Model",
        "semantic": False,
        "idea": "Chỉ xem từ nào trùng nhau. Dễ hiểu nhưng kém khi dùng từ đồng nghĩa.",
    },
    {
        "name": "Toy Semantic Normalization Model",
        "semantic": True,
        "idea": "Chuẩn hóa một số từ đồng nghĩa trước khi vector hóa. Đây là mô hình học tập, không phải model production.",
    },
]


def main():
    documents = load_documents()
    query = "CV ứng viên có phù hợp với job không"

    for model in MODELS:
        print("=" * 80)
        print(f"MODEL: {model['name']}")
        print(model["idea"])
        results = rank_by_similarity(query, documents, semantic=model["semantic"])
        print_results("DEMO 5: So sánh Embedding Models", query, results, top_k=5)

    print("Gợi ý nâng cấp:")
    print("- TF-IDF: giảm trọng số các từ quá phổ biến.")
    print("- Word2Vec/FastText: học vector cho từ dựa trên ngữ cảnh.")
    print("- Sentence-BERT: tạo embedding cho cả câu, phù hợp semantic search hơn.")
    print("- OpenAI/text-embedding hoặc model tương tự: dùng cho hệ thống RAG production.")


if __name__ == "__main__":
    main()

