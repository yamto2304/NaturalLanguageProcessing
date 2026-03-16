import nltk
from nltk.corpus import brown
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
import pandas as pd

# Tải tài nguyên
nltk.download('brown')
nltk.download('universal_tagset')
nltk.download('averaged_perceptron_tagger_eng')

# 1. Lấy dữ liệu chuẩn từ Brown (Gold Standard)
tagged_sentences = brown.tagged_sents(tagset='universal')
gold_labels = [tag for sent in tagged_sentences for word, tag in sent]
sentences_text = [[word for word, tag in sent] for sent in tagged_sentences]
all_words_flat = [word for sent in sentences_text for word in sent]

# 2. Khởi tạo 2 bộ Tagger khác nhau

# Tagger A: RegexpTagger (Gán nhãn dựa trên cấu trúc từ)
patterns = [
    (r'.*ing$', 'VERB'), (r'.*ed$', 'VERB'), (r'.*es$', 'VERB'),
    (r'.*ly$', 'ADV'), (r'.*able$', 'ADJ'), (r'.*s$', 'NOUN'),
    (r'.*', 'NOUN') # Mặc định vẫn là NOUN nếu không khớp luật nào
]
tagger_rule_based = nltk.RegexpTagger(patterns)

# Tagger B: Perceptron Tagger (Pre-trained ML model)
def get_perceptron_preds(sents):
    tagged_sents = nltk.pos_tag_sents(sents, tagset='universal')
    return [tag for sent in tagged_sents for word, tag in sent]

# 3. Thực hiện gán nhãn
print("--- Đang bắt đầu quá trình gán nhãn ---")
preds_a = [tag for word, tag in tagger_rule_based.tag(all_words_flat)]
preds_b = get_perceptron_preds(sentences_text)

# 4. Hàm tính toán thông số
def calculate_metrics(gold, pred):
    acc = accuracy_score(gold, pred)
    precision, recall, f1, _ = precision_recall_fscore_support(gold, pred, average='macro', zero_division=0)
    return acc, precision, recall, f1

metrics_a = calculate_metrics(gold_labels, preds_a)
metrics_b = calculate_metrics(gold_labels, preds_b)

# 5. LOG SO SÁNH CUỐI CÙNG
print("\n" + "="*50)
print("LOG SO SÁNH THÔNG SỐ POS TAGGER (BROWN CORPUS)")
print("="*50)

data = {
    "Chỉ số": ["Accuracy", "Precision (Macro)", "Recall (Macro)", "F1-Score (Macro)"],
    "Regexp Tagger (Rule-based)": [f"{m:.4f}" for m in metrics_a],
    "Perceptron Tagger (ML)": [f"{m:.4f}" for m in metrics_b]
}

df_log = pd.DataFrame(data)
print(df_log.to_string(index=False))
print("="*50)