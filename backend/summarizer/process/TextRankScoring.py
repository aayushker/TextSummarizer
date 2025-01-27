import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def text_rank_summarization(sentences):
    # Vectorize sentences
    vectorizer = CountVectorizer().fit_transform(sentences)
    vectors = vectorizer.toarray()

    # Compute cosine similarity between sentences
    similarity_matrix = cosine_similarity(vectors)

    # Build a graph and rank sentences using PageRank
    graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(graph)

    # Rank sentences by their scores
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    # Extract the top sentences for the summary
    summary = " ".join([ranked_sentences[i][1] for i in range(3)])
    return summary