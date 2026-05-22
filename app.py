from pathlib import Path
from typing import List, Tuple

import streamlit as st
import torch
from transformers import AutoTokenizer

from src.models.multitask_model import PhobertCRFMultiTask
from src.utils.utils import clean_vietnamese_text


MODEL_NAME = "vinai/phobert-base-v2"
MAX_LEN = 256
ID2LABEL = {0: "O", 1: "B-COMP", 2: "I-COMP"}
PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_CHECKPOINT_DIR = PROJECT_ROOT / "checkpoints"
COMPLAINT_HINT_TERMS = [
    "quá chậm",
    "rất tệ",
    "không vừa",
    "không đúng",
    "sai hàng",
    "móp méo",
    "vỡ",
    "hỏng",
    "lỗi",
    "chậm",
    "tệ",
]


def get_default_checkpoint() -> str:
    candidates = sorted(
        DEFAULT_CHECKPOINT_DIR.glob("checkpoint_epoch_*.pt"),
        key=lambda path: int(path.stem.split("_")[-1]) if path.stem.split("_")[-1].isdigit() else -1,
    )
    if candidates:
        return str(candidates[-1])

    fallback_candidates = [
        Path("../checkpoints/checkpoint_epoch_1.pt"),
        Path("c:/Users/PC/Downloads/checkpoints/checkpoint_epoch_1.pt"),
    ]
    for path in fallback_candidates:
        if path.exists():
            return str(path)
    return str(DEFAULT_CHECKPOINT_DIR / "checkpoint_epoch_1.pt")


def list_available_checkpoints() -> List[str]:
    candidates = sorted(
        DEFAULT_CHECKPOINT_DIR.glob("checkpoint_epoch_*.pt"),
        key=lambda path: int(path.stem.split("_")[-1]) if path.stem.split("_")[-1].isdigit() else -1,
    )
    return [str(path) for path in candidates]


def normalize_token(token: str) -> str:
    token = token.replace("@@", "")
    if token.startswith("▁"):
        token = token[1:]
    return token.strip()


def encode_like_training(text: str, tokenizer: AutoTokenizer):
    words = text.split()
    input_ids = [tokenizer.cls_token_id]
    first_piece_mask = [False]

    for word in words:
        word_tokens = tokenizer.tokenize(word)
        if not word_tokens:
            continue
        w_ids = tokenizer.convert_tokens_to_ids(word_tokens)
        input_ids.extend(w_ids)
        first_piece_mask.append(True)
        if len(w_ids) > 1:
            first_piece_mask.extend([False] * (len(w_ids) - 1))

    input_ids.append(tokenizer.sep_token_id)
    first_piece_mask.append(False)

    if len(input_ids) > MAX_LEN:
        input_ids = input_ids[: MAX_LEN - 1] + [tokenizer.sep_token_id]
        first_piece_mask = first_piece_mask[: MAX_LEN - 1] + [False]

    attention_mask = [1] * len(input_ids)
    pad_len = MAX_LEN - len(input_ids)
    if pad_len > 0:
        input_ids.extend([tokenizer.pad_token_id] * pad_len)
        attention_mask.extend([0] * pad_len)
        first_piece_mask.extend([False] * pad_len)

    return {
        "input_ids": torch.tensor([input_ids], dtype=torch.long),
        "attention_mask": torch.tensor([attention_mask], dtype=torch.long),
        "first_piece_mask": first_piece_mask,
    }


def extract_entities(tokens: List[str], tag_ids: List[int], first_piece_mask: List[bool]) -> List[str]:
    entities: List[str] = []
    current_phrase: List[str] = []

    for token, tag_id, is_first_piece in zip(tokens, tag_ids, first_piece_mask):
        if token is None:
            continue
        if token in ["<s>", "</s>", "<pad>"]:
            continue
        if not is_first_piece:
            continue

        tag = ID2LABEL.get(tag_id, "O")
        clean_tok = normalize_token(token)
        if not clean_tok:
            continue

        if tag == "B-COMP":
            if current_phrase:
                entities.append(" ".join(current_phrase).strip())
            current_phrase = [clean_tok]
        elif tag == "I-COMP":
            if current_phrase:
                current_phrase.append(clean_tok)
            else:
                current_phrase = [clean_tok]
        else:
            if current_phrase:
                entities.append(" ".join(current_phrase).strip())
                current_phrase = []

    if current_phrase:
        entities.append(" ".join(current_phrase).strip())

    entities = [e for e in entities if e]
    deduped: List[str] = []
    for ent in entities:
        if ent not in deduped:
            deduped.append(ent)
    return deduped


def extract_entities_fallback(normalized_text: str) -> List[str]:
    hits: List[str] = []
    for term in COMPLAINT_HINT_TERMS:
        if term in normalized_text and term not in hits:
            hits.append(term)
    return hits


@st.cache_resource
def load_assets(checkpoint_path: str) -> Tuple[PhobertCRFMultiTask, AutoTokenizer]:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=False)
    model = PhobertCRFMultiTask(num_classes=2, num_ner_tags=3)

    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    state_dict = checkpoint.get("model_state_dict", checkpoint)
    model.load_state_dict(state_dict, strict=True)
    model.eval()
    return model, tokenizer


def predict(text: str, model: PhobertCRFMultiTask, tokenizer: AutoTokenizer):
    normalized_text = clean_vietnamese_text(text)
    encoded = encode_like_training(text, tokenizer)
    input_ids = encoded["input_ids"]
    attention_mask = encoded["attention_mask"]
    first_piece_mask = encoded["first_piece_mask"]

    with torch.no_grad():
        cls_logits, ner_predictions = model(
            input_ids=input_ids,
            attention_mask=attention_mask,
        )

    cls_id = int(torch.argmax(cls_logits, dim=-1).item())
    cls_label = "Khiếu nại" if cls_id == 1 else "Bình thường"

    valid_len = int(attention_mask[0].sum().item())
    token_ids = input_ids[0][:valid_len].tolist()
    tokens = tokenizer.convert_ids_to_tokens(token_ids)
    tag_ids = ner_predictions[0][:valid_len]
    first_piece_mask = first_piece_mask[:valid_len]

    entities = extract_entities(tokens, tag_ids, first_piece_mask)
    fallback_entities = []
    if not entities:
        fallback_entities = extract_entities_fallback(normalized_text)

    return (
        cls_label,
        entities,
        fallback_entities,
        list(zip(tokens, [ID2LABEL.get(t, "O") for t in tag_ids])),
    )


def main():
    st.set_page_config(page_title="Demo Complaint Detection + NER", page_icon="🧠", layout="wide")
    st.title("Demo Multi-task PhoBERT + CRF")
    st.caption("Nhận diện khiếu nại và trích xuất cụm từ khiếu nại từ đánh giá sản phẩm")

    with st.sidebar:
        st.subheader("Cấu hình")
        available_checkpoints = list_available_checkpoints()
        if available_checkpoints:
            default_checkpoint = get_default_checkpoint()
            default_index = available_checkpoints.index(default_checkpoint) if default_checkpoint in available_checkpoints else len(available_checkpoints) - 1
            checkpoint_path = st.selectbox("Checkpoint trong project", available_checkpoints, index=default_index)
            custom_checkpoint = st.text_input("Hoặc nhập checkpoint khác", value="")
            if custom_checkpoint.strip():
                checkpoint_path = custom_checkpoint.strip()
        else:
            checkpoint_path = st.text_input("Đường dẫn checkpoint", value=get_default_checkpoint())
        st.caption(f"Đang dùng: {checkpoint_path}")
        st.write("Model backbone:", MODEL_NAME)

    try:
        model, tokenizer = load_assets(checkpoint_path)
        st.success("Đã load model thành công")
    except Exception as exc:
        st.error(f"Không thể load model: {exc}")
        st.stop()

    user_text = st.text_area(
        "Nhập nội dung đánh giá sản phẩm",
        height=180,
        placeholder="Ví dụ: Giao hàng quá chậm, hộp bị móp và shop phản hồi rất tệ...",
    )

    if st.button("Phân tích", type="primary"):
        if not user_text.strip():
            st.warning("Vui lòng nhập nội dung đánh giá trước khi phân tích.")
            st.stop()

        cls_label, entities, fallback_entities, token_tags = predict(user_text.strip(), model, tokenizer)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Kết quả phân loại")
            if cls_label == "Khiếu nại":
                st.error(cls_label)
            else:
                st.success(cls_label)

        with col2:
            st.subheader("Thực thể khiếu nại (NER)")
            if entities:
                st.write(" | ".join(entities))
            elif fallback_entities:
                st.warning("Model chưa trích được span BIO, đang hiển thị từ khóa gợi ý.")
                st.write(" | ".join(fallback_entities))
            else:
                st.info("Không phát hiện cụm từ khiếu nại.")

        with st.expander("Chi tiết token và nhãn BIO"):
            st.table(
                {
                    "Token": [tok for tok, _ in token_tags],
                    "Tag": [tag for _, tag in token_tags],
                }
            )


if __name__ == "__main__":
    main()