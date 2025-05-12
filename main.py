import streamlit as st
import importlib.util
import os

def load_page_module(filename, alias):
    filepath = os.path.join("pages", filename)
    spec = importlib.util.spec_from_file_location(alias, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

Chatbot = load_page_module("1_Chatbot.py", "Chatbot")
Admin = load_page_module("2_Admin.py", "Admin")
Insights = load_page_module("3_Insights.py", "Insights")


st.set_page_config(page_title="Regalium Agentic AI", layout="wide")
st.title("Regalium Agentic AI")

menu = st.sidebar.selectbox("Navigate", ["Chatbot", "Admin", "Insights"])

if menu == "Chatbot":
    Chatbot.render()
elif menu == "Admin":
    Admin.render()
elif menu == "Insights":
    Insights.render()
