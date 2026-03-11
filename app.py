import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
from chat_utils import build_prompt, generate_response
from history_utils import save_history, load_history

# ------------------------------------------------
# CONFIG
# ------------------------------------------------

load_dotenv()

st.set_page_config(
    page_title="Career AI Assistant",
    layout="wide"
)

api = st.secrets["general"]["GOOGLE_API_KEY"]
genai.configure(api_key=api)

# ------------------------------------------------
# SESSION INIT
# ------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = load_history()

if "profile" not in st.session_state:
    st.session_state.profile = {}

# ------------------------------------------------
# LOAD LOGO
# ------------------------------------------------

logo = Image.open("logo.png").resize((200,150))

# ------------------------------------------------
# SIDEBAR PROFILE
# ------------------------------------------------

st.sidebar.image(logo)

st.sidebar.subheader("👤 Your Profile")

interests = st.sidebar.text_input("Interests")
skills = st.sidebar.text_input("Skills")
education = st.sidebar.text_input("Education")
experience = st.sidebar.text_input("Experience")

if st.sidebar.button("Save Profile"):

    st.session_state.profile = {
        "interests": interests,
        "skills": skills,
        "education": education,
        "experience": experience
    }

    st.sidebar.success("Profile saved!")

# ------------------------------------------------
# FLOATING CHAT STYLE
# ------------------------------------------------

st.markdown(
"""
<style>
.chat-box {
position: fixed;
bottom: 20px;
right: 20px;
width: 380px;
background-color: white;
border-radius: 10px;
border: 1px solid #ddd;
padding: 10px;
}
</style>
""",
unsafe_allow_html=True
)

# ------------------------------------------------
# CHATBOT TAB
# ------------------------------------------------

tab1, tab2 = st.tabs(["Chatbot","History"])

with tab1:

    st.title("🎓 AI Career Guidance Assistant")

    # display previous messages
    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask your career question...")

    if user_input:

        if not st.session_state.profile:

            st.error("Please fill profile first.")

        else:

            st.session_state.messages.append(
                {"role":"user","content":user_input}
            )

            with st.chat_message("user"):
                st.markdown(user_input)

            prompt = build_prompt(
                st.session_state.profile,
                st.session_state.messages
            )

            with st.spinner("Thinking..."):

                reply = generate_response(prompt)

            st.session_state.messages.append(
                {"role":"assistant","content":reply}
            )

            with st.chat_message("assistant"):
                st.markdown(reply)

            save_history(st.session_state.messages)

# ------------------------------------------------
# HISTORY TAB
# ------------------------------------------------

with tab2:

    st.title("📜 Chat History")

    if not st.session_state.messages:
        st.warning("No history yet")

    for msg in st.session_state.messages:

        role = "User" if msg["role"] == "user" else "Assistant"

        st.markdown("---")
        st.markdown(f"**{role}:** {msg['content']}")
