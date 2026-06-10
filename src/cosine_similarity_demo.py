from text_utils import cosine_similarity


def explain_pair(name_a, vec_a, name_b, vec_b):
    score = cosine_similarity(vec_a, vec_b)
    print(f"{name_a:18s} {vec_a}")
    print(f"{name_b:18s} {vec_b}")
    print(f"cosine_similarity = {score:.3f}")
    print("-" * 80)


def main():
    print("=" * 80)
    print("DEMO 3: Cosine Similarity")
    print("Vector minh họa có 3 chiều: [NLP, tuyển dụng, thể thao]")
    print("=" * 80)

    embedding_doc = [0.9, 0.1, 0.0]
    semantic_doc = [0.85, 0.2, 0.0]
    resume_doc = [0.1, 0.95, 0.0]
    football_doc = [0.0, 0.0, 1.0]

    explain_pair("embedding_doc", embedding_doc, "semantic_doc", semantic_doc)
    explain_pair("embedding_doc", embedding_doc, "resume_doc", resume_doc)
    explain_pair("embedding_doc", embedding_doc, "football_doc", football_doc)

    print("Ý nghĩa:")
    print("- Score gần 1: hai vector cùng hướng, nội dung gần nghĩa.")
    print("- Score gần 0: hai vector gần vuông góc, nội dung ít liên quan.")
    print("- Score âm: có thể xuất hiện trong embedding thật, thường thể hiện hướng đối nghịch.")


if __name__ == "__main__":
    main()

