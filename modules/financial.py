import streamlit as st
import matplotlib.pyplot as plt

# Global state for revenue and costs
if "calculated_revenue" not in st.session_state:
    st.session_state["calculated_revenue"] = 0.0
if "calculated_costs" not in st.session_state:
    st.session_state["calculated_costs"] = 0.0


def financial_forecasting():
    st.header("Financial Forecasting")
    st.info("Use this module to project revenues, calculate costs, analyze cash flow, and forecast profits.")

    # Define the sub-module selection
    sub_module = st.selectbox("Select a Sub-Module", [
        "Revenue Projections", "Cost Projections", 
        "Cash Flow Analysis", "Profit & Loss Projections", "Scenario Comparison"
    ])

    # Handle Revenue Projections
    if sub_module == "Revenue Projections":
        st.subheader("Revenue Projections")
        st.write("Calculate current and projected monthly revenue based on the number of clients, package price, and growth rate.")

        # Use sliders for interactive inputs
        clients = st.slider("Number of Clients", min_value=1, max_value=1000, value=10, step=1)
        package_price = st.slider("Package Price (\u00A3)", min_value=100.0, max_value=100000.0, value=1500.0, step=100.0)
        growth_rate = st.slider("Annual Growth Rate (%)", min_value=0, max_value=100, value=10) / 100
        projection_period = st.slider("Projection Period (Months)", min_value=1, max_value=60, value=12, step=1)

        # Dynamic Calculations
        current_revenue = clients * package_price
        monthly_growth_rate = (1 + growth_rate) ** (1 / 12) - 1
        revenue_trend = [current_revenue * (1 + monthly_growth_rate) ** i for i in range(projection_period)]

        # Display Results
        st.write(f"Current Monthly Revenue: \u00A3{current_revenue:.2f}")
        st.session_state["calculated_revenue"] = revenue_trend[-1]  # Save last month's revenue in session state
        st.write(f"Projected Annual Revenue with {int(growth_rate * 100)}% Growth: \u00A3{revenue_trend[-1] * 12:.2f}")


        # Visualization
        st.write("### Revenue Projection Trend")
        months = list(range(1, projection_period + 1))
        plt.figure(figsize=(10, 5))
        plt.plot(months, revenue_trend, marker='o', linestyle='-', color='b')
        plt.title("Projected Revenue Over Time")
        plt.xlabel("Months")
        plt.ylabel("Revenue (\u00A3)")
        plt.grid(True)
        st.pyplot(plt)

    # Handle Cost Projections
    elif sub_module == "Cost Projections":
        st.subheader("Cost Projections")
        st.write("Estimate monthly costs based on fixed costs, variable costs, and expected growth.")

        # Use sliders for interactive inputs
        fixed_costs = st.slider("Monthly Fixed Costs (\u00A3)", min_value=0.0, max_value=100000.0, value=500.0, step=100.0)
        variable_costs = st.slider("Monthly Variable Costs (\u00A3)", min_value=0.0, max_value=100000.0, value=750.0, step=100.0)
        cost_growth_rate = st.slider("Expected Annual Cost Growth Rate (%)", min_value=0, max_value=100, value=10) / 100
        projection_period = st.slider("Projection Period (Months)", min_value=1, max_value=60, value=12, step=1)

        # Dynamic Calculations
        base_monthly_costs = fixed_costs + variable_costs
        monthly_growth_rate = (1 + cost_growth_rate) ** (1 / 12) - 1
        cost_trend = [base_monthly_costs * (1 + monthly_growth_rate) ** i for i in range(projection_period)]

        # Display Results
        st.write(f"Base Monthly Costs (before growth): \u00A3{base_monthly_costs:.2f}")
        st.session_state["calculated_costs"] = cost_trend[-1]  # Save last month's costs in session state
        st.write(f"Total Monthly Costs (after growth): \u00A3{cost_trend[-1]:.2f}")


        # Visualization
        st.write("### Cost Projection Trend")
        months = list(range(1, projection_period + 1))
        plt.figure(figsize=(10, 5))
        plt.plot(months, cost_trend, marker='o', linestyle='-', color='r')
        plt.title("Projected Costs Over Time")
        plt.xlabel("Months")
        plt.ylabel("Costs (\u00A3)")
        plt.grid(True)
        st.pyplot(plt)

    # Handle Scenario Comparison
    elif sub_module == "Scenario Comparison":
        st.subheader("Scenario Comparison")
        st.write("Compare two scenarios side by side.")

        # Inputs for Scenario 1
        st.write("### Scenario 1")
        clients_1 = st.number_input("Number of Clients (Scenario 1)", min_value=1, max_value=1000, value=10, step=1)
        package_price_1 = st.number_input("Package Price (\u00A3) (Scenario 1)", min_value=100.0, max_value=100000.0, value=1500.0, step=100.0)
        growth_rate_1 = st.slider("Annual Growth Rate (%) (Scenario 1)", min_value=0, max_value=100, value=10) / 100

        # Inputs for Scenario 2
        st.write("### Scenario 2")
        clients_2 = st.number_input("Number of Clients (Scenario 2)", min_value=1, max_value=1000, value=10, step=1)
        package_price_2 = st.number_input("Package Price (\u00A3) (Scenario 2)", min_value=100.0, max_value=100000.0, value=1500.0, step=100.0)
        growth_rate_2 = st.slider("Annual Growth Rate (%) (Scenario 2)", min_value=0, max_value=100, value=10) / 100

        # Dynamic Calculations
        revenue_1 = clients_1 * package_price_1 * (1 + growth_rate_1)
        revenue_2 = clients_2 * package_price_2 * (1 + growth_rate_2)

        # Display Results
        col1, col2 = st.columns(2)
        with col1:
            st.write("### Scenario 1 Results")
            st.write(f"- **Projected Revenue:** \u00A3{revenue_1:.2f}")
        with col2:
            st.write("### Scenario 2 Results")
            st.write(f"- **Projected Revenue:** \u00A3{revenue_2:.2f}")

        # Visualization
        st.write("### Comparison Chart")
        scenarios = ["Scenario 1", "Scenario 2"]
        revenues = [revenue_1, revenue_2]
        plt.figure(figsize=(6, 4))
        plt.bar(scenarios, revenues, color=['blue', 'orange'])
        plt.title("Revenue Comparison")
        plt.ylabel("Revenue (\u00A3)")
        st.pyplot(plt)
    
    elif sub_module == "Cash Flow Analysis":
        st.subheader("Cash Flow Analysis")
        st.write("Analyze net cash flow and closing balances based on profit projections and starting balance.")

        # Input for opening balance
        opening_balance = st.slider(
            "Opening Balance (\u00A3)", 
            min_value=0.0, 
            max_value=100000.0, 
            value=1000.0, 
            step=100.0,
            help="Enter the available cash balance at the start of the period."
        )

        # Fetch Net Profit from session state
        net_profit = st.session_state.get("calculated_revenue", 0) - st.session_state.get("calculated_costs", 0) - st.session_state.get("additional_expenses", 0)

        # Dynamic calculations
        closing_balance = opening_balance + net_profit

        # Display Results
        st.write("### Cash Flow Breakdown")
        st.write(f"- **Opening Balance:** \u00A3{opening_balance:.2f}")
        st.write(f"- **Net Profit Impact:** \u00A3{net_profit:.2f}")
        st.write(f"- **Closing Balance:** \u00A3{closing_balance:.2f}")

        # Visualization
        st.write("### Cash Flow Visualization")
        labels = ['Opening Balance', 'Net Profit Impact', 'Closing Balance']
        values = [opening_balance, net_profit, closing_balance]
        plt.figure(figsize=(6, 4))
        plt.bar(labels, values, color=['blue', 'green', 'orange'])
        plt.title("Cash Flow Analysis")
        plt.ylabel("Amount (\u00A3)")
        st.pyplot(plt)


    elif sub_module == "Profit & Loss Projections":
        st.subheader("Profit & Loss Projections")
        st.write("Forecast your profit and loss based on revenue, costs, and additional expenses.")

        # Inputs
        # Automatically fetch revenue and costs from session state
        monthly_revenue = st.session_state.get("calculated_revenue", 0.0)  # Default to 0.0 if not yet calculated
        monthly_costs = st.session_state.get("calculated_costs", 0.0)  # Default to 0.0 if not yet calculated

        st.write(f"Using calculated values: Revenue = \u00A3{monthly_revenue:.2f}, Costs = \u00A3{monthly_costs:.2f}")

        # Additional Expenses
        additional_expenses = st.slider("Additional Expenses (\u00A3)", min_value=0.0, max_value=50000.0, value=500.0, step=50.0)


        # Dynamic Calculations
        gross_profit = monthly_revenue - monthly_costs
        net_profit = gross_profit - additional_expenses

        # Display Results
        st.write("### Profit & Loss Breakdown")
        st.write(f"- **Monthly Revenue:** \u00A3{monthly_revenue:.2f}")
        st.write(f"- **Monthly Costs:** \u00A3{monthly_costs:.2f}")
        st.write(f"- **Gross Profit:** \u00A3{gross_profit:.2f}")
        st.write(f"- **Additional Expenses:** \u00A3{additional_expenses:.2f}")
        st.write(f"- **Net Profit:** \u00A3{net_profit:.2f}")

        # Visualization
                # Visualization
        st.write("### Profit Breakdown")
        if net_profit < 0:
            st.warning("Net Profit is negative! Pie charts cannot display negative values. Showing a bar chart instead.")
            
            # Bar chart for negative net profit
            labels = ['Gross Profit', 'Additional Expenses']
            values = [gross_profit, additional_expenses]
            plt.figure(figsize=(6, 4))
            plt.bar(labels, values, color=['blue', 'orange'])
            plt.title("Profit Breakdown")
            plt.ylabel("Amount (\u00A3)")
            st.pyplot(plt)

        else:
            # Pie chart for non-negative net profit
            labels = ['Gross Profit', 'Additional Expenses', 'Net Profit']
            values = [gross_profit, additional_expenses, net_profit]
            colors = ['blue', 'orange', 'green']

            plt.figure(figsize=(6, 6))
            plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
            plt.title("Profit Breakdown")
            st.pyplot(plt)


