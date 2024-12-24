import streamlit as st
from modules.financial import financial_forecasting  # Import the financial forecasting module

# Application Title and Navigation
st.title("Business Forecasting Tool")
st.sidebar.header("Navigation")
selected_module = st.sidebar.selectbox(
    "Select a Module",
    ["Home", "Financial Forecasting"]  # Add additional modules here as they are created
)

# Home Page
if selected_module == "Home":
    st.header("Welcome to the Business Forecasting Tool")
    st.write("""
        This tool is designed to help you plan and forecast key aspects of your business, 
        including financial projections, operational planning, and risk assessment. 
        Use the sidebar to navigate between modules.
    """)

# Financial Forecasting Module
elif selected_module == "Financial Forecasting":
    financial_forecasting()
