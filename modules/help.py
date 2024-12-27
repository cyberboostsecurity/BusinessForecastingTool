import streamlit as st

def help_page():
    st.title("Application Help Guide")
    st.info("Learn how to use the Business Forecasting Tool and understand its features.")

    # Section: Overview
    st.header("Overview")
    st.write("""
    The Business Forecasting Tool helps you analyze and plan various aspects of your business, including growth, financials, risks, and workforce strategies.
    Use the sidebar to navigate through the modules and access their functionalities.
    """)

    # Section: Modules
    st.header("Modules")

    st.subheader("1. Financial Forecasting")
    st.write("""
    **Purpose**: Predict revenue, costs, and profits based on historical and projected data.

    **Features**:
    - Revenue Projections with Monte Carlo: Forecast income using probabilistic simulations based on growth rates and variability.
    - Cost Projections: Analyze fixed and variable costs over a specified period.
    - Cash Flow Analysis: Examine liquidity by factoring in revenue, costs, and opening balance.
    - Profit & Loss Projections: Assess profitability, factoring in fixed, variable, and additional expenses.
    - Scenario Comparison with Monte Carlo: Compare different business scenarios probabilistically.

    **Interpreting Monte Carlo Simulations**:
    - Use the **Mean Trend** to guide planning (average projection).
    - Review **Percentiles (5th and 95th)** for best- and worst-case bounds.
    - Narrow percentiles = less variability; wide percentiles = higher uncertainty.
    """)

    st.subheader("2. Operational Planning")
    st.write("""
    **Purpose**: Optimize resource usage and improve efficiency.

    **Features**:
    - Resource Allocation: Distribute resources efficiently across business operations.
    - Business Efficiency Metrics: Measure productivity and identify bottlenecks.
    - Technology Recommendations: Suggest cost-saving tools and technologies.
    """)

    st.subheader("3. Risk Assessment")
    st.write("""
    **Purpose**: Identify and evaluate risks, adjusting business plans accordingly.

    **Features**:
    - Define and analyze risks based on their likelihood and impact.
    - Visualize risks with charts and heatmaps.
    - Adjust risk factors to influence Monte Carlo simulations.
    """)

    st.subheader("4. Growth & Scaling Strategy")
    st.write("""
    **Purpose**: Evaluate growth opportunities and strategies for scaling the business.

    **Features**:
    - Market Expansion: Analyze ROI and the payback period for market entry.
    - Customer Metrics: Calculate Customer Lifetime Value (CLV) and Customer Acquisition Cost (CAC).
    - Partnerships: Assess the dependency and ROI for partnerships.
    - Growth Path Analysis: Compare strategies like diversification, expansion, or pricing adjustments.
    - Scenario Planning: Analyze Best Case, Most Likely, and Worst Case outcomes using Monte Carlo simulations.
    - Risk-Adjusted Scaling: Evaluate scaling strategies with built-in risk metrics.
    - Scaling Efficiency: Assess how well resources and costs are utilized during scaling.
    """)

    # Section: Monte Carlo Simulations
    st.header("Monte Carlo Simulations")
    st.write("""
    Monte Carlo simulations provide probabilistic forecasts by modeling uncertainties in inputs like growth rates and costs.

    **Key Metrics to Interpret**:
    - **Mean ROI**: Average profitability across simulations. Higher values indicate better outcomes.
    - **Risk-Adjusted ROI**: ROI adjusted for risk factors (e.g., market volatility, competition).
    - **Breakeven Point**: Range of months needed to recover costs. Shorter ranges indicate quicker profitability.

    **Visualizing Risk-Adjusted Scores**:
    - Box Plot:
      - **Median**: The middle line in the box shows the central value of simulations.
      - **Interquartile Range (IQR)**: The box shows the middle 50% of results (from 25th to 75th percentile).
      - **Whiskers**: Represent variability in outcomes, excluding outliers.
      - **Outliers**: Extreme points beyond typical outcomes.

    **Practical Insights**:
    - Narrow boxes and whiskers = more predictable outcomes.
    - Wide boxes or whiskers = higher uncertainty.
    """)

    # Section: Interpreting Latest Changes
    st.header("Interpreting Latest Changes")
    st.write("""
    **Scenario Planning Enhancements**:
    - Use the graph of Risk-Adjusted Score Distribution across scenarios to compare potential outcomes.
    - Identify scenarios with:
      - **Higher Medians**: Indicate better average performance.
      - **Narrow Boxes and Whiskers**: Reflect less uncertainty and more consistent results.
      - **Risk Tolerance**: Opt for scenarios with acceptable variability relative to your business goals.

    **Growth Path Analysis**:
    - Compare multiple strategies based on ROI, breakeven, and risk-adjusted growth.
    - Use the grouped bar chart to visualize the differences in key metrics across strategies.

    **Partnership Projections**:
    - Assess dependency and risk-adjusted ROI to decide whether a partnership is viable.
    - The bar chart for metrics (e.g., costs, revenue, ROI) helps identify areas for optimization.

    **Risk-Adjusted Scaling**:
    - Review scaling strategies by analyzing risk scores and risk-adjusted ROI.
    - Focus on strategies with higher ROI and lower risk scores for sustainable growth.

    **Scaling Efficiency**:
    - Measure Revenue per Resource and Cost Scaling Factor to assess operational efficiency.
    - Higher metrics indicate better resource utilization and cost management.
    """)

    # Section: Tips
    st.header("Tips")
    st.write("""
    - Regularly update inputs to keep projections accurate.
    - Use Scenario Comparison to evaluate the impact of different strategies.
    - Adjust risk factors in the Risk Assessment module for a more realistic forecast.
    """)

    # Section: New Features
    st.header("New Features")
    st.write("""
    - **Monte Carlo Simulations**: Now integrated into Scenario Planning, Risk-Adjusted Scaling, and Scaling Efficiency.
    - **Risk-Adjusted Metrics**: Evaluate ROI and efficiency while accounting for market and business risks.
    - **Enhanced Visualizations**: Compare distributions and outcomes across multiple scenarios and strategies.
    """)

if __name__ == "__main__":
    help_page()
