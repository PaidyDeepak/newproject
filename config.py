import google.generativeai as genai
import streamlit as st

API_KEY = st.secrets["general"]["GOOGLE_API_KEY"]

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")
