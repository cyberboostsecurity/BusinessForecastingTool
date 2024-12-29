import streamlit as st
import numpy as np
import plotly.express as px
from modules.db_utils import save_to_database, load_from_database
import sqlite3

# Ensure session state keys are initialized
if "calculated_revenue" not in st.session_state:
    st.session_state["calculated_revenue"] = 0.0
if "calculated_costs" not in st.session_state:
    st.session_state["calculated_costs"] = 0.0

def calculate_adjusted_growth_rate(base_growth_rate):
    """Calculate adjusted growth rate based on the overall risk score."""
    conn = sqlite3.connect("business_calculator.db")
    cursor = conn.cursor()

    try:
        # Fetch the latest overall risk score from the database
        cursor.execute("SELECT score FROM overall_risk_score ORDER BY id DESC LIMIT 1")
        result = cursor.fetchone()
        conn.close()

        if result:
            overall_risk_score = result[0]
            # Adjust the formula to decrease growth rate based on the risk score
            if overall_risk_score > 0:
                # Decrease growth rate when risk increases
                risk_factor = 1 - (overall_risk_score / 10000)  # More risk, smaller growth
            else:
                # For negative risk, we can increase growth slightly
                risk_factor = 1 + (abs(overall_risk_score) / 5000)   # Small increase for negative risk
            
            # Debugging output
            st.write("**Debug:** Overall Risk Score:", overall_risk_score)
            st.write("**Debug:** Risk Factor:", risk_factor)
            print(f"Overall Risk Score: {overall_risk_score}")
            print(f"Risk Factor: {risk_factor}")
        else:
            st.warning("No Overall Risk Score found in the database.")
            print("No Overall Risk Score found in the database.")
            risk_factor = 1.0  # Default factor if no score is found

        # Calculate the adjusted growth rate
        adjusted_growth_rate = base_growth_rate * risk_factor

        # Provide feedback to the user
        if risk_factor < 1:
            st.write(f"**Note:** The growth rate has been adjusted by {100 * (1 - risk_factor):.2f}% due to risk factors.")
        
        return adjusted_growth_rate

    except Exception as e:
        conn.close()
        st.error(f"Error loading Overall Risk Score: {e}")
        print(f"Error loading Overall Risk Score: {e}")
        return base_growth_rate  # Fallback to base growth rate



def monte_carlo_simulations(base_value, growth_rate, projection_period, iterations=1000, std_dev_factor=0.05):
    """Run Monte Carlo simulations, handling both positive and negative growth scenarios."""
    simulated_growth_rates = np.random.normal(
        loc=growth_rate,
        scale=std_dev_factor * max(abs(growth_rate), 0.01),  # Ensure variability
        size=iterations
    )

    revenue_simulations = []
    for gr in simulated_growth_rates:
        single_simulation = []
        value = base_value
        for _ in range(projection_period):
            value *= (1 + gr / 12)  # Monthly growth or decline
            single_simulation.append(max(value, 0))  # Ensure revenue doesn't go negative
        revenue_simulations.append(single_simulation)

    return np.array(revenue_simulations)


def revenue_projections():
    """Revenue Projections with Monte Carlo simulations."""
    st.subheader("Revenue Projections with Monte Carlo")
    clients = st.slider("Number of Clients", 1, 1000, 10, 1)
    package_price = st.slider("Package Price (£)", 100.0, 100000.0, 1500.0, 100.0)
    base_growth_rate = st.slider("Annual Growth Rate (%)", -100, 100, 10) / 100
    projection_period = st.slider("Projection Period (Months)", 1, 60, 12, 1)
    risk_adjustment = st.checkbox("Include Risk Adjustment", value=False)

    base_value = clients * package_price
    growth_rate = base_growth_rate

    if risk_adjustment:
        growth_rate = calculate_adjusted_growth_rate(base_growth_rate)
        if growth_rate < 0:
            st.warning("Risk adjustment resulted in a negative growth rate.")

    simulations = monte_carlo_simulations(base_value, growth_rate, projection_period)

    if simulations.size == 0:
        st.error("Simulation failed. Check input values.")
        return

    mean_revenue = simulations.mean(axis=0)
    p5 = np.percentile(simulations, 5, axis=0)
    p95 = np.percentile(simulations, 95, axis=0)

    months = list(range(1, projection_period + 1))
    fig = px.line(x=months, y=mean_revenue, labels={"x": "Months", "y": "Revenue (£)"}, title="Mean Revenue Projection")
    fig.add_scatter(x=months, y=p5, mode="lines", name="5th Percentile", line=dict(dash="dot"))
    fig.add_scatter(x=months, y=p95, mode="lines", name="95th Percentile", line=dict(dash="dot"))
    st.plotly_chart(fig)

    st.write("### Key Metrics")
    st.write(f"- **Initial Revenue (Month 1):** £{base_value:,.2f}")
    st.write(f"- **Final Mean Revenue (Month {projection_period}):** £{mean_revenue[-1]:,.2f}")
    st.write(f"- **Growth Rate (Adjusted):** {growth_rate * 100:.2f}%")
    st.write(f"- **5th Percentile (Final Month):** £{p5[-1]:,.2f}")
    st.write(f"- **95th Percentile (Final Month):** £{p95[-1]:,.2f}")

    if st.button("Export Revenue Data to SQL"):
        save_to_database("revenue_projections", {
            "clients": clients,
            "package_price": package_price,
            "base_growth_rate": base_growth_rate,
            "projection_period": projection_period,
            "mean_revenue": mean_revenue.tolist(),
            "p5": p5.tolist(),
            "p95": p95.tolist()
        })
        st.session_state["calculated_revenue"] = sum(mean_revenue)
        st.success("Revenue data exported successfully.")


def cost_projections():
    """Cost Projections."""
    st.subheader("Cost Projections")
    fixed_costs = st.slider("Fixed Costs (£)", 0.0, 100000.0, 5000.0, 100.0)
    variable_costs_per_client = st.slider("Variable Costs per Client (£)", 0.0, 10000.0, 500.0, 50.0)
    projection_period = st.slider("Projection Period (Months)", 1, 60, 12, 1)
    clients = st.slider("Number of Clients", 1, 1000, 10, 1)

    monthly_costs = [
        fixed_costs + (variable_costs_per_client * clients)
        for _ in range(projection_period)
    ]

    months = list(range(1, projection_period + 1))
    fig = px.line(x=months, y=monthly_costs, labels={"x": "Months", "y": "Costs (£)"}, title="Cost Projections Over Time")
    st.plotly_chart(fig)

    st.write("### Total Costs")
    st.write(f"- **Fixed Costs:** £{fixed_costs:,.2f}")
    st.write(f"- **Variable Costs per Client:** £{variable_costs_per_client:,.2f}")
    st.write(f"- **Total Costs (Projection Period):** £{sum(monthly_costs):,.2f}")

    if st.button("Export Cost Data to SQL"):
        save_to_database("cost_projections", {
            "fixed_costs": fixed_costs,
            "variable_costs_per_client": variable_costs_per_client,
            "projection_period": projection_period,
            "clients": clients,
            "monthly_costs": monthly_costs
        })
        st.session_state["calculated_costs"] = sum(monthly_costs)
        st.success("Cost data exported successfully.")

def cash_flow_analysis():
    """Cash Flow Analysis."""
    st.subheader("Cash Flow Analysis")
    opening_balance = st.number_input("Opening Balance (£)", 0.0, 100000.0, 5000.0)

    revenue_data = load_from_database("revenue_projections", {"mean_revenue": []})
    cost_data = load_from_database("cost_projections", {"monthly_costs": []})

    total_revenue = sum(revenue_data.get("mean_revenue", []))
    total_costs = sum(cost_data.get("monthly_costs", []))

    st.write(f"- **Total Revenue (From SQL):** £{total_revenue:,.2f}")
    st.write(f"- **Total Costs (From SQL):** £{total_costs:,.2f}")

    net_profit = total_revenue - total_costs
    closing_balance = opening_balance + net_profit

    st.write(f"- **Opening Balance:** £{opening_balance:,.2f}")
    st.write(f"- **Net Profit Impact:** £{net_profit:,.2f}")
    st.write(f"- **Closing Balance:** £{closing_balance:,.2f}")

    labels = ["Opening Balance", "Net Profit Impact", "Closing Balance"]
    values = [opening_balance, net_profit, closing_balance]
    fig = px.bar(x=labels, y=values, labels={"x": "Category", "y": "Amount (£)"}, title="Cash Flow Analysis")
    st.plotly_chart(fig)

    if st.button("Export Cash Flow Data to SQL"):
        save_to_database("cash_flow_analysis", {
            "opening_balance": opening_balance,
            "net_profit": net_profit,
            "closing_balance": closing_balance,
        })
        st.success("Cash Flow data exported successfully.")

def profit_and_loss_projections():
    """Profit & Loss Projections."""
    st.subheader("Profit & Loss Projections")

    if st.button("Pull Data from SQL"):
        revenue_data = load_from_database("revenue_projections", {"mean_revenue": [0]})
        cost_data = load_from_database("cost_projections", {"monthly_costs": [0]})
        st.session_state["calculated_revenue"] = sum(revenue_data.get("mean_revenue", []))
        st.session_state["calculated_costs"] = sum(cost_data.get("monthly_costs", []))
        st.success("Data successfully pulled from SQL!")

    total_revenue = st.session_state.get("calculated_revenue", 0)
    total_costs = st.session_state.get("calculated_costs", 0)

    additional_expenses = st.slider("Additional Expenses (£)", 0.0, 50000.0, 500.0, 50.0)
    gross_profit = total_revenue - total_costs
    net_profit = gross_profit - additional_expenses

    st.write(f"- **Gross Profit:** £{gross_profit:,.2f}")
    st.write(f"- **Net Profit:** £{net_profit:,.2f}")

    labels = ["Gross Profit", "Additional Expenses", "Net Profit"]
    values = [gross_profit, additional_expenses, net_profit]
    fig = px.pie(values=values, names=labels, title="Profit Breakdown")
    st.plotly_chart(fig)

    if st.button("Export Profit & Loss Data to SQL"):
        save_to_database("profit_loss", {
            "gross_profit": gross_profit,
            "additional_expenses": additional_expenses,
            "net_profit": net_profit,
        })
        st.success("Profit & Loss data exported successfully.")

def financial_forecasting():
    """Main Financial Forecasting Module."""
    st.header("Financial Forecasting")
    st.info("Use this module to project revenues, costs, cash flow, and profits.")

    sub_module = st.selectbox("Select a Sub-Module", [
        "Revenue Projections with Monte Carlo",
        "Cost Projections",
        "Cash Flow Analysis",
        "Profit & Loss Projections",
    ])

    if sub_module == "Revenue Projections with Monte Carlo":
        revenue_projections()
    elif sub_module == "Cost Projections":
        cost_projections()
    elif sub_module == "Cash Flow Analysis":
        cash_flow_analysis()
    elif sub_module == "Profit & Loss Projections":
        profit_and_loss_projections()
