# 🤖 CAPTCHA Solver – Kết hợp Python GPT + Power Automate Desktop (PAD)

## 🧠 Mục tiêu

Giải tự động **CAPTCHA dạng lưới hình ảnh (reCAPTCHA)** bằng cách:
- Dùng Python + GPT-4o để phân tích đề bài và hình ảnh
- Dùng Power Automate Desktop (PAD) để **tự động click vào các ô** đúng

---

## 🧩 Thành phần hệ thống

| Thành phần | Vai trò |
|------------|---------|
| `captchaGPT.py` | Script Python giải CAPTCHA bằng GPT |
| `CaptchaRPA.txt` | Mô tả chi tiết flow RPA của PAD để xử lý ảnh và thực hiện click |
| `img/captcha7.png` | Ảnh CAPTCHA đầu vào |
| `result.txt` | File chứa kết quả GPT trả về: các ô cần chọn |

---

## ⚙️ Cấu trúc hoạt động của `captchaGPT.py`

1. **Tách đề bài (instruction)**:
   - Dùng Tesseract OCR đọc phần đầu ảnh (khoảng 130px) để trích xuất câu hỏi.

2. **Chuyển ảnh thành base64**:
   - Chuyển toàn bộ ảnh CAPTCHA thành chuỗi base64 để gửi cho GPT.

3. **Gửi lên GPT-4o**:
   - Câu hỏi và ảnh được gửi vào GPT dưới dạng **input hình ảnh và văn bản**.
   - GPT trả về danh sách các ô phù hợp, ví dụ: `1,3,7`.

4. **Ghi kết quả vào `result.txt`**:
   - Chuỗi số được lưu để PAD đọc và xử lý click.

---

## 🔁 Flow làm việc của RPA (Power Automate Desktop)

Nội dung được mô tả chi tiết trong `CaptchaRPA.txt`, tóm tắt như sau:

### 1. **Chụp ảnh CAPTCHA**

- PAD chụp ảnh vùng chứa CAPTCHA
- Lưu ảnh thành `captcha7.png` trong thư mục `img/`

### 2. **Gọi script Python**

Run Python Script: captchaGPT.py
PAD chạy captchaGPT.py để phân tích ảnh

Script tạo ra result.txt chứa chuỗi số ô cần click

### 3. Đọc kết quả từ result.txt
PAD đọc nội dung file, tách thành danh sách số

### 4. Click vào các ô CAPTCHA
Mỗi ô trong ảnh CAPTCHA ứng với vị trí (1 → 9)

PAD dùng hành động “Click UI Element” hoặc tọa độ tương ứng với từng số được GPT chọn

### 5. Xác nhận kết quả
PAD nhấn nút “Xác minh” hoặc “Tiếp tục”

Nếu CAPTCHA hiện thêm ảnh → lặp lại bước 1

▶️ Cách sử dụng
A. Cài đặt Python + GPT
bash
Sao chép
Chỉnh sửa
pip install openai pytesseract pillow
Cài thêm Tesseract OCR theo hệ điều hành của bạn.

B. Cấu hình OpenAI
Trong captchaGPT.py, điền API key:

python
Sao chép
Chỉnh sửa
client = OpenAI(api_key="sk-...")
C. Chạy thủ công (test trước khi tích hợp PAD)
bash
Sao chép
Chỉnh sửa
python captchaGPT.py
Sau đó kiểm tra result.txt, ví dụ:

text
Sao chép
Chỉnh sửa
2,4,5
📌 Ghi chú kỹ thuật
Ảnh CAPTCHA nên gồm cả đề bài (instruction) và lưới

Cần điều chỉnh kích thước crop() nếu layout bị lệch

PAD nên map số ô với vị trí cố định để click chính xác

Số ô	Vị trí
1 → 3	hàng đầu
4 → 6	hàng giữa
7 → 9	hàng dưới


📎 Tài liệu kèm theo
CaptchaRPA.txt: Mô tả đầy đủ flow PAD để chạy cùng với script

img/captcha7.png: Mẫu ảnh CAPTCHA dùng để test

result.txt: Kết quả GPT output (để PAD click theo)

