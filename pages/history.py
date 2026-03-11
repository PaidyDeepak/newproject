import streamlit as st
import json
from utils import load_chat

st.title("Chat History")

history = load_chat()

st.json(history)

download = json.dumps(history)

st.download_button(
    label="Download Chat History",
    data=download,
    file_name="chat_history.json",
    mime="application/json"
)
