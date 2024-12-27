import streamlit as st
from modules.operational import operational_planning
from modules.financial import financial_forecasting
from modules.risk_assessment import risk_assessment
from modules.growth_scaling import growth_scaling
from modules.investment_financing import investment_financing
from modules.workforce import workforce_projections
from modules.help import help_page
from modules.dashboard import dashboard  # Directly import the function
from modules.db_utils import clear_data
import os

# Navigation
st.title("Business Forecasting Tool")
st.sidebar.header("Navigation")

# Update the navigation menu to use a radio button
selected_module = st.sidebar.radio(
    "Select a Module",
    [
        "Home",
        "Help",
        "Risk Assessment",
        "Financial Forecasting",
        "Workforce and Culture Projections",            
        "Growth & Scaling Strategy",
        "Operational Planning",
        "Investment and Financing Needs",        
        "Dashboard",
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
    image_path = "path_to_homepage_image.jpg"  # Update with your image path
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.warning("Image not found. Please check the file path.")

# Dashboard Module
elif selected_module == "Dashboard":
    dashboard()

# Financial Forecasting Module
elif selected_module == "Financial Forecasting":
    try:
        financial_forecasting()
    except Exception as e:
        st.error(f"An error occurred in Financial Forecasting: {e}")

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

# Option to Clear Database
if st.sidebar.button("Clear All Database Data"):
    try:
        clear_data()
        st.sidebar.success("All database data has been cleared!")
    except Exception as e:
        st.sidebar.error(f"Failed to clear database data: {e}")
