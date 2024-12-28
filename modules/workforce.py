import streamlit as st
import numpy as np
import plotly.express as px
from modules.db_utils import save_to_database, load_from_database

def workforce_projections():
    st.header("Workforce and Culture Projections with Monte Carlo")
    st.info("Analyze staffing costs, productivity metrics, and employee affordability.")

    sub_module = st.selectbox("Select a Sub-Module", [
        "Staffing Costs", "Employee Affordability"
    ])

    # Submodule: Staffing Costs
    if sub_module == "Staffing Costs":
        st.subheader("Staffing Costs with Monte Carlo")
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
            average_salary = st.number_input(f"Average Salary per Employee (£) for Role {i + 1}", min_value=0.0, step=1000.0, value=30000.0)
            salary_variability = st.slider(f"Salary Variability (%) for Role {i + 1}", min_value=0, max_value=50, value=10) / 100
            average_benefits = st.number_input(f"Average Benefits per Employee (£) for Role {i + 1}", min_value=0.0, step=500.0, value=5000.0)
            benefits_variability = st.slider(f"Benefits Variability (%) for Role {i + 1}", min_value=0, max_value=50, value=10) / 100
            role_data.append((role_count, average_salary, salary_variability, average_benefits, benefits_variability))

        # Additional costs
        recruitment_costs = st.number_input("Recruitment Costs (£)", min_value=0.0, step=500.0, value=1000.0)
        training_costs = st.number_input("Training Costs (£)", min_value=0.0, step=500.0, value=2000.0)
        overhead_allocation = st.slider("Operational Overhead Allocation (%)", min_value=0, max_value=50, value=10) / 100
        tax_rate = st.slider("Salary Tax Rate (%)", min_value=0, max_value=50, value=15) / 100

        # Monte Carlo Simulations for Costs
        simulations = 1000
        simulated_costs = []

        for _ in range(simulations):
            total_salary = sum(
                role[0] * np.random.normal(loc=role[1], scale=role[1] * role[2]) for role in role_data
            )
            total_benefits = sum(
                role[0] * np.random.normal(loc=role[3], scale=role[3] * role[4]) for role in role_data
            )
            salary_taxes = total_salary * tax_rate
            total_staffing_costs = total_salary + total_benefits
            overhead_costs = total_staffing_costs * overhead_allocation
            grand_total_costs = total_staffing_costs + recruitment_costs + training_costs + salary_taxes + overhead_costs
            simulated_costs.append(grand_total_costs)

        # Results
        mean_costs = np.mean(simulated_costs)
        p5_costs = np.percentile(simulated_costs, 5)
        p95_costs = np.percentile(simulated_costs, 95)

        st.write("### Monte Carlo Results")
        st.write(f"- **Mean Total Staffing Costs:** £{mean_costs:.2f}")
        st.write(f"- **Staffing Costs Range (5th to 95th Percentile):** £{p5_costs:.2f} to £{p95_costs:.2f}")

        # Visualization
        st.write("### Cost Distribution")
        fig_costs = px.histogram(
            simulated_costs,
            nbins=50,
            title="Total Staffing Costs Distribution",
            labels={"x": "Total Staffing Costs (£)", "y": "Frequency"}
        )
        st.plotly_chart(fig_costs)

        if st.button("Export Staffing Costs to SQL"):
            save_to_database("staffing_costs", {
                "mean_costs": mean_costs,
                "p5_costs": p5_costs,
                "p95_costs": p95_costs
            })
            st.success("Staffing costs data exported successfully!")

    # Submodule: Employee Affordability
    elif sub_module == "Employee Affordability":
        st.subheader("Employee Affordability with Monte Carlo")
        st.write("Estimate the time required to afford a new employee based on revenue growth.")

        # Inputs
        salary = st.number_input("Annual Salary of Employee (£)", min_value=0.0, step=1000.0)
        overhead = st.number_input("Overhead Costs (£)", min_value=0.0, step=500.0)
        production_rate = st.slider("Production Rate (% Billable Time)", min_value=0, max_value=100, value=65) / 100
        initial_revenue = st.slider(
            "Current Monthly Revenue (£)", min_value=0.0, max_value=100000.0, step=500.0, value=10000.0,
            help="Set your current monthly revenue."
        )
        growth_rate = st.slider("Expected Monthly Revenue Growth Rate (%)", min_value=0, max_value=50, value=10) / 100
        revenue_variability = st.slider(
            "Revenue Growth Variability (%)", min_value=0, max_value=50, value=10,
            help="Expected variability in monthly revenue growth."
        )
        max_simulation_months = st.number_input(
            "Max Simulation Duration (Months)", min_value=12, max_value=120, value=36,
            help="Maximum number of months to simulate for affordability."
        )

        # Monte Carlo Simulations
        simulations = 1000
        total_employee_cost = (salary + overhead) / 12

        time_to_afford = []
        for _ in range(simulations):
            current_revenue = initial_revenue
            time = 0
            affordable = False

            while time <= max_simulation_months:
                # Simulate revenue growth with variability
                growth = np.random.normal(loc=growth_rate, scale=growth_rate * (revenue_variability / 100))
                current_revenue *= (1 + growth)
                time += 1

                # Check if revenue reaches affordability threshold
                if current_revenue * production_rate >= total_employee_cost:
                    time_to_afford.append(time)
                    affordable = True
                    break

            if not affordable:
                time_to_afford.append(float('inf'))

        # Filter results
        finite_times = [t for t in time_to_afford if t != float('inf')]
        mean_time = np.mean(finite_times)
        p5_time = np.percentile(finite_times, 5)
        p95_time = np.percentile(finite_times, 95)

        # Results
        st.write("### Monte Carlo Results")
        if finite_times:
            st.write(f"- **Mean Time to Affordability:** {mean_time:.2f} months")
            st.write(f"- **Time Range (5th to 95th Percentile):** {p5_time:.2f} to {p95_time:.2f} months")
        else:
            st.warning("Affordability is not achievable within the simulation duration. Consider adjusting inputs.")

        # Visualization
        st.write("### Time to Afford Distribution")
        if finite_times:
            fig = px.histogram(
                finite_times,
                nbins=50,
                title="Time to Afford Employee Distribution",
                labels={"x": "Time to Afford (Months)", "y": "Frequency"}
            )
            st.plotly_chart(fig)
        else:
            st.write("No affordability achieved in the given time frame.")

        if st.button("Export Employee Affordability to SQL"):
            save_to_database("employee_affordability", {
                "mean_time": mean_time,
                "p5_time": p5_time,
                "p95_time": p95_time
            })
            st.success("Employee affordability data exported successfully!")
