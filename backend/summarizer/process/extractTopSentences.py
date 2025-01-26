def summarize_text(sentence_scores, num_sentences=3):
    # Sort sentences by score
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    
    # Pick top N sentences
    summary = " ".join(sorted_sentences[:num_sentences])
    return summary
