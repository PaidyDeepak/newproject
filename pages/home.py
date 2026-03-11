import streamlit as st
from utils import save_profile

st.title("Career Guidance Chatbot")

st.header("Enter Your Details")

education = st.text_input("Education")
qualification = st.text_input("Qualification")
technologies = st.text_input("Known Technologies")
experience = st.number_input("Years of Experience", 0, 50)

if st.button("Save Profile"):

    profile = {
        "education": education,
        "qualification": qualification,
        "technologies": technologies,
        "experience": experience
    }

    save_profile(profile)

    st.success("Profile saved successfully")
