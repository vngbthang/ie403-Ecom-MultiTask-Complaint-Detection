from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st
import torch

from src.inference.predict_complaint_spans import (
    DEFAULT_MODEL_NAME,
    bio_to_spans,
    load_model,
    predict_token_labels,
)


DEFAULT_CHECKPOINT = (
    "outputs/metrics/demo_full_unweighted_phobert_ner_5epoch/checkpoints/"
    "ner_single_task_epoch_5.pt"
)
EXAMPLES = [
    "áo đẹp nhưng giao hàng chậm quá, shop đóng gói sơ sài",
    "app hay bị lag, đăng nhập mãi không được",
    "sản phẩm ổn nhưng giao sai màu và thiếu phụ kiện",
    "hàng đẹp, đóng gói chắc chắn, giao nhanh",
    "pin tụt nhanh, máy nóng và camera bị mờ",
]


def read_checkpoint_metadata(checkpoint_path: str) -> dict[str, object]:
    path = Path(checkpoint_path)
    if not path.exists():
        return {}
    try:
        checkpoint = torch.load(path, map_location="cpu")
    except Exception:
        return {}
    if not isinstance(checkpoint, dict):
        return {}
    return {
        "epoch": checkpoint.get("epoch"),
        "best_entity_f1": checkpoint.get("best_entity_f1"),
    }


@st.cache_resource(show_spinner="Loading PhoBERT NER checkpoint...")
def load_cached_model(checkpoint_path: str, model_name: str):
    return load_model(checkpoint_path=checkpoint_path, model_name=model_name)


def render_highlight(tokens: list[str], labels: list[str]) -> str:
    pieces = []
    for token, label in zip(tokens, labels):
        escaped = (
            token.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )
        if label in {"B-COMP", "I-COMP"}:
            pieces.append(
                "<span style='background:#fff2a8; color:#2b2110; "
                "border-radius:4px; padding:2px 5px; margin:2px; "
                "display:inline-block;'>"
                f"{escaped}<sup style='font-size:0.65rem; margin-left:4px;'>{label}</sup>"
                "</span>"
            )
        else:
            pieces.append(
                "<span style='padding:2px 3px; margin:2px; display:inline-block;'>"
                f"{escaped}</span>"
            )
    return "<div style='line-height:2.2; font-size:1rem;'>" + " ".join(pieces) + "</div>"


st.set_page_config(page_title="Vietnamese Complaint Span Extraction", layout="wide")

st.title("Vietnamese Complaint Span Extraction Demo")
st.markdown(
    """
Demo rút trích vùng khiếu nại trong review tiếng Việt.

- Model: **PhoBERT NER**
- Dataset task: **UIT-ViOCD complaint span extraction with AI-assisted BIO labels**
- Output là **complaint spans**, không phải review-level classification.
"""
)

with st.sidebar:
    st.header("Model settings")
    checkpoint_path = st.text_input("Checkpoint path", value=DEFAULT_CHECKPOINT)
    model_name = st.text_input("Model name", value=DEFAULT_MODEL_NAME)
    max_len = st.number_input("Max length", min_value=32, max_value=512, value=256, step=16)

    device_label = "cuda" if torch.cuda.is_available() else "cpu"
    st.caption(f"Device available: `{device_label}`")

    metadata = read_checkpoint_metadata(checkpoint_path)
    if metadata:
        st.caption(f"Checkpoint epoch: `{metadata.get('epoch')}`")
        st.caption(f"Best Entity-F1: `{metadata.get('best_entity_f1')}`")
    else:
        st.caption("Checkpoint metadata unavailable.")

st.subheader("Input review")
example = st.selectbox("Example reviews", EXAMPLES)
text = st.text_area("Review text", value=example, height=130)

if st.button("Extract complaint spans", type="primary"):
    if not text.strip():
        st.warning("Please enter a Vietnamese review.")
        st.stop()

    if not Path(checkpoint_path).exists():
        st.error(
            "Checkpoint not found. Please check: "
            "outputs/metrics/demo_full_unweighted_phobert_ner_5epoch/checkpoints/"
            "ner_single_task_epoch_5.pt"
        )
        st.stop()

    try:
        model, tokenizer, id2label, device = load_cached_model(checkpoint_path, model_name)
    except Exception as exc:
        st.error(f"Could not load model: {exc}")
        st.stop()

    try:
        tokens, labels = predict_token_labels(
            text=text,
            model=model,
            tokenizer=tokenizer,
            id2label=id2label,
            device=device,
            max_len=int(max_len),
        )
        spans = bio_to_spans(tokens, labels)
    except Exception as exc:
        st.error(f"Prediction failed: {exc}")
        st.stop()

    st.subheader("Input review")
    st.write(text)

    st.subheader("Complaint spans")
    if spans:
        for span in spans:
            st.markdown(
                f"- `{span['text']}` "
                f"(tokens {span['start_token']}:{span['end_token']})"
            )
    else:
        st.info("No complaint span detected.")

    st.subheader("Highlighted tokens")
    st.markdown(render_highlight(tokens, labels), unsafe_allow_html=True)

    with st.expander("Token-level BIO labels", expanded=False):
        st.dataframe(
            pd.DataFrame({"Token": tokens, "BIO Label": labels}),
            use_container_width=True,
            hide_index=True,
        )

st.caption(
    "Note: predictions are produced by a model trained on constructed AI-assisted "
    "span labels, not an official UIT-ViOCD benchmark."
)
