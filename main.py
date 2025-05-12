import streamlit as st
from pages import Chatbot, Admin, Insights

st.set_page_config(page_title="Regalium Agentic AI", layout="wide")
st.title("Regalium Agentic AI")

menu = st.sidebar.selectbox("Navigate", ["Chatbot", "Admin", "Insights"])

if menu == "Chatbot":
    Chatbot.render()
elif menu == "Admin":
    Admin.render()
elif menu == "Insights":
    Insights.render()
