from collections import defaultdict

def score_sentences(sentences, words):
    # Calculate word frequency
    word_freq = defaultdict(int)
    for word in words:
        word_freq[word] += 1
    
    # Score sentences based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in sentence.split():
            if word.lower() in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = 0
                sentence_scores[sentence] += word_freq[word.lower()]
    return sentence_scores
