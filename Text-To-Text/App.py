from transformers import pipeline
import torch
import streamlit as st

device = 0 if torch.cuda.is_available() else -1
summarizer = pipeline("summarization", device=device)


st.title("Text summarizer")
st.divider()

text = st.text_area("Insert text", height=150)

if text:
    summary = summarizer('"""'+text+'"""', max_length=280, min_length=60, do_sample=False)
    st.write(summary[0]['summary_text'])
    