import streamlit as st

def workforce_projections():
    st.header("Workforce and Culture Projections")
    st.info("Analyze staffing costs and productivity metrics for better workforce planning.")

    sub_module = st.selectbox("Select a Sub-Module", [
        "Staffing Costs", "Productivity Management"
    ])

    # Staffing Costs
    if sub_module == "Staffing Costs":
        st.subheader("Staffing Costs")
        st.write("Forecast staffing costs based on salaries, benefits, and headcount.")

        headcount = st.number_input(
            "Number of Employees", min_value=0, step=1,
            help="Enter the total number of employees."
        )
        average_salary = st.number_input(
            "Average Salary per Employee (\u00A3)", min_value=0.0, step=1000.0,
            help="Enter the average annual salary per employee."
        )
        average_benefits = st.number_input(
            "Average Benefits per Employee (\u00A3)", min_value=0.0, step=500.0,
            help="Enter the average annual benefits per employee."
        )

        if st.button("Calculate Staffing Costs"):
            total_salary = headcount * average_salary
            total_benefits = headcount * average_benefits
            total_staffing_costs = total_salary + total_benefits

            st.write("### Staffing Cost Breakdown")
            st.write(f"- **Total Salary Costs:** \u00A3{total_salary:.2f}")
            st.write(f"- **Total Benefits Costs:** \u00A3{total_benefits:.2f}")
            st.write(f"- **Total Staffing Costs:** \u00A3{total_staffing_costs:.2f}")

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

