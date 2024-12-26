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
    **Purpose**: Predict revenue, costs, and profits based on historical and projected data.

    **Features**:
    - Revenue Projections: Forecast income based on growth rate and client numbers.
    - Profit & Loss: Assess profitability by factoring in fixed and variable costs.
    - Cash Flow Analysis: Analyze liquidity based on revenue, costs, and opening balance.
    - Scenario Comparison: Compare different business scenarios side by side.

    **Formulas**:
    - **Net Profit** = Revenue - (Fixed Costs + Variable Costs)
    - **Cash Flow** = Opening Balance + Revenue - Costs
    - **ROI** = (Revenue - Costs) / Costs × 100

    **Example**:
    - Input: Revenue = £50,000, Fixed Costs = £10,000, Variable Costs = £5,000.
    - Output: **Net Profit** = £35,000.

    **Explanation of Formulas**:
    - **Net Profit**: Subtract total costs (fixed and variable) from revenue to get the net profit.
    - **Cash Flow**: Cash flow is calculated by adding the revenue to the opening balance and subtracting the total costs.
    - **ROI**: Measures return on investment by calculating the percentage return relative to the initial costs.
    """)

    st.subheader("2. Operational Planning")
    st.write("""
    **Purpose**: Optimize resource usage and improve efficiency.

    **Features**:
    - Resource Allocation: Distribute resources efficiently across business operations.
    - Business Efficiency Metrics: Measure productivity and identify bottlenecks.
    - Technology Recommendations: Suggest cost-saving tools and technologies.

    **Formulas**:
    - **Productivity Rate** = (Output / Total Input) × 100
    - **Efficiency Metric** = Sales per Employee

    **Example**:
    - Input: Employees = 10, Sales = 500.
    - Output: **Productivity Rate** = 50 units per employee.

    **Explanation of Formulas**:
    - **Productivity Rate**: This formula measures how efficiently input resources (e.g., labor) are turned into output (e.g., products sold or services rendered).
    - **Efficiency Metric**: This formula measures sales performance per employee, helping businesses assess employee efficiency.
    """)

    st.subheader("3. Risk Assessment")
    st.write("""
    **Purpose**: Identify and evaluate risks, adjusting business plans accordingly.

    **Features**:
    - Define and analyze risks based on their likelihood and impact.
    - Visualize risks with charts and heatmaps.
    - Prioritize risks for mitigation based on their scores.

    **Formulas**:
    - **Risk Score** = Likelihood (%) × Adjusted Impact (1-5)
    - **Risk Factor**: Adjusts growth projections based on risk levels.

    **Example**:
    - Input: Risk = "Market Misalignment", Likelihood = 50%, Impact = 3.
    - Output: **Risk Score** = 1.5, **Risk Factor** impacts growth rate.

    **Explanation of Formulas**:
    - **Risk Score**: The **Risk Score** is calculated by multiplying the likelihood (probability of the risk occurring) by the impact (the severity of the consequences). The formula helps prioritize risks by their severity.
    - **Risk Factor**: The **Risk Factor** is calculated from the average **Risk Score** across selected risks, which then adjusts the **growth rate** in financial forecasting to reflect the influence of risks on the business.
    """)

    st.subheader("4. Growth & Scaling Strategy")
    st.write("""
    **Purpose**: Evaluate growth opportunities and strategies for scaling the business.

    **Features**:
    - Market Expansion: Analyze ROI and the payback period for market entry.
    - Customer Metrics: Calculate Customer Lifetime Value (CLV) and Customer Acquisition Cost (CAC).
    - Partnerships: Assess the dependency and ROI for partnerships.

    **Formulas**:
    - **ROI** = (Revenue - Costs) / Costs × 100
    - **CLV-to-CAC Ratio** = CLV / CAC

    **Example**:
    - Input: Market Costs = £50,000, Revenue = £100,000.
    - Output: **ROI** = 100%.

    **Explanation of Formulas**:
    - **ROI (Return on Investment)**: This formula calculates the return you get for every pound spent on a particular investment (in this case, market expansion costs).
    - **CLV-to-CAC Ratio**: The **CLV-to-CAC Ratio** helps determine how much value you’re generating for each pound spent on acquiring customers. A ratio greater than 1 suggests that customer acquisition is generating positive returns.
    """)

    st.subheader("5. Workforce Planning")
    st.write("""
    **Purpose**: Assess staffing needs, measure productivity, and calculate workforce costs.

    **Features**:
    - Calculate employee affordability based on salary and overheads.
    - Measure workforce productivity across different departments.

    **Formulas**:
    - **Monthly Cost** = (Salary + Overheads) / 12
    - **Revenue Increase Needed** = Monthly Cost / Productivity Rate

    **Example**:
    - Input: Salary = £30,000, Overheads = £5,000, Productivity = 70%.
    - Output: **Revenue Needed** = £3,750/month.

    **Explanation of Formulas**:
    - **Monthly Cost**: This formula calculates the total monthly cost of an employee by adding salary and overheads and dividing by 12.
    - **Revenue Increase Needed**: This formula determines the amount of additional revenue needed to cover an employee's monthly costs based on their productivity.
    """)

    # Section: FAQs
    st.header("FAQs")
    st.write("""
    **Q: Can I save my data?**
    - Yes, you can save your data from each module to a database, and it will be shared across the app for seamless analysis.

    **Q: What if I don't understand a metric?**
    - Refer to the formulas and examples provided in each module for clarification.

    **Q: Can I compare scenarios across modules?**
    - Yes, the tool allows for scenario testing and comparison across multiple modules for a more comprehensive analysis.
    """)

    # Section: Tips
    st.header("Tips")
    st.write("""
    - Regularly update inputs to keep projections accurate.
    - Use scenario planning to test different strategies and mitigate risks.
    - Leverage the Risk Factor to adjust growth projections based on real-time data.
    """)

    # Section: New Features
    st.header("New Features")
    st.write("""
    - **Risk Factor Adjustment**: The Risk Factor now influences the growth rate in the Financial Forecasting module, providing more accurate projections under varying risk conditions.
    - **Scenario Comparison**: You can now compare two different business scenarios side by side, assessing their revenue, costs, and profitability.
    - **Database Integration**: Data is now exported and shared across all modules, ensuring consistency and reducing redundant calculations.
    """)

if __name__ == "__main__":
    help_page()
