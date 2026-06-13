# NER Experiment Summary

| experiment_name | dataset | train_records | test_records | loss_type | epochs | entity_precision | entity_recall | entity_f1 | token_f1_macro | avg_loss | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pilot100 Unweighted PhoBERT NER | UIT-ViOCD pilot 100 | 100 |  | CrossEntropy | 3 | 0.0000 | 0.0000 | 0.0000 | 0.3002 | 0.6437 | model biased to O on small pilot data |
| Pilot100 Weighted PhoBERT NER | UIT-ViOCD pilot 100 | 100 |  | Weighted CrossEntropy | 7 | 0.0893 | 0.2941 | 0.1370 | 0.5845 | 0.3660 | class weights helped the model predict COMP labels but data size remained small |
| Full Complaint Weighted PhoBERT NER | UIT-ViOCD full AI-assisted complaint span dataset | 2280 | 291 | Weighted CrossEntropy | 5 | 0.7937 | 0.9045 | 0.8455 | 0.8620 | 0.2486 | best result after expanding annotation to all complaint reviews |
