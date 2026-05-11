"""
Merge BIO Annotations from 4 Team Members
Run this AFTER all 4 people finish their annotations
"""

import json
import os
from pathlib import Path

def merge_annotations():
    """Merge all 4 annotated files into one"""
    
    output_files = {
        'A': 'data/processed/bio_annotations_A.jsonl',
        'B': 'data/processed/bio_annotations_B.jsonl',
        'C': 'data/processed/bio_annotations_C.jsonl',
        'D': 'data/processed/bio_annotations_D.jsonl',
    }
    
    all_annotations = []
    
    print("🔄 Đang gộp annotations từ 4 người...")
    print("=" * 60)
    
    for person, filepath in output_files.items():
        if os.path.exists(filepath):
            count = 0
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    all_annotations.append(json.loads(line))
                    count += 1
            
            print(f"✅ Người {person}: {count} annotations")
        else:
            print(f"⚠️  Người {person}: FILE CHƯA CÓ ({filepath})")
    
    print("=" * 60)
    print(f"\n📊 Tổng cộng: {len(all_annotations)} annotations")
    
    # Save merged file
    output_path = 'data/processed/bio_annotations_merged.jsonl'
    with open(output_path, 'w', encoding='utf-8') as f:
        for ann in all_annotations:
            f.write(json.dumps(ann, ensure_ascii=False) + '\n')
    
    print(f"✅ Đã lưu vào: {output_path}")
    
    # Summary statistics
    print("\n📈 THỐNG KÊ:")
    
    all_labels = []
    annotators = {}
    
    for ann in all_annotations:
        all_labels.extend(ann['labels'])
        annotator = ann.get('annotator', 'unknown')
        if annotator not in annotators:
            annotators[annotator] = 0
        annotators[annotator] += 1
    
    print("\n👥 Số lượng samples mỗi người:")
    for person in ['A', 'B', 'C', 'D']:
        count = annotators.get(person, 0)
        print(f"  Người {person}: {count}")
    
    print("\n🏷️  Phân bố labels:")
    label_counts = {}
    for label in all_labels:
        label_counts[label] = label_counts.get(label, 0) + 1
    
    for label in ["B-COMP", "I-COMP", "O"]:
        if label in label_counts:
            count = label_counts[label]
            pct = count / len(all_labels) * 100
            print(f"  {label}: {count} ({pct:.1f}%)")
    
    print("\n" + "=" * 60)
    print("✨ Gộp annotations thành công!")
    print("=" * 60)

if __name__ == "__main__":
    merge_annotations()
