import streamlit as st

def investment_financing():
    st.header("Investment and Financing Needs")
    st.info("Analyze funding requirements, investment returns, and financing options.")

    sub_module = st.selectbox("Select a Sub-Module", [
        "Funding Requirements", "Investment Returns", "Debt vs. Equity"
    ])

    # Funding Requirements
    if sub_module == "Funding Requirements":
        st.subheader("Funding Requirements")
        st.write("Identify funding gaps and plan repayment schedules.")

        startup_costs = st.number_input(
            "Startup Costs (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the total startup costs."
        )
        growth_capital = st.number_input(
            "Growth Capital (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the capital required for growth."
        )
        operational_needs = st.number_input(
            "Operational Needs (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the monthly operational costs."
        )
        available_funding = st.number_input(
            "Available Funding (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the amount of funding already available."
        )

        if st.button("Calculate Funding Gap"):
            total_needs = startup_costs + growth_capital + operational_needs
            funding_gap = total_needs - available_funding
            st.write(f"**Total Funding Requirements:** \u00A3{total_needs:.2f}")
            st.write(f"**Funding Gap:** \u00A3{funding_gap:.2f}")

    # Investment Returns
    elif sub_module == "Investment Returns":
        st.subheader("Investment Returns")
        st.write("Estimate ROI on planned investments.")

        investment_amount = st.number_input(
            "Investment Amount (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the total amount invested."
        )
        expected_returns = st.number_input(
            "Expected Returns (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the expected financial returns from the investment."
        )

        if st.button("Calculate ROI"):
            if investment_amount > 0:
                roi = ((expected_returns - investment_amount) / investment_amount) * 100
                st.write(f"**Return on Investment (ROI):** {roi:.2f}%")
            else:
                st.warning("Investment amount must be greater than zero.")

    # Debt vs. Equity
    elif sub_module == "Debt vs. Equity":
        st.subheader("Debt vs. Equity")
        st.write("Compare financing options and their costs.")

        debt_amount = st.number_input(
            "Debt Amount (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the total amount of debt financing."
        )
        equity_amount = st.number_input(
            "Equity Amount (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the total amount of equity financing."
        )
        debt_interest_rate = st.slider(
            "Debt Interest Rate (%)", min_value=0, max_value=50, value=5,
            help="Select the annual interest rate for debt financing."
        )
        equity_share_percentage = st.slider(
            "Equity Share (%)", min_value=0, max_value=100, value=20,
            help="Select the percentage of equity offered."
        )

        if st.button("Compare Financing Options"):
            annual_debt_cost = debt_amount * (debt_interest_rate / 100)
            st.write(f"**Annual Debt Cost:** \u00A3{annual_debt_cost:.2f}")
            st.write(f"**Equity Share Value:** \u00A3{equity_amount:.2f} for {equity_share_percentage}% ownership.")

            if annual_debt_cost < (equity_share_percentage / 100) * equity_amount:
                st.write("Debt financing is more cost-effective.")
            else:
                st.write("Equity financing is more cost-effective.")


