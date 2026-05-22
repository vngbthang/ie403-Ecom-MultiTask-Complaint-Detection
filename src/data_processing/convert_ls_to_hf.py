import json
import os
import sys
from sklearn.model_selection import train_test_split

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def convert_label_studio_to_hf(input_path, train_path, test_path):
    dataset = []
    
    # Đọc dữ liệu: Đọc file JSONL đầu vào một cách an toàn
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                    
                # Trích xuất văn bản gốc (text)
                text = record.get('text', '')
                if not text:
                    continue
                    
                # Chú ý: Đề phòng trường hợp text đã là dạng list (đã tokenized sẵn),
                # ta chuyển về lại dạng string để demo đúng yêu cầu Character-level.
                if isinstance(text, list):
                    text = " ".join(text)
                    
                # Tạo một mảng gán nhãn 'O' cho toàn bộ các ký tự trong câu.
                char_labels = ['O'] * len(text)
                
                # Dựa vào danh sách annotations (chứa start, end, labels),
                # đắp nhãn B-COMP hoặc I-COMP đè lên mảng ký tự tương ứng.
                annotations = record.get('annotations', [])
                
                # Hỗ trợ thêm format doccano (phòng hờ) nếu trường là 'label'
                if not annotations and 'label' in record:
                    for ann in record['label']:
                        # Bỏ qua nếu label đã là BIO tags thay vì offset (như trong file hiện tại)
                        if isinstance(ann, str): 
                            break
                        if isinstance(ann, list) and len(ann) >= 2:
                            start, end = ann[0], ann[1]
                            if start < len(char_labels) and end <= len(char_labels):
                                char_labels[start] = 'B-COMP'
                                for i in range(start + 1, end):
                                    char_labels[i] = 'I-COMP'
                else:
                    for ann in annotations:
                        start = ann.get('start')
                        end = ann.get('end')
                        if start is not None and end is not None:
                            char_labels[start] = 'B-COMP'
                            for i in range(start + 1, end):
                                char_labels[i] = 'I-COMP'
                                
                # Dùng split() để tách câu thành các từ (tokens) dựa trên khoảng trắng.
                tokens = []
                ner_tags = []
                current_idx = 0
                
                for token in text.split():
                    # Chiếu ngược lại vị trí ký tự gốc bằng hàm find
                    start_idx = text.find(token, current_idx)
                    end_idx = start_idx + len(token)
                    
                    # Lấy nhãn cho toàn bộ token đó
                    token_label = 'O'
                    for i in range(start_idx, end_idx):
                        if char_labels[i] != 'O':
                            if char_labels[i] == 'B-COMP':
                                token_label = 'B-COMP'
                                break  # Ưu tiên B-COMP nếu token chứa ký tự B-COMP
                            if token_label == 'O':
                                token_label = 'I-COMP'
                                
                    tokens.append(token)
                    ner_tags.append(token_label)
                    
                    # Cập nhật vị trí tìm kiếm cho token tiếp theo
                    current_idx = end_idx
                    
                # Đóng gói: Lưu trữ kết quả (bỏ qua những câu không hợp lệ hoặc bị rỗng)
                # Câu không có từ nào bôi đen (tất cả là 'O') vẫn được đóng gói thành công
                if tokens:
                    dataset.append({
                        "tokens": tokens,
                        "ner_tags": ner_tags
                    })
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {input_path}")
        return

    if not dataset:
        print("Không có dữ liệu hợp lệ để xử lý.")
        return

    # Chia tập dữ liệu: Train (80%) và Test (20%) với random_state=42
    train_data, test_data = train_test_split(dataset, test_size=0.2, random_state=42)
    
    # Đảm bảo thư mục đầu ra tồn tại
    os.makedirs(os.path.dirname(train_path), exist_ok=True)
    
    # Lưu file: Ghi kết quả ra 2 file JSON với ensure_ascii=False và indent=2
    with open(train_path, 'w', encoding='utf-8') as f:
        json.dump(train_data, f, ensure_ascii=False, indent=2)
        
    with open(test_path, 'w', encoding='utf-8') as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)
        
    print("----- HOÀN TẤT CHUYỂN ĐỔI -----")
    print(f"Tổng số câu: {len(dataset)}")
    print(f"Số câu tập Train: {len(train_data)} - Lưu tại: {train_path}")
    print(f"Số câu tập Test: {len(test_data)} - Lưu tại: {test_path}")

def main():
    input_file = r"c:\Users\Thang Vu\Documents\ie403-Ecom-MultiTask-Complaint-Detection\data\processed\bio_annotations_final.jsonl"
    train_file = r"c:\Users\Thang Vu\Documents\ie403-Ecom-MultiTask-Complaint-Detection\data\processed\ner_train.json"
    test_file = r"c:\Users\Thang Vu\Documents\ie403-Ecom-MultiTask-Complaint-Detection\data\processed\ner_test.json"
    
    convert_label_studio_to_hf(input_file, train_file, test_file)

if __name__ == "__main__":
    main()
