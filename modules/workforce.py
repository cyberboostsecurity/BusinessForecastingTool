import streamlit as st

def workforce_projections():
    st.header("Workforce and Culture Projections")
    st.info("Analyze staffing costs, productivity metrics, and employee affordability.")

    sub_module = st.selectbox("Select a Sub-Module", [
        "Staffing Costs", "Productivity Management", "Employee Affordability"
    ])

    # Staffing Costs
    if sub_module == "Staffing Costs":
        st.subheader("Staffing Costs")
        st.write("Forecast staffing costs based on salaries, benefits, taxes, and additional expenses.")

        # Inputs for multiple roles
        number_of_roles = st.number_input(
            "Number of Roles", min_value=1, step=1, value=1, 
            help="Enter the number of distinct employee roles."
        )

        role_data = []
        for i in range(int(number_of_roles)):
            st.write(f"### Role {i + 1}")
            role_count = st.number_input(f"Number of Employees for Role {i + 1}", min_value=0, step=1, value=0)
            average_salary = st.number_input(f"Average Salary per Employee (\u00A3) for Role {i + 1}", min_value=0.0, step=1000.0, value=30000.0)
            average_benefits = st.number_input(f"Average Benefits per Employee (\u00A3) for Role {i + 1}", min_value=0.0, step=500.0, value=5000.0)
            role_data.append((role_count, average_salary, average_benefits))

        # Additional costs
        recruitment_costs = st.number_input("Recruitment Costs (\u00A3)", min_value=0.0, step=500.0, value=1000.0)
        training_costs = st.number_input("Training Costs (\u00A3)", min_value=0.0, step=500.0, value=2000.0)
        overhead_allocation = st.slider("Operational Overhead Allocation (%)", min_value=0, max_value=50, value=10) / 100
        tax_rate = st.slider("Salary Tax Rate (%)", min_value=0, max_value=50, value=15) / 100

        # Calculate costs
        if st.button("Calculate Staffing Costs"):
            total_salary = sum(role[0] * role[1] for role in role_data)
            total_benefits = sum(role[0] * role[2] for role in role_data)
            salary_taxes = total_salary * tax_rate
            total_staffing_costs = total_salary + total_benefits
            overhead_costs = total_staffing_costs * overhead_allocation
            grand_total_costs = total_staffing_costs + recruitment_costs + training_costs + salary_taxes + overhead_costs

            # Display results
            st.write("### Staffing Cost Breakdown")
            st.write(f"- **Total Salary Costs:** \u00A3{total_salary:.2f}")
            st.write(f"- **Total Benefits Costs:** \u00A3{total_benefits:.2f}")
            st.write(f"- **Salary Taxes ({int(tax_rate * 100)}%):** \u00A3{salary_taxes:.2f}")
            st.write(f"- **Recruitment Costs:** \u00A3{recruitment_costs:.2f}")
            st.write(f"- **Training Costs:** \u00A3{training_costs:.2f}")
            st.write(f"- **Overhead Costs (Allocated):** \u00A3{overhead_costs:.2f}")
            st.write(f"- **Grand Total Staffing Costs:** \u00A3{grand_total_costs:.2f}")

            # Visualization
            st.write("### Cost Breakdown")
            import matplotlib.pyplot as plt

            labels = ['Salaries', 'Benefits', 'Taxes', 'Recruitment', 'Training', 'Overhead']
            values = [total_salary, total_benefits, salary_taxes, recruitment_costs, training_costs, overhead_costs]
            plt.figure(figsize=(6, 6))
            plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.title("Staffing Cost Breakdown")
            st.pyplot(plt)



    # Productivity Management
    elif sub_module == "Productivity Management":
        st.subheader("Productivity Management")
        st.write("Analyze workforce productivity and utilization rates.")

        hours_worked_per_employee = st.number_input(
            "Average Hours Worked per Employee (Monthly)", min_value=0.0, step=1.0,
            help="Enter the average hours worked by each employee in a month."
        )
        total_hours_available = st.number_input(
            "Total Hours Available (Monthly)", min_value=0.0, step=1.0,
            help="Enter the total available hours across all employees in a month."
        )
        revenue_generated = st.number_input(
            "Monthly Revenue (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the total monthly revenue generated."
        )

        if st.button("Calculate Productivity"):
            if total_hours_available > 0:
                productivity_rate = (hours_worked_per_employee / total_hours_available) * 100
                revenue_per_hour = revenue_generated / total_hours_available

                st.write("### Productivity Metrics")
                st.write(f"- **Productivity Rate:** {productivity_rate:.2f}%")
                st.write(f"- **Revenue per Hour:** \u00A3{revenue_per_hour:.2f}")
            else:
                st.warning("Total hours available must be greater than zero.")

    # Employee Affordability
    elif sub_module == "Employee Affordability":
        st.subheader("Employee Affordability Calculator")
        st.write("Estimate the revenue increase and time required to afford a new employee.")

        salary = st.number_input("Annual Salary of Employee (\u00A3)", min_value=0.0, step=1000.0)
        overhead = st.number_input("Overhead Costs (\u00A3)", min_value=0.0, step=500.0)
        production_rate = st.slider("Production Rate (% Billable Time)", min_value=0, max_value=100, value=65) / 100
        current_revenue = st.number_input("Current Monthly Revenue (\u00A3)", min_value=0.0, step=100.0)
        growth_rate = st.slider("Expected Monthly Revenue Growth Rate (%)", min_value=0, max_value=50, value=10) / 100
        safety_buffer = st.slider("Safety Buffer (% Extra Revenue)", min_value=0, max_value=50, value=10) / 100

        if st.button("Calculate Affordability"):
            # Step 1: Calculate monthly cost of the employee
            monthly_cost = (salary + overhead) / 12

            # Step 2: Calculate required revenue increase with safety buffer
            required_monthly_revenue = (monthly_cost / production_rate) * (1 + safety_buffer)

            # Step 3: Calculate time to achieve target
            if growth_rate > 0:
                monthly_growth = current_revenue * growth_rate
                time_to_target = required_monthly_revenue / monthly_growth
            else:
                time_to_target = float('inf')  # Infinite if no growth rate

            # Display results
            st.write("### Results")
            st.write(f"- **Monthly Employee Cost (Salary + Overhead):** \u00A3{monthly_cost:.2f}")
            st.write(f"- **Required Monthly Revenue (with {int(safety_buffer * 100)}% Buffer):** \u00A3{required_monthly_revenue:.2f}")
            st.write(f"- **Estimated Time to Achieve Target Revenue:** {time_to_target:.2f} months")

            if time_to_target == float('inf'):
                st.warning("A growth rate of 0% means the target will never be reached.")
