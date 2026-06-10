# So sánh Embedding Models

| Model | Ý tưởng | Ưu điểm | Nhược điểm | Khi dùng |
|---|---|---|---|---|
| One-hot | Mỗi từ là một vector có đúng một vị trí bằng 1 | Rất dễ hiểu | Vector thưa, không hiểu nghĩa | Học khái niệm ban đầu |
| Bag of Words | Đếm số lần xuất hiện của từ | Đơn giản, nhanh | Mất thứ tự từ, không hiểu đồng nghĩa | Baseline search |
| TF-IDF | Tăng trọng số từ quan trọng, giảm từ phổ biến | Tốt hơn BoW cho keyword search | Vẫn yếu về ngữ nghĩa | Search truyền thống |
| Word2Vec | Học vector từ ngữ cảnh | Từ gần nghĩa gần nhau | Vector theo từ, khó biểu diễn cả câu | Học embedding cổ điển |
| GloVe | Học từ thống kê đồng xuất hiện toàn cục | Vector ổn định | Không xử lý tốt ngữ cảnh động | NLP cổ điển |
| FastText | Biểu diễn từ bằng subword | Tốt với từ hiếm | Vẫn chủ yếu là word embedding | Ngôn ngữ nhiều biến thể |
| BERT | Contextual embedding | Hiểu ngữ cảnh tốt | Nặng hơn, cần pooling cho câu | NLP nâng cao |
| Sentence-BERT | Tối ưu embedding cho câu | Rất hợp semantic search | Cần chọn model đúng domain | Search, clustering, matching |
| Commercial embedding APIs | Model lớn, tiện dùng | Chất lượng cao, dễ tích hợp | Chi phí, phụ thuộc API | RAG production |

## Ví dụ dễ nhớ

Câu 1: "Tôi muốn mua xe hơi"

Câu 2: "Tôi cần tìm ô tô"

Keyword search có thể thấy khác nhau vì "xe hơi" và "ô tô" không trùng từ hoàn toàn.

Semantic embedding tốt sẽ đặt hai câu gần nhau vì cùng nói về phương tiện.

```text
Không gian vector

  xe hơi  *        * ô tô
          \      /
           \    /
            gần nhau về ý nghĩa

  bóng đá *                           * cosine similarity
```

## Cách chọn model

- Dữ liệu nhỏ, học cơ bản: Bag of Words, TF-IDF.
- Search theo keyword: TF-IDF hoặc BM25.
- Search theo ý nghĩa: Sentence-BERT hoặc embedding API.
- RAG production: embedding model mạnh + vector database + reranker.
- Domain đặc thù: đánh giá bằng dataset thật thay vì chỉ tin benchmark chung.

