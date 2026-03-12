import pickle
import os
from preprocessing import load_and_preprocess
from calculate import get_sentence_probability, generate_sentence

def main():
    # 1. Định nghĩa đường dẫn và huấn luyện
    corpus_path = "corpus-title/corpus-title.txt"
    model_file = "ngram_model.pkl"

    # Kiểm tra xem đã có mô hình lưu sẵn chưa
    if os.path.exists(model_file):
        print("--- Đang tải mô hình đã lưu ---")
        with open(model_file, 'rb') as f:
            unigrams, bigrams, vocab = pickle.load(f)
    else:
        print("--- Đang huấn luyện mới ---")
        unigrams, bigrams, vocab = load_and_preprocess(corpus_path)
        # Lưu lại để lần sau dùng
        with open(model_file, 'wb') as f:
            pickle.dump((unigrams, bigrams, vocab), f)
            # Lọc bỏ những unigram xuất hiện ít hơn 2 lần để dọn rác
        vocab = [word for word in vocab if unigrams[word] > 3]
    V = len(vocab)
    print(f"Hoàn tất! Kích thước từ vựng: {V}\n")

    # 2. Tính xác suất câu mẫu
    test_str = "Hôm nay trời đẹp lắm"
    prob = get_sentence_probability(test_str, unigrams, bigrams, V)
    print(f"Xác suất của câu '{test_str}': {prob:.10f}\n")

    # 3. Sinh câu ngẫu nhiên
    print("--- 5 câu được sinh ra từ mô hình ---")
    for i in range(5):
        sent = generate_sentence(unigrams, bigrams, vocab)
        print(f"{i+1}. {sent}")

if __name__ == "__main__":
    main()