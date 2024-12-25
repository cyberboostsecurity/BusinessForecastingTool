import streamlit as st
from modules.operational import operational_planning  # Correct import
from modules.financial import financial_forecasting
from modules.risk_assessment import risk_assessment
from modules.growth_scaling import growth_scaling
from modules.investment_financing import investment_financing
from modules.workforce import workforce_projections  
from modules.help import help_page

# Navigation
st.title("Business Forecasting Tool")
st.sidebar.header("Navigation")

# Update the navigation menu
selected_module = st.sidebar.selectbox(
    "Select a Module",
    ["Home", "Financial Forecasting", "Operational Planning", "Risk Assessment", "Growth & Scaling Strategy", "Investment and Financing Needs", "Workforce and Culture Projections", "Help"]
)
# Home Page
if selected_module == "Home":
    st.header("Welcome to the Business Forecasting Tool")
    st.write("""
        This tool helps you forecast key aspects of your business, 
        including financial projections, operational planning, risk assessment, growth, and workforce planning.
        Use the sidebar to navigate between modules.
    """)


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

# Add a condition to display the help page
elif selected_module == "Help":
    help_page()
