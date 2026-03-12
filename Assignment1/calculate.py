import math
import random

def get_sentence_probability(sentence, unigrams, bigrams, vocab_size):
    sentence = sentence.lower().strip()
    tokens = ['<s>'] + sentence.split() + ['</s>']
    total_log_prob = 0
    
    for i in range(len(tokens) - 1):
        w_prev = tokens[i]
        w_curr = tokens[i+1]
        
        # Laplace Smoothing
        count_bigram = bigrams.get((w_prev, w_curr), 0)
        count_unigram = unigrams.get(w_prev, 0)
        prob = (count_bigram + 1) / (count_unigram + vocab_size)
        
        total_log_prob += math.log(prob)
    
    return total_log_prob

def generate_sentence(unigrams, bigrams, vocab, max_len=15):
    result = ['<s>']
    while result[-1] != '</s>' and len(result) < max_len:
        prev_word = result[-1]
        # Tránh chọn lại thẻ bắt đầu
        possible_next_words = [v for v in vocab if v != '<s>']
        
        # Tính trọng số cho việc chọn từ tiếp theo
        weights = []
        for w in possible_next_words:
            c_bigram = bigrams.get((prev_word, w), 0)
            c_unigram = unigrams.get(prev_word, 0)
            weights.append(c_bigram / (c_unigram + 1e-9))
        
        next_word = random.choices(possible_next_words, weights=weights, k=1)[0]
        result.append(next_word)
        
    return " ".join(result[1:-1])