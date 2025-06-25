import base64
from PIL import Image
import pytesseract
from openai import OpenAI
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

CAPTCHA_IMAGE_PATH = "img/captcha7.png"
RESULT_PATH = "result.txt"

if not os.path.exists(CAPTCHA_IMAGE_PATH):
    print("❌ Không tìm thấy ảnh CAPTCHA.")
    exit(1)

image = Image.open(CAPTCHA_IMAGE_PATH)

instruction_img = image.crop((0, 0, image.width, 130))  

try:
    instruction_text = pytesseract.image_to_string(instruction_img, lang="vie").strip()
except Exception as e:
    print("❌ OCR lỗi:", e)
    instruction_text = ""

if not instruction_text:
    instruction_text = "Chọn tất cả hình ảnh có xe đạp"
    print("⚠️ Không đọc được đề bài, dùng fallback:", instruction_text)
else:
    print("✅ Đề bài OCR được:", instruction_text)

client = OpenAI(api_key="...")  # <- Thay bằng API key của bạn

with open(CAPTCHA_IMAGE_PATH, "rb") as img_file:
    base64_image = base64.b64encode(img_file.read()).decode("utf-8")

prompt = (
    f"Đây là ảnh CAPTCHA Google dạng lưới.\n"
    f"Câu hỏi: \"{instruction_text}\"\n"
    f"Lưới gồm 9 hoặc 16 ô, đánh số từ 1 đến N trái qua phải, trên xuống dưới.\n"
    f"Chỉ trả về duy nhất một danh sách số cách nhau bởi dấu phẩy, ví dụ: 2,4,9\n"
    f"Không mô tả, không giải thích, không dấu [] hay văn bản thừa."
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
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

raw_result = response.choices[0].message.content.strip()
cleaned_result = raw_result.replace("[", "").replace("]", "").replace(" ", "")

with open(RESULT_PATH, "w", encoding="utf-8") as f:
    f.write(cleaned_result)

print("✅ Kết quả GPT:", cleaned_result)
print("✅ Đã ghi vào result.txt")
