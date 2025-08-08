from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(temperature=0)

def analyze_logs(log_text):
    prompt = f"""
You are a log analysis expert. Given the following log snippet, summarize key issues and possible root causes.

Logs:
{log_text}

Respond with:
- Summary of issues
- Root cause analysis (if possible)
- Suggested next actions
"""
    return llm.invoke(prompt)
