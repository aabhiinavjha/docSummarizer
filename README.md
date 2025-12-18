# Feature-Based Document Summarizer

This project implements a **feature-based, cluster-aware extractive document summarization system**, inspired by the research paper  
**“Feature-based cluster ranking approach for single document summarization.”**

The system generates concise summaries from **single documents** by clustering similar sentences and ranking them using multiple statistical features.

---

## 📌 Motivation

Automatic text summarization helps reduce reading effort for long documents such as research papers, reports, and articles.  
This project was developed to understand and practically implement a **feature-based clustering approach** to extractive summarization, as proposed in academic literature.

The focus is on:
- simplicity
- explainability
- alignment with classical NLP research methods

---

## 🧠 Methodology

The summarization process follows these steps:

1. **Sentence Segmentation**  
   The input document is split into individual sentences.

2. **Feature Extraction (TF-IDF)**  
   Each sentence is converted into a TF-IDF vector to capture word importance.

3. **Sentence Clustering**  
   Sentences are grouped using **K-Means clustering** to represent different topics and reduce redundancy.

4. **Feature-Based Ranking**  
   Each sentence is scored using:
   - TF-IDF score (semantic importance)
   - Sentence position score
   - Sentence length normalization

5. **Cluster-wise Sentence Selection**  
   The highest-scoring sentence from each cluster is selected.

6. **Summary Generation**  
   Top-ranked sentences are combined while preserving original order to produce the final extractive summary.

---

## 📂 Supported Input Formats

- `.txt` — Text files  
- `.pdf` — Text-based PDF documents  
- `.docx` — Microsoft Word documents  

> Note: Scanned PDFs without selectable text are not supported.

---

## ▶️ How to Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
