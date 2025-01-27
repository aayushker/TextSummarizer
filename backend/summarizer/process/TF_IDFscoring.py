from sklearn.feature_extraction.text import TfidfVectorizer
from .extractTopSentences import summarize_text
from .preProcessing import preProcess_text

def score_sentences_tfidf(sentences):
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    
    # Sum up the TF-IDF scores of each word in the sentence
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        sentence_scores[sentence] = tfidf_matrix[i].sum()
    return sentence_scores

sentences, words = preProcess_text(text)
sentence_scores = score_sentences_tfidf(sentences)
summary = summarize_text(sentence_scores)
print(summary)
