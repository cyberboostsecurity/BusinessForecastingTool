import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def operational_planning():
    st.header("Operational Planning")
    st.info("Plan your resources, evaluate efficiency, and explore technology recommendations.")

    # Sub-module selection
    sub_module = st.selectbox(
        "Choose a Sub-Module",
        ["Resource Allocation", "Efficiency Metrics", "Technology Recommendations"]
    )

    # Call the appropriate sub-module
    if sub_module == "Resource Allocation":
        resource_allocation()
    elif sub_module == "Efficiency Metrics":
        efficiency_metrics()
    elif sub_module == "Technology Recommendations":
        technology_recommendations()

# Resource Allocation Module
def resource_allocation():
    st.subheader("Resource Allocation")
    st.info("Allocate resources dynamically, analyze costs, and optimize resource usage.")

    categories = st.text_area(
        "Enter Resource Categories (one per line)", 
        placeholder="E.g., Sales Team, Manufacturing Equipment, IT Tools..."
    ).splitlines()

    if categories:
        allocation_data = []
        for category in categories:
            st.write(f"#### {category}")
            resource_count = st.number_input(
                f"Number of Resources for {category}", min_value=0, step=1, key=f"{category}_count"
            )
            cost_per_unit = st.number_input(
                f"Cost per Unit (\u00A3) for {category}", min_value=0.0, step=0.1, key=f"{category}_cost"
            )
            demand_adjustment = st.slider(
                f"Demand Adjustment (%) for {category}", min_value=-50, max_value=50, value=0, key=f"{category}_adjustment"
            )
            adjusted_count = resource_count * (1 + demand_adjustment / 100)
            total_cost = adjusted_count * cost_per_unit
            allocation_data.append({
                "Category": category,
                "Resource Count": resource_count,
                "Cost per Unit (\u00A3)": cost_per_unit,
                "Adjusted Count": adjusted_count,
                "Total Cost (\u00A3)": total_cost
            })

        df = pd.DataFrame(allocation_data)

        # Display Allocation Summary
        st.write("### Allocation Summary")
        st.dataframe(df)

        # Visualization: Total Costs
        st.write("#### Visualization: Total Costs")
        plt.bar(df["Category"], df["Total Cost (\u00A3)"], color='skyblue')
        plt.xlabel("Category")
        plt.ylabel("Total Cost (\u00A3)")
        plt.title("Resource Allocation Costs")
        st.pyplot(plt)

# Efficiency Metrics Module
def efficiency_metrics():
    st.subheader("Efficiency Metrics")
    st.info("Evaluate workforce productivity and resource utilization.")

    employees = st.number_input(
        "Number of Employees", min_value=0, step=1, help="Enter the total number of employees."
    )
    revenue = st.number_input(
        "Monthly Revenue (\u00A3)", min_value=0.0, step=100.0, help="Enter the total monthly revenue."
    )
    hours_worked = st.number_input(
        "Total Hours Worked (Monthly)", min_value=0.0, step=1.0, help="Enter the total number of hours worked."
    )

    if st.button("Calculate Efficiency Metrics"):
        if employees > 0 and hours_worked > 0:
            revenue_per_employee = revenue / employees
            productivity_rate = (hours_worked / (employees * 160)) * 100  # Assuming 160 hours/month per employee

            st.write("### Efficiency Metrics")
            st.write(f"- **Revenue per Employee:** \u00A3{revenue_per_employee:.2f}")
            st.write(f"- **Productivity Rate:** {productivity_rate:.2f}%")
        else:
            st.error("Number of employees and hours worked must be greater than zero.")

# Technology Recommendations Module
def technology_recommendations():
    st.subheader("Technology Recommendations")
    st.info("Get suggestions for technology upgrades or cost-saving measures.")

    current_tools = st.text_area(
        "Current Tools and Technologies",
        placeholder="E.g., Office 365, Slack, QuickBooks..."
    )
    scaling_needs = st.text_area(
        "Scaling Requirements",
        placeholder="E.g., Need more storage, faster processing, better collaboration tools..."
    )

    if st.button("Generate Recommendations"):
        st.write("### Recommendations")
        if "cloud" in current_tools.lower() or "storage" in scaling_needs.lower():
            st.write("- Consider migrating to cloud-based solutions for better scalability.")
        if "manual" in current_tools.lower():
            st.write("- Automate processes using workflow automation tools.")
        st.write("- Conduct a cost-benefit analysis before any major upgrades.")

