import re

# Dictionary chuẩn hóa teencode cơ bản
TEENCODE_DICT = {
    "sp": "sản phẩm",
    "đt": "điện thoại",
    "ko": "không",
    "k": "không",
    "kg": "không",
    "khg": "không",
    "dc": "được",
    "đc": "được",
    "mik": "mình",
    "mk": "mình",
    "shop": "cửa hàng",
    "vs": "với",
    "r": "rồi",
    "rùi": "rồi",
    "ok": "tốt",
    "oke": "tốt",
    "cx": "cũng",
    "ntn": "như thế này",
}

def clean_vietnamese_text(text: str) -> str:
    """
    Hàm làm sạch và chuẩn hóa văn bản tiếng Việt.
    """
    if not isinstance(text, str):
        return ""
    
    # 1. Xóa thẻ HTML (ví dụ: <br>, <b>)
    text = re.sub(r'<.*?>', ' ', text)
    
    # 2. Chuyển về chữ thường (lowercase)
    text = text.lower()
    
    # 3. Giữ lại chữ cái, số, khoảng trắng và dấu câu quan trọng (. , ? !)
    # \w mặc định trong Python 3 sẽ bao gồm cả các ký tự unicode (tiếng Việt có dấu)
    text = re.sub(r'[^\w\s.,?!]', ' ', text)
    
    # 4. Loại bỏ khoảng trắng thừa
    text = re.sub(r'\s+', ' ', text).strip()
    
    # 5. Áp dụng chuẩn hóa teencode
    words = text.split()
    cleaned_words = [TEENCODE_DICT.get(word, word) for word in words]
    text = ' '.join(cleaned_words)
    
    # 6. Xóa khoảng trắng thừa đứng ngay trước dấu câu (ví dụ: "chậm ," -> "chậm,")
    text = re.sub(r'\s+([.,?!])', r'\1', text)
    
    return text
