import streamlit as st

def help_page():
    # Title of the Help Page
    st.title("Application Help Guide")
    st.info("Learn how to use the Business Forecasting Tool and understand its features.")

    # Section 1: Overview of the Tool
    st.header("Overview")
    st.write("""
    The Business Forecasting Tool is a modular system designed to help businesses plan, optimize, and forecast key operations.
    The tool combines advanced analytics with Monte Carlo simulations, ensuring robust decision-making.
    
    The tool consists of multiple modules:
    - **Risk Assessment**: Identify and prioritize risks.
    - **Financial Forecasting**: Forecast revenue, costs, and profits.
    - **Workforce and Culture Planning**: Plan staffing, analyze productivity.
    - **Growth & Scaling Strategy**: Analyze market expansion, customer acquisition, partnerships.
    - **Scenario Comparison**: Compare business scenarios with probabilistic outcomes.
    """)

    # Section 2: How to Use the Tool
    st.header("How to Use the Tool")
    st.write("""
    The tool is divided into modules that guide you through various steps. Here’s a recommended sequence:

    **1. Start with Risk Assessment**:
    - Identify and assess risks.
    - Adjust revenue and cost estimates based on risk data.

    **2. Move to Financial Forecasting**:
    - Use the adjusted metrics to predict revenue, costs, and profitability.
    - Monte Carlo simulations provide insight into the range of possible outcomes.

    **3. Workforce Planning**:
    - Plan staffing needs based on financial projections.
    - Analyze employee affordability, assessing the time to hire new staff based on predicted growth.

    **4. Explore Growth & Scaling Strategy**:
    - Analyze potential market entry, customer acquisition, and partnerships.
    - Use Monte Carlo simulations to evaluate scaling efficiency.

    **5. Compare Scenarios**:
    - Use Scenario Comparison to assess different business strategies under various conditions.
    - Evaluate the best approach using risk-adjusted ROI and breakeven analysis.

    **6. View Results in the Dashboard**:
    - All your data is integrated into the dashboard for easy access and decision-making.
    """)

    # Section 3: Detailed Explanation of Modules
    st.header("Modules")
    
    # Risk Assessment Module
    st.subheader("1. Risk Assessment")
    st.write("""
    **Purpose**: The Risk Assessment module helps identify and evaluate potential risks that could affect your business.

    **How to Use**:
    - Select risks from predefined categories (e.g., Market Misalignment, Customer Churn).
    - Adjust the likelihood of each risk and define the potential impact.
    - Set the mitigation effectiveness and associated cost for each risk.

    **Input Example**:
    - Risk: *Data Breach*
    - Likelihood: *50%*
    - Minimum Impact: *£1,000*
    - Most Likely Impact: *£5,000*
    - Maximum Impact: *£10,000*
    - Mitigation Effectiveness: *50%*
    - Mitigation Cost: *£500*

    **Expected Output**:
    - Risk Score: The calculated score based on likelihood, impact, and mitigation.

    **Key Outputs**:
    - **Risk Score**: A numeric value indicating the severity of the risk.
    - **Risk Prioritization**: A list of risks sorted by their severity.
    """)

    # Financial Forecasting Module
    st.subheader("2. Financial Forecasting")
    st.write("""
    **Purpose**: Predict revenue, costs, and profits based on historical and projected data.

    **How to Use**:
    - Input the number of clients, package price, and growth rate.
    - Use Monte Carlo simulations to estimate potential revenue, considering variability in growth rates.
    - Forecast total costs by entering fixed costs, variable costs per client, and the projection period.

    **Input Example**:
    - Number of Clients: *100*
    - Package Price: *£1,500*
    - Growth Rate: *10%*
    - Projection Period: *12 months*

    **Expected Output**:
    - Revenue: Predicted revenue over the period, along with percentiles (5th and 95th) to show variability.
    - Costs: Estimated costs based on input assumptions.
    - Profit: Calculated by subtracting costs from revenue.

    **Key Outputs**:
    - **Mean Revenue**: Central estimate of revenue over the projection period.
    - **Risk-Adjusted ROI**: Return on investment accounting for risk.
    - **Breakeven Point**: Time period required to recover costs.
    """)

    # Workforce and Culture Planning Module
    st.subheader("3. Workforce and Culture Planning")
    st.write("""
    **Purpose**: Analyze staffing costs, productivity, and employee affordability.

    **How to Use**:
    - Input salary, benefits, taxes, and operational costs for each role.
    - Estimate the number of employees required.
    - Use Monte Carlo simulations to forecast staffing costs under different scenarios.

    **Input Example**:
    - Number of Roles: *1*
    - Average Salary per Employee: *£30,000*
    - Benefits per Employee: *£5,000*
    - Recruitment Costs: *£1,000*
    - Training Costs: *£2,000*

    **Expected Output**:
    - Total Staffing Costs: Projected costs for staffing including salary, benefits, and additional costs.
    - Breakdowns of the staffing costs by category.

    **Key Outputs**:
    - **Total Staffing Costs**: Sum of all employee-related costs.
    - **Revenue per Employee**: The amount of revenue generated per employee.
    """)

    # Growth & Scaling Strategy Module
    st.subheader("4. Growth & Scaling Strategy")
    st.write("""
    **Purpose**: Evaluate potential growth opportunities, market expansion, and scaling strategies.

    **How to Use**:
    - Input expansion costs, expected revenue, and scaling factors.
    - Assess ROI and payback periods for different growth strategies.

    **Input Example**:
    - Market Entry Costs: *£20,000*
    - Expected Revenue per Customer: *£1,500*
    - Revenue Variability: *20%*

    **Expected Output**:
    - ROI: Return on investment based on input assumptions.
    - Payback Period: Time required to recover the market entry costs.

    **Key Outputs**:
    - **Mean ROI**: Average ROI across simulations.
    - **Payback Period**: Estimated time to break even.
    """)

    # Scenario Comparison Module
    st.subheader("5. Scenario Comparison")
    st.write("""
    **Purpose**: Compare different business scenarios based on key metrics such as ROI, breakeven point, and risk-adjusted results.

    **How to Use**:
    - Input multiple scenarios and their respective metrics (revenue, cost, growth rate).
    - Use Monte Carlo simulations to evaluate the impact of variability and risks on each scenario.

    **Key Outputs**:
    - **Risk-Adjusted ROI**: ROI adjusted for risk.
    - **Breakeven Point**: Time to recover costs for each scenario.
    """)

    # Section 4: Monte Carlo Simulations
    st.header("Monte Carlo Simulations")
    st.write("""
    Monte Carlo simulations provide probabilistic forecasts by modeling uncertainties in inputs like growth rates and costs.

    **Key Metrics to Interpret**:
    - **Mean ROI**: Average profitability across simulations.
    - **Risk-Adjusted ROI**: ROI adjusted for risk factors.
    - **Breakeven Point**: Time range to recover costs (shorter is better).

    **Visualizations**:
    - **Line Graphs:** Show revenue/cost trends and percentiles.
    - **Box Plots:** Highlight variability and median outcomes.
    - **Histograms:** Display distribution of key metrics like ROI.

    **Practical Tips**:
    - Use the mean for planning but consider variability (percentiles) for risk mitigation.
    - Narrow boxes indicate more predictable outcomes.
    """)

    # Section 5: Tips and New Features
    st.header("Tips and New Features")
    st.write("""
    - Regularly update inputs to keep projections accurate.
    - Use Scenario Comparison to evaluate the impact of different strategies.
    - Adjust risk factors in Risk Assessment for a more realistic forecast.

    **New Features**:
    - Enhanced Risk Integration: Adjust forecasts based on risk severity and mitigation costs.
    - Monte Carlo in Workforce Planning: Predict time-to-affordability with probabilistic modeling.
    - Visual Enhancements: Improved heatmaps and ROI charts.
    """)

# Run the help page
if __name__ == "__main__":
    help_page()
