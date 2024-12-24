import streamlit as st

def financial_forecasting():
    st.header("Financial Forecasting")
    st.info("Use this module to project revenues, calculate costs, analyze cash flow, and forecast profits.")

    # Define the sub-module selection
    sub_module = st.selectbox("Select a Sub-Module", [
        "Revenue Projections", "Cost Projections", 
        "Cash Flow Analysis", "Profit & Loss Projections"
    ])

    # Handle Revenue Projections
    if sub_module == "Revenue Projections":
        st.subheader("Revenue Projections")
        st.write("Calculate current and projected monthly revenue based on the number of clients, package price, and growth rate.")

        clients = st.number_input("Number of Clients", min_value=0, step=1, help="Enter the total number of active clients.")
        package_price = st.number_input("Package Price (\u00A3)", min_value=0.0, step=100.0, help="Enter the price per package in GBP.")
    
        # Clarify that the growth rate is annual
        growth_rate = st.slider(
            "Annual Growth Rate (%)", min_value=0, max_value=100, value=10,
            help="Select the expected annual percentage growth in revenue."
        )

        if st.button("Calculate Revenue"):
            # Ensure growth rate is properly reflected in calculations
            current_revenue = clients * package_price
            projected_revenue = current_revenue * (1 + (growth_rate / 100))  # Annual growth rate applied

            st.write(f"Current Monthly Revenue: \u00A3{current_revenue:.2f}")
            st.write(f"Projected Annual Revenue with {growth_rate}% Growth: \u00A3{projected_revenue:.2f}")

    # Handle Cost Projections
    elif sub_module == "Cost Projections":
        st.subheader("Cost Projections")
        st.write("Estimate monthly costs based on fixed costs, variable costs, and expected growth.")

        # Inputs for fixed and variable costs
        fixed_costs = st.number_input(
            "Monthly Fixed Costs (\u00A3)", min_value=0.0, step=100.0,
            help="Enter costs that do not change with revenue (e.g., rent, salaries)."
        )
        variable_costs = st.number_input(
            "Monthly Variable Costs (\u00A3)", min_value=0.0, step=100.0,
            help="Enter costs that vary based on revenue (e.g., raw materials, client services)."
        )
    
        # Expected growth rate (annual)
        cost_growth_rate = st.slider(
            "Expected Annual Cost Growth Rate (%)", min_value=-50, max_value=50, value=0,
            help="Enter the expected percentage increase or decrease in total costs annually."
        ) / 100  # Convert to decimal for calculations

        if st.button("Calculate Costs"):
            # Step 1: Calculate base costs
            base_annual_costs = (fixed_costs + variable_costs) * 12
            base_monthly_costs = base_annual_costs / 12

            # Step 2: Apply growth rate
            growth_effect_annual = base_annual_costs * cost_growth_rate
            growth_effect_monthly = growth_effect_annual / 12

            total_annual_costs = base_annual_costs + growth_effect_annual
            total_monthly_costs = total_annual_costs / 12

            # Display results with detailed breakdown
            st.write("### Calculation Breakdown")
            st.write(f"- **Base Monthly Costs (before growth):** \u00A3{base_monthly_costs:.2f}")
            st.write(f"- **Growth Effect (monthly):** \u00A3{growth_effect_monthly:.2f}")
            st.write(f"- **Total Monthly Costs (after growth):** \u00A3{total_monthly_costs:.2f}")

    # Handle Profit & Loss Projections
    elif sub_module == "Profit & Loss Projections":
        st.subheader("Profit & Loss Projections")
        st.write("Forecast your profit and loss based on revenue, costs, and additional expenses.")

        # Inputs for revenue and costs
        revenue = st.number_input(
            "Monthly Revenue (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the total revenue generated in a month."
        )
        costs = st.number_input(
            "Monthly Costs (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the total costs incurred in a month."
        )
    
        # Additional expenses
        additional_expenses = st.number_input(
            "Additional Expenses (\u00A3)", min_value=0.0, step=100.0,
            help="Enter any additional expenses like taxes, overheads, etc."
        )

        if st.button("Calculate Profit & Loss"):
            # Calculate Gross Profit and Net Profit
            gross_profit = revenue - costs
            net_profit = gross_profit - additional_expenses

            # Display results with a breakdown
            st.write("### Profit & Loss Breakdown")
            st.write(f"- **Revenue:** \u00A3{revenue:.2f}")
            st.write(f"- **Costs:** \u00A3{costs:.2f}")
            st.write(f"- **Gross Profit:** \u00A3{gross_profit:.2f}")
            st.write(f"- **Additional Expenses:** \u00A3{additional_expenses:.2f}")
            st.write(f"- **Net Profit:** \u00A3{net_profit:.2f}")

            # Highlight if the business is in a loss
            if net_profit < 0:
                st.warning("Your business is running at a loss! Consider reducing costs or increasing revenue.")

    # Handle Cash Flow Analysis
    elif sub_module == "Cash Flow Analysis":
        st.subheader("Cash Flow Analysis")
        st.write("Analyze net cash flow and closing balances based on revenues, costs, and the starting balance.")

        opening_balance = st.number_input(
            "Opening Balance (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the available cash balance at the beginning of the period."
        )
        revenue = st.number_input(
            "Monthly Revenue (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the total revenue generated in the period."
        )
        costs = st.number_input(
            "Monthly Costs (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the total costs incurred in the period."
        )

        if st.button("Calculate Cash Flow"):
            net_cash_flow = revenue - costs
            closing_balance = opening_balance + net_cash_flow

            st.write(f"Net Cash Flow: \u00A3{net_cash_flow:.2f}")
            st.write(f"Closing Balance: \u00A3{closing_balance:.2f}")

            if closing_balance < 0:
                st.warning("Alert: Your closing balance is negative! Review your expenses or increase revenue.")
