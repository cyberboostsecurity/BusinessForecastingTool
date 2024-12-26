import streamlit as st
import pandas as pd
import plotly.express as px

# Ensure session state keys are initialized
if "calculated_revenue" not in st.session_state:
    st.session_state["calculated_revenue"] = 0.0
if "calculated_costs" not in st.session_state:
    st.session_state["calculated_costs"] = 0.0
if "risk_adjusted_data" not in st.session_state:
    st.session_state["risk_adjusted_data"] = {"risk_factor": 1.0}  # Default risk factor

def financial_forecasting():
    st.header("Financial Forecasting")
    st.info("Use this module to project revenues, calculate costs, analyze cash flow, and forecast profits.")

    # Sub-Module Selection
    sub_module = st.selectbox("Select a Sub-Module", [
        "Revenue Projections", "Cost Projections", 
        "Cash Flow Analysis", "Profit & Loss Projections", "Scenario Comparison"
    ])

    # Revenue Projections
    if sub_module == "Revenue Projections":
        st.subheader("Revenue Projections")
        clients = st.slider("Number of Clients", 1, 1000, 10, 1)
        package_price = st.slider("Package Price (£)", 100.0, 100000.0, 1500.0, 100.0)
        growth_rate = st.slider("Annual Growth Rate (%)", 0, 100, 10) / 100
        risk_adjustment = st.checkbox("Include Risk Adjustment", value=False)

        # Risk factor from Risk Assessment module
        risk_factor = st.session_state["risk_adjusted_data"].get("risk_factor", 1.0)
        if risk_adjustment:
            growth_rate *= risk_factor

        current_revenue = clients * package_price
        projection_period = st.slider("Projection Period (Months)", 1, 60, 12, 1)

        revenue_trend = [current_revenue * ((1 + growth_rate) ** (i / 12)) for i in range(projection_period)]
        st.session_state["calculated_revenue"] = revenue_trend[-1]

        st.write(f"Adjusted Growth Rate: {growth_rate:.2%}")
        st.write(f"Projected Revenue (Last Month): £{revenue_trend[-1]:,.2f}")

        # Visualization
        months = list(range(1, projection_period + 1))
        fig = px.line(x=months, y=revenue_trend, labels={"x": "Months", "y": "Revenue (£)"}, title="Revenue Trend")
        st.plotly_chart(fig)

        # Export Option
        export_data = pd.DataFrame({"Month": months, "Revenue (£)": revenue_trend})
        st.download_button(
            label="Download Revenue Data as CSV",
            data=export_data.to_csv(index=False),
            file_name="revenue_projections.csv",
            mime="text/csv"
        )

    # Cost Projections
    elif sub_module == "Cost Projections":
        st.subheader("Cost Projections")
        fixed_costs = st.slider("Monthly Fixed Costs (£)", 0.0, 100000.0, 500.0, 100.0)
        variable_costs = st.slider("Variable Costs as % of Revenue", 0.0, 100.0, 10.0, 1.0) / 100
        unexpected_costs = st.number_input("Unexpected Costs (£)", 0.0, 50000.0, 1000.0)

        monthly_revenue = st.session_state["calculated_revenue"]
        total_variable_costs = monthly_revenue * variable_costs
        total_costs = fixed_costs + total_variable_costs + unexpected_costs

        st.session_state["calculated_costs"] = total_costs

        st.write(f"Monthly Fixed Costs: £{fixed_costs:,.2f}")
        st.write(f"Variable Costs (Revenue Adjusted): £{total_variable_costs:,.2f}")
        st.write(f"Total Monthly Costs: £{total_costs:,.2f}")

        # Visualization
        fig = px.bar(x=["Fixed Costs", "Variable Costs", "Unexpected Costs"], y=[fixed_costs, total_variable_costs, unexpected_costs],
                     labels={"x": "Cost Type", "y": "Amount (£)"}, title="Cost Breakdown")
        st.plotly_chart(fig)

        # Export Option
        cost_data = pd.DataFrame({
            "Cost Type": ["Fixed Costs", "Variable Costs", "Unexpected Costs"],
            "Amount (£)": [fixed_costs, total_variable_costs, unexpected_costs]
        })
        st.download_button(
            label="Download Cost Data as CSV",
            data=cost_data.to_csv(index=False),
            file_name="cost_projections.csv",
            mime="text/csv"
        )

    # Cash Flow Analysis
    elif sub_module == "Cash Flow Analysis":
        st.subheader("Cash Flow Analysis")
        opening_balance = st.slider("Opening Balance (£)", 0.0, 100000.0, 1000.0, 100.0)

        net_profit = st.session_state["calculated_revenue"] - st.session_state["calculated_costs"]
        closing_balance = opening_balance + net_profit

        st.write(f"Opening Balance: £{opening_balance:,.2f}")
        st.write(f"Net Profit Impact: £{net_profit:,.2f}")
        st.write(f"Closing Balance: £{closing_balance:,.2f}")

        # Visualization
        labels = ["Opening Balance", "Net Profit Impact", "Closing Balance"]
        values = [opening_balance, net_profit, closing_balance]
        fig = px.bar(x=labels, y=values, labels={"x": "Category", "y": "Amount (£)"}, title="Cash Flow Analysis")
        st.plotly_chart(fig)

    # Profit & Loss Projections
    elif sub_module == "Profit & Loss Projections":
        st.subheader("Profit & Loss Projections")
        additional_expenses = st.slider("Additional Expenses (£)", 0.0, 50000.0, 500.0, 50.0)

        gross_profit = st.session_state["calculated_revenue"] - st.session_state["calculated_costs"]
        net_profit = gross_profit - additional_expenses

        st.write(f"Gross Profit: £{gross_profit:,.2f}")
        st.write(f"Net Profit: £{net_profit:,.2f}")

        # Visualization
        labels = ["Gross Profit", "Additional Expenses", "Net Profit"]
        values = [gross_profit, additional_expenses, max(net_profit, 0)]
        fig = px.pie(values=values, names=labels, title="Profit Breakdown")
        st.plotly_chart(fig)

    # Scenario Comparison
    elif sub_module == "Scenario Comparison":
        st.subheader("Scenario Comparison")
        st.write("Compare two scenarios side by side.")

        # Inputs for Scenario 1
        st.write("### Scenario 1")
        clients_1 = st.number_input("Clients (Scenario 1)", 1, 1000, 10, 1)
        price_1 = st.number_input("Package Price (£, Scenario 1)", 100.0, 100000.0, 1500.0, 100.0)
        growth_1 = st.slider("Growth Rate (%) (Scenario 1)", 0, 100, 10) / 100

        # Inputs for Scenario 2
        st.write("### Scenario 2")
        clients_2 = st.number_input("Clients (Scenario 2)", 1, 1000, 10, 1)
        price_2 = st.number_input("Package Price (£, Scenario 2)", 100.0, 100000.0, 1500.0, 100.0)
        growth_2 = st.slider("Growth Rate (%) (Scenario 2)", 0, 100, 15) / 100

        revenue_1 = clients_1 * price_1 * (1 + growth_1)
        revenue_2 = clients_2 * price_2 * (1 + growth_2)

        st.write(f"Scenario 1 Revenue: £{revenue_1:,.2f}")
        st.write(f"Scenario 2 Revenue: £{revenue_2:,.2f}")

        # Visualization
        fig = px.bar(x=["Scenario 1", "Scenario 2"], y=[revenue_1, revenue_2],
                     labels={"x": "Scenario", "y": "Revenue (£)"}, title="Scenario Comparison")
        st.plotly_chart(fig)
