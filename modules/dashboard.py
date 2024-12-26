import streamlit as st
import plotly.express as px  # For advanced visualizations

# Dashboard module
def dashboard():
    st.header("Dashboard")
    st.info("Visualize and manage metrics from all modules.")

    # Example Summary Statistics
    st.write("### Summary Statistics")
    summary_data = {
        "Financial Forecasting": {"Revenue Projection": "£50,000", "Profit Margin": "25%"},
        "Operational Planning": {"Resource Utilization": "80%", "Efficiency Rating": "4.5/5"},
        "Risk Assessment": {"Highest Risk": "Market Misalignment", "Risk Score": "1.2"},
        "Growth & Scaling": {"ROI": "30%", "Viability Index": "4.8"},
        "Workforce": {"Total Staffing Costs": "£20,000", "Employee Affordability": "Achieved"},
    }
    for module, metrics in summary_data.items():
        st.subheader(module)
        for metric, value in metrics.items():
            st.write(f"- **{metric}:** {value}")

    # Example Visualizations
    st.write("### Visualizations")

    # Example: Financial Forecasting Metrics
    st.subheader("Financial Forecasting Metrics")
    financial_data = {"Month": ["Jan", "Feb", "Mar"], "Revenue": [10000, 15000, 20000]}
    fig = px.line(financial_data, x="Month", y="Revenue", title="Monthly Revenue Projection")
    st.plotly_chart(fig)

    # Example: Operational Planning Metrics
    st.subheader("Operational Planning Metrics")
    operational_data = {"Resource": ["Sales", "IT", "Marketing"], "Utilization (%)": [85, 90, 75]}
    fig = px.bar(operational_data, x="Resource", y="Utilization (%)", title="Resource Utilization")
    st.plotly_chart(fig)

    # Example: Risk Assessment Heatmap
    st.subheader("Risk Assessment Heatmap")
    risks = ["Risk A", "Risk B", "Risk C"]
    likelihood = [30, 60, 80]
    impact = [2, 4, 3]
    fig = px.scatter(
        x=likelihood, y=impact, text=risks,
        size=[i * j for i, j in zip(likelihood, impact)],
        title="Risk Heatmap",
        labels={"x": "Likelihood (%)", "y": "Impact"}
    )
    st.plotly_chart(fig)

    # Recommendations Section
    st.write("### Recommendations")
    st.success("Focus on increasing marketing efforts in March to maximize ROI.")
    st.warning("Resource utilization in Marketing is below 80%. Consider reallocation.")
    st.error("Risk Assessment indicates a critical issue with 'Risk C'. Mitigate immediately.")

    # Save Results Option
    st.write("### Save Results")
    if st.button("Export Dashboard Data"):
        # Placeholder for export functionality
        st.info("Dashboard data exported successfully.")
