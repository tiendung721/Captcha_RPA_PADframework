import base64
from PIL import Image
from openai import OpenAI
import os

# Đường dẫn file
CAPTCHA_IMAGE_PATH = "img\\captcha.png"
RESULT_PATH = "result.txt"

# Kiểm tra file đầu vào
if not os.path.exists(CAPTCHA_IMAGE_PATH):
    print("Không tìm thấy captcha.png")
    exit(1)



# Mã hóa ảnh
with open(CAPTCHA_IMAGE_PATH, "rb") as img_file:
    base64_image = base64.b64encode(img_file.read()).decode("utf-8")


# Gửi yêu cầu đến OpenAI
client = OpenAI(api_key="...") # Thay thế bằng API key của bạn

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        f"Đây là ảnh CAPTCHA reCAPTCHA dạng lưới.\n"
                        f"Hãy đọc yêu cầu của captcha và trả lời bằng một danh sách các ô cần chọn.\n"
                        "Lưới gồm 9 ô, đánh số từ 1 đến 9 (trái sang phải, trên xuống dưới).\n"
                        "Hoặc lưới gồm 16 ô, đánh số từ 1 đến 16 (trái sang phải, trên xuống dưới).\n"
                        "Chỉ trả về duy nhất một danh sách số, ví dụ: [1, 3, 6]."
                        "Không giải thích, không văn bản thêm."
                    )
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    max_tokens=100
)

# Trích kết quả
raw_result = response.choices[0].message.content.strip()

# Làm sạch: loại bỏ [ ] và khoảng trắng, giữ lại các số và dấu phẩy
cleaned_result = raw_result.replace("[", "").replace("]", "").replace(" ", "")

# Ghi ra file
with open(RESULT_PATH, "w", encoding="utf-8") as f:
    f.write(cleaned_result)

print("DONE")
