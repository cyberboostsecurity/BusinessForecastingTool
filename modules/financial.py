import streamlit as st
import pandas as pd
import plotly.express as px
from modules.db_utils import save_risk_data, clear_data
from modules.db_utils import load_risk_data, save_to_database

# Ensure session state keys are initialized
if "calculated_revenue" not in st.session_state:
    st.session_state["calculated_revenue"] = 0.0
if "calculated_costs" not in st.session_state:
    st.session_state["calculated_costs"] = 0.0
if "risk_adjusted_data" not in st.session_state:
    st.session_state["risk_adjusted_data"] = {"risk_factor": 1.0}  # Default risk factor

def calculate_adjusted_growth_rate(base_growth_rate):
    """Calculate adjusted growth rate based on risk data."""
    risk_data = load_risk_data()
    # Default risk factor is 1.0 (no adjustment)
    risk_factor = 1.0
    
    # Example: You can calculate a simple risk factor based on stored risk scores (you can customize this as needed)
    if risk_data:
        # Calculate the average risk score as a simple example of adjustment (you can modify this calculation)
        average_risk_score = sum([row[4] for row in risk_data]) / len(risk_data)
        risk_factor = 1 - (average_risk_score / 100)  # Adjust growth rate based on average risk score
    
    # Apply the risk factor to the base growth rate
    adjusted_growth_rate = base_growth_rate * risk_factor
    return adjusted_growth_rate

def handle_complex_data(data):
    """Handle complex numbers by converting them to their real part."""
    if isinstance(data, complex):
        return data.real  # Only return the real part if it's a complex number
    elif isinstance(data, list):
        return [handle_complex_data(x) for x in data]  # Recursively handle each element in the list
    return data  # If not a complex number, return the data as is

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

        # Inputs for revenue projections
        clients = st.slider("Number of Clients", 1, 1000, 10, 1)
        package_price = st.slider("Package Price (£)", 100.0, 100000.0, 1500.0, 100.0)
        growth_rate = st.slider("Annual Growth Rate (%)", 0, 100, 10) / 100
        projection_period = st.slider("Projection Period (Months)", 1, 60, 12, 1)

        # Risk Adjustment
        risk_adjustment = st.checkbox("Include Risk Adjustment", value=False)
        risk_factor = st.session_state["risk_adjusted_data"].get("risk_factor", 1.0)
        if risk_adjustment:
            growth_rate = calculate_adjusted_growth_rate(growth_rate)

        # Revenue calculations
        current_revenue = clients * package_price
        revenue_trend = [current_revenue * ((1 + growth_rate) ** (i / 12)) for i in range(projection_period)]
        
        # Handle any complex numbers in the revenue trend
        revenue_trend = handle_complex_data(revenue_trend)
        
        st.session_state["calculated_revenue"] = revenue_trend[-1]

        # Display Results
        st.write(f"Adjusted Growth Rate: {growth_rate:.2%}")
        st.write(f"Projected Revenue (Last Month): £{revenue_trend[-1]:,.2f}")

        # Visualization
        months = list(range(1, projection_period + 1))
        fig = px.line(x=months, y=revenue_trend, labels={"x": "Months", "y": "Revenue (£)"}, title="Revenue Trend")
        st.plotly_chart(fig)

        # Export Button
        if st.button("Export Revenue Data to SQL"):
            save_to_database("financial_revenue", {"clients": clients, "package_price": package_price, 
                                                    "growth_rate": growth_rate, "projection_period": projection_period, 
                                                    "revenue_trend": revenue_trend})
            st.success("Revenue data exported successfully.")

        # Clear Data Button
        if st.button("Clear Revenue Data in SQL"):
            clear_data("financial_revenue")
            st.success("Revenue data cleared successfully.")

    # Cost Projections Submodule
    elif sub_module == "Cost Projections":
        st.subheader("Cost Projections")
        st.write("Project and visualize your costs over a period of time.")

        # Inputs for cost projections
        fixed_costs = st.slider("Fixed Costs (£)", 0.0, 100000.0, 5000.0, 100.0)
        variable_costs = st.slider("Variable Costs per Client (£)", 0.0, 10000.0, 500.0, 50.0)
        growth_rate = st.slider("Annual Growth Rate for Costs (%)", 0, 100, 5) / 100
        projection_period = st.slider("Projection Period (Months)", 1, 60, 12, 1)

        # Calculate total costs
        total_costs = [fixed_costs + (clients * variable_costs) for clients in range(1, projection_period + 1)]
        
        # Handle any complex numbers in total costs
        total_costs = handle_complex_data(total_costs)
        
        st.session_state["calculated_costs"] = sum(total_costs)

        # Display Results
        st.write(f"Total Costs for {projection_period} months: £{st.session_state['calculated_costs']:,.2f}")

        # Visualization
        months = list(range(1, projection_period + 1))
        fig = px.line(x=months, y=total_costs, labels={"x": "Months", "y": "Total Costs (£)"}, title="Cost Projections")
        st.plotly_chart(fig)

        # Export Button
        if st.button("Export Cost Data to SQL"):
            save_to_database("financial_costs", {"fixed_costs": fixed_costs, "variable_costs": variable_costs, 
                                                 "growth_rate": growth_rate, "projection_period": projection_period, 
                                                 "total_costs": total_costs})
            st.success("Cost data exported successfully.")

        # Clear Data Button
        if st.button("Clear Cost Data in SQL"):
            clear_data("financial_costs")
            st.success("Cost data cleared successfully.")

    # Cash Flow Analysis Submodule
    elif sub_module == "Cash Flow Analysis":
        st.subheader("Cash Flow Analysis")
        st.write("Analyze net cash flow and closing balances based on profit projections and starting balance.")

        # Input for opening balance
        opening_balance = st.slider("Opening Balance (£)", 0.0, 100000.0, 1000.0, 100.0)

        # Fetch net profit from session state
        net_profit = st.session_state["calculated_revenue"] - st.session_state["calculated_costs"]
        closing_balance = opening_balance + net_profit

        # Display results
        st.write(f"Opening Balance: £{opening_balance:,.2f}")
        st.write(f"Net Profit Impact: £{net_profit:,.2f}")
        st.write(f"Closing Balance: £{closing_balance:,.2f}")

        # Visualization
        labels = ["Opening Balance", "Net Profit Impact", "Closing Balance"]
        values = [opening_balance, net_profit, closing_balance]
        fig = px.bar(x=labels, y=values, labels={"x": "Category", "y": "Amount (£)"}, title="Cash Flow Analysis")
        st.plotly_chart(fig)

        # Export to SQL
        if st.button("Export Cash Flow Data to Database"):
            data = {
                "opening_balance": opening_balance,
                "net_profit": net_profit,
                "closing_balance": closing_balance,
            }
            save_to_database("cash_flow", data)
            st.success("Cash Flow data exported successfully.")

    # Profit & Loss Projections Submodule
    elif sub_module == "Profit & Loss Projections":
        st.subheader("Profit & Loss Projections")
        st.write("Forecast your profit and loss based on revenue, costs, and additional expenses.")

        # Additional Expenses
        additional_expenses = st.slider("Additional Expenses (£)", 0.0, 50000.0, 500.0, 50.0)

        # Calculate profit
        gross_profit = st.session_state["calculated_revenue"] - st.session_state["calculated_costs"]
        net_profit = gross_profit - additional_expenses

        # Display results
        st.write(f"Gross Profit: £{gross_profit:,.2f}")
        st.write(f"Net Profit: £{net_profit:,.2f}")

        # Visualization
        labels = ["Gross Profit", "Additional Expenses", "Net Profit"]
        values = [gross_profit, additional_expenses, max(net_profit, 0)]
        fig = px.pie(values=values, names=labels, title="Profit Breakdown")
        st.plotly_chart(fig)

        # Export to SQL
        if st.button("Export Profit & Loss Data to Database"):
            data = {
                "gross_profit": gross_profit,
                "additional_expenses": additional_expenses,
                "net_profit": net_profit,
            }
            save_to_database("profit_loss", data)
            st.success("Profit & Loss data exported successfully.")

    # Scenario Comparison Submodule
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

        # Display results
        st.write(f"Scenario 1 Revenue: £{revenue_1:,.2f}")
        st.write(f"Scenario 2 Revenue: £{revenue_2:,.2f}")

        # Visualization
        fig = px.bar(x=["Scenario 1", "Scenario 2"], y=[revenue_1, revenue_2],
                     labels={"x": "Scenario", "y": "Revenue (£)"}, title="Scenario Comparison")
        st.plotly_chart(fig)

        # Export to SQL
        if st.button("Export Scenario Comparison Data to Database"):
            data = {
                "scenario_1": {
                    "clients": clients_1,
                    "package_price": price_1,
                    "growth_rate": growth_1,
                    "revenue": revenue_1,
                },
                "scenario_2": {
                    "clients": clients_2,
                    "package_price": price_2,
                    "growth_rate": growth_2,
                    "revenue": revenue_2,
                },
            }
            save_to_database("scenario_comparison", data)
            st.success("Scenario Comparison data exported successfully.")
