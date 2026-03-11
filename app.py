import streamlit as st

st.set_page_config(
    page_title="Career Guidance Chatbot",
    layout="wide"
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Home", "Chatbot", "History"]
)

if page == "Home":
    import pages.home

elif page == "Chatbot":
    import pages.chatbot_page

elif page == "History":
    import pages.history
