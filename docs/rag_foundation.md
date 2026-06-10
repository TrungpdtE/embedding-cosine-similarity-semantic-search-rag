# Vì sao Embedding là nền tảng của RAG?

RAG là viết tắt của **Retrieval Augmented Generation**.

Ý tưởng:

1. Người dùng hỏi một câu.
2. Hệ thống biến câu hỏi thành embedding.
3. Hệ thống tìm các tài liệu có embedding gần câu hỏi nhất.
4. Các tài liệu liên quan được đưa vào prompt.
5. LLM tạo câu trả lời dựa trên ngữ cảnh vừa tìm được.

```text
User Question
     |
     v
[Embedding Model]
     |
     v
Query Vector --------------+
                           |
                           v
                    [Vector Database]
                           |
                           v
                 Top-k Relevant Chunks
                           |
                           v
                    [LLM / ChatGPT]
                           |
                           v
                    Final Answer
```

Nếu không có embedding, hệ thống khó biết câu hỏi "làm sao chatbot lấy dữ liệu công ty?" liên quan đến tài liệu có chữ "retrieval augmented generation".

Embedding giúp RAG:

- Tìm theo ý nghĩa, không chỉ theo từ khóa.
- Truy xuất nhanh trên lượng tài liệu lớn.
- Giảm hallucination bằng cách cung cấp nguồn thông tin liên quan.
- Cá nhân hóa LLM bằng dữ liệu riêng mà không cần train lại model.

Điểm cần nhớ khi phỏng vấn:

- Embedding không tự trả lời câu hỏi.
- Embedding chỉ giúp tìm nội dung liên quan.
- LLM mới là thành phần sinh câu trả lời.
- Chất lượng RAG phụ thuộc vào chunking, embedding model, vector database, reranking và prompt.

