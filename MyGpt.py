import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Safety check
if not API_KEY:
    st.error("API key not found. Please check your .env file.")
    st.stop()

st.set_page_config(page_title="MyGPT", page_icon="🤖")

st.title("🤖 MyGPT Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
prompt = st.chat_input("Ask anything...")

if prompt:
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # API endpoint (correct model)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={API_KEY}"

    # Request body
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    # API call
    try:
        res = requests.post(url, headers=headers, json=data)

        if res.status_code == 200:
            res_json = res.json()
            response = res_json['candidates'][0]['content']['parts'][0]['text']
        else:
            response = f"API Error {res.status_code}: {res.text}"

    except Exception as e:
        response = f"Request failed: {str(e)}"

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })