import streamlit as st
from backend.db import get_user_insights

def render():
    st.header("User Insights & Personas")
    insights = get_user_insights()
    st.json(insights)
