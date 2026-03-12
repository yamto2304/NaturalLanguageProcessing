Mô hình Ngôn ngữ Bigram cấp Âm tiết cho Tiếng Việt

Dự án này xây dựng một mô hình ngôn ngữ N-gram (Bigram) mức độ âm tiết dành cho tiếng Việt, phục vụ mục đích tính xác suất của câu và sinh văn bản tự động. Đây là bài tập thực hành trong phạm vi môn học Xử lý ngôn ngữ tự nhiên.

1. Cấu trúc dự án

preprocessing.py: Chứa các hàm đọc dữ liệu từ corpus, tiền xử lý văn bản (loại bỏ ký tự lạ, chuẩn hóa tiếng Việt) và thống kê tần suất Unigram/Bigram.

calculate.py: Chứa logic toán học của mô hình bao gồm tính xác suất câu sử dụng Log-probability và kỹ thuật làm trơn Laplace, cùng thuật toán sinh câu ngẫu nhiên.

main.py: Điểm điều khiển chính của chương trình, thực hiện huấn luyện, lưu trữ mô hình và hiển thị kết quả.

corpus-title/: Thư mục chứa dữ liệu huấn luyện (.txt).
Source: [Binhvq News Corpus](https://github.com/binhvq/news-corpus/blob/master/README.md)

ngram_model.pkl: File lưu trữ mô hình sau khi huấn luyện (tự động tạo ra).

2. Các kỹ thuật áp dụng

Tiền xử lý văn bản: Sử dụng biểu thức chính quy (Regex) để chỉ giữ lại các âm tiết tiếng Việt thuần túy, loại bỏ rác dữ liệu (số, mã, ký tự đặc biệt).

Thẻ biên giới câu: Sử dụng các ký hiệu <s> (bắt đầu câu) và </s> (kết thúc câu) để mô hình học được ngữ cảnh mở đầu và kết thúc.

Log-probability: Tính toán xác suất thông qua tổng các log thay vì tích các số thực để tránh hiện tượng Arithmetic Underflow (tràn số dưới).

Laplace Smoothing (Add-one): Kỹ thuật làm trơn giúp xử lý các cụm từ chưa từng xuất hiện trong tập huấn luyện, đảm bảo xác suất không bao giờ bằng 0.

Pruning: Loại bỏ các âm tiết xuất hiện quá ít (tần suất thấp) để giảm nhiễu và tối ưu kích thước từ vựng.

3. Hướng dẫn sử dụng

Yêu cầu
Python 3.x

Dữ liệu huấn luyện đặt tại: corpus-title/corpus-title.txt

Cách chạy
Mở terminal tại thư mục dự án và chạy lệnh:

Bash
python main.py

4. Kết quả thực nghiệm

Mô hình sau khi huấn luyện cho kết quả khả quan với:

Kích thước từ vựng: Khoảng ~33,000 âm tiết (sau khi lọc).

Xác suất câu mẫu: Câu "Hôm nay trời đẹp lắm" đạt giá trị log-prob ổn định (xấp xỉ -33.5).

Khả năng sinh câu: Mô hình có khả năng tạo ra các cụm từ có nghĩa, đặc biệt là các cụm từ mang tính chất tiêu đề tin tức.