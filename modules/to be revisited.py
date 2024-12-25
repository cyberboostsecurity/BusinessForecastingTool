import streamlit as st
import pandas as pd

# Enhanced Resource Allocation Module
def resource_allocation():
    st.header("Enhanced Resource Allocation")
    st.info("Plan and allocate resources dynamically with cost analysis and seasonal adjustments.")

    # Step 1: Input Resource Categories
    st.write("### Step 1: Define Resource Categories")
    categories = st.text_area(
        "Enter Resource Categories (one per line)", 
        placeholder="E.g., Sales Team, Manufacturing Equipment, IT Tools..."
    ).splitlines()

    # Step 2: Input Allocation Data
    if categories:
        st.write("### Step 2: Input Allocation Details")
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
            allocation_data.append({
                "Category": category,
                "Resource Count": resource_count,
                "Cost per Unit (\u00A3)": cost_per_unit,
                "Adjusted Count": adjusted_count,
                "Total Cost (\u00A3)": adjusted_count * cost_per_unit
            })

        # Convert allocation data to a DataFrame
        df = pd.DataFrame(allocation_data)

        # Save data in session state
        st.session_state["resource_allocation_data"] = df

        # Step 3: Display Allocation Summary
        st.write("### Step 3: Allocation Summary")
        st.dataframe(df)

        # Display Total Cost
        total_cost = df["Total Cost (\u00A3)"].sum()
        st.write(f"**Total Allocation Cost:** \u00A3{total_cost:.2f}")

        # Step 4: Optimal Utilization Suggestions
        st.write("### Step 4: Optimization Suggestions")
        for index, row in df.iterrows():
            if row["Adjusted Count"] > row["Resource Count"]:
                st.warning(f"Increase allocation for {row['Category']} due to high demand (+{int(row['Adjusted Count'] - row['Resource Count'])} units).")
            elif row["Adjusted Count"] < row["Resource Count"]:
                st.info(f"Reduce allocation for {row['Category']} to avoid overallocation (-{int(row['Resource Count'] - row['Adjusted Count'])} units).")

    # View saved data
    if "resource_allocation_data" in st.session_state:
        if st.button("View Saved Data"):
            st.write("### Previously Entered Allocation Data")
            st.dataframe(st.session_state["resource_allocation_data"])

    # Clear data
    if st.button("Clear Data"):
        if "resource_allocation_data" in st.session_state:
            del st.session_state["resource_allocation_data"]
        st.success("All allocation data cleared.")
