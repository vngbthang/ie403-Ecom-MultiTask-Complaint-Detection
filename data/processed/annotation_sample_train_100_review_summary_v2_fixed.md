# Annotation Review Summary V2

## Global Summary

- Total records: `100`
- Warning records: `24`
- Likely OK: `23`
- Needs review: `1`

## Likely OK Warning Records

| id | tokens | comp_ratio | spans | max_span_len | warnings |
|---|---:|---:|---:|---:|---|
| `train_000589` | 4 | 75.0% | 1 | 3 | COMP ratio > 60% (75.0%) |
| `train_000645` | 71 | 0.0% | 0 | 0 | spans=[] nhưng cls_label=1 |
| `train_000709` | 74 | 0.0% | 0 | 0 | spans=[] nhưng cls_label=1 |
| `train_000828` | 10 | 90.0% | 2 | 5 | COMP ratio > 60% (90.0%) |
| `train_001184` | 7 | 85.7% | 2 | 4 | COMP ratio > 60% (85.7%) |
| `train_001698` | 8 | 0.0% | 0 | 0 | spans=[] nhưng cls_label=1 |
| `train_001731` | 3 | 66.7% | 1 | 2 | COMP ratio > 60% (66.7%) |
| `train_001735` | 4 | 100.0% | 1 | 4 | COMP ratio > 60% (100.0%) |
| `train_001836` | 7 | 100.0% | 2 | 4 | COMP ratio > 60% (100.0%) |
| `train_002070` | 82 | 0.0% | 0 | 0 | spans=[] nhưng cls_label=1 |
| `train_002107` | 4 | 100.0% | 1 | 4 | COMP ratio > 60% (100.0%) |
| `train_002774` | 17 | 76.5% | 1 | 13 | COMP ratio > 60% (76.5%) |
| `train_002798` | 13 | 61.5% | 2 | 4 | COMP ratio > 60% (61.5%) |
| `train_002814` | 8 | 87.5% | 2 | 4 | COMP ratio > 60% (87.5%) |
| `train_002844` | 6 | 66.7% | 1 | 4 | COMP ratio > 60% (66.7%) |
| `train_002940` | 17 | 64.7% | 1 | 11 | COMP ratio > 60% (64.7%) |
| `train_003263` | 4 | 100.0% | 1 | 4 | COMP ratio > 60% (100.0%) |
| `train_003285` | 18 | 77.8% | 1 | 14 | COMP ratio > 60% (77.8%) |
| `train_003334` | 7 | 100.0% | 2 | 4 | COMP ratio > 60% (100.0%) |
| `train_003497` | 22 | 0.0% | 0 | 0 | spans=[] nhưng cls_label=1 |
| `train_003566` | 10 | 70.0% | 2 | 4 | COMP ratio > 60% (70.0%) |
| `train_004184` | 5 | 100.0% | 1 | 5 | COMP ratio > 60% (100.0%) |
| `train_004263` | 6 | 83.3% | 1 | 5 | COMP ratio > 60% (83.3%) |

## Needs Review Records

| id | tokens | comp_ratio | spans | max_span_len | warnings | text | spans detail |
|---|---:|---:|---:|---:|---|---|---|
| `train_000054` | 73 | 31.5% | 5 | 7 | nhiều hơn 4 spans (5) | tôi rất thích game này nhưng càng lúc cấu hình game càng nặng, thật sự rất lag luôn, máy bên tôi lúc nào cũng trễ hơn bên đồng đội vài giây, có khi còn bị đứng ... | [29:61] `càng lúc cấu hình game càng nặng` (7 tok)<br>[71:83] `rất lag luôn` (3 tok)<br>[110:139] `trễ hơn bên đồng đội vài giây` (7 tok)<br>[152:164] `bị đứng hình` (3 tok)<br>[175:188] `chạy giật lùi` (3 tok) |
