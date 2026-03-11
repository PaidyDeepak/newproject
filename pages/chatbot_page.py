import streamlit as st
import google.generativeai as genai
import json

# -----------------------------
# Gemini API Configuration
# -----------------------------

API_KEY = st.secrets["general"]["GOOGLE_API_KEY"]

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


# -----------------------------
# Session Initialization
# -----------------------------

if "sessions" not in st.session_state:
    st.session_state.sessions = {}

if "current_session" not in st.session_state:
    st.session_state.current_session = "Session 1"
    st.session_state.sessions["Session 1"] = []

if "chat_open" not in st.session_state:
    st.session_state.chat_open = False


# -----------------------------
# Sidebar Chat Sessions
# -----------------------------

st.sidebar.title("Chat Sessions")

if st.sidebar.button("➕ New Chat"):

    new_session = f"Session {len(st.session_state.sessions)+1}"

    st.session_state.sessions[new_session] = []

    st.session_state.current_session = new_session


sessions = list(st.session_state.sessions.keys())

st.session_state.current_session = st.sidebar.selectbox(
    "Select Session",
    sessions,
    index=sessions.index(st.session_state.current_session)
)


# -----------------------------
# Floating Chat CSS
# -----------------------------

st.markdown(
"""
<style>

.chat-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #ff4b4b;
    color: white;
    border-radius: 50%;
    padding: 18px;
    font-size: 22px;
    cursor: pointer;
}

.chat-box {
    position: fixed;
    bottom: 80px;
    right: 20px;
    width: 350px;
    height: 450px;
    background: white;
    border-radius: 10px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
    padding: 10px;
    overflow-y: auto;
}

</style>
""",
unsafe_allow_html=True
)


# -----------------------------
# Floating Chat Button
# -----------------------------

if st.button("💬 Open Chat"):

    st.session_state.chat_open = not st.session_state.chat_open


# -----------------------------
# Gemini Response Function
# -----------------------------

def get_response(prompt):

    response = model.generate_content(prompt)

    return response.text


# -----------------------------
# Floating Chat Window
# -----------------------------

if st.session_state.chat_open:

    st.markdown('<div class="chat-box">', unsafe_allow_html=True)

    chat_history = st.session_state.sessions[
        st.session_state.current_session
    ]

    for msg in chat_history:

        with st.chat_message(msg["role"]):

            st.write(msg["content"])

    prompt = st.chat_input("Ask career question")

    if prompt:

        chat_history.append({
            "role": "user",
            "content": prompt
        })

        response = get_response(prompt)

        chat_history.append({
            "role": "assistant",
            "content": response
        })

        st.session_state.sessions[
            st.session_state.current_session
        ] = chat_history

        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# Save Sessions to JSON
# -----------------------------

if st.sidebar.button("Save Chat History"):

    with open("chat_history.json", "w") as f:

        json.dump(st.session_state.sessions, f)

    st.sidebar.success("Chat history saved!")
