# Interview Notes: Embedding

## Cách giải thích 30 giây

Tiếng Việt:

Embedding là cách biến dữ liệu như từ, câu, đoạn văn thành vector số. Nếu hai nội dung có ý nghĩa gần nhau, vector của chúng thường nằm gần nhau trong không gian vector. Nhờ vậy máy tính có thể so sánh, tìm kiếm, phân cụm và truy xuất thông tin theo ý nghĩa.

English:

An embedding maps text into a numeric vector space. Semantically similar texts are placed close to each other, which enables similarity search, clustering, recommendation, and retrieval.

## Cách giải thích 2 phút

Text ban đầu là ký hiệu rời rạc. Máy tính không tự hiểu "ô tô" gần nghĩa với "xe hơi". Embedding model học từ dữ liệu để ánh xạ text thành vector nhiều chiều. Sau đó ta dùng cosine similarity hoặc dot product để đo mức độ gần nhau. Trong semantic search, ta embedding cả query và documents, rồi lấy documents có vector gần query nhất. RAG dùng đúng cơ chế này để lấy tài liệu liên quan trước khi LLM tạo câu trả lời.

## 20 câu hỏi phỏng vấn

### 1. Embedding là gì?

VN: Embedding là vector số biểu diễn ý nghĩa của text hoặc dữ liệu khác.

EN: An embedding is a numeric vector representation of text or other data.

### 2. Vì sao cần embedding?

VN: Vì model cần số để tính toán, còn text thô không thể so sánh trực tiếp về mặt toán học.

EN: Models need numeric inputs, and embeddings make semantic comparison possible.

### 3. Text được biến thành vector như thế nào?

VN: Text được tokenize, đưa qua mô hình đã học, rồi model xuất ra vector nhiều chiều.

EN: Text is tokenized, passed through a trained model, and converted into a dense vector.

### 4. Cosine similarity là gì?

VN: Là độ đo so sánh hướng của hai vector, thường nằm trong khoảng -1 đến 1.

EN: It measures the angle-based similarity between two vectors.

### 5. Vì sao cosine similarity phổ biến?

VN: Vì nó tập trung vào hướng vector hơn là độ dài, phù hợp khi so sánh ý nghĩa.

EN: It focuses on vector direction rather than magnitude.

### 6. Semantic search khác keyword search thế nào?

VN: Keyword search tìm từ trùng khớp; semantic search tìm nội dung gần nghĩa.

EN: Keyword search matches words, while semantic search matches meaning.

### 7. Embedding có phải là LLM không?

VN: Không. Embedding model tạo vector; LLM sinh hoặc xử lý ngôn ngữ.

EN: No. An embedding model produces vectors; an LLM generates or reasons over text.

### 8. Vector database dùng để làm gì?

VN: Lưu embedding và tìm nearest neighbors nhanh trên tập dữ liệu lớn.

EN: It stores embeddings and performs fast nearest-neighbor search.

### 9. RAG dùng embedding ở đâu?

VN: RAG dùng embedding ở bước retrieval để tìm tài liệu liên quan đến câu hỏi.

EN: RAG uses embeddings during retrieval to find relevant context.

### 10. Chunking là gì trong RAG?

VN: Chunking là chia tài liệu dài thành đoạn nhỏ để embedding và truy xuất hiệu quả hơn.

EN: Chunking splits long documents into smaller retrievable passages.

### 11. Embedding dimension là gì?

VN: Là số chiều của vector, ví dụ 384, 768 hoặc 1536.

EN: It is the number of numeric components in the vector.

### 12. Dimension càng lớn càng tốt không?

VN: Không luôn. Dimension lớn có thể biểu diễn nhiều thông tin hơn nhưng tốn bộ nhớ và chi phí.

EN: Not always. Higher dimensions may capture more information but cost more storage and compute.

### 13. One-hot khác embedding thế nào?

VN: One-hot thưa và không thể hiện ngữ nghĩa; embedding dày và học được quan hệ ý nghĩa.

EN: One-hot vectors are sparse and non-semantic; embeddings are dense and semantic.

### 14. TF-IDF có phải embedding không?

VN: Có thể xem là vector representation, nhưng thường là sparse lexical vector, không phải dense semantic embedding.

EN: It is a vector representation, but usually sparse and lexical rather than dense and semantic.

### 15. Làm sao đánh giá embedding search?

VN: Dùng bộ query có đáp án đúng, đo precision@k, recall@k, MRR hoặc nDCG.

EN: Use labeled queries and metrics like precision@k, recall@k, MRR, or nDCG.

### 16. Tại sao search engine vẫn dùng keyword search?

VN: Keyword search chính xác với tên riêng, mã sản phẩm, thuật ngữ hiếm và dễ kiểm soát ranking.

EN: Keyword search is strong for exact terms, names, IDs, and controllable ranking.

### 17. Hybrid search là gì?

VN: Là kết hợp keyword search và semantic search để tận dụng cả trùng khớp từ và ý nghĩa.

EN: Hybrid search combines lexical and semantic retrieval.

### 18. Resume matching dùng embedding thế nào?

VN: Biến CV và job description thành vector rồi so sánh mức độ phù hợp.

EN: It embeds resumes and job descriptions, then compares their similarity.

### 19. Embedding có hạn chế gì?

VN: Có thể sai domain, thiên lệch, không hiểu số liệu chính xác, và phụ thuộc chất lượng dữ liệu huấn luyện.

EN: It can be domain-mismatched, biased, weak with exact facts, and dependent on training data.

### 20. Khi nào cần fine-tune embedding model?

VN: Khi model chung không hiểu domain, thuật ngữ nội bộ hoặc tiêu chí matching đặc thù.

EN: Fine-tune when a general model fails on domain-specific language or matching criteria.

