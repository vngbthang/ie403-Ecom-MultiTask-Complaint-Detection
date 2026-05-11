"""
Split 500 annotation samples into 4 equal parts for team members
"""

import json

# Read all records
records = []
with open('data/processed/annotation_sample.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        records.append(json.loads(line))

total = len(records)
chunk_size = total // 4

# Split into 4 files
for idx, (name, start, end) in enumerate([
    ('A', 0, chunk_size),
    ('B', chunk_size, 2*chunk_size),
    ('C', 2*chunk_size, 3*chunk_size),
    ('D', 3*chunk_size, total)
], 1):
    filename = f'data/processed/annotation_sample_{name}.jsonl'
    with open(filename, 'w', encoding='utf-8') as f:
        for rec in records[start:end]:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    
    print(f"✅ Người {name}: samples {start}-{end-1} → {filename}")

print(f"\n📊 Tổng: {total} samples, mỗi người: ~{chunk_size} samples")
