"""
Streamlit BIO Tagging Annotation Tool - TEAM VERSION
Người C: Annotate samples 250-374
"""

import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
import re

# Config
DATA_FILE = 'data/processed/annotation_sample_C.jsonl'
OUTPUT_FILE = 'data/processed/bio_annotations_C.jsonl'
ANNOTATOR = 'C'

# Vietnamese word tokenizer
def tokenize_vietnamese(text):
    tokens = []
    current = ""
    for char in text:
        if char in ",.!?;:\"-()[]{}":
            if current:
                tokens.append(current)
                current = ""
            tokens.append(char)
        elif char == " ":
            if current:
                tokens.append(current)
                current = ""
        else:
            current += char
    if current:
        tokens.append(current)
    return tokens

st.set_page_config(page_title=f"BIO Annotation - Team {ANNOTATOR}", layout="wide")
st.title(f"🏷️ Công cụ gán nhãn BIO - Người {ANNOTATOR.upper()}")

# Load data
@st.cache_data
def load_data():
    records = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                records.append(json.loads(line))
    return records

records = load_data()
total_records = len(records)

# Session state
if 'current_idx' not in st.session_state:
    st.session_state.current_idx = 0
    st.session_state.annotations = {}
    st.session_state.token_labels = {}

if st.session_state.current_idx < total_records:
    current_record = records[st.session_state.current_idx]
    review_text = current_record['text']
    
    # Tokenize
    tokens = tokenize_vietnamese(review_text)
    current_idx_global = st.session_state.current_idx
    
    # Initialize token labels if not exists
    if current_idx_global not in st.session_state.token_labels:
        st.session_state.token_labels[current_idx_global] = ['O'] * len(tokens)
    
    current_labels = st.session_state.token_labels[current_idx_global]
    
    # Progress
    col1, col2 = st.columns([1, 5])
    with col1:
        st.metric("Progress", f"{st.session_state.current_idx + 1}/{total_records}")
    with col2:
        st.progress(st.session_state.current_idx / total_records)
    
    st.markdown("---")
    
    # Display source and original text
    col1, col2 = st.columns(2)
    with col1:
        source = current_record.get('meta', {}).get('source', 'unknown')
        st.caption(f"📍 Source: {source.upper()}")
    with col2:
        st.caption(f"ID: {st.session_state.current_idx}")
    
    st.subheader("📝 Bình luận gốc:")
    st.info(review_text)
    
    st.markdown("---")
    
    # Token labeling interface
    st.subheader("🎯 Gán nhãn BIO cho từng token:")
    
    # Legend
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**🔴 B-COMP**: Từ ĐẦU của khiếu nại")
    with col2:
        st.markdown("**🟠 I-COMP**: Từ TIẾP THEO trong khiếu nại")
    with col3:
        st.markdown("**⚪ O**: Từ KHÔNG phải khiếu nại")
    
    st.markdown("---")
    
    # Token buttons grid
    cols = st.columns(4)
    for token_idx, token in enumerate(tokens):
        col_idx = token_idx % 4
        
        with cols[col_idx]:
            st.text(f"**{token}**")
            
            # Buttons for this token
            button_cols = st.columns(3, gap="small")
            
            with button_cols[0]:
                if st.button("B", key=f"b_{current_idx_global}_{token_idx}", 
                            help="Begin - Từ đầu khiếu nại",
                            use_container_width=True):
                    current_labels[token_idx] = "B-COMP"
                    st.session_state.token_labels[current_idx_global] = current_labels
                    st.rerun()
            
            with button_cols[1]:
                if st.button("I", key=f"i_{current_idx_global}_{token_idx}",
                            help="Inside - Từ tiếp theo khiếu nại",
                            use_container_width=True):
                    current_labels[token_idx] = "I-COMP"
                    st.session_state.token_labels[current_idx_global] = current_labels
                    st.rerun()
            
            with button_cols[2]:
                if st.button("O", key=f"o_{current_idx_global}_{token_idx}",
                            help="Outside - Không phải khiếu nại",
                            use_container_width=True):
                    current_labels[token_idx] = "O"
                    st.session_state.token_labels[current_idx_global] = current_labels
                    st.rerun()
            
            # Display current label
            label = current_labels[token_idx]
            if label == "B-COMP":
                st.caption("🔴 B-COMP")
            elif label == "I-COMP":
                st.caption("🟠 I-COMP")
            else:
                st.caption("⚪ O")
            
            st.divider()
    
    st.markdown("---")
    
    # Preview BIO sequence
    st.subheader("👁️ Preview BIO Sequence:")
    bio_text = " | ".join([f"{t}:{l}" for t, l in zip(tokens, current_labels)])
    st.code(bio_text, language="text")
    
    st.markdown("---")
    
    # Actions
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("⬅️ Quay lại", use_container_width=True):
            if st.session_state.current_idx > 0:
                st.session_state.current_idx -= 1
                st.rerun()
    
    with col2:
        if st.button("✅ Lưu & Tiếp theo", use_container_width=True, key="next_btn"):
            # Save current annotation
            source = current_record.get('meta', {}).get('source', 'unknown')
            st.session_state.annotations[current_idx_global] = {
                'text': review_text,
                'tokens': tokens,
                'labels': current_labels,
                'source': source,
                'annotator': ANNOTATOR,
                'timestamp': datetime.now().isoformat()
            }
            st.session_state.current_idx += 1
            st.rerun()
    
    with col3:
        if st.button("⏭️ Bỏ qua", use_container_width=True):
            st.session_state.current_idx += 1
            st.rerun()

else:
    st.success("🎉 Hoàn tát annotation tất cả samples của Người C!")
    
    # Export results
    if len(st.session_state.annotations) > 0:
        if st.button("📥 Export JSONL", use_container_width=True):
            # Write JSONL format
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                for idx, annotation in st.session_state.annotations.items():
                    f.write(json.dumps(annotation, ensure_ascii=False) + '\n')
            
            st.success(f"✅ Đã export {len(st.session_state.annotations)} annotations")
            st.write(f"📁 File: {OUTPUT_FILE}")

# Sidebar statistics
with st.sidebar:
    st.subheader(f"👤 Người {ANNOTATOR.upper()}")
    st.caption(f"Annotator: {ANNOTATOR}")
    
    st.subheader("📈 Thống kê")
    st.metric("Tổng samples", total_records)
    st.metric("Đã gán nhãn", len(st.session_state.annotations))
    remaining = total_records - len(st.session_state.annotations)
    st.metric("Còn lại", remaining)
    
    if len(st.session_state.annotations) > 0:
        st.subheader("📊 Label Distribution")
        
        all_labels = []
        for ann in st.session_state.annotations.values():
            all_labels.extend(ann['labels'])
        
        label_counts = {}
        for label in all_labels:
            label_counts[label] = label_counts.get(label, 0) + 1
        
        for label in ["B-COMP", "I-COMP", "O"]:
            if label in label_counts:
                count = label_counts[label]
                pct = count / len(all_labels) * 100
                if label == "B-COMP":
                    st.write(f"🔴 **B-COMP**: {count} ({pct:.1f}%)")
                elif label == "I-COMP":
                    st.write(f"🟠 **I-COMP**: {count} ({pct:.1f}%)")
                else:
                    st.write(f"⚪ **O**: {count} ({pct:.1f}%)")

# Help section
with st.expander("ℹ️ Hướng dẫn gán nhãn BIO"):
    st.markdown("""
    ### Quy tắc gán nhãn:
    
    1. **B-COMP (Begin)**: Từ **ĐẦU TIÊN** của cụm khiếu nại
    2. **I-COMP (Inside)**: Các từ **TIẾP THEO** trong cụm khiếu nại
    3. **O (Outside)**: Từ **KHÔNG** phải khiếu nại
    """)
