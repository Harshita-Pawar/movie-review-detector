import streamlit as st
from transformers import pipeline

st.title("🎬 Movie Review Detector")

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

classifier = load_model()

text = st.text_area("Enter a movie review:")

if st.button("Analyze"):
    if text:
        result = classifier(text)[0]
        if result["label"] == "POSITIVE":
            st.success("Genuine Review ✅")
        else:
            st.error("Misleading Review ❌")
