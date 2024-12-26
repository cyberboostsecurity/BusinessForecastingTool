import streamlit as st

def help_page():
    st.title("Application Help Guide")
    st.info("Learn how to use the Business Forecasting Tool and understand its features.")

    # Section: Overview
    st.header("Overview")
    st.write("""
    The Business Forecasting Tool helps you analyze and plan various aspects of your business, including growth, financials, risks, and workforce strategies.
    Use the sidebar to navigate through the modules and access the functionalities.
    """)

    # Section: Modules
    st.header("Modules")

    st.subheader("1. Financial Forecasting")
    st.write("""
    **Purpose**: Predict revenue, costs, and profits.

    **Features**:
    - Revenue Projections: Forecast income.
    - Profit & Loss: Assess profitability.
    - Cash Flow Analysis: Check liquidity.

    **Formulas**:
    - Net Profit = Revenue - (Fixed Costs + Variable Costs)
    - Cash Flow = Opening Balance + Revenue - Costs

    **Example**:
    - Input: Revenue = \u00A350,000, Fixed Costs = \u00A310,000.
    - Output: Net Profit = \u00A340,000.
    """)

    st.subheader("2. Operational Planning")
    st.write("""
    **Purpose**: Optimize resource usage.

    **Features**:
    - Resource Allocation: Distribute resources efficiently.
    - Business Efficiency Metrics: Measure productivity.
    - Technology Recommendations: Suggest cost-saving tools.

    **Formulas**:
    - Productivity Rate = (Output / Total Input) × 100
    - Efficiency Metric = Sales per Employee

    **Example**:
    - Input: Employees = 10, Sales = 500.
    - Output: Productivity Rate = 50 units per employee.
    """)

    st.subheader("3. Risk Assessment")
    st.write("""
    **Purpose**: Identify and evaluate risks.

    **Features**:
    - Define and analyze risks.
    - Visualize risks with heatmaps.
    - Prioritize risks for mitigation.

    **Formulas**:
    - Risk Score = Likelihood (%) × Impact (1-5)

    **Example**:
    - Input: Risk = "Market Misalignment", Likelihood = 50%, Impact = 3.
    - Output: Risk Score = 1.5.
    """)

    st.subheader("4. Growth & Scaling Strategy")
    st.write("""
    **Purpose**: Evaluate growth opportunities and strategies.

    **Features**:
    - Market Expansion: Analyze ROI and payback periods.
    - Customer Metrics: Calculate CLV and CAC.
    - Partnerships: Assess dependency and ROI.

    **Formulas**:
    - ROI = (Revenue - Costs) / Costs × 100
    - CLV-to-CAC Ratio = CLV / CAC

    **Example**:
    - Input: Market Costs = \u00A350,000, Revenue = \u00A3100,000.
    - Output: ROI = 100%.
    """)

    st.subheader("5. Workforce Planning")
    st.write("""
    **Purpose**: Assess staffing needs and costs.

    **Features**:
    - Calculate employee affordability.
    - Measure workforce productivity.

    **Formulas**:
    - Monthly Cost = (Salary + Overheads) / 12
    - Revenue Increase Needed = Monthly Cost / Productivity Rate

    **Example**:
    - Input: Salary = \u00A330,000, Overheads = \u00A35,000, Productivity = 70%.
    - Output: Revenue Needed = \u00A33,750/month.
    """)

    # FAQs Section
    st.header("FAQs")
    st.write("""
    **Q: Can I save my data?**
    - Yes, modules provide options to save data in JSON or CSV formats.

    **Q: What if I don't understand a metric?**
    - Refer to the formulas and examples for clarification.

    **Q: Can I compare scenarios across modules?**
    - Inter-module comparisons are planned for future updates.
    """)

    # Tips Section
    st.header("Tips")
    st.write("""
    - Regularly update inputs to keep projections accurate.
    - Use scenario planning to test different strategies.
    """)

if __name__ == "__main__":
    help_page()
