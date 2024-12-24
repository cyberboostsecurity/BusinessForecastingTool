import streamlit as st

def operational_planning():
    st.header("Operational Planning")
    st.info("Plan your resources, evaluate efficiency, and get technology recommendations.")

    sub_module = st.selectbox("Select a Sub-Module", [
        "Resource Allocation", "Business Efficiency Metrics", "Technology & Tools"
    ])

    # Resource Allocation
    if sub_module == "Resource Allocation":
        st.subheader("Resource Allocation")
        st.write("Allocate resources based on expected sales and available capacity.")

        expected_sales = st.number_input(
            "Expected Sales (Units)", min_value=0, step=1, 
            help="Enter the number of expected sales units."
        )
        resources_available = st.number_input(
            "Available Resources", min_value=0, step=1, 
            help="Enter the number of resources (e.g., employees, equipment)."
        )

        if st.button("Calculate Resource Allocation"):
            if resources_available > 0:
                allocation = expected_sales / resources_available
                st.write(f"Each resource needs to handle approximately {allocation:.2f} sales units.")
            else:
                st.warning("Available resources must be greater than zero.")

    # Business Efficiency Metrics
    elif sub_module == "Business Efficiency Metrics":
        st.subheader("Business Efficiency Metrics")
        st.write("Evaluate productivity and efficiency rates.")

        employees = st.number_input(
            "Number of Employees", min_value=0, step=1, 
            help="Enter the total number of employees."
        )
        sales_per_employee = st.number_input(
            "Sales per Employee", min_value=0.0, step=1.0,
            help="Enter the average sales per employee."
        )

        if st.button("Calculate Efficiency"):
            if employees > 0:
                total_sales = employees * sales_per_employee
                st.write(f"Total sales: {total_sales:.2f}")
            else:
                st.warning("Number of employees must be greater than zero.")

    # Technology & Tools
    elif sub_module == "Technology & Tools":
        st.subheader("Technology & Tools")
        st.write("Get recommendations for technology upgrades or cost-saving measures.")

        current_tools = st.text_area(
            "Current Tools Used", 
            help="List the tools and technologies you currently use (e.g., software, hardware)."
        )
        scaling_needs = st.text_area(
            "Scaling Requirements",
            help="Describe your scaling requirements (e.g., need for faster processing, more storage)."
        )

        if st.button("Get Recommendations"):
            st.write("### Recommendations")
            if "cloud" in current_tools.lower() or "storage" in scaling_needs.lower():
                st.write("- Consider migrating to cloud-based solutions for better scalability.")
            if "manual" in current_tools.lower():
                st.write("- Automate processes using workflow automation tools.")
            st.write("- Conduct a cost-benefit analysis before any major upgrades.")

