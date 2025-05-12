import streamlit as st
from backend.chatbot import chat_with_user

def render():
    st.header("Regalium Chatbot")
    user_input = st.text_input("Ask something about our properties:")
    if user_input:
        response = chat_with_user(user_input)
        st.write(response)
