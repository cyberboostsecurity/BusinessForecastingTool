import streamlit as st

def growth_scaling():
    st.header("Growth & Scaling Strategy")
    st.info("Analyze and plan your business growth and scaling strategies.")

    # Submenu Navigation
    submenu = st.selectbox("Select a Sub-Module", [
        "Market Expansion",
        "Customer Metrics",
        "Partnership Projections",
        "Growth Path Analysis",
        "Risk-Adjusted Scaling",
        "Scaling Efficiency"
    ])

    # Load selected submodule
    if submenu == "Market Expansion":
        market_expansion()
    elif submenu == "Customer Metrics":
        customer_metrics()
    elif submenu == "Partnership Projections":
        partnership_projections()
    elif submenu == "Growth Path Analysis":
        growth_path_analysis()
    elif submenu == "Risk-Adjusted Scaling":
        risk_adjusted_scaling()
    elif submenu == "Scaling Efficiency":
        scaling_efficiency()

# Submodule Functions
import streamlit as st
import plotly.express as px  # Ensure Plotly Express is imported

def market_expansion():
    st.subheader("Market Expansion")
    st.write("Analyze the feasibility and profitability of entering a new market.")

    # Step 1: Input Costs
    st.write("### Step 1: Market Entry Costs")
    marketing_costs = st.number_input(
        "Marketing Costs (\u00A3)", min_value=0.0, step=100.0,
        help="Estimated costs for campaigns, advertisements, and promotions."
    )
    infrastructure_costs = st.number_input(
        "Infrastructure Costs (\u00A3)", min_value=0.0, step=100.0,
        help="Costs for setting up infrastructure, equipment, or technology."
    )
    compliance_costs = st.number_input(
        "Compliance/Legal Costs (\u00A3)", min_value=0.0, step=100.0,
        help="Costs for meeting legal or regulatory requirements."
    )
    training_costs = st.number_input(
        "Training/Staffing Costs (\u00A3)", min_value=0.0, step=100.0,
        help="Expenses for training or hiring staff."
    )
    total_entry_costs = marketing_costs + infrastructure_costs + compliance_costs + training_costs

    st.write(f"**Total Market Entry Costs:** \u00A3{total_entry_costs:.2f}")

    # Step 2: Revenue Potential
    st.write("### Step 2: Revenue Potential")
    average_revenue_per_customer = st.number_input(
        "Average Revenue per Customer (\u00A3)", min_value=0.0, step=100.0,
        help="The average annual revenue per customer."
    )
    expected_customers = st.number_input(
        "Expected Number of Customers", min_value=0, step=1,
        help="The number of customers you expect to acquire in the new market."
    )
    expected_revenue = average_revenue_per_customer * expected_customers

    st.write(f"**Expected Annual Revenue:** \u00A3{expected_revenue:.2f}")

    # Step 3: Market Characteristics
    st.write("### Step 3: Market Characteristics")
    market_saturation = st.slider(
        "Market Saturation (%)", min_value=0, max_value=100, value=50,
        help="Percentage of the market already served by competitors."
    )
    competition_intensity = st.slider(
        "Competition Intensity (1-5)", min_value=1, max_value=5, value=3,
        help="Level of competition, with 1 being low and 5 being high."
    )
    market_volatility = st.slider(
        "Market Volatility (1-5)", min_value=1, max_value=5, value=2,
        help="Unpredictability of the market, with 1 being stable and 5 being highly volatile."
    )

    # Step 4: Calculations
    st.write("### Step 4: Advanced Metrics")
    if total_entry_costs > 0:
        roi = ((expected_revenue - total_entry_costs) / total_entry_costs) * 100
        payback_period = total_entry_costs / (expected_revenue / 12) if expected_revenue > 0 else float('inf')
        risk_score = ((market_saturation / 100) * competition_intensity * market_volatility)

        # Outputs
        st.write(f"- **Return on Investment (ROI):** {roi:.2f}%")
        st.write(f"- **Payback Period:** {payback_period:.2f} months")
        st.write(f"- **Risk Score:** {risk_score:.2f} (higher = riskier)")

        # Recommendations
        if roi > 20 and risk_score < 3:
            st.success("This market appears viable. Consider entering with a solid plan.")
        elif risk_score >= 3:
            st.warning("This market has significant risks. Reassess your strategy.")
        else:
            st.warning("This market may have low returns. Consider alternatives.")

        # Visualization
        metrics = ["Total Costs", "Expected Revenue", "ROI"]
        values = [total_entry_costs, expected_revenue, roi]
        fig = px.bar(x=metrics, y=values, labels={"x": "Metrics", "y": "Amount (\u00A3)"}, title="Market Expansion Metrics")
        st.plotly_chart(fig)

    else:
        st.warning("Market entry costs must be greater than zero to calculate metrics.")


def customer_metrics():
    st.subheader("Customer Metrics")
    st.write("Evaluate the profitability and efficiency of customer acquisition and retention.")

    # Step 1: Input Customer Metrics
    st.write("### Step 1: Input Customer Metrics")
    avg_revenue_per_customer = st.number_input(
        "Average Annual Revenue per Customer (\u00A3)", min_value=0.0, step=100.0, value=5000.0,
        help="The average annual revenue generated per customer."
    )
    avg_customer_retention_duration = st.number_input(
        "Average Retention Duration (Years)", min_value=0.0, step=0.1, value=5.0,
        help="The average number of years customers stay with your business."
    )
    acquisition_costs = st.number_input(
        "Total Acquisition Campaign Costs (\u00A3)", min_value=0.0, step=100.0, value=20000.0,
        help="Total costs incurred for customer acquisition campaigns."
    )
    new_customers_acquired = st.number_input(
        "New Customers Acquired", min_value=1, step=1, value=100,
        help="Total number of new customers acquired during the campaigns."
    )

    # Step 2: Calculate Metrics
    st.write("### Step 2: Calculations")
    clv = avg_revenue_per_customer * avg_customer_retention_duration
    cac = acquisition_costs / new_customers_acquired
    clv_to_cac_ratio = clv / cac if cac > 0 else 0

    st.write(f"- **Customer Lifetime Value (CLV):** \u00A3{clv:.2f}")
    st.write(f"- **Customer Acquisition Cost (CAC):** \u00A3{cac:.2f}")
    st.write(f"- **CLV-to-CAC Ratio:** {clv_to_cac_ratio:.2f} (Higher is better)")

    # Step 3: Churn Rate (Optional)
    st.write("### Step 3: Churn Rate (Optional)")
    lost_customers = st.number_input(
        "Lost Customers in the Last Year", min_value=0, step=1, value=10,
        help="Total number of customers lost in the last year."
    )
    total_customers = st.number_input(
        "Total Customers at the Start of the Year", min_value=1, step=1, value=500,
        help="Total number of customers at the start of the year."
    )
    churn_rate = (lost_customers / total_customers) * 100 if total_customers > 0 else 0

    st.write(f"- **Churn Rate:** {churn_rate:.2f}% (Lower is better)")

    # Recommendations
    st.write("### Recommendations")
    if clv_to_cac_ratio >= 3:
        st.success("Your customer acquisition strategy is highly efficient. Keep scaling!")
    elif clv_to_cac_ratio >= 1:
        st.info("Your acquisition strategy is acceptable, but there's room for improvement.")
    else:
        st.warning("Your customer acquisition costs are too high relative to lifetime value. Reassess your strategy.")

    if churn_rate > 10:
        st.warning("High churn rate detected. Focus on improving customer retention.")

    # Visualization
    st.write("### Visualizations")
    metrics = ["CLV", "CAC", "CLV-to-CAC Ratio"]
    values = [clv, cac, clv_to_cac_ratio]
    fig = px.bar(x=metrics, y=values, title="Customer Metrics Overview", labels={"x": "Metrics", "y": "Values"})
    st.plotly_chart(fig)

    # Save Results
    if st.button("Save Metrics"):
        st.session_state["customer_metrics"] = {
            "CLV": clv,
            "CAC": cac,
            "CLV-to-CAC Ratio": clv_to_cac_ratio,
            "Churn Rate": churn_rate
        }
        st.success("Metrics saved!")


def partnership_projections():
    st.subheader("Partnership Projections")
    st.write("Evaluate the revenue contribution and ROI of potential partnerships.")

    # Step 1: Partnership Costs
    st.write("### Step 1: Partnership Costs")
    partnership_formation_costs = st.number_input(
        "Partnership Formation Costs (\u00A3)", min_value=0.0, step=100.0, value=5000.0,
        help="Costs associated with forming the partnership (e.g., legal fees, onboarding)."
    )
    partnership_maintenance_costs = st.number_input(
        "Partnership Maintenance Costs (\u00A3)", min_value=0.0, step=100.0, value=2000.0,
        help="Ongoing costs of maintaining the partnership (e.g., revenue sharing, support)."
    )
    total_partnership_costs = partnership_formation_costs + partnership_maintenance_costs

    st.write(f"**Total Partnership Costs:** \u00A3{total_partnership_costs:.2f}")

    # Step 2: Revenue from Partnerships
    st.write("### Step 2: Revenue from Partnerships")
    partnership_revenue = st.number_input(
        "Expected Revenue from Partnerships (\u00A3)", min_value=0.0, step=100.0, value=15000.0,
        help="Estimated revenue generated through the partnership."
    )

    # Step 3: Dependency on Partnerships
    st.write("### Step 3: Dependency on Partnerships")
    total_business_revenue = st.number_input(
        "Total Business Revenue (\u00A3)", min_value=0.0, step=1000.0, value=50000.0,
        help="Total revenue generated by your business, including partnerships."
    )
    dependency_score = (partnership_revenue / total_business_revenue) * 100 if total_business_revenue > 0 else 0

    # Step 4: Calculations
    st.write("### Step 4: ROI and Risk Analysis")
    if total_partnership_costs > 0:
        partnership_roi = ((partnership_revenue - total_partnership_costs) / total_partnership_costs) * 100
        st.write(f"- **Partnership ROI:** {partnership_roi:.2f}%")
    else:
        partnership_roi = 0
        st.warning("Partnership costs must be greater than zero to calculate ROI.")

    st.write(f"- **Dependency Score:** {dependency_score:.2f}% (Percentage of revenue reliant on partnerships)")

    # Risk Adjustment
    partnership_risk = st.slider(
        "Partnership Risk Factor (1-5)", min_value=1, max_value=5, value=3,
        help="Evaluate the stability and risk associated with the partnership, with 1 being low risk and 5 being high risk."
    )
    risk_adjusted_roi = partnership_roi - (partnership_risk * 5)

    st.write(f"- **Risk-Adjusted ROI:** {risk_adjusted_roi:.2f}% (Accounting for partnership risks)")

    # Recommendations
    st.write("### Recommendations")
    if partnership_roi > 20 and risk_adjusted_roi > 15 and dependency_score < 30:
        st.success("This partnership appears profitable and sustainable. Proceed with confidence.")
    elif risk_adjusted_roi <= 15:
        st.warning("This partnership poses significant risks. Evaluate alternatives.")
    elif dependency_score >= 30:
        st.warning("High dependency on partnerships detected. Diversify your revenue streams.")

    # Visualization
    st.write("### Visualization")
    metrics = ["Costs", "Revenue", "ROI", "Risk-Adjusted ROI"]
    values = [total_partnership_costs, partnership_revenue, partnership_roi, risk_adjusted_roi]
    fig = px.bar(x=metrics, y=values, title="Partnership Metrics Overview", labels={"x": "Metrics", "y": "Amount (\u00A3)"})
    st.plotly_chart(fig)

    # Save Results
    if st.button("Save Partnership Metrics"):
        st.session_state["partnership_metrics"] = {
            "Total Costs": total_partnership_costs,
            "Revenue": partnership_revenue,
            "ROI": partnership_roi,
            "Risk-Adjusted ROI": risk_adjusted_roi,
            "Dependency Score": dependency_score
        }
        st.success("Partnership metrics saved!")


import streamlit as st
import plotly.graph_objects as go

def growth_path_analysis():
    st.subheader("Growth Path Analysis")
    st.write("Analyze and compare different strategies to identify the best growth path.")

    # Step 1: Define Growth Strategies
    st.write("### Step 1: Define Growth Strategies")
    strategy_options = ["Product Diversification", "Geographical Expansion", "Pricing Strategies"]
    selected_strategy = st.selectbox(
        "Select Growth Strategy",
        strategy_options,
        help="Choose a growth strategy to analyze."
    )

    expected_revenue_growth = st.number_input(
        f"Expected Revenue Growth (%) for {selected_strategy}",
        min_value=0.0,
        step=1.0,
        help="Estimated percentage increase in revenue from this strategy."
    )
    strategy_costs = st.number_input(
        f"Estimated Costs (\u00A3) for {selected_strategy}",
        min_value=0.0,
        step=100.0,
        help="Costs associated with implementing this strategy."
    )
    strategy_timeline = st.slider(
        "Strategy Implementation Timeline (Months)",
        min_value=1,
        max_value=60,
        value=12,
        help="Timeframe over which the strategy will be implemented."
    )
    strategy_risk = st.slider(
        "Risk Factor (1-5)",
        min_value=1,
        max_value=5,
        value=3,
        help="Perceived risk level of the strategy, with 1 being low risk and 5 being high risk."
    )

    # Step 2: Calculate Metrics
    st.write("### Step 2: Calculate Metrics")
    if strategy_costs > 0:
        strategy_roi = ((expected_revenue_growth * strategy_costs / 100) - strategy_costs) / strategy_costs * 100
        breakeven_point = strategy_costs / ((expected_revenue_growth * strategy_costs / 100) / strategy_timeline) if expected_revenue_growth > 0 else float('inf')
        risk_adjusted_growth = strategy_roi - (strategy_risk * 5)

        st.write(f"- **Return on Investment (ROI):** {strategy_roi:.2f}%")
        st.write(f"- **Breakeven Point:** {breakeven_point:.2f} months")
        st.write(f"- **Risk-Adjusted Growth Score:** {risk_adjusted_growth:.2f}")
    else:
        st.warning("Strategy costs must be greater than zero to calculate metrics.")
        strategy_roi = 0
        breakeven_point = 0
        risk_adjusted_growth = 0

    # Step 3: Compare Strategies
    st.write("### Step 3: Compare Strategies")
    if "strategies" not in st.session_state:
        st.session_state["strategies"] = []

    new_strategy_name = st.text_input("Enter Strategy Name")
    if st.button("Add Strategy", key="add_strategy_button"):
        if new_strategy_name:
            st.session_state["strategies"].append({
                "Name": new_strategy_name,
                "ROI": strategy_roi,
                "Risk-Adjusted Growth": risk_adjusted_growth,
                "Breakeven Point": breakeven_point,
            })
            st.success(f"Strategy '{new_strategy_name}' added!")

    if st.session_state["strategies"]:
        st.write("### Saved Strategies")
        for strategy in st.session_state["strategies"]:
            st.write(f"- **Name:** {strategy['Name']}, **ROI:** {strategy['ROI']:.2f}%, "
                     f"**Risk-Adjusted Growth:** {strategy['Risk-Adjusted Growth']:.2f}, "
                     f"**Breakeven Point:** {strategy['Breakeven Point']:.2f} months")

    # Visualization
    st.write("### Visualization")
    if st.session_state["strategies"]:
        names = [strategy["Name"] for strategy in st.session_state["strategies"]]
        rois = [strategy["ROI"] for strategy in st.session_state["strategies"]]
        risk_adjusted_growths = [strategy["Risk-Adjusted Growth"] for strategy in st.session_state["strategies"]]

        fig = go.Figure()
        fig.add_trace(go.Bar(name="ROI", x=names, y=rois))
        fig.add_trace(go.Bar(name="Risk-Adjusted Growth", x=names, y=risk_adjusted_growths))
        fig.update_layout(barmode="group", title="Comparison of Strategies", xaxis_title="Strategies", yaxis_title="Values")
        st.plotly_chart(fig)

    # Save Results
    st.write("### Save Results")
    if st.button("Save All Strategies", key="save_all_strategies"):
        st.success("All strategies saved successfully!")


import streamlit as st
import plotly.graph_objects as go

def scenario_planning():
    st.subheader("Scenario Planning")
    st.write("Simulate and compare outcomes for best-case, worst-case, and most-likely scenarios.")

    # Step 1: Define Scenarios
    st.write("### Step 1: Define Scenarios")
    scenarios = ["Best Case", "Most Likely", "Worst Case"]

    revenue_assumptions = {}
    cost_assumptions = {}
    risk_levels = {}

    for scenario in scenarios:
        st.write(f"#### {scenario} Scenario")
        revenue_assumptions[scenario] = st.number_input(
            f"Expected Revenue (\u00A3) for {scenario} Scenario", min_value=0.0, step=1000.0,
            help=f"Enter the expected revenue for the {scenario.lower()} scenario."
        )
        cost_assumptions[scenario] = st.number_input(
            f"Expected Costs (\u00A3) for {scenario} Scenario", min_value=0.0, step=1000.0,
            help=f"Enter the expected costs for the {scenario.lower()} scenario."
        )
        risk_levels[scenario] = st.slider(
            f"Risk Level (1-5) for {scenario} Scenario", min_value=1, max_value=5, value=3,
            help=f"Assess the risk level for the {scenario.lower()} scenario."
        )

    # Step 2: Calculate Metrics
    st.write("### Step 2: Calculate Metrics")
    metrics = {"Scenario": [], "ROI (%)": [], "Breakeven Point (Months)": [], "Risk-Adjusted Score": []}

    for scenario in scenarios:
        revenue = revenue_assumptions[scenario]
        costs = cost_assumptions[scenario]
        risk = risk_levels[scenario]

        if costs > 0:
            roi = ((revenue - costs) / costs) * 100
            breakeven_point = costs / (revenue / 12) if revenue > 0 else float('inf')
            risk_adjusted_score = roi - (risk * 5)
        else:
            roi = 0
            breakeven_point = float('inf')
            risk_adjusted_score = 0

        metrics["Scenario"].append(scenario)
        metrics["ROI (%)"].append(roi)
        metrics["Breakeven Point (Months)"].append(breakeven_point)
        metrics["Risk-Adjusted Score"].append(risk_adjusted_score)

        st.write(f"#### {scenario} Scenario Results")
        st.write(f"- **ROI:** {roi:.2f}%")
        st.write(f"- **Breakeven Point:** {breakeven_point:.2f} months")
        st.write(f"- **Risk-Adjusted Score:** {risk_adjusted_score:.2f}")

    # Step 3: Visualization
    st.write("### Step 3: Visualization")
    fig = go.Figure()
    fig.add_trace(go.Bar(name="ROI (%)", x=metrics["Scenario"], y=metrics["ROI (%)"]))
    fig.add_trace(go.Bar(name="Risk-Adjusted Score", x=metrics["Scenario"], y=metrics["Risk-Adjusted Score"]))
    fig.update_layout(barmode="group", title="Scenario Comparison", xaxis_title="Scenario", yaxis_title="Values")
    st.plotly_chart(fig)

    # Step 4: Recommendations
    st.write("### Step 4: Recommendations")
    best_scenario = max(metrics["Risk-Adjusted Score"], default=0)
    if best_scenario > 0:
        best_index = metrics["Risk-Adjusted Score"].index(best_scenario)
        best_name = metrics["Scenario"][best_index]
        st.success(f"The recommended strategy is the **{best_name} Scenario** based on the highest risk-adjusted score.")
    else:
        st.warning("No scenario is showing a strong advantage. Reassess your inputs.")

    # Save Results
    st.write("### Save Results")
    if st.button("Save Scenario Results"):
        st.session_state["scenario_results"] = metrics
        st.success("Scenario results saved!")

    if "scenario_results" in st.session_state:
        st.write("Saved Results:", st.session_state["scenario_results"])
        st.download_button(
            label="Download Results as JSON",
            data=str(st.session_state["scenario_results"]),
            file_name="scenario_results.json"
        )



def risk_adjusted_scaling():
    st.subheader("Risk-Adjusted Scaling")
    st.write("""
    Integrate risk metrics into your scaling strategy. 
    Metrics include:
    - Market saturation risk
    - Competition intensity
    - Volatility adjustments
    """)

def scaling_efficiency():
    st.subheader("Scaling Efficiency")
    st.write("""
    Ensure your scaling strategy is efficient and sustainable. 
    Metrics include:
    - Revenue per resource
    - Cost-scaling factors
    - Sales efficiency ratios
    """)
