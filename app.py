import streamlit as st
from modules.operational import operational_planning
from modules.financial import financial_forecasting
from modules.risk_assessment import risk_assessment
from modules.growth_scaling import growth_scaling
from modules.investment_financing import investment_financing
from modules.workforce import workforce_projections
from modules.help import help_page
from modules.dashboard import dashboard  # Directly import the function

# Navigation
st.title("Business Forecasting Tool")
st.sidebar.header("Navigation")

# Update the navigation menu to use a radio button
selected_module = st.sidebar.radio(
    "Select a Module",
    [
        "Home",
        "Dashboard",  # Dashboard is now in its separate module
        "Financial Forecasting",
        "Operational Planning",
        "Risk Assessment",
        "Growth & Scaling Strategy",
        "Investment and Financing Needs",
        "Workforce and Culture Projections",
        "Help"
    ]
)

# Home Page
if selected_module == "Home":
    st.header("Welcome to the Business Forecasting Tool")
    st.write("""
        This tool helps you forecast key aspects of your business, 
        including financial projections, operational planning, risk assessment, growth, and workforce planning.
        Use the sidebar to navigate between modules.
    """)

# Dashboard Module
elif selected_module == "Dashboard":
    dashboard()

# Financial Forecasting Module
elif selected_module == "Financial Forecasting":
    financial_forecasting()

# Operational Planning Module
elif selected_module == "Operational Planning":
    operational_planning()

# Risk Assessment Module
elif selected_module == "Risk Assessment":
    risk_assessment()

# Growth & Scaling Strategy Module
elif selected_module == "Growth & Scaling Strategy":
    growth_scaling()

# Investment and Financing Needs Module
elif selected_module == "Investment and Financing Needs":
    investment_financing()

# Workforce and Culture Projections Module
elif selected_module == "Workforce and Culture Projections":
    workforce_projections()

# Help Module
elif selected_module == "Help":
    help_page()
