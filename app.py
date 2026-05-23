"""
Vietnamese E-commerce Complaint Detection Demo
============================================
Streamlit demo: Multi-task PhoBERT + CRF for complaint detection.
  1. Classification: Complaint / Non-Complaint
  2. NER: Extract complaint spans via BIO (O / B-COMP / I-COMP)
"""

from pathlib import Path
from typing import Dict, List, Tuple

import streamlit as st
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer

from src.models.multitask_model import PhobertCRFMultiTask


# =============================================================================
# Constants
# =============================================================================

MODEL_NAME = "vinai/phobert-base-v2"
MAX_LEN = 256
ID2LABEL = {0: "O", 1: "B-COMP", 2: "I-COMP"}
CLS_LABELS = {0: "Non-Complaint", 1: "Complaint"}


# =============================================================================
# Checkpoint helpers
# =============================================================================

def find_default_checkpoint() -> str:
    candidates = [
        Path("checkpoints/checkpoint_epoch_3.pt"),
        Path("outputs/demo_checkpoint/checkpoint_epoch_3.pt"),
    ]
    for p in candidates:
        if p.exists():
            return str(p)
    return str(candidates[0])


def get_checkpoint_state_dict(path: Path) -> Tuple[bool, str, Dict]:
    if not path.exists():
        return False, f"Checkpoint not found: {path}", {}
    try:
        ckpt = torch.load(path, map_location="cpu", weights_only=False)
        if "model_state_dict" in ckpt:
            sd = ckpt["model_state_dict"]
        elif "state_dict" in ckpt:
            sd = ckpt["state_dict"]
        else:
            sd = ckpt
        if not isinstance(sd, dict):
            return False, "Cannot read state_dict", {}
        return True, "OK", sd
    except Exception as exc:
        return False, f"Error: {exc}", {}


# =============================================================================
# Model loading
# =============================================================================

@st.cache_resource
def load_model_resource(checkpoint_path: str):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=False)
    model = PhobertCRFMultiTask(num_classes=2, num_ner_tags=3)

    ok, msg, sd = get_checkpoint_state_dict(Path(checkpoint_path))
    if not ok:
        raise RuntimeError(msg)

    model.load_state_dict(sd, strict=False)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()

    return model, tokenizer, device


# =============================================================================
# Post-processing
# =============================================================================

def tokens_to_text(span_tokens: List[str], tokenizer: AutoTokenizer) -> str:
    special = {
        tokenizer.cls_token, tokenizer.sep_token,
        tokenizer.pad_token, tokenizer.unk_token,
        "<s>", "</s>", "<pad>", "", None,
    }
    clean = [t for t in span_tokens if t not in special and t is not None]
    try:
        text = tokenizer.convert_tokens_to_string(clean)
        text = text.replace("@@ ", "").replace("@@", "").replace("  ", " ").strip()
        if text:
            return text
    except Exception:
        pass
    words, cur = [], ""
    for tok in clean:
        if tok.startswith("##"):
            cur += tok[2:]
        elif tok.endswith("@@"):
            cur += tok[:-2]
        else:
            if cur:
                words.append(cur)
            cur = tok
    if cur:
        words.append(cur)
    return " ".join(words).strip()


def extract_spans(tokens: List[str], tag_ids: List[int], tokenizer: AutoTokenizer) -> List[str]:
    spans, cur = [], []
    for tok, tag_id in zip(tokens, tag_ids):
        label = ID2LABEL.get(tag_id, "O")
        if label == "B-COMP":
            if cur:
                spans.append(tokens_to_text(cur, tokenizer))
            cur = [tok]
        elif label == "I-COMP":
            if cur:
                cur.append(tok)
            else:
                cur = [tok]
        else:
            if cur:
                spans.append(tokens_to_text(cur, tokenizer))
                cur = []
    if cur:
        spans.append(tokens_to_text(cur, tokenizer))
    seen, result = set(), []
    for s in spans:
        s = s.strip()
        if s and s not in seen:
            seen.add(s)
            result.append(s)
    return result


def normalize_bio_tags(tag_ids: List[int]) -> List[int]:
    """Fix I-COMP that starts a span or follows O — convert to B-COMP."""
    normalized = []
    prev = 0
    for tag in tag_ids:
        tag = int(tag)
        if tag == 2 and prev == 0:
            tag = 1
        normalized.append(tag)
        prev = tag
    return normalized


# =============================================================================
# Inference
# =============================================================================

def run_inference(text: str, model: PhobertCRFMultiTask,
                  tokenizer: AutoTokenizer, device: torch.device) -> Dict:
    encoded = tokenizer(
        text, max_length=MAX_LEN, truncation=True,
        padding="max_length", return_tensors="pt",
    )
    input_ids = encoded["input_ids"].to(device)
    attention_mask = encoded["attention_mask"].to(device)

    with torch.no_grad():
        cls_logits, ner_preds = model(input_ids=input_ids, attention_mask=attention_mask)

    cls_probs = F.softmax(cls_logits, dim=-1)[0].cpu().numpy()
    cls_id = int(torch.argmax(cls_logits, dim=-1).item())
    cls_label = CLS_LABELS[cls_id]
    confidence = float(cls_probs[cls_id])

    valid_len = int(attention_mask[0].sum().item())
    ids = input_ids[0][:valid_len].tolist()
    tokens = tokenizer.convert_ids_to_tokens(ids)

    first_piece_mask = []
    for tok in tokens:
        if tok in (tokenizer.cls_token, tokenizer.sep_token, tokenizer.pad_token, "<s>", "</s>", "<pad>"):
            first_piece_mask.append(False)
        elif tok.startswith("##"):
            first_piece_mask.append(False)
        else:
            first_piece_mask.append(True)

    raw_tag_ids = ner_preds[0][:valid_len]

    special_tokens = {
        tokenizer.cls_token, tokenizer.sep_token, tokenizer.pad_token,
        tokenizer.unk_token, "<s>", "</s>", "<pad>",
    }

    # Collect raw word-level tokens and tags
    raw_word_tokens, raw_word_tags = [], []
    for tok, tag_id, is_first in zip(tokens[:valid_len], raw_tag_ids, first_piece_mask[:valid_len]):
        if tok in special_tokens or not is_first:
            continue
        raw_word_tokens.append(tok)
        raw_word_tags.append(tag_id)

    # Normalize BIO tags: I-COMP after O/beginning -> B-COMP
    word_tags = normalize_bio_tags(raw_word_tags)
    word_tokens = raw_word_tokens

    spans = extract_spans(word_tokens, word_tags, tokenizer)

    visible_norm_labels = [ID2LABEL.get(tag, "O") for tag in word_tags]

    debug_tokens = [
        tok.replace("@@", "").replace("##", "").strip()
        for tok in tokens[:valid_len] if tok not in special_tokens
    ]
    debug_raw_labels = [
        ID2LABEL.get(raw_tag_ids[i], "O")
        for i in range(valid_len) if tokens[i] not in special_tokens
    ]
    debug_labels = []
    visible_idx = 0
    for i in range(valid_len):
        if tokens[i] in special_tokens:
            continue
        is_subword = (i > 0 and tokens[i - 1] not in special_tokens and tokens[i].startswith("##"))
        if is_subword:
            debug_labels.append("")
        else:
            debug_labels.append(visible_norm_labels[visible_idx])
            visible_idx += 1

    return {
        "prediction_label": cls_label,
        "confidence": confidence,
        "complaint_prob": float(cls_probs[1]),
        "non_complaint_prob": float(cls_probs[0]),
        "spans": spans,
        "debug_tokens": debug_tokens,
        "debug_raw_labels": debug_raw_labels,
        "debug_labels": debug_labels,
        "device": str(device),
    }


# =============================================================================
# Highlight
# =============================================================================

def highlight_review(text: str, spans: List[str]) -> str:
    safe = text
    for span in spans:
        if not span:
            continue
        safe = safe.replace(
            span,
            f"<mark style='background-color:#FEF08A;padding:2px 4px;border-radius:4px;'>{span}</mark>",
        )
    return f"<div style='font-size:1rem;line-height:2'>{safe}</div>"


# =============================================================================
# Minimal CSS
# =============================================================================

def inject_css():
    st.markdown(
        """
        <style>
        .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }
        </style>
        """,
        unsafe_allow_html=True,
    )


# =============================================================================
# Sidebar
# =============================================================================

def render_sidebar() -> Tuple:
    with st.sidebar:
        st.header("Configuration")

        default_ckpt = find_default_checkpoint()
        checkpoint_path = st.text_input(
            "Checkpoint path",
            value=default_ckpt,
            key="checkpoint_path_input",
        )
        ckpt_name = Path(checkpoint_path).name
        st.caption(f"Loaded: `{ckpt_name}`")

        st.divider()
        st.subheader("Model Status")
        try:
            with st.spinner("Loading..."):
                model, tokenizer, device = load_model_resource(checkpoint_path)
            st.success(f"Ready on {device}")
        except Exception as exc:
            st.error(f"Failed: {exc}")
            st.stop()

        st.divider()
        st.subheader("Test Metrics")
        st.metric("Entity-F1", "0.3299")
        st.metric("Token-F1", "0.6587")
        st.caption("Alpha = 1.0")

        st.divider()
        st.caption(
            "Detects Vietnamese e-commerce complaints and "
            "extracts complaint spans via BIO tagging."
        )

    return model, tokenizer, device, ckpt_name


# =============================================================================
# Main
# =============================================================================

def main():
    st.set_page_config(
        page_title="Complaint Detection Demo",
        page_icon="X",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_css()

    model, tokenizer, device, ckpt_name = render_sidebar()

    st.title("Vietnamese E-commerce Complaint Detection")
    st.markdown(
        "Multi-task PhoBERT + CRF for complaint classification "
        "and complaint span extraction."
    )
    st.markdown("**PhoBERT** · **Multi-task Learning** · **BIO + CRF**")

    st.divider()
    st.subheader("Try a sample")
    samples = [
        ("sample_0", "Giao hàng chậm",   "shop giao hàng quá chậm, sản phẩm bị móp méo"),
        ("sample_1", "Sai màu sản phẩm", "mình đặt màu đen nhưng shop giao màu trắng"),
        ("sample_2", "Sản phẩm tốt",     "sản phẩm tốt, giao nhanh, sẽ ủng hộ shop"),
        ("sample_3", "Đóng gói kém",     "đóng gói không cẩn thận, hộp bị rách"),
        ("sample_4", "Hàng bị hỏng",     "chất lượng kém, dùng vài ngày đã hỏng"),
    ]
    if "review_text" not in st.session_state:
        st.session_state["review_text"] = ""
    cols = st.columns(5)
    for i, (key, label, sample_text) in enumerate(samples):
        with cols[i]:
            if st.button(label, key=key, use_container_width=True):
                st.session_state["review_text"] = sample_text
                st.rerun()

    st.divider()
    st.subheader("Input Review")
    user_text = st.text_area(
        "Review text",
        height=130,
        placeholder="Nhap hoac dan noi dung danh gia tieng Viet...",
        label_visibility="collapsed",
        key="review_text",
    )
    analyze = st.button("Analyze Review", key="analyze_button", type="primary")

    if analyze:
        if not user_text.strip():
            st.warning("Vui long nhap noi dung danh gia truoc khi phan tich.")
            st.stop()

        with st.spinner("Dang phan tich..."):
            result = run_inference(user_text.strip(), model, tokenizer, device)

        st.divider()
        st.subheader("Results")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Classification**")
            if result["prediction_label"] == "Complaint":
                st.error(f"Complaint detected — Confidence: {result['confidence']:.1%}")
            else:
                st.success(f"No complaint detected — Confidence: {result['confidence']:.1%}")
            st.write("Complaint probability")
            st.progress(result["complaint_prob"])
            st.write("Non-Complaint probability")
            st.progress(result["non_complaint_prob"])

        with col2:
            st.markdown("**Extracted Complaint Spans**")
            spans = result["spans"]
            if spans:
                for span in spans:
                    st.info(span)
            elif result["prediction_label"] == "Complaint":
                st.warning(
                    "No complaint span extracted. "
                    "This may be an uncertain or false-positive prediction."
                )
            else:
                st.info("No complaint span extracted.")

        st.divider()
        st.markdown("**Highlighted Review**")
        st.markdown(highlight_review(user_text.strip(), spans), unsafe_allow_html=True)

        with st.expander("Token-level BIO Details", expanded=False):
            st.caption(
                "PhoBERT uses subword tokenization — "
                "some words may be split into pieces."
            )
            df = {
                "Token": result["debug_tokens"],
                "Raw BIO": result["debug_raw_labels"],
                "Display BIO": result["debug_labels"],
            }
            st.dataframe(df, use_container_width=True, hide_index=True)

        with st.expander("Model Information", expanded=False):
            st.write({
                "Backbone": "vinai/phobert-base-v2",
                "Architecture": "Multi-task PhoBERT + CRF",
                "Tasks": "Classification + Complaint Span Extraction",
                "Checkpoint": ckpt_name,
                "Entity-F1": "0.3299",
                "Token-F1": "0.6587",
            })


if __name__ == "__main__":
    main()
