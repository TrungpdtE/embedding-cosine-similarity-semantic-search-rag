# embedding-search-lab

Project học tập hoàn chỉnh về **Embedding, Cosine Similarity, Semantic Search và nền tảng của RAG**.

Đối tượng: sinh viên Khoa học Máy tính đang học NLP và muốn có khả năng tự giải thích embedding cho người khác.

Project này không chỉ có code. Nó được thiết kế như một lab học tập gồm:

- Giải thích tiếng Việt từ cơ bản đến nâng cao.
- Minh họa ASCII để hình dung trực quan.
- Demo code chạy được.
- Ví dụ thực tế: ChatGPT, RAG, resume matching, search engine.
- Ghi chú phỏng vấn bằng tiếng Việt và câu trả lời tiếng Anh ngắn gọn.

## 1. Lộ trình đọc project

Nếu bạn mới học embedding, hãy đọc theo thứ tự này:

1. Đọc phần `2. Embedding là gì?`
2. Chạy demo cosine similarity:

```powershell
python src/cosine_similarity_demo.py
```

3. Đọc phần `3. Text được biến thành vector như thế nào?`
4. Chạy keyword search:

```powershell
python src/keyword_search.py
```

5. Chạy semantic search:

```powershell
python src/semantic_search.py
```

6. Chạy visualize embedding:

```powershell
python src/visualize_embeddings.py
```

7. Đọc [docs/rag_foundation.md](docs/rag_foundation.md)
8. Đọc [docs/model_comparison.md](docs/model_comparison.md)
9. Đọc [docs/interview_notes.md](docs/interview_notes.md)
10. Trả lời lại 20 câu hỏi phỏng vấn ở cuối README mà không nhìn đáp án.

## 2. Cài đặt và chạy demo

Yêu cầu:

- Python 3.10+
- `pip`

Cài thư viện:

```powershell
cd embedding-search-lab
pip install -r requirements.txt
```

Chạy tất cả demo:

```powershell
python src/run_all_demos.py
```

Chạy từng demo:

```powershell
python src/keyword_search.py
python src/semantic_search.py
python src/cosine_similarity_demo.py
python src/compare_embedding_models.py
python src/visualize_embeddings.py
```

Sau khi chạy `visualize_embeddings.py`, project sẽ tạo file:

```text
embedding_visualization.png
```

## 3. Cấu trúc project

```text
embedding-search-lab/
|
+-- README.md
+-- requirements.txt
+-- data/
|   +-- documents.json
+-- src/
|   +-- text_utils.py
|   +-- keyword_search.py
|   +-- semantic_search.py
|   +-- cosine_similarity_demo.py
|   +-- visualize_embeddings.py
|   +-- compare_embedding_models.py
|   +-- run_all_demos.py
+-- docs/
|   +-- rag_foundation.md
|   +-- model_comparison.md
|   +-- interview_notes.md
+-- notebooks/
    +-- README.md
```

## 4. Embedding là gì?

Embedding là cách biến một đối tượng thành vector số.

Trong NLP, đối tượng thường là:

- Một từ: `"cat"`
- Một câu: `"Tôi đang học NLP"`
- Một đoạn văn
- Một tài liệu

Ví dụ minh họa:

```text
"học NLP"  --->  [0.12, -0.45, 0.88, 0.03, ...]
"AI"       --->  [0.20, -0.31, 0.76, 0.10, ...]
"bóng đá"  --->  [-0.71, 0.04, 0.11, 0.93, ...]
```

Điểm quan trọng:

```text
Text gần nghĩa  => vector gần nhau
Text khác nghĩa => vector xa nhau
```

Minh họa ASCII:

```text
Không gian embedding 2D minh họa

       NLP
        ^
        |
  embedding *     * vector
        |   * semantic search
        |
        |
        |                         * bóng đá
        |
        +----------------------------------> chủ đề khác
```

Trong thực tế, embedding thường không chỉ có 2 chiều. Nó có thể có 384, 768, 1536 hoặc nhiều chiều hơn. Ta vẽ 2D chỉ để dễ hiểu.

## 5. Vì sao máy tính cần vector?

Máy tính không hiểu chữ theo cách con người hiểu.

Máy tính thấy text ban đầu như chuỗi ký tự:

```text
"xe hơi"
"ô tô"
```

Con người biết hai cụm này gần nghĩa. Nhưng nếu chỉ so sánh chuỗi, chúng khác nhau.

Embedding giúp biến nghĩa thành dạng có thể tính toán:

```text
"xe hơi" -> [0.91, 0.12, 0.33]
"ô tô"  -> [0.89, 0.10, 0.35]
```

Hai vector này gần nhau, nên hệ thống có thể suy ra chúng liên quan.

## 6. Text được biến thành vector như thế nào?

Quy trình tổng quát:

```text
Raw text
   |
   v
Tokenization
   |
   v
Embedding model
   |
   v
Dense vector
```

Ví dụ:

```text
"Tôi đang học NLP"
   |
   v
["Tôi", "đang", "học", "NLP"]
   |
   v
Model
   |
   v
[0.14, -0.21, 0.77, 0.02, ...]
```

Các mức độ biểu diễn:

| Loại | Ví dụ | Ý nghĩa |
|---|---|---|
| Character embedding | vector cho từng ký tự | dùng trong mô hình xử lý ký tự |
| Word embedding | vector cho từng từ | Word2Vec, GloVe, FastText |
| Sentence embedding | vector cho cả câu | Sentence-BERT, embedding API |
| Document embedding | vector cho tài liệu | search, clustering, RAG |

## 7. Từ One-hot đến Embedding

### One-hot

Giả sử vocabulary có 5 từ:

```text
[cat, dog, car, NLP, search]
```

One-hot:

```text
cat    -> [1, 0, 0, 0, 0]
dog    -> [0, 1, 0, 0, 0]
car    -> [0, 0, 1, 0, 0]
NLP    -> [0, 0, 0, 1, 0]
search -> [0, 0, 0, 0, 1]
```

Vấn đề:

- Vector rất dài nếu vocabulary lớn.
- Không thể hiện quan hệ ngữ nghĩa.
- `cat` và `dog` cũng xa nhau như `cat` và `car`.

### Dense embedding

```text
cat -> [0.8, 0.6, 0.1]
dog -> [0.7, 0.7, 0.1]
car -> [0.1, 0.2, 0.9]
```

Ở đây `cat` và `dog` gần nhau hơn `cat` và `car`.

```text
Animal dimension ^
                 |
 cat *  dog *
                 |
                 |
                 |                  car *
                 +--------------------------> Vehicle dimension
```

## 8. Cosine Similarity là gì?

Cosine similarity đo độ giống nhau về hướng giữa hai vector.

Công thức:

```text
cosine(A, B) = (A dot B) / (||A|| * ||B||)
```

Trong đó:

- `A dot B`: tích vô hướng
- `||A||`: độ dài vector A
- `||B||`: độ dài vector B

Trực giác:

```text
Hai vector cùng hướng:

       A
      /
     /
    /
   /
  +----------> B

cosine gần 1
```

```text
Hai vector vuông góc:

       A
       |
       |
       |
       +
        \
         \
          B

cosine gần 0
```

```text
Hai vector ngược hướng:

<---------- + ----------> 
     A             B

cosine gần -1
```

Code ví dụ:

```python
import math

def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot / (norm_a * norm_b)

print(cosine_similarity([1, 0], [1, 0]))  # 1.0
print(cosine_similarity([1, 0], [0, 1]))  # 0.0
```

Chạy demo:

```powershell
python src/cosine_similarity_demo.py
```

Cách trả lời phỏng vấn:

VN: Cosine similarity là độ đo so sánh hướng giữa hai vector. Trong embedding search, nếu hai câu có vector cùng hướng, cosine similarity cao, nghĩa là chúng gần nhau về ngữ nghĩa.

EN: Cosine similarity measures the angle between two vectors. In embedding search, a high cosine score means the texts are semantically similar.

## 9. Keyword Search

Keyword search tìm bằng từ trùng khớp.

Ví dụ query:

```text
"embedding là gì"
```

Tài liệu:

```text
"Embedding biến từ, câu hoặc đoạn văn thành vector số..."
```

Vì có từ `embedding`, tài liệu này được điểm cao.

Minh họa:

```text
Query:    embedding là gì
Doc A:    embedding biến text thành vector
Doc B:    bóng đá là môn thể thao

Trùng từ:
Doc A: embedding
Doc B: là
```

Ưu điểm:

- Dễ hiểu.
- Nhanh.
- Tốt với tên riêng, mã sản phẩm, từ khóa chính xác.

Nhược điểm:

- Không hiểu đồng nghĩa.
- Không hiểu paraphrase.
- Dễ bỏ lỡ tài liệu đúng ý nhưng khác từ.

Chạy demo:

```powershell
python src/keyword_search.py
```

Cách trả lời phỏng vấn:

VN: Keyword search dựa trên trùng khớp từ hoặc thống kê từ. Nó mạnh với truy vấn chính xác nhưng yếu khi người dùng diễn đạt cùng ý bằng từ khác.

EN: Keyword search relies on exact or lexical word matching. It is strong for exact terms but weak for synonyms and paraphrases.

## 10. Semantic Search

Semantic search tìm theo ý nghĩa.

Ví dụ:

```text
Query: "xe hơi"
Document: "ô tô là phương tiện giao thông"
```

Keyword search có thể không tìm tốt vì `xe hơi` và `ô tô` không trùng hoàn toàn.

Semantic search có thể tìm được vì hiểu hai cụm gần nghĩa.

Quy trình:

```text
Query text       Documents
    |                |
    v                v
Query vector     Document vectors
    |                |
    +------ compare --+
             |
             v
       top-k documents
```

Chạy demo:

```powershell
python src/semantic_search.py
```

Trong project này, semantic search demo dùng một mô hình học tập đơn giản: chuẩn hóa một số từ đồng nghĩa trước khi vector hóa. Đây không phải model production, nhưng giúp bạn thấy trực giác rằng "ý nghĩa gần nhau" làm kết quả search tốt hơn.

Cách trả lời phỏng vấn:

VN: Semantic search embedding query và documents vào cùng không gian vector, sau đó tìm documents có vector gần query nhất bằng cosine similarity hoặc độ đo tương tự.

EN: Semantic search embeds the query and documents into the same vector space, then retrieves documents whose vectors are closest to the query.

## 11. Visualize Embedding

Embedding thật thường có rất nhiều chiều. Để vẽ, ta giảm xuống 2D hoặc 3D bằng PCA, t-SNE, UMAP hoặc tạo dữ liệu minh họa.

Trong project này, file `src/visualize_embeddings.py` tạo biểu đồ 2D đơn giản:

```text
NLP terms cluster:
embedding, vector, semantic search, RAG, ChatGPT

Recruitment terms cluster:
CV, resume, job matching

Search terms cluster:
search engine, keyword search
```

Chạy:

```powershell
python src/visualize_embeddings.py
```

Kết quả:

```text
embedding_visualization.png
```

Cách trả lời phỏng vấn:

VN: Khi visualize embedding, ta thường giảm chiều vector xuống 2D hoặc 3D để quan sát cluster. Các điểm gần nhau thường có ý nghĩa gần nhau, nhưng biểu đồ chỉ là xấp xỉ sau giảm chiều.

EN: To visualize embeddings, we reduce high-dimensional vectors to 2D or 3D. Nearby points often indicate semantic similarity, but the visualization is only an approximation.

## 12. So sánh nhiều Embedding Models

Chạy:

```powershell
python src/compare_embedding_models.py
```

Các nhóm model quan trọng:

```text
One-hot
  |
  v
Bag of Words
  |
  v
TF-IDF / BM25
  |
  v
Word2Vec / GloVe / FastText
  |
  v
BERT / Sentence-BERT
  |
  v
Modern embedding APIs / domain-specific embedding models
```

Tóm tắt:

| Model | Dễ hiểu | Hiểu ngữ nghĩa | Dùng production search |
|---|---:|---:|---:|
| One-hot | Cao | Thấp | Thấp |
| Bag of Words | Cao | Thấp | Trung bình nếu keyword |
| TF-IDF/BM25 | Trung bình | Thấp đến vừa | Cao cho keyword |
| Word2Vec | Trung bình | Vừa | Tùy bài toán |
| Sentence-BERT | Vừa | Cao | Cao |
| Embedding API hiện đại | Vừa | Cao | Cao |

## 13. Vì sao Embedding là nền tảng của RAG?

RAG cần tìm tài liệu liên quan trước khi LLM trả lời.

Embedding là cầu nối giữa câu hỏi và kho tài liệu.

```text
User hỏi:
"Hợp đồng nghỉ phép của công ty quy định thế nào?"

          |
          v
Embedding query
          |
          v
Tìm trong vector database
          |
          v
Lấy 3 đoạn tài liệu liên quan nhất
          |
          v
Đưa vào prompt cho LLM
          |
          v
LLM trả lời dựa trên tài liệu
```

Không có embedding, hệ thống thường chỉ tìm bằng keyword. Khi người dùng diễn đạt khác tài liệu, retrieval dễ thất bại.

Đọc thêm: [docs/rag_foundation.md](docs/rag_foundation.md)

## 14. Embedding trong ChatGPT, Resume Matching, Search Engine

### ChatGPT và hệ thống hỏi đáp dữ liệu riêng

ChatGPT bản thân là LLM. Trong các ứng dụng thực tế, người ta thường kết hợp LLM với embedding để tìm dữ liệu riêng.

Ví dụ:

```text
Kho tài liệu công ty -> chunk -> embedding -> vector database

User hỏi -> embedding -> retrieve chunks -> ChatGPT trả lời
```

### Resume Matching

Bài toán:

```text
CV ứng viên      -> embedding A
Job description  -> embedding B
cosine(A, B)     -> mức độ phù hợp
```

Ví dụ:

```text
CV: "Python, NLP, semantic search, vector database"
JD: "Build RAG system using embeddings and Python"
```

Hai text không trùng hoàn toàn, nhưng embedding có thể cho thấy chúng gần nhau.

### Search Engine

Search engine hiện đại thường dùng hybrid search:

```text
Keyword search + Semantic search + Ranking + User feedback
```

Keyword search tốt với:

- Tên riêng
- Mã sản phẩm
- Từ khóa chính xác

Semantic search tốt với:

- Câu hỏi tự nhiên
- Đồng nghĩa
- Paraphrase
- Tìm tài liệu theo ý định

## 15. Những hiểu lầm thường gặp

### Hiểu lầm 1: Embedding tự hiểu như con người

Không chính xác. Embedding là biểu diễn học được từ dữ liệu. Nó có thể sai, lệch domain hoặc bị bias.

### Hiểu lầm 2: Vector gần nhau luôn đúng

Không luôn. Gần nhau chỉ là tín hiệu similarity, không phải chứng minh logic.

### Hiểu lầm 3: Semantic search thay thế hoàn toàn keyword search

Không. Nhiều hệ thống tốt dùng hybrid search.

### Hiểu lầm 4: RAG chỉ cần embedding là xong

Không. RAG tốt cần chunking, retrieval, reranking, prompt design, evaluation và guardrails.

## 16. Công thức học sâu hơn

Sau khi hiểu project này, học tiếp:

1. TF-IDF và BM25
2. Word2Vec: Skip-gram, CBOW
3. FastText và subword
4. Transformer embedding
5. Sentence-BERT
6. Approximate nearest neighbor search
7. Vector database: FAISS, Milvus, Pinecone, Weaviate, Chroma
8. Hybrid search
9. Reranking
10. RAG evaluation

## 17. 20 câu hỏi phỏng vấn Embedding

### 1. Embedding là gì?

VN: Embedding là vector số biểu diễn ý nghĩa của text hoặc dữ liệu khác.

EN: An embedding is a numeric vector representation of text or other data.

### 2. Vì sao cần embedding?

VN: Vì thuật toán cần số để tính toán, còn text thô không thể so sánh trực tiếp về mặt toán học.

EN: Embeddings convert raw text into numeric form so models can compute semantic similarity.

### 3. Text được biến thành vector như thế nào?

VN: Text được tokenize, đưa qua embedding model, rồi model xuất ra vector nhiều chiều.

EN: Text is tokenized, passed through an embedding model, and converted into a dense vector.

### 4. Cosine similarity là gì?

VN: Là độ đo so sánh hướng giữa hai vector.

EN: It measures angle-based similarity between two vectors.

### 5. Cosine similarity cao nghĩa là gì?

VN: Hai vector gần cùng hướng, thường nghĩa là hai text gần nghĩa.

EN: It means the vectors point in similar directions, often indicating semantic similarity.

### 6. Keyword search khác semantic search thế nào?

VN: Keyword search tìm từ trùng; semantic search tìm ý nghĩa gần nhau.

EN: Keyword search matches words; semantic search matches meaning.

### 7. One-hot encoding có hạn chế gì?

VN: Vector dài, thưa và không biểu diễn quan hệ ngữ nghĩa.

EN: It creates sparse vectors and does not capture semantic relationships.

### 8. Bag of Words có hạn chế gì?

VN: Mất thứ tự từ và không hiểu đồng nghĩa.

EN: It ignores word order and does not understand synonyms.

### 9. TF-IDF tốt hơn Bag of Words ở đâu?

VN: TF-IDF giảm trọng số từ phổ biến và tăng trọng số từ đặc trưng.

EN: TF-IDF downweights common words and highlights informative terms.

### 10. Word2Vec học embedding bằng cách nào?

VN: Nó học từ ngữ cảnh, ví dụ dự đoán từ xung quanh hoặc dự đoán từ trung tâm.

EN: It learns from context, such as predicting surrounding words or the center word.

### 11. Sentence embedding khác word embedding thế nào?

VN: Word embedding biểu diễn từ; sentence embedding biểu diễn cả câu hoặc đoạn.

EN: Word embeddings represent individual words; sentence embeddings represent full sentences or passages.

### 12. Vector database là gì?

VN: Là hệ thống lưu vector và tìm vector gần nhất rất nhanh.

EN: It stores vectors and supports fast nearest-neighbor search.

### 13. RAG dùng embedding để làm gì?

VN: Để tìm tài liệu liên quan đến câu hỏi trước khi LLM sinh câu trả lời.

EN: RAG uses embeddings to retrieve relevant context before generation.

### 14. Chunking quan trọng vì sao?

VN: Vì tài liệu quá dài cần chia thành đoạn nhỏ để retrieval chính xác hơn.

EN: Chunking makes long documents easier to retrieve accurately.

### 15. Hybrid search là gì?

VN: Là kết hợp keyword search và semantic search.

EN: It combines lexical search and semantic search.

### 16. Embedding có dùng trong ChatGPT không?

VN: Trong các hệ thống xây quanh ChatGPT, embedding thường được dùng để truy xuất dữ liệu riêng hoặc tạo memory/search.

EN: In ChatGPT-based systems, embeddings are often used for retrieval, memory, and private knowledge search.

### 17. Resume matching dùng embedding thế nào?

VN: So sánh vector của CV và job description để xếp hạng mức độ phù hợp.

EN: It compares resume and job-description embeddings to rank fit.

### 18. Làm sao đánh giá semantic search?

VN: Tạo tập query có đáp án đúng rồi đo precision@k, recall@k, MRR hoặc nDCG.

EN: Use labeled queries and evaluate with precision@k, recall@k, MRR, or nDCG.

### 19. Khi nào embedding model có thể sai?

VN: Khi domain khác dữ liệu train, text mơ hồ, có thuật ngữ hiếm hoặc cần suy luận logic chính xác.

EN: It can fail with domain mismatch, ambiguity, rare terms, or tasks requiring precise reasoning.

### 20. Khi nào cần fine-tune embedding?

VN: Khi model chung không đáp ứng tốt dữ liệu domain hoặc tiêu chí matching của bài toán.

EN: Fine-tune when the general model performs poorly on domain-specific data or matching criteria.

## 18. Checklist sau khi học xong

Bạn đạt mục tiêu khi có thể tự trả lời:

- Embedding là gì?
- Vì sao text cần biến thành vector?
- Cosine similarity đo cái gì?
- Keyword search và semantic search khác nhau thế nào?
- RAG dùng embedding ở bước nào?
- Vì sao search engine hiện đại thường dùng hybrid search?
- Resume matching dùng embedding ra sao?
- Vì sao embedding không đảm bảo luôn đúng?

Nếu trả lời được các câu trên bằng lời của bạn, bạn đã hiểu nền tảng embedding đủ tốt để giải thích cho người khác.

