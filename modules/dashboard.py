import streamlit as st
import plotly.express as px
import pandas as pd
from modules.db_utils import load_from_database

def dashboard():
    st.title("Business Forecasting Dashboard")
    st.info("Get a comprehensive overview of your business performance metrics.")

    # Tabs for different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Financial Overview", "Workforce Overview", "Growth & Scaling", "Risk Assessment", "Debug SQL Data"])

    # Financial Overview
    with tab1:
        st.subheader("Financial Overview")

        # Load data from database
        financial_data = load_from_database("financial_metrics", default={})
        if financial_data:
            st.metric("Total Revenue", f"\u00A3{financial_data.get('total_revenue', 0):.2f}")
            st.metric("Total Costs", f"\u00A3{financial_data.get('total_costs', 0):.2f}")
            st.metric("Profit/Loss", f"\u00A3{financial_data.get('profit_loss', 0):.2f}")

            # Visualization: Revenue vs Costs
            fig = px.bar(
                x=["Revenue", "Costs"],
                y=[financial_data.get('total_revenue', 0), financial_data.get('total_costs', 0)],
                labels={"x": "Category", "y": "Amount"},
                title="Revenue vs Costs"
            )
            st.plotly_chart(fig)
        else:
            st.warning("No financial data available. Please complete the Financial Forecasting module.")

    # Workforce Overview
    with tab2:
        st.subheader("Workforce Overview")

        # Load data from database
        workforce_data = load_from_database("workforce_metrics", default={})
        if workforce_data:
            st.metric("Total Staffing Costs", f"\u00A3{workforce_data.get('total_staffing_costs', 0):.2f}")
            st.metric("Average Revenue per Employee", f"\u00A3{workforce_data.get('revenue_per_employee', 0):.2f}")

            # Visualization: Staffing Cost Breakdown
            fig = px.pie(
                names=workforce_data.get('cost_categories', []),
                values=workforce_data.get('cost_values', []),
                title="Staffing Cost Breakdown"
            )
            st.plotly_chart(fig)
        else:
            st.warning("No workforce data available. Please complete the Workforce Planning module.")

    # Growth & Scaling Overview
    with tab3:
        st.subheader("Growth & Scaling Overview")

        # Load data from database
        growth_data = load_from_database("growth_metrics", default={})
        if growth_data:
            st.metric("Average ROI", f"{growth_data.get('average_roi', 0):.2f}%")
            st.metric("Payback Period", f"{growth_data.get('payback_period', 0):.2f} months")

            # Visualization: ROI Distribution
            fig = px.histogram(
                growth_data.get('roi_distribution', []),
                title="ROI Distribution",
                labels={"value": "ROI (%)", "count": "Frequency"}
            )
            st.plotly_chart(fig)
        else:
            st.warning("No growth data available. Please complete the Growth & Scaling module.")

    # Risk Assessment Overview
    with tab4:
        st.subheader("Risk Assessment Overview")

        # Load data from database
        risk_data = load_from_database("risk_metrics", default={})
        if risk_data:
            st.metric("Overall Risk Score", f"{risk_data.get('overall_risk_score', 0):.2f}")
            st.metric("Mitigated Risks", f"{risk_data.get('mitigated_risks', 0)}")
            st.metric("Unmitigated Risks", f"{risk_data.get('unmitigated_risks', 0)}")

            # Visualization: Risk Breakdown
            fig = px.bar(
                x=risk_data.get('risk_categories', []),
                y=risk_data.get('risk_values', []),
                labels={"x": "Risk Category", "y": "Risk Score"},
                title="Risk Breakdown"
            )
            st.plotly_chart(fig)
        else:
            st.warning("No risk data available. Please complete the Risk Assessment module.")

    # Debug SQL Data
    with tab5:
        st.subheader("Debug SQL Data Extraction")

        # Define the keys/modules to test
        keys_to_test = [
            "financial_metrics",
            "workforce_metrics",
            "growth_metrics",
            "risk_metrics",
            "funding_for_goals",
            "investment_returns",
            "debt_vs_equity"
        ]

        for key in keys_to_test:
            st.write(f"### Debugging `{key}`")

            # Attempt to load data from the database
            data = load_from_database(key, default=None)

            if data:
                st.success(f"Data for `{key}` loaded successfully!")
                st.json(data)  # Display the data as JSON
            else:
                st.error(f"No data found for `{key}`. Check if the corresponding module has saved the data.")

    # Add refresh button
    st.write("To refresh data, please restart the application or manually reload the page.")
