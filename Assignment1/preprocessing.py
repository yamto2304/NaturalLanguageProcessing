import collections
import re

def load_and_preprocess(file_path):
    unigram_counts = collections.Counter()
    bigram_counts = collections.Counter()
    vocabulary = set()

    # Regex định nghĩa bảng chữ cái tiếng Việt thuần túy
    vietnamese_chars = r"a-záàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ"

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.lower().strip()
            
            # 1. Loại bỏ tất cả ký tự không phải chữ cái tiếng Việt và khoảng trắng
            line = re.sub(rf"[^{vietnamese_chars}\s]", " ", line)
            
            # 2. Loại bỏ các khoảng trắng thừa
            line = re.sub(r"\s+", " ", line).strip()
            
            if not line:
                continue

            # 3. Thêm token đặc biệt
            tokens = ['<s>'] + line.split() + ['</s>']
            
            # Lọc thêm: Chỉ đếm các từ có độ dài từ 1-7 ký tự (tránh rác dính liền)
            tokens = [t for t in tokens if len(t) <= 7 or t in ['<s>', '</s>']]

            # 4. Đếm tần suất
            for i in range(len(tokens)):
                unigram_counts[tokens[i]] += 1
                vocabulary.add(tokens[i])
                if i < len(tokens) - 1:
                    bigram_counts[(tokens[i], tokens[i+1])] += 1
                    
    return unigram_counts, bigram_counts, list(vocabulary)