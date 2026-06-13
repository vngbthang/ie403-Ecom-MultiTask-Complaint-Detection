# Mapping rewrite bao cao ACL cu sang huong UIT-ViOCD complaint span extraction

## Nguon tham chieu

- Bao cao cu: `docs/old_report_acl.tex`
- Dan y moi: `docs/report_revision_outline.md`
- Bang ket qua NER moi: `outputs/metrics/summary/ner_experiment_summary.md`
- So lieu chinh cho bao cao: `outputs/metrics/summary/report_key_numbers.md`

## Muc tieu rewrite

Bao cao moi can chuyen tu cau chuyen cu:

Shopee Reviews classification + NER BIO subset nho + Multi-task PhoBERT + CRF

sang cau chuyen moi:

UIT-ViOCD-only -> review-level complaint label limitation -> AI-assisted complaint span annotation -> validation / offset repair / overlap resolving / BIO conversion -> PhoBERT NER voi class-weighted CrossEntropyLoss -> ket qua tren full AI-assisted complaint span dataset.

## Mapping tung phan

| Old section | Current content summary | New section | Action | Reason | Rewrite instruction |
|---|---|---|---|---|---|
| Title | `A Multi-task Learning Approach for Vietnamese Complaint Detection and Complaint Span Extraction in E-commerce Reviews` | Title moi | REWRITE | Title cu dat Multi-task lam phuong phap chinh, khong con dung voi huong moi. | Doi thanh: "Nhan dien va rut trich vung khieu nai trong danh gia thuong mai dien tu tieng Viet bang PhoBERT va quy trinh gan nhan ho tro boi AI". Neu bao cao viet tieng Anh, dich sat nghia va giu trong tam AI-assisted span annotation + PhoBERT NER. |
| Abstract | Noi ve Shopee dataset, manually annotated BIO subset, LinearSVM classification, Multi-task PhoBERT + CRF Entity-F1 0.3279. | Abstract | REWRITE | Gan nhu toan bo abstract cu la cau chuyen cu. | Viet lai 4 phan: boi canh UIT-ViOCD chi co review-level label; phuong phap AI-assisted span annotation va quality control; PhoBERT NER voi weighted loss; ket qua Pilot100 unweighted 0.0000, Pilot100 weighted 0.1370, Full weighted 0.8455. Neu de cap limitation, noi ro span labels la AI-assisted. |
| Introduction | Dong luc complaint detection va ly do can span extraction; sau do gioi thieu Multi-task PhoBERT + CRF. | Ch. 1. Gioi thieu | REWRITE | Motivation ve span extraction con dung, nhung phuong phap va contribution cu khong dung. | Giu phan dong luc ve complaint review, informal Vietnamese, mixed sentiment va can biet "khieu nai nam o dau". Viet lai muc tieu: chi dung UIT-ViOCD, mo rong tu review-level classification sang complaint span extraction. Contribution moi: chuan hoa UIT-ViOCD, xay dung AI-assisted annotation pipeline, tao full complaint span dataset 2854 records, train PhoBERT NER weighted. |
| Related Work | Complaint detection, UIT-ViOCD classification, PhoBERT, BIO tagging, Multi-task learning. | Ch. 2. Co so ly thuyet va nghien cuu lien quan | REWRITE | Mot so nen tang con dung, Multi-task khong con la trong tam. | Giu complaint detection, UIT-ViOCD, PhoBERT, BIO tagging. Giam hoac chuyen Multi-task learning thanh huong phat trien, khong trinh bay nhu phuong phap chinh. Them AI-assisted annotation, data quality control, class imbalance trong NER, weighted CrossEntropy. |
| Dataset | Shopee Reviews 7,817 samples, rating-derived labels, UIT-ViOCD chi la reference, BIO subset 400/100, NER-matched subset 189. | Ch. 3. Phan tich du lieu UIT-ViOCD | REWRITE | Dataset cu khong con la dataset chinh; Shopee/rating mapping phai bo. | Viet lai hoan toan theo UIT-ViOCD: raw schema `review`, `review_tokenize`, `label`, `domain`; processed schema `id`, `review`, `review_tokenize`, `complaint_label`, `domain`, `split`; train 4387, val 548, test 549; complaint candidates train 2292, val 283, test 279; total complaint candidates 2854. |
| Dataset table | Bang cu: Shopee Reviews 6253/1564, NER BIO subset 400/100, NER-matched 189/100. | Bang thong ke dataset moi | DROP | Bang cu dua Shopee va subset khong con dung. | Thay bang bang UIT-ViOCD processed split va bang full complaint span dataset: 2854 records, records_with_spans 2773, records_without_spans 81, total spans 10195, total tokens 109783, domain distribution app/cosmetic/fashion/mobile. |
| Data Annotation and Label Construction | Mo ta manual BIO annotation, complaint span shortest phrase, BIO tags, small dataset motivates multi-task. | Ch. 4. AI-assisted span annotation va BIO conversion | REWRITE | Dinh nghia complaint span va BIO con dung, nhung quy trinh manual/small dataset/MTL motivation khong dung. | Giu dinh nghia complaint span va BIO labels. Viet lai thanh AI-assisted annotation: prompt guideline, output JSONL `id`, `text`, `spans`, `reason`; span phai la substring; `start/end` theo Python slicing. Them quy tac rut gon span va manual review mot phan. |
| Methodology | Tong quan multi-task: classification + NER. | Ch. 4. Phuong phap de xuat | REWRITE | Huong moi la pipeline annotation + PhoBERT NER single-task weighted, khong phai MTL chinh. | Doi Methodology thanh pipeline: prepare UIT-ViOCD, select complaint candidates, AI annotation, validation, repair, overlap resolving, BIO conversion, split, PhoBERT NER weighted. |
| Problem Formulation | Multi-task formulation voi `y_c` classification va `y_s` BIO. | Problem formulation moi | REWRITE | Classification label van la nguon loc/boi canh, nhung model thuc nghiem hien tai la NER complaint span. | Formulate chinh: voi complaint review `x = {w_i}`, du doan BIO sequence `y = {t_i}`, `t_i in {O, B-COMP, I-COMP}`. Co the noi review-level label UIT-ViOCD duoc giu de xac dinh complaint candidates, nhung span extraction la task thuc nghiem chinh. |
| Baseline Methods | TF-IDF Logistic Regression/LinearSVM/Naive Bayes classification; PhoBERT Linear/CRF NER baselines. | Experiments / baselines | DROP | Classification baselines tren Shopee khong con nam trong pipeline chinh; CRF baseline cu khong phai ket qua moi. | Bo bang/ket qua Shopee classification. Neu muon co baseline, chi giu Pilot100 unweighted vs weighted vs full weighted theo bang summary moi. |
| Proposed Multi-task Architecture | PhoBERT shared encoder, classification head, linear + CRF sequence head; Figure Multi-task PhoBERT + CRF. | PhoBERT NER architecture | REWRITE | Kien truc chinh moi la PhoBERT token classification voi class-weighted CrossEntropyLoss. | Thay figure multi-task bang figure pipeline PhoBERT NER: input tokens -> PhoBERT tokenizer/subwords -> PhoBERT encoder -> token classifier -> BIO labels. Neu de cap CRF/MTL, dua vao future work. |
| Training Objective | `L = L_cls + alpha L_ner`; CRF negative log-likelihood; alpha 1.0/2.0. | Training objective moi | REWRITE | Loss cu khong dung voi thuc nghiem moi. | Viet CrossEntropy cho token classification voi `ignore_index=-100`. Them class-weighted CrossEntropyLoss: `weight_c = total_labeled_tokens / (num_classes * count_c)`. Noi ro mask evaluation/loss chi tinh labels != -100. |
| Implementation Details | PyTorch/HF, shared encoder, classification labels, missing NER, CRF, Streamlit post-processing. | Implementation details moi | REWRITE | Phan tool/framework con dung, nhung shared MTL/CRF/demo checkpoint cu khong dung. | Giu PyTorch, Transformers, `vinai/phobert-base-v2`, Kaggle GPU. Them scripts pipeline, validation/repair/overlap, no-save-checkpoint, weighted loss, prediction CSV alignment. Bo noi dung missing NER supervision va `--only-ner-matched`. |
| Experiments | Shopee classification experiments, NER baselines, MTL PhoBERT+CRF alpha 1/2, NER-matched subset 189. | Ch. 5. Thuc nghiem va danh gia | REWRITE | Setup cu khong phu hop voi data/phuong phap moi. | Viet lai voi 3 thuc nghiem: Pilot100 Unweighted PhoBERT NER, Pilot100 Weighted PhoBERT NER, Full Complaint Weighted PhoBERT NER. Dua split full: train 2280, val 283, test 291. Metrics: Entity P/R/F1, Token-F1 macro, avg loss. |
| Experimental setup table | Backbone, batch size, LR, NER epochs, Multi-task epochs, alpha, classification test size, NER test size. | Bang setup moi | REWRITE | Alpha/MTL/classification test cu khong dung. | Thay bang: backbone PhoBERT-base-v2, labels O/B-COMP/I-COMP, loss CrossEntropy/Weighted CrossEntropy, learning rate 2e-5, batch size 8, epochs 3/7/5 theo experiment, Kaggle GPU, full split train/val/test. |
| Result Analysis | Tong hop classification va NER cu. | Ch. 5. Ket qua va phan tich | REWRITE | Ket qua cu khong dung voi huong moi. | Tap trung vao vi sao Pilot100 unweighted predict O, weighted loss cai thien, full data tang Entity-F1 len 0.8455. Giai thich vai tro mo rong annotation va class weights. |
| Classification Results | LinearSVM/LogReg/NB tren Shopee, Macro-F1 0.9428. | None or background only | DROP | Khong dung Shopee/rating mapping trong pipeline chinh moi. | Xoa bang classification Shopee va figure `f1_comparison_Shopee.png`. Neu can classification label, chi noi UIT-ViOCD co label review-level de loc complaint candidates, khong bao cao ket qua Shopee. |
| NER Results | PhoBERT Linear/CRF very low; MTL PhoBERT+CRF Entity-F1 0.3279, Token-F1 0.6627. | NER experiment results moi | REWRITE | Ket qua chinh moi la weighted PhoBERT NER tren full AI-assisted dataset. | Thay bang cu bang 3 dong: Pilot100 Unweighted Entity-F1 0.0000, Pilot100 Weighted 0.1370, Full Complaint Weighted 0.8455. Dung so trong `outputs/metrics/summary/ner_experiment_summary.md`. |
| NER figures | Entity-F1/Token-F1 comparison of MTL alpha configs. | Figure ket qua moi | REWRITE | Figure cu so sanh alpha MTL khong con dung. | Tao/ve lai bieu do Entity F1 va Token F1 cho 3 experiment moi. Neu chua tao hinh, de bang ket qua la du. |
| Error Analysis | Classification FP/FN Shopee; NER boundary/missed errors for old baselines. | Error analysis moi | REWRITE | Classification error Shopee phai bo; boundary ambiguity con dung. | Bo Shopee FP/FN. Viet lai theo huong: Pilot100 unweighted bias to O; class weights giup du doan COMP; span boundary ambiguity; AI-assisted label noise; possible errors from long spans, implicit complaints, noisy Vietnamese. |
| NER error table | Boundary/Missed/Spurious/Correct for Linear/CRF old baselines. | Optional qualitative error analysis | DROP | Table cu khong lien quan ket qua moi. | Neu co predictions CSV full, tao bang moi sau; neu chua co error analysis day du, khong giu bang cu. |
| Qualitative Discussion | Noi model bat duoc vung chung nhung sai boundary, mixed sentiment, implicit complaint. | Qualitative discussion moi | KEEP | Nhan xet ve boundary va mixed sentiment van co gia tri. | Giu tinh than, viet lai gan voi AI-assisted full dataset va PhoBERT NER weighted. Them canh bao exact span Entity-F1 rat nhay voi boundary. |
| Demo System and Reproducibility | Streamlit demo classification + span extraction using MTL checkpoint. | Reproducibility / optional demo | DROP | Demo cu dua vao MTL checkpoint va classification branch; neu demo khong con la noi dung chinh thi khong nen giu. | Bo Streamlit demo khoi bao cao chinh, hoac chi giu 1 doan reproducibility ve scripts/data pipeline neu giao vien yeu cau. Khong trinh bay demo MTL cu. |
| Conclusion and Future Work | Ket luan MTL PhoBERT + CRF, Shopee LinearSVM, alpha=1/2, future expand BIO/active learning. | Ch. 6. Ket luan va huong phat trien | REWRITE | Ket luan cu dua ket qua/phuong phap cu. | Viet lai: da chuan hoa UIT-ViOCD, xay dung AI-assisted complaint span dataset 2854 complaint reviews, quality control, BIO conversion, PhoBERT weighted NER dat Entity-F1 0.8455. Future: human review toan bo, CRF/constrained decoding, multitask classification+NER sau khi co du lieu span on dinh. |
| Limitations | Small BIO dataset 400/100, matched subset 189, Shopee rating label noise. | Limitations moi | REWRITE | Limitation cu khong con dung; can trung thuc ve AI-assisted labels. | Ghi ro: Full span labels are AI-assisted annotations, not fully human gold-standard labels. Automatic validation, offset repair, overlap resolving and partial manual review were used. Results should be interpreted on constructed AI-assisted dataset. Can human review nhieu hon neu muon benchmark chuan. |
| References | `viocd2021`, `phobert2020`, `roberta2019`, `caruana1997multitask`, co the co references cu ve MTL/CRF. | References cleanup | REWRITE | References phai khop cau chuyen moi. | Giu UIT-ViOCD, PhoBERT, RoBERTa/BERT, BIO/NER neu co. Xem lai references ve Multi-task/CRF: neu chi la future/related work thi de lai it hon; them references ve AI-assisted annotation/class imbalance neu co nguon phu hop. |

## Phan can DROP ro rang

- Shopee review dataset la classification dataset chinh.
- Rating-derived classification labels.
- Bang va hinh ket qua classification tren Shopee: LinearSVM, Logistic Regression, Naive Bayes.
- NER BIO subset 400 train / 100 test nhu dataset chinh.
- NER-matched subset 189.
- `--only-ner-matched` la setting thuc nghiem chinh.
- Multi-task PhoBERT + CRF la phuong phap chinh.
- Loss `L = L_cls + alpha L_ner` va alpha=1.0/2.0 nhu ket qua chinh.
- Ket qua cu: MTL PhoBERT + CRF Entity-F1 0.3279, Token-F1 0.6627 nhu main result.
- Streamlit demo dua tren checkpoint MTL cu neu khong cap nhat demo theo pipeline moi.

## Phan co the KEEP hoac REWRITE

- Motivation ve can rut trich complaint span thay vi chi classification.
- Thach thuc cua review tieng Viet: informal language, spelling variation, abbreviations, emojis, mixed sentiment, implicit complaint.
- Gioi thieu UIT-ViOCD nhu dataset complaint detection tieng Viet, nhung nhan manh han che review-level label.
- Giai thich BIO tagging voi `O`, `B-COMP`, `I-COMP`.
- Nen tang PhoBERT cho tieng Viet.
- Label alignment voi `-100` cho special tokens/subwords trong training/evaluation.
- Entity-F1 va Token-F1 explanation.
- Nhan xet ve ambiguous span boundaries.
- Reproducibility theo scripts pipeline, nhung khong giu noi dung demo MTL cu.

## Phan ADD_NEW bat buoc

- UIT-ViOCD-only dataset description.
- Schema raw va processed UIT-ViOCD.
- Complaint candidates: train 2292, val 283, test 279, total 2854.
- AI-assisted annotation pipeline.
- Annotation guideline va quy tac rut gon span.
- Output schema annotation: `id`, `text`, `spans`, `reason`.
- Offset validation.
- Offset repair.
- Overlap resolving.
- BIO conversion.
- Full complaint span dataset statistics:
  - total records: 2854
  - records with spans: 2773
  - records without spans: 81
  - total spans: 10195
  - total tokens: 109783
  - COMP token count: 82497
  - COMP token ratio: 0.7515
  - domain distribution: app 1510, cosmetic 475, fashion 732, mobile 137
- Train/val/test split full NER:
  - train: 2280 records, 87726 tokens, 65946 COMP tokens
  - val: 283 records, 10569 tokens, 8015 COMP tokens
  - test: 291 records, 11488 tokens, 8536 COMP tokens
- PhoBERT NER token classification.
- Class-weighted CrossEntropyLoss:

```text
weight_c = total_labeled_tokens / (num_classes * count_c)
```

- Ket qua pilot100 experiments:
  - Pilot100 Unweighted: Entity F1 = 0.0000, Token F1 = 0.3002, Avg loss = 0.6437
  - Pilot100 Weighted: Entity F1 = 0.1370, Token F1 = 0.5845, Avg loss = 0.3660
- Ket qua full complaint weighted experiment:
  - Entity Precision = 0.7937
  - Entity Recall = 0.9045
  - Entity F1 = 0.8455
  - Token F1 macro = 0.8620
  - Avg loss = 0.2486
- Honest limitations about AI-assisted labels.

## Rewrite order recommendation

1. Abstract
2. Introduction
3. Dataset
4. Methodology
5. Experiments
6. Results
7. Limitations
8. Conclusion
9. Related Work cleanup
10. References cleanup

## Checklist

### Tables to update

- Bang thong ke UIT-ViOCD processed theo split va complaint label.
- Bang complaint candidates theo split.
- Bang domain distribution cua full complaint span dataset.
- Bang BIO label mapping.
- Bang annotation pipeline statistics: pilot100, batch200, remaining full batches, full dataset.
- Bang full NER train/val/test split.
- Bang NER experiment results moi.
- Bang limitations va mitigation neu can.

### Figures to update

- Pipeline tong quan: raw UIT-ViOCD -> processed -> complaint candidates -> AI annotation -> validation/repair/overlap resolving -> BIO -> PhoBERT NER.
- Vi du review-level label vs complaint span labels.
- Flow validation / offset repair / overlap resolving.
- BIO conversion illustration.
- PhoBERT token classification architecture.
- Entity F1 comparison cho 3 experiment moi.
- Token F1 macro comparison cho 3 experiment moi.

### Results to remove

- LinearSVM / Logistic Regression / Naive Bayes classification results tren Shopee.
- Shopee classification Macro-F1 0.9428 va Complaint-F1 0.9470 nhu ket qua chinh.
- PhoBERT + Linear NER 0.0194 va PhoBERT + CRF 0.0170 tren BIO subset cu neu khong con reproduce trong pipeline moi.
- MTL PhoBERT + CRF alpha=1.0/2.0 Entity-F1 0.3279/0.3244 nhu ket qua chinh.
- Error table cu cho Linear NER / CRF NER.
- Claim ve NER-matched subset 189.

### Results to add

- Pilot100 Unweighted PhoBERT NER: Entity F1 0.0000, Token F1 0.3002, Avg loss 0.6437.
- Pilot100 Weighted PhoBERT NER: Entity F1 0.1370, Token F1 0.5845, Avg loss 0.3660.
- Full Complaint Weighted PhoBERT NER: Entity Precision 0.7937, Entity Recall 0.9045, Entity F1 0.8455, Token F1 0.8620, Avg loss 0.2486.
- Full complaint span dataset statistics: 2854 records, 10195 spans, 109783 tokens, 82497 COMP tokens.
- Quality control results: validation pass, overlap warnings resolved to 0 before final merge.

### Claims to avoid

- Khong noi full span labels la human gold-standard.
- Khong noi Entity F1 = 0.8455 la benchmark chinh thuc cua UIT-ViOCD goc.
- Khong noi mo hinh giai quyet hoan toan bai toan.
- Khong noi AI annotation hoan toan chinh xac.
- Khong noi Shopee dataset la dataset chinh nua.
- Khong noi Multi-task PhoBERT + CRF la phuong phap chinh cua ban moi.
- Khong noi ket qua tren AI-assisted span dataset tuong duong voi ket qua tren gold-standard human annotation.

