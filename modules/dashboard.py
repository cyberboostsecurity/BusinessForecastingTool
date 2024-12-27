import streamlit as st
import plotly.express as px
import pandas as pd

# Dashboard Function
def dashboard():
    st.title("Business Forecasting Dashboard")
    st.info("Get a comprehensive overview of your business performance metrics.")

    # Tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs([
        "Financial Overview", "Workforce Overview", "Growth & Scaling", "Risk Assessment"])

    # Financial Overview
    with tab1:
        st.subheader("Financial Overview")

        # Check if financial data is available
        if "financial_metrics" in st.session_state:
            financial_data = st.session_state["financial_metrics"]
            
            # Display metrics
            st.metric("Total Revenue", f"\u00A3{financial_data['total_revenue']:.2f}")
            st.metric("Total Costs", f"\u00A3{financial_data['total_costs']:.2f}")
            st.metric("Profit/Loss", f"\u00A3{financial_data['profit_loss']:.2f}")

            # Visualization: Revenue vs Costs
            fig = px.bar(
                x=["Revenue", "Costs"],
                y=[financial_data['total_revenue'], financial_data['total_costs']],
                labels={"x": "Category", "y": "Amount"},
                title="Revenue vs Costs"
            )
            st.plotly_chart(fig)
        else:
            st.warning("No financial data available. Please complete the Financial Forecasting module.")

    # Workforce Overview
    with tab2:
        st.subheader("Workforce Overview")

        # Check if workforce data is available
        if "workforce_metrics" in st.session_state:
            workforce_data = st.session_state["workforce_metrics"]

            # Display metrics
            st.metric("Total Staffing Costs", f"\u00A3{workforce_data['total_staffing_costs']:.2f}")
            st.metric("Average Revenue per Employee", f"\u00A3{workforce_data['revenue_per_employee']:.2f}")

            # Visualization: Staffing Cost Breakdown
            fig = px.pie(
                names=workforce_data['cost_categories'],
                values=workforce_data['cost_values'],
                title="Staffing Cost Breakdown"
            )
            st.plotly_chart(fig)
        else:
            st.warning("No workforce data available. Please complete the Workforce Planning module.")

    # Growth & Scaling Overview
    with tab3:
        st.subheader("Growth & Scaling Overview")

        # Check if growth data is available
        if "growth_metrics" in st.session_state:
            growth_data = st.session_state["growth_metrics"]

            # Display metrics
            st.metric("Average ROI", f"{growth_data['average_roi']:.2f}%")
            st.metric("Payback Period", f"{growth_data['payback_period']:.2f} months")

            # Visualization: ROI Distribution
            fig = px.histogram(
                growth_data['roi_distribution'],
                title="ROI Distribution",
                labels={"value": "ROI (%)", "count": "Frequency"}
            )
            st.plotly_chart(fig)
        else:
            st.warning("No growth data available. Please complete the Growth & Scaling module.")

    # Risk Assessment Overview
    with tab4:
        st.subheader("Risk Assessment Overview")

        # Check if risk data is available
        if "risk_metrics" in st.session_state:
            risk_data = st.session_state["risk_metrics"]

            # Display metrics
            st.metric("Overall Risk Score", f"{risk_data['overall_risk_score']:.2f}")
            st.metric("Mitigated Risks", f"{risk_data['mitigated_risks']}")
            st.metric("Unmitigated Risks", f"{risk_data['unmitigated_risks']}")

            # Visualization: Risk Breakdown
            fig = px.bar(
                x=risk_data['risk_categories'],
                y=risk_data['risk_values'],
                labels={"x": "Risk Category", "y": "Risk Score"},
                title="Risk Breakdown"
            )
            st.plotly_chart(fig)
        else:
            st.warning("No risk data available. Please complete the Risk Assessment module.")

# Test the Dashboard function (Uncomment to test locally)
# if __name__ == "__main__":
#     dashboard()
