import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.tokenize import sent_tokenize
import nltk


# ensure tokenizer is available
nltk.download('punkt', quiet=True)


def summarize(text, num_clusters=4, summary_ratio=0.25):
    sentences = sent_tokenize(text)
    if len(sentences) < 5:
        return text

    tfidf = TfidfVectorizer(stop_words="english")
    X = tfidf.fit_transform(sentences)

    k = min(num_clusters, max(1, len(sentences) // 2))
    clusters = KMeans(n_clusters=k, random_state=42).fit_predict(X)

    tfidf_score = X.sum(axis=1).A1
    position_score = np.array([1 / (i + 1) for i in range(len(sentences))])
    length_score = np.array([len(s.split()) for s in sentences])
    if length_score.max() > 0:
        length_score = length_score / length_score.max()

    final_score = tfidf_score + position_score + length_score

    selected = []
    for c in range(k):
        idx = np.where(clusters == c)[0]
        if len(idx):
            selected.append(idx[np.argmax(final_score[idx])])

    n_summary = max(1, int(len(sentences) * summary_ratio))
    selected = sorted(selected, key=lambda i: final_score[i], reverse=True)
    selected = sorted(selected[:n_summary])

    return " ".join(sentences[i] for i in selected)
