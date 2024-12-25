import streamlit as st

# Help Page Implementation
def help_page():
    st.title("Application Help Guide")
    st.info("Learn how to use the Business Forecasting Tool and its modules.")

    # Section: Overview
    st.header("Overview")
    st.write("""
    The Business Forecasting Tool provides comprehensive modules to help businesses plan and analyze 
    various aspects of growth, scaling, financial forecasting, and operational efficiency.
    
    Navigate through the application using the sidebar to explore each module.
    """)

    # Section: Module Descriptions
    st.header("Modules")

    st.subheader("1. Financial Forecasting")
    st.write("""
    **Purpose**: Predict revenue, costs, and profits for future planning.

    **How to Use**:
    - Input historical data and expected growth rates.
    - Provide cost estimates.
    - View cash flow and profit projections.

    **Key Metrics**:
    - Revenue Projections: Future income based on inputs.
    - Profit & Loss: Net income/loss calculated from revenue and expenses.
    - Cash Flow: Available liquidity over time.

    **Example**:
    - Input: Revenue growth rate = 10%, Fixed costs = \u00A310,000.
    - Output: Monthly revenue, profit, and cash flow forecasts.
    """)

    st.subheader("2. Operational Planning")
    st.write("""
    **Purpose**: Optimize resource allocation, efficiency, and technology use.

    **How to Use**:
    - Enter expected sales and available resources.
    - Use submodules for business efficiency metrics and tech recommendations.

    **Key Metrics**:
    - Resource Allocation: Analyze resource usage and identify gaps.
    - Efficiency Metrics: Productivity per employee or resource.
    - Tech Upgrades: Suggestions for improving operational efficiency.

    **Example**:
    - Input: Employees = 10, Sales per employee = 50.
    - Output: Total sales and resource utilization recommendations.
    """)

    st.subheader("3. Risk Assessment")
    st.write("""
    **Purpose**: Evaluate and prioritize risks based on their likelihood and impact.

    **How to Use**:
    - Define risks (predefined or custom).
    - Input likelihood and impact values.
    - Analyze risk scores and visualize with heatmaps.

    **Key Metrics**:
    - Risk Score: Combines likelihood and impact.
    - Heatmap: Visual representation of risks.

    **Example**:
    - Input: Risk = "Market Misalignment", Likelihood = 40%, Impact = 3.
    - Output: Risk Score = 1.2.
    """)

    st.subheader("4. Growth & Scaling Strategy")
    st.write("""
    **Purpose**: Analyze growth opportunities and scaling strategies.

    **How to Use**:
    - Explore submodules: Market Expansion, Customer Metrics, Partnerships, etc.
    - Provide relevant inputs for each strategy.
    - View advanced metrics like ROI and viability index.

    **Key Metrics**:
    - ROI: Return on investment.
    - Payback Period: Time to recover costs.
    - Market Viability Index: Combines risk and reward metrics.

    **Example**:
    - Input: Market entry costs = \u00A350,000, Revenue = \u00A3100,000.
    - Output: ROI = 100%, Payback Period = 6 months.
    """)

    st.subheader("5. Workforce and Culture Projections")
    st.write("""
    **Purpose**: Analyze staffing costs, productivity, and employee affordability.

    **How to Use**:
    - Input desired salaries, overheads, and expected revenue.
    - Use submodules for productivity management and affordability analysis.

    **Key Metrics**:
    - Staffing Costs: Salaries, taxes, and benefits.
    - Productivity Metrics: Revenue per employee.
    - Affordability Calculator: Revenue required to hire new employees.

    **Example**:
    - Input: Salary = \u00A330,000, Overheads = \u00A35,000, Productivity = 70%.
    - Output: Revenue needed to afford a new employee.
    """)

    # General Tips
    st.header("General Tips")
    st.write("""
    - Save your results after completing each module.
    - Use the scenario planning features to simulate different business conditions.
    - Check the help section in each module for specific guidance.
    """)

    # FAQs
    st.header("FAQs")
    st.write("""
    **Q: Can I save my data?**
    - Yes, each module includes options to save and export your data.

    **Q: What if I don't understand a metric?**
    - Refer to the key metrics section for explanations.

    **Q: Can I compare scenarios across modules?**
    - Currently, scenario comparison is limited to individual modules, but inter-module data sharing is in development.
    """)

# Adding the Help Menu to Navigation
if "Help Menu" not in st.session_state:
    st.session_state["Help Menu"] = help_page
