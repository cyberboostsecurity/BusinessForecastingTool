import streamlit as st
import numpy as np
import plotly.express as px
from modules.db_utils import save_to_database, clear_data, load_risk_data

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
    risk_factor = 1.0  # Default risk factor

    if risk_data:
        # Average risk score as a simple adjustment
        average_risk_score = sum([row[4] for row in risk_data]) / len(risk_data)
        risk_factor = 1 - (average_risk_score / 100)  # Example adjustment logic

    adjusted_growth_rate = base_growth_rate * risk_factor
    return max(adjusted_growth_rate, 0)  # Ensure growth rate is non-negative


def monte_carlo_simulations(base_value, growth_rate, projection_period, iterations=1000, std_dev_factor=0.05):
    """Run Monte Carlo simulations."""
    growth_rate = max(growth_rate, 0)  # Ensure non-negative growth rates

    simulated_growth_rates = np.random.normal(
        loc=growth_rate,
        scale=std_dev_factor * max(growth_rate, 0.01),  # Avoid 0 scale
        size=iterations
    )
    revenue_simulations = [
        [base_value * ((1 + gr) ** (i / 12)) for gr in simulated_growth_rates]
        for i in range(projection_period)
    ]
    return np.array(revenue_simulations).T  # Transpose for better visualization


def revenue_projections_monte_carlo():
    """Revenue Projections with Monte Carlo simulations."""
    st.subheader("Revenue Projections with Monte Carlo")
    clients = st.slider("Number of Clients", 1, 1000, 10, 1)
    package_price = st.slider("Package Price (£)", 100.0, 100000.0, 1500.0, 100.0)
    base_growth_rate = st.slider("Annual Growth Rate (%)", 0, 100, 10) / 100
    projection_period = st.slider("Projection Period (Months)", 1, 60, 12, 1)
    risk_adjustment = st.checkbox("Include Risk Adjustment", value=False)

    base_value = clients * package_price
    growth_rate = base_growth_rate
    if risk_adjustment:
        growth_rate = calculate_adjusted_growth_rate(base_growth_rate)
        if growth_rate == 0:
            st.warning("Risk adjustment resulted in a negative growth rate. Defaulting to 0% growth.")

    simulations = monte_carlo_simulations(base_value, growth_rate, projection_period)
    mean_revenue = simulations.mean(axis=0)
    p5 = np.percentile(simulations, 5, axis=0)
    p95 = np.percentile(simulations, 95, axis=0)

    months = list(range(1, projection_period + 1))
    fig = px.line(x=months, y=mean_revenue, labels={"x": "Months", "y": "Revenue (£)"}, title="Mean Revenue Projection")
    fig.add_scatter(x=months, y=p5, mode="lines", name="5th Percentile", line=dict(dash="dot"))
    fig.add_scatter(x=months, y=p95, mode="lines", name="95th Percentile", line=dict(dash="dot"))
    st.plotly_chart(fig)

    final_month_revenues = simulations[:, -1]
    fig_hist = px.histogram(final_month_revenues, nbins=50, title="Revenue Distribution for Final Month")
    st.plotly_chart(fig_hist)

    if st.button("Export Revenue Data to SQL"):
        save_to_database("revenue_projections", {
            "clients": clients,
            "package_price": package_price,
            "base_growth_rate": base_growth_rate,
            "projection_period": projection_period,
            "mean_revenue": mean_revenue.tolist(),
            "revenue_simulations": simulations.tolist(),
            
        })


def cost_projections():
    """Cost Projections."""
    st.subheader("Cost Projections")
    fixed_costs = st.slider("Fixed Costs (£)", 0.0, 100000.0, 5000.0, 100.0)
    variable_costs = st.slider("Variable Costs per Client (£)", 0.0, 10000.0, 500.0, 50.0)
    projection_period = st.slider("Projection Period (Months)", 1, 60, 12, 1)

    total_costs = [fixed_costs + variable_costs * i for i in range(1, projection_period + 1)]
    st.session_state["calculated_costs"] = sum(total_costs)

    months = list(range(1, projection_period + 1))
    fig = px.line(x=months, y=total_costs, labels={"x": "Months", "y": "Costs (£)"}, title="Cost Projections")
    st.plotly_chart(fig)


def cash_flow_analysis():
    """Cash Flow Analysis."""
    st.subheader("Cash Flow Analysis")
    opening_balance = st.number_input("Opening Balance (£)", 0.0, 100000.0, 1000.0)
    net_profit = st.session_state["calculated_revenue"] - st.session_state["calculated_costs"]
    closing_balance = opening_balance + net_profit

    st.write(f"Opening Balance: £{opening_balance:,.2f}")
    st.write(f"Net Profit Impact: £{net_profit:,.2f}")
    st.write(f"Closing Balance: £{closing_balance:,.2f}")

    labels = ["Opening Balance", "Net Profit Impact", "Closing Balance"]
    values = [opening_balance, net_profit, closing_balance]
    fig = px.bar(x=labels, y=values, labels={"x": "Category", "y": "Amount (£)"}, title="Cash Flow Analysis")
    st.plotly_chart(fig)


def profit_and_loss_projections():
    """Profit & Loss Projections."""
    st.subheader("Profit & Loss Projections")

    # Ensure session state values are valid
    revenue = st.session_state.get("calculated_revenue", 0.0)
    costs = st.session_state.get("calculated_costs", 0.0)

    # Display current revenue and costs for debugging
    st.write(f"Calculated Revenue: £{revenue:,.2f}")
    st.write(f"Calculated Costs: £{costs:,.2f}")

    additional_expenses = st.slider("Additional Expenses (£)", 0.0, 50000.0, 500.0, 50.0)

    # Calculate gross profit and net profit
    gross_profit = max(revenue - costs, 0)  # Ensure no negative gross profit
    net_profit = max(gross_profit - additional_expenses, 0)  # Ensure no negative net profit

    # Display results
    st.write(f"Gross Profit: £{gross_profit:,.2f}")
    st.write(f"Net Profit: £{net_profit:,.2f}")

    # Visualization
    labels = ["Gross Profit", "Additional Expenses", "Net Profit"]
    values = [gross_profit, additional_expenses, net_profit]
    fig = px.pie(values=values, names=labels, title="Profit Breakdown")
    st.plotly_chart(fig)

    # Save to SQL
    if st.button("Export Profit & Loss Data to SQL"):
        save_to_database("profit_loss", {
            "gross_profit": gross_profit,
            "additional_expenses": additional_expenses,
            "net_profit": net_profit,
        })
        st.success("Profit & Loss data exported successfully.")



def scenario_comparison():
    """Scenario Comparison Submodule with Monte Carlo."""
    st.subheader("Scenario Comparison with Monte Carlo")
    st.write("Compare two revenue scenarios with probabilistic outcomes.")

    # Inputs for Scenario 1
    st.write("### Scenario 1")
    clients_1 = st.slider("Number of Clients (Scenario 1)", 1, 1000, 10, 1)
    price_1 = st.slider("Package Price (£, Scenario 1)", 100.0, 100000.0, 1500.0, 100.0)
    growth_1 = st.slider("Annual Growth Rate (%) (Scenario 1)", 0, 100, 10) / 100
    projection_period_1 = st.slider("Projection Period (Months, Scenario 1)", 1, 60, 12, 1)
    risk_adjustment_1 = st.checkbox("Include Risk Adjustment for Scenario 1", value=False)

    # Inputs for Scenario 2
    st.write("### Scenario 2")
    clients_2 = st.slider("Number of Clients (Scenario 2)", 1, 1000, 10, 1)
    price_2 = st.slider("Package Price (£, Scenario 2)", 100.0, 100000.0, 1500.0, 100.0)
    growth_2 = st.slider("Annual Growth Rate (%) (Scenario 2)", 0, 100, 15) / 100
    projection_period_2 = st.slider("Projection Period (Months, Scenario 2)", 1, 60, 12, 1)
    risk_adjustment_2 = st.checkbox("Include Risk Adjustment for Scenario 2", value=False)

    # Calculate base values
    base_value_1 = clients_1 * price_1
    base_value_2 = clients_2 * price_2

    # Adjust growth rates for risk
    if risk_adjustment_1:
        growth_1 = calculate_adjusted_growth_rate(growth_1)
    if risk_adjustment_2:
        growth_2 = calculate_adjusted_growth_rate(growth_2)

    # Monte Carlo Simulations for both scenarios
    simulations_1 = monte_carlo_simulations(base_value_1, growth_1, projection_period_1)
    simulations_2 = monte_carlo_simulations(base_value_2, growth_2, projection_period_2)

    # Calculate statistics
    final_revenues_1 = simulations_1[:, -1]
    final_revenues_2 = simulations_2[:, -1]
    mean_1 = final_revenues_1.mean()
    mean_2 = final_revenues_2.mean()
    p5_1 = np.percentile(final_revenues_1, 5)
    p95_1 = np.percentile(final_revenues_1, 95)
    p5_2 = np.percentile(final_revenues_2, 5)
    p95_2 = np.percentile(final_revenues_2, 95)

    # Display Statistics
    st.write("### Results")
    st.write(f"**Scenario 1**: Mean Revenue: £{mean_1:,.2f}, 5th Percentile: £{p5_1:,.2f}, 95th Percentile: £{p95_1:,.2f}")
    st.write(f"**Scenario 2**: Mean Revenue: £{mean_2:,.2f}, 5th Percentile: £{p5_2:,.2f}, 95th Percentile: £{p95_2:,.2f}")

    # Visualization: Distribution of final revenues
    fig = px.histogram(
        x=[final_revenues_1, final_revenues_2],
        nbins=50,
        labels={"value": "Final Revenue (£)", "variable": "Scenario"},
        title="Final Revenue Distribution",
        color_discrete_map={"Scenario 1": "blue", "Scenario 2": "green"},
    )
    fig.update_layout(barmode="overlay")
    fig.update_traces(opacity=0.6)
    st.plotly_chart(fig)

    # Visualization: Trend with Percentiles
    months = list(range(1, max(projection_period_1, projection_period_2) + 1))
    mean_revenue_1 = simulations_1.mean(axis=0)
    mean_revenue_2 = simulations_2.mean(axis=0)
    p5_revenue_1 = np.percentile(simulations_1, 5, axis=0)
    p95_revenue_1 = np.percentile(simulations_1, 95, axis=0)
    p5_revenue_2 = np.percentile(simulations_2, 5, axis=0)
    p95_revenue_2 = np.percentile(simulations_2, 95, axis=0)

    fig_trend = px.line(x=months[:projection_period_1], y=mean_revenue_1,
                        labels={"x": "Months", "y": "Revenue (£)"}, title="Revenue Trend for Scenarios")
    fig_trend.add_scatter(x=months[:projection_period_1], y=p5_revenue_1, mode="lines", name="5th Percentile (Scenario 1)", line=dict(dash="dot"))
    fig_trend.add_scatter(x=months[:projection_period_1], y=p95_revenue_1, mode="lines", name="95th Percentile (Scenario 1)", line=dict(dash="dot"))
    fig_trend.add_scatter(x=months[:projection_period_2], y=mean_revenue_2, mode="lines", name="Mean (Scenario 2)")
    fig_trend.add_scatter(x=months[:projection_period_2], y=p5_revenue_2, mode="lines", name="5th Percentile (Scenario 2)", line=dict(dash="dot"))
    fig_trend.add_scatter(x=months[:projection_period_2], y=p95_revenue_2, mode="lines", name="95th Percentile (Scenario 2)", line=dict(dash="dot"))
    st.plotly_chart(fig_trend)

    # Export and Clear Data Options
    if st.button("Export Scenario Comparison Data to SQL"):
        save_to_database("scenario_comparison", {
            "scenario_1": {
                "clients": clients_1,
                "package_price": price_1,
                "growth_rate": growth_1,
                "projection_period": projection_period_1,
                "final_revenues": final_revenues_1.tolist(),
            },
            "scenario_2": {
                "clients": clients_2,
                "package_price": price_2,
                "growth_rate": growth_2,
                "projection_period": projection_period_2,
                "final_revenues": final_revenues_2.tolist(),
            },
        })
        st.success("Scenario comparison data exported successfully.")


def financial_forecasting():
    """Main Financial Forecasting Module."""
    st.header("Financial Forecasting")
    st.info("Use this module to project revenues, costs, cash flow, and profits.")

    sub_module = st.selectbox("Select a Sub-Module", [
        "Revenue Projections with Monte Carlo",
        "Cost Projections",
        "Cash Flow Analysis",
        "Profit & Loss Projections",
        "Scenario Comparison"  # Add Scenario Comparison here
    ])

    if sub_module == "Revenue Projections with Monte Carlo":
        revenue_projections_monte_carlo()
    elif sub_module == "Cost Projections":
        cost_projections()
    elif sub_module == "Cash Flow Analysis":
        cash_flow_analysis()
    elif sub_module == "Profit & Loss Projections":
        profit_and_loss_projections()
    elif sub_module == "Scenario Comparison":
        scenario_comparison()