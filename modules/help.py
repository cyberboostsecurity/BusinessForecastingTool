import streamlit as st

def help_page():
    st.title("Application Help Guide")
    st.info("Learn how to use the Business Forecasting Tool and understand its features.")

    # Section: Overview
    st.header("Overview")
    st.write("""
    The Business Forecasting Tool is a modular system designed to help businesses plan, optimize, and forecast key operations. 
    The tool combines advanced analytics with Monte Carlo simulations, ensuring robust decision-making.
    
    Use the sidebar to navigate between modules. Certain modules build on data from others for seamless integration.
    """)

    # Section: Workflow Guidance
    st.header("How to Use the Tool")
    st.write("""
    The tool's modular design allows you to work through the following workflow for optimal results:

    **1. Start with Risk Assessment:**
    - Identify risks and their potential impacts.
    - Adjust revenue and cost factors based on likelihood and mitigation measures.

    **2. Move to Financial Forecasting:**
    - Use risk-adjusted metrics to predict revenue, costs, and profitability.
    - Include Monte Carlo simulations to handle variability in projections.

    **3. Workforce Planning:**
    - Plan staffing needs based on financial projections.
    - Assess employee affordability to ensure sustainable workforce growth.

    **4. Explore Growth & Scaling Strategy:**
    - Assess market entry, customer acquisition, and partnerships.
    - Compare strategies and evaluate scaling efficiency with Monte Carlo simulations.

    **5. Scenario Comparison:**
    - Combine metrics from Financial Forecasting and Risk Assessment to compare probabilistic outcomes.
    - Identify the best strategy based on risk-adjusted ROI and breakeven points.

    **6. Review Dashboard Outputs:**
    - View aggregated results across modules for a comprehensive business overview.
    """)

    # Section: Modules
    st.header("Modules")

    st.subheader("1. Risk Assessment")
    st.write("""
    **Purpose**: Identify and evaluate risks, adjusting business plans accordingly.

    **Features**:
    - Define and analyze risks based on their likelihood, impact, and mitigation costs.
    - Calculate risk-adjusted metrics for integration into Financial Forecasting.
    - Visualize risks with heatmaps and severity charts.

    **Key Outputs:**
    - Overall risk score: Prioritized list of risks by severity.
    - Adjusted revenue and cost factors for Financial Forecasting.
    """)

    st.subheader("2. Financial Forecasting")
    st.write("""
    **Purpose**: Predict revenue, costs, and profits based on historical and projected data.

    **Features**:
    - Revenue Projections: Forecast income using growth rates and variability.
    - Cost Projections: Analyze fixed and variable costs over time.
    - Cash Flow Analysis: Examine liquidity trends based on revenue and costs.
    - Profit & Loss Projections: Assess profitability considering risk-adjusted inputs.
    - Scenario Comparison: Use Monte Carlo simulations to evaluate variability and risks.

    **Key Metrics:**
    - **Mean Revenue/Cost:** Central trend for planning.
    - **Risk-Adjusted ROI:** ROI influenced by risks.
    - **Breakeven Point:** Time required to recover costs.
    """)

    st.subheader("3. Workforce and Culture Planning")
    st.write("""
    **Purpose**: Analyze staffing costs, productivity, and employee affordability.

    **Features**:
    - Staffing Costs: Forecast costs based on salaries, benefits, and taxes.
    - Productivity Management: Assess workforce efficiency and utilization rates.
    - Employee Affordability: Estimate the revenue growth needed to afford new hires.

    **Monte Carlo Integration**:
    - Predict time to achieve affordability under variable growth rates.
    """)

    st.subheader("4. Growth & Scaling Strategy")
    st.write("""
    **Purpose**: Evaluate growth opportunities and scaling strategies.

    **Features**:
    - Market Expansion: Analyze ROI and payback periods for new markets.
    - Customer Metrics: Assess Customer Lifetime Value (CLV) and Customer Acquisition Costs (CAC).
    - Partnerships: Evaluate ROI and dependency risks for partnerships.
    - Risk-Adjusted Scaling: Incorporate risk metrics into scaling strategies.
    - Scaling Efficiency: Assess resource utilization and scaling cost effectiveness.
    """)

    st.subheader("5. Scenario Comparison")
    st.write("""
    **Purpose**: Compare probabilistic outcomes of multiple business scenarios.

    **Features**:
    - Monte Carlo Simulations: Test scenarios with variability in key metrics.
    - Risk-Adjusted Comparisons: Evaluate scenarios by ROI, breakeven, and variability.
    """)

    # Section: Monte Carlo Simulations
    st.header("Monte Carlo Simulations")
    st.write("""
    Monte Carlo simulations provide probabilistic forecasts by modeling uncertainties in inputs like growth rates and costs.

    **Key Metrics to Interpret**:
    - **Mean ROI**: Average profitability across simulations.
    - **Risk-Adjusted ROI**: ROI adjusted for risk factors.
    - **Breakeven Point**: Time range to recover costs (shorter is better).

    **Visualizations:**
    - **Line Graphs:** Show revenue/cost trends and percentiles.
    - **Box Plots:** Highlight variability and median outcomes.
    - **Histograms:** Display distribution of key metrics like ROI.

    **Practical Tips:**
    - Use the mean for planning but consider variability (percentiles) for risk mitigation.
    - Narrow boxes indicate more predictable outcomes.
    """)

    # Section: Tips and New Features
    st.header("Tips and New Features")
    st.write("""
    - Regularly update inputs to keep projections accurate.
    - Use Scenario Comparison to evaluate the impact of different strategies.
    - Adjust risk factors in Risk Assessment for a more realistic forecast.

    **New Features:**
    - Enhanced Risk Integration: Adjust forecasts based on risk severity and mitigation costs.
    - Monte Carlo in Workforce Planning: Predict time-to-affordability with probabilistic modeling.
    - Visual Enhancements: Improved heatmaps and ROI charts.
    """)

if __name__ == "__main__":
    help_page()
