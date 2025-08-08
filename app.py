import streamlit as st
from agent import analyze_logs
from utils import read_logs
import os

st.set_page_config(page_title="🧠 Agentic AI Log Analyzer", layout="wide")
st.title("🧠 Agentic AI Log Analyzer")
st.markdown("Upload a log file or analyze a sample to get started.")

# File uploader
uploaded_file = st.file_uploader("Upload a log file (.log)", type=["log", "txt"])

# Or use sample
use_sample = st.button("Use sample log (app.log)")

log_text = ""

if uploaded_file:
    log_text = read_logs(uploaded_file, max_lines=100)
elif use_sample:
    with open("logs/app.log", "r") as f:
        log_text = f.read()
st.text(f"Log length: {len(log_text)}")

if log_text:
    st.subheader("📄 Log Snippet")
    st.code(log_text, language="bash")
    result = None
    if st.button("🔍 Analyze Logs"):
        with st.spinner("Analyzing with LLM..."):
            try:
                print("🟡 Calling analyze_logs...")
                result = analyze_logs(log_text)
                print("✅ Analysis complete")
            except Exception as e:
                st.error(f"Error: {e}")
                result = None

    if result:
        st.subheader("🧠 Analysis Result")
        st.markdown(result)

