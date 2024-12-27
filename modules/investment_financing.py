import streamlit as st
import numpy as np
import plotly.express as px

def investment_financing():
    st.header("Investment and Financing Needs with Monte Carlo")
    st.info("Plan your funding, evaluate investments, and compare financing options.")

    # Submodule Selector
    sub_module = st.selectbox("Select a Sub-Module", [
        "Funding for Specific Goals",
        "Investment Returns",
        "Debt vs. Equity Analysis"
    ])

    # Submodule: Funding for Specific Goals
    if sub_module == "Funding for Specific Goals":
        st.subheader("Funding for Specific Goals")
        st.write("Estimate funding needs for hiring, market expansion, or product launches.")

        # Step 1: Input Goal-Specific Costs
        st.write("### Step 1: Input Goal-Specific Costs")
        goals = ["Hiring New Employees", "Market Expansion", "Product Launch", "Operational Upgrades"]
        cost_data = {}

        for goal in goals:
            st.write(f"#### {goal}")
            base_cost = st.number_input(f"Base Cost for {goal} (\u00A3)", min_value=0.0, step=1000.0, value=10000.0)
            variability = st.slider(f"{goal} Cost Variability (%)", min_value=0, max_value=50, value=10) / 100
            cost_data[goal] = (base_cost, variability)

        # Step 2: Monte Carlo Simulation for Funding Needs
        st.write("### Step 2: Monte Carlo Simulations")
        simulations = 1000
        simulated_totals = []

        for _ in range(simulations):
            total_cost = sum(
                np.random.normal(loc=cost_data[goal][0], scale=cost_data[goal][0] * cost_data[goal][1])
                for goal in goals
            )
            simulated_totals.append(total_cost)

        # Results
        mean_cost = np.mean(simulated_totals)
        p5_cost = np.percentile(simulated_totals, 5)
        p95_cost = np.percentile(simulated_totals, 95)

        st.write("### Monte Carlo Results")
        st.write(f"- **Mean Total Funding Required:** \u00A3{mean_cost:.2f}")
        st.write(f"- **Funding Range (5th to 95th Percentile):** \u00A3{p5_cost:.2f} to \u00A3{p95_cost:.2f}")

        # Visualization
        st.write("### Funding Requirements Distribution")
        fig = px.histogram(
            simulated_totals,
            nbins=50,
            title="Funding Requirements Distribution",
            labels={"x": "Total Funding (\u00A3)", "y": "Frequency"}
        )
        st.plotly_chart(fig)

        # Recommendations
        st.write("### Recommendations")
        if mean_cost < 50000:
            st.success("Your funding requirements are manageable. Consider internal funding or small loans.")
        elif mean_cost >= 50000 and mean_cost <= 200000:
            st.info("Your funding requirements are moderate. Evaluate loan options or partnerships.")
        else:
            st.warning("Your funding requirements are high. Consider detailed financial planning or raising equity.")

    # Submodule: Investment Returns
    elif sub_module == "Investment Returns":
        st.subheader("Investment Returns with Monte Carlo")
        st.write("Simulate ROI and payback periods for planned investments.")

        # Step 1: Input Investment Details
        st.write("### Step 1: Input Investment Details")
        investment_amount = st.number_input(
            "Initial Investment Amount (\u00A3)", min_value=0.0, step=1000.0, value=50000.0
        )
        projected_revenue = st.number_input(
            "Projected Annual Revenue from Investment (\u00A3)", min_value=0.0, step=1000.0, value=70000.0
        )
        variability = st.slider(
            "Revenue Variability (%)", min_value=0, max_value=50, value=10
        )
        duration = st.number_input(
            "Investment Duration (Years)", min_value=1, max_value=10, value=5
        )

        # Monte Carlo Simulations
        simulations = 1000
        annual_revenues = np.random.normal(
            loc=projected_revenue,
            scale=projected_revenue * (variability / 100),
            size=(simulations, duration)
        )
        cumulative_revenues = np.cumsum(annual_revenues, axis=1)
        rois = ((cumulative_revenues - investment_amount) / investment_amount) * 100

        # Calculate payback periods
        payback_periods = np.argmax(cumulative_revenues >= investment_amount, axis=1) + 1
        payback_periods[cumulative_revenues[:, -1] < investment_amount] = 9999

        # Results
        mean_roi = np.mean(rois[:, -1])
        p5_roi = np.percentile(rois[:, -1], 5)
        p95_roi = np.percentile(rois[:, -1], 95)

        achievable_payback_periods = payback_periods[payback_periods != 9999]
        mean_payback = np.mean(achievable_payback_periods) if len(achievable_payback_periods) > 0 else float('inf')
        p5_payback = np.percentile(achievable_payback_periods, 5) if len(achievable_payback_periods) > 0 else float('inf')
        p95_payback = np.percentile(achievable_payback_periods, 95) if len(achievable_payback_periods) > 0 else float('inf')

        # Outputs
        st.write("### Monte Carlo Results")
        st.write(f"- **Mean ROI at End of Period:** {mean_roi:.2f}%")
        st.write(f"- **ROI Range (5th to 95th Percentile):** {p5_roi:.2f}% to {p95_roi:.2f}%")
        if len(achievable_payback_periods) > 0:
            st.write(f"- **Mean Payback Period:** {mean_payback:.2f} years")
            st.write(f"- **Payback Period Range (5th to 95th Percentile):** {p5_payback:.2f} to {p95_payback:.2f} years")
        else:
            st.warning("Payback period not achievable within the given duration for most simulations.")

        # Visualization
        st.write("### ROI Distribution")
        fig_roi = px.histogram(
            rois[:, -1],
            nbins=50,
            title="ROI Distribution at End of Period",
            labels={"x": "ROI (%)", "y": "Frequency"}
        )
        st.plotly_chart(fig_roi)

        st.write("### Payback Period Distribution")
        if len(achievable_payback_periods) > 0:
            fig_payback = px.histogram(
                achievable_payback_periods,
                nbins=20,
                title="Payback Period Distribution",
                labels={"x": "Payback Period (Years)", "y": "Frequency"}
            )
            st.plotly_chart(fig_payback)
        else:
            st.write("No achievable payback periods in the simulations.")

        # Recommendations
        st.write("### Recommendations")
        if mean_roi > 50 and mean_payback < 5:
            st.success("This investment appears highly profitable. Consider proceeding!")
        elif mean_roi > 20 and mean_payback < duration:
            st.info("This investment is moderately profitable. Proceed with caution.")
        else:
            st.warning("This investment may not yield significant returns. Reassess your plans.")

    # Submodule: Debt vs. Equity Analysis
    elif sub_module == "Debt vs. Equity Analysis":
        st.subheader("Debt vs. Equity Analysis")
        st.write("Compare the financial impact of debt and equity funding options.")

        # Debt Inputs
        st.write("### Step 1: Debt Funding")
        loan_amount = st.number_input("Loan Amount (\u00A3)", min_value=0.0, step=1000.0, value=50000.0)
        interest_rate = st.slider("Annual Interest Rate (%)", min_value=1.0, max_value=20.0, step=0.1, value=5.0) / 100
        repayment_period = st.number_input("Repayment Period (Years)", min_value=1, max_value=30, step=1, value=5)

        monthly_interest_rate = interest_rate / 12
        total_months = repayment_period * 12
        monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_months) / (
            (1 + monthly_interest_rate) ** total_months - 1
        )
        total_repayment = monthly_payment * total_months
        cost_of_debt = total_repayment - loan_amount

        st.write("### Debt Metrics")
        st.write(f"- **Monthly Payment:** \u00A3{monthly_payment:.2f}")
        st.write(f"- **Total Repayment:** \u00A3{total_repayment:.2f}")
        st.write(f"- **Cost of Debt:** \u00A3{cost_of_debt:.2f}")

        # Equity Inputs
        st.write("### Step 2: Equity Funding")
        business_valuation = st.number_input("Business Valuation (\u00A3)", min_value=0.0, step=10000.0, value=500000.0)
        equity_offered = st.slider("Equity Percentage Offered (%)", min_value=1, max_value=50, step=1, value=10) / 100
        cost_of_equity = business_valuation * equity_offered
        ownership_dilution = equity_offered * 100

        st.write("### Equity Metrics")
        st.write(f"- **Cost of Equity:** \u00A3{cost_of_equity:.2f}")
        st.write(f"- **Ownership Dilution:** {ownership_dilution:.2f}%")

        # Comparison
        st.write("### Comparison")
        comparison_data = {
            "Funding Type": ["Debt", "Equity"],
            "Cost (\u00A3)": [cost_of_debt, cost_of_equity]
        }
        fig_comparison = px.bar(
            comparison_data,
            x="Funding Type",
            y="Cost (\u00A3)",
            title="Debt vs. Equity Cost Comparison",
            labels={"Cost (\u00A3)": "Cost"}
        )
        st.plotly_chart(fig_comparison)

        # Recommendations
        st.write("### Recommendations")
        if cost_of_debt < cost_of_equity:
            st.success("Debt funding is more cost-effective based on your inputs.")
        else:
            st.info("Equity funding may be favorable for long-term growth.")
