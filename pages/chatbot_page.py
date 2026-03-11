import streamlit as st
from chatbot import get_response
from utils import load_profile, load_chat, save_chat

st.title("Career Chatbot")

profile = load_profile()

chat_history = load_chat()

user_input = st.chat_input("Ask career questions")

if user_input:

    response = get_response(user_input, profile)

    chat_history.append({
        "user": user_input,
        "bot": response
    })

    save_chat(chat_history)

for chat in chat_history:
    st.chat_message("user").write(chat["user"])
    st.chat_message("assistant").write(chat["bot"])
