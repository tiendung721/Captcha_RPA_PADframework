# Captcha_RPA_PADframework
🎯 CAPTCHA Solver RPA Bot
Một hệ thống RPA (Robotic Process Automation) sử dụng Power Automate Desktop và mô hình GPT-4o của OpenAI để giải reCAPTCHA dạng hình ảnh lưới một cách tự động.

📂 Cấu trúc dự án
captcha.py
▸ Mã Python gửi ảnh CAPTCHA tới OpenAI GPT-4o và nhận về danh sách ô cần click (ví dụ: [1, 3, 6]).

CaptchaRPA.txt
▸ Flow của Power Automate Desktop thực hiện:

Mở trang mẫu chứa CAPTCHA

Hover, chụp ảnh CAPTCHA và lưu tại img/captcha.png

Gọi script captcha.py để xử lý ảnh

Đọc kết quả từ result.txt

Click vào các ô tương ứng dựa trên kết quả trả về

Xác minh CAPTCHA

🧠 Cách hoạt động
PAD chụp ảnh từ khung CAPTCHA và lưu thành captcha.png.

captcha.py mã hóa ảnh, gửi tới OpenAI GPT-4o với hướng dẫn cụ thể (số ô 1–9 hoặc 1–16).

GPT-4o trả về danh sách các ô nên chọn.

Kết quả được làm sạch và lưu vào result.txt.

PAD đọc danh sách, tự động click vào từng ô dựa theo chỉ số UIElement.

🛠 Yêu cầu
Python 3.x

Thư viện: openai, Pillow

Tài khoản và API key OpenAI (GPT-4o)

Power Automate Desktop (PAD)

🚀 Hướng dẫn sử dụng
Cấu hình đúng API key trong captcha.py.

Chạy flow trong Power Automate Desktop (CaptchaRPA.txt).

Quan sát quá trình tự động giải CAPTCHA:

Click vào checkbox

Chụp CAPTCHA

Phân tích ảnh bằng GPT-4o

Click vào các ô tương ứng

Nhấn “Xác minh”

⚠️ Cảnh báo
❗ Dự án chỉ mang tính nghiên cứu, học tập. Việc tự động hóa giải CAPTCHA có thể vi phạm điều khoản của một số nền tảng. Vui lòng sử dụng một cách có trách nhiệm.

