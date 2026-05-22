"""
Train và evaluate các Classical Baseline Models cho binary complaint classification.
Huấn luyện TF-IDF + Logistic Regression, TF-IDF + Linear SVM, TF-IDF + Naive Bayes.

Dataset mặc định: data/processed/shopee_mapped.csv
Hỗ trợ: data/raw/UIT-ViOCD/train.csv, val.csv, test.csv

Output:
    outputs/metrics/classical_baselines.csv  - Bảng metrics tổng hợp
    outputs/figures/                         - Confusion matrix PNG cho từng model
"""
import os
import sys
import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.calibration import CalibratedClassifierCV

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.utils.utils import clean_vietnamese_text
from src.evaluation.evaluate_classification import (
    compute_classification_metrics,
    save_all_results,
    build_summary_table,
    save_summary_csv,
    plot_f1_comparison_bar,
)

sys.stdout.reconfigure(encoding="utf-8")

OUTPUT_ROOT = PROJECT_ROOT / "outputs"
OUTPUT_METRICS = OUTPUT_ROOT / "metrics"
OUTPUT_FIGURES = OUTPUT_ROOT / "figures"


# =============================================================================
# Model Definitions
# =============================================================================

def make_logistic_regression():
    return LogisticRegression(
        class_weight="balanced",
        max_iter=1000,
        random_state=42,
        solver="lbfgs",
        C=1.0,
    )


def make_linear_svm():
    return CalibratedClassifierCV(
        LinearSVC(
            class_weight="balanced",
            max_iter=2000,
            random_state=42,
            C=1.0,
        ),
        cv=3,
        method="sigmoid",
    )


def make_naive_bayes():
    return MultinomialNB(alpha=0.1)


MODELS = {
    "LogisticRegression": make_logistic_regression,
    "LinearSVM": make_linear_svm,
    "NaiveBayes": make_naive_bayes,
}


# =============================================================================
# Data Loading
# =============================================================================

def load_dataset(path: str, label_col: str = None) -> pd.DataFrame:
    """
    Load dataset, tự động nhận diện format Shopee vs UIT-ViOCD.

    Shopee format  : review, rating, complaint_label
    UIT-ViOCD format: review, review_tokenize, label (0.0/1.0), domain
    """
    df = pd.read_csv(path, encoding="utf-8-sig")
    df.columns = df.columns.str.strip()

    if label_col is None:
        if "complaint_label" in df.columns:
            label_col = "complaint_label"
        elif "label" in df.columns:
            label_col = "label"
        else:
            raise ValueError(
                f"Khong tim thay cot nhan trong {path}. Cac cot: {df.columns.tolist()}"
            )

    if "review" in df.columns:
        text_col = "review"
    elif "review_tokenize" in df.columns:
        text_col = "review_tokenize"
    else:
        raise ValueError(
            f"Khong tim thay cot text trong {path}. Cac cot: {df.columns.tolist()}"
        )

    df = df.dropna(subset=[text_col]).reset_index(drop=True)
    label_series = df[label_col].astype(float).astype(int)

    return pd.DataFrame({
        "text": df[text_col].astype(str),
        "label": label_series,
    })


def preprocess_texts(texts: pd.Series) -> pd.Series:
    return texts.apply(lambda x: clean_vietnamese_text(str(x)))


# =============================================================================
# Main Training Pipeline
# =============================================================================

def train_and_evaluate(
    train_df: pd.DataFrame,
    test_df: pd.DataFrame,
    dataset_name: str,
    tfidf_kwargs: dict = None,
) -> list[dict]:
    """Huấn luyện và đánh giá tất cả classical models."""
    if tfidf_kwargs is None:
        tfidf_kwargs = {}

    print(f"\n{'=' * 60}")
    print(f"Dataset: {dataset_name} | Train: {len(train_df)} | Test: {len(test_df)}")
    print(f"Label dist (train): {dict(train_df['label'].value_counts().sort_index())}")
    print(f"Label dist (test) : {dict(test_df['label'].value_counts().sort_index())}")
    print(f"{'=' * 60}")

    # Tien xu ly
    print("\n[PREPROCESS] Applying clean_vietnamese_text...")
    X_train_text = preprocess_texts(train_df["text"])
    X_test_text = preprocess_texts(test_df["text"])
    y_train = train_df["label"].values
    y_test = test_df["label"].values

    # TF-IDF
    print("[TF-IDF] Fitting vectorizer...")
    vectorizer = TfidfVectorizer(
        lowercase=True,
        min_df=2,
        max_df=0.8,
        strip_accents="unicode",
        **tfidf_kwargs,
    )
    X_train = vectorizer.fit_transform(X_train_text)
    X_test = vectorizer.transform(X_test_text)
    print(f"  TF-IDF shape: {X_train.shape} (train), {X_test.shape} (test)")

    results = []

    for model_key, model_factory in MODELS.items():
        print(f"\n[MODEL] {model_key}")
        model = model_factory()

        # Huan luyen
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Lay xac suat neu co
        y_prob = None
        if hasattr(model, "predict_proba"):
            try:
                y_prob = model.predict_proba(X_test)
            except Exception:
                pass

        # Tinh metrics
        metrics = compute_classification_metrics(y_test, y_pred, y_prob)
        metrics["model"] = model_key
        metrics["dataset"] = dataset_name

        # In report
        print(f"  Accuracy       : {metrics['accuracy']:.4f}")
        print(f"  F1-Macro      : {metrics['f1_macro']:.4f}")
        print(f"  F1-Complaint  : {metrics['f1_complaint']:.4f}")

        # Luu ket qua chi tiet
        model_output_dir = OUTPUT_METRICS / dataset_name / model_key
        saved = save_all_results(
            metrics=metrics,
            output_dir=str(model_output_dir),
            y_true=y_test,
            y_pred=y_pred,
            y_prob=y_prob,
            texts=test_df["text"].tolist(),
            model_name=model_key,
            dataset_name=dataset_name,
        )
        print(f"  [SAVE] {model_output_dir}")

        results.append(metrics)

    return results


# =============================================================================
# CLI Entry Point
# =============================================================================

def parse_args():
    parser = argparse.ArgumentParser(
        description="Train Classical Baselines (LR, SVM, NB) for Complaint Classification"
    )
    parser.add_argument(
        "--train",
        type=str,
        default="data/processed/shopee_mapped.csv",
        help="Duong dan file train (mac dinh: data/processed/shopee_mapped.csv)",
    )
    parser.add_argument(
        "--test",
        type=str,
        default=None,
        help="Duong dan file test. Neu khong truyen, tu dong chia train/val tu train (80/20).",
    )
    parser.add_argument(
        "--val",
        type=str,
        default=None,
        help="Duong dan file validation.",
    )
    parser.add_argument(
        "--label-col",
        type=str,
        default=None,
        help="Ten cot nhan (mac dinh: tu dong nhan dien)",
    )
    parser.add_argument(
        "--test-size",
        type=float,
        default=0.2,
        help="Ty le test split neu khong truyen --test (mac dinh: 0.2)",
    )
    parser.add_argument(
        "--random-state",
        type=int,
        default=42,
        help="Random seed cho reproducibility (mac dinh: 42)",
    )
    parser.add_argument(
        "--max-features",
        type=int,
        default=10000,
        help="max_features cho TF-IDF (mac dinh: 10000)",
    )
    parser.add_argument(
        "--ngram-range",
        type=str,
        default="1,2",
        help="N-gram range, vi du '1,2' (mac dinh: '1,2')",
    )
    parser.add_argument(
        "--output-csv",
        type=str,
        default=None,
        help="Duong dan luu bang metrics tong hop CSV. "
             "Mac dinh: outputs/metrics/classical_baselines.csv",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    OUTPUT_METRICS.mkdir(parents=True, exist_ok=True)
    OUTPUT_FIGURES.mkdir(parents=True, exist_ok=True)

    # Parse ngram range
    ngram_parts = args.ngram_range.split(",")
    ngram_range = (int(ngram_parts[0]), int(ngram_parts[1]))

    # Dat ten dataset tu duong dan
    train_path = Path(args.train)
    if train_path.stem == "shopee_mapped":
        dataset_name = "Shopee"
    elif "UIT-ViOCD" in str(train_path):
        dataset_name = "UIT-ViOCD"
    else:
        dataset_name = train_path.stem

    print(f"\n{'=' * 60}")
    print("Classical Baselines Training")
    print(f"Train path : {args.train}")
    print(f"Test path  : {args.test}")
    print(f"Dataset    : {dataset_name}")
    print(f"Seed       : {args.random_state}")
    print(f"{'=' * 60}")

    # Load train data
    train_df = load_dataset(args.train, label_col=args.label_col)

    # Load test data hoac chia tu train
    if args.test:
        test_df = load_dataset(args.test, label_col=args.label_col)
    elif args.val:
        test_df = load_dataset(args.val, label_col=args.label_col)
    else:
        print(
            f"\n[SPLIT] Chia train/test voi test_size={args.test_size}, "
            f"seed={args.random_state}"
        )
        train_df, test_df = train_test_split(
            train_df,
            test_size=args.test_size,
            random_state=args.random_state,
            stratify=train_df["label"],
        )
        train_df = train_df.reset_index(drop=True)
        test_df = test_df.reset_index(drop=True)
        print(f"  Train: {len(train_df)} | Test: {len(test_df)}")

    # TF-IDF kwargs
    tfidf_kwargs = {
        "max_features": args.max_features,
        "ngram_range": ngram_range,
    }

    # Train & evaluate
    all_results = train_and_evaluate(
        train_df=train_df,
        test_df=test_df,
        dataset_name=dataset_name,
        tfidf_kwargs=tfidf_kwargs,
    )

    # Luu bang tong hop
    output_csv = (
        Path(args.output_csv) if args.output_csv
        else OUTPUT_METRICS / "classical_baselines.csv"
    )
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    save_summary_csv(all_results, str(output_csv))

    # Bar chart so sanh F1
    chart_path = OUTPUT_FIGURES / f"f1_comparison_{dataset_name}.png"
    plot_f1_comparison_bar(all_results, str(chart_path), dataset_name)

    print(f"\n{'=' * 60}")
    print("HOAN TAT!")
    print(f"Summary CSV : {output_csv}")
    print(f"F1 Chart    : {chart_path}")
    print(f"Details     : {OUTPUT_METRICS / dataset_name}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
