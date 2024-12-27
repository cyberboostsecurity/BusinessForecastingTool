import streamlit as st
import plotly.graph_objects as go
import plotly.express as px  # Ensure Plotly Express is imported
import numpy as np
from modules.db_utils import save_to_database  # Ensure this function is implemented



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
        "Scaling Efficiency",
        "Scenario Planning"
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
    elif submenu == "Scenario Planning":  # Link Scenario Planning
        scenario_planning()

# Submodule Functions


def market_expansion():
    st.subheader("Market Expansion with Monte Carlo")
    st.write("Analyze the feasibility and profitability of entering a new market.")

    # Step 1: Input Costs
    st.write("### Step 1: Market Entry Costs")
    marketing_costs = st.number_input(
        "Marketing Costs (£)", min_value=0.0, step=100.0,
        help="Estimated costs for campaigns, advertisements, and promotions."
    )
    infrastructure_costs = st.number_input(
        "Infrastructure Costs (£)", min_value=0.0, step=100.0,
        help="Costs for setting up infrastructure, equipment, or technology."
    )
    compliance_costs = st.number_input(
        "Compliance/Legal Costs (£)", min_value=0.0, step=100.0,
        help="Costs for meeting legal or regulatory requirements."
    )
    training_costs = st.number_input(
        "Training/Staffing Costs (£)", min_value=0.0, step=100.0,
        help="Expenses for training or hiring staff."
    )
    total_entry_costs = marketing_costs + infrastructure_costs + compliance_costs + training_costs

    st.write(f"**Total Market Entry Costs:** £{total_entry_costs:.2f}")

    # Step 2: Revenue Potential
    st.write("### Step 2: Revenue Potential")
    average_revenue_per_customer = st.number_input(
        "Average Revenue per Customer (£)", min_value=0.0, step=100.0,
        help="The average annual revenue per customer."
    )
    expected_customers = st.number_input(
        "Expected Number of Customers", min_value=0, step=1,
        help="The number of customers you expect to acquire in the new market."
    )

    # Step 3: Variability Factors
    st.write("### Step 3: Variability Factors")
    revenue_variability = st.slider(
        "Revenue Variability (%)", min_value=0, max_value=50, value=10,
        help="Percentage variability in revenue assumptions."
    )
    cost_variability = st.slider(
        "Cost Variability (%)", min_value=0, max_value=50, value=10,
        help="Percentage variability in cost assumptions."
    )

    # Monte Carlo Simulations
    simulations = 1000
    simulated_revenues = np.random.normal(
        loc=average_revenue_per_customer * expected_customers,
        scale=(revenue_variability / 100) * average_revenue_per_customer * expected_customers,
        size=simulations
    )
    simulated_costs = np.random.normal(
        loc=total_entry_costs,
        scale=(cost_variability / 100) * total_entry_costs,
        size=simulations
    )

    simulated_roi = ((simulated_revenues - simulated_costs) / simulated_costs) * 100
    simulated_payback = np.where(simulated_revenues > 0, simulated_costs / (simulated_revenues / 12), float('inf'))

    # Calculate statistics
    mean_roi = np.mean(simulated_roi)
    p5_roi = np.percentile(simulated_roi, 5)
    p95_roi = np.percentile(simulated_roi, 95)

    mean_payback = np.mean(simulated_payback)
    p5_payback = np.percentile(simulated_payback, 5)
    p95_payback = np.percentile(simulated_payback, 95)

    # Outputs
    st.write("### Results")
    st.write(f"- **Mean ROI:** {mean_roi:.2f}%")
    st.write(f"- **ROI Range (5th to 95th Percentile):** {p5_roi:.2f}% to {p95_roi:.2f}%")
    st.write(f"- **Mean Payback Period:** {mean_payback:.2f} months")
    st.write(f"- **Payback Period Range (5th to 95th Percentile):** {p5_payback:.2f} to {p95_payback:.2f} months")

    # Visualization: ROI Distribution
    st.write("### ROI Distribution")
    fig_roi = px.histogram(simulated_roi, nbins=50, title="ROI Distribution", labels={"x": "ROI (%)", "y": "Frequency"})
    st.plotly_chart(fig_roi)

    # Visualization: Payback Period Distribution
    st.write("### Payback Period Distribution")
    fig_payback = px.histogram(simulated_payback, nbins=50, title="Payback Period Distribution", labels={"x": "Payback Period (Months)", "y": "Frequency"})
    st.plotly_chart(fig_payback)

    # Recommendations
    st.write("### Recommendations")
    if mean_roi > 20 and p5_roi > 10 and mean_payback < 24:
        st.success("This market appears viable. Proceed with a detailed market entry plan.")
    elif mean_roi < 0 or mean_payback > 36:
        st.warning("This market may not be profitable. Consider alternative opportunities.")
    else:
        st.info("This market has moderate potential. Proceed with caution and further analysis.")



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
    st.subheader("Partnership Projections with Monte Carlo")
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

    # Monte Carlo Simulations
    st.write("### Monte Carlo Simulations")
    simulations = 1000

    # Simulate variability in costs and revenues
    simulated_revenues = np.random.normal(
        loc=partnership_revenue,
        scale=partnership_revenue * 0.1,
        size=simulations
    )
    simulated_costs = np.random.normal(
        loc=total_partnership_costs,
        scale=total_partnership_costs * 0.1,
        size=simulations
    )

    # Calculate metrics
    simulated_roi = ((simulated_revenues - simulated_costs) / simulated_costs) * 100
    risk_adjusted_roi = simulated_roi - (dependency_score * 0.1)

    # Summary statistics
    mean_roi = np.mean(simulated_roi)
    mean_risk_adjusted_roi = np.mean(risk_adjusted_roi)
    p5_roi = np.percentile(simulated_roi, 5)
    p95_roi = np.percentile(simulated_roi, 95)

    st.write(f"- **Mean ROI:** {mean_roi:.2f}%")
    st.write(f"- **ROI Range (5th to 95th Percentile):** {p5_roi:.2f}% to {p95_roi:.2f}%")
    st.write(f"- **Mean Risk-Adjusted ROI:** {mean_risk_adjusted_roi:.2f}%")

    # Visualization: ROI Distribution
    st.write("### ROI Distribution")
    fig_roi = px.histogram(
        simulated_roi,
        nbins=50,
        title="ROI Distribution",
        labels={"x": "ROI (%)", "y": "Frequency"}
    )
    st.plotly_chart(fig_roi)

    # Visualization: Risk-Adjusted ROI Distribution
    st.write("### Risk-Adjusted ROI Distribution")
    fig_risk_adjusted = px.histogram(
        risk_adjusted_roi,
        nbins=50,
        title="Risk-Adjusted ROI Distribution",
        labels={"x": "Risk-Adjusted ROI (%)", "y": "Frequency"}
    )
    st.plotly_chart(fig_risk_adjusted)

    # Recommendations
    st.write("### Recommendations")
    if mean_roi > 20 and mean_risk_adjusted_roi > 15 and dependency_score < 30:
        st.success("This partnership appears profitable and sustainable. Proceed with confidence.")
    elif mean_risk_adjusted_roi <= 15:
        st.warning("This partnership poses significant risks. Evaluate alternatives.")
    elif dependency_score >= 30:
        st.warning("High dependency on partnerships detected. Diversify your revenue streams.")

    # Save Results
    st.write("### Save Results")
    if st.button("Save Partnership Metrics"):
        st.session_state["partnership_metrics"] = {
            "Mean ROI": mean_roi,
            "ROI Range": (p5_roi, p95_roi),
            "Mean Risk-Adjusted ROI": mean_risk_adjusted_roi,
            "Dependency Score": dependency_score
        }
        st.success("Partnership metrics saved!")


def growth_path_analysis():
    st.subheader("Growth Path Analysis with Monte Carlo")
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

    # Step 2: Monte Carlo Simulations
    st.write("### Step 2: Monte Carlo Simulations")
    simulations = 1000

    # Simulate variability in revenue growth and costs
    simulated_revenue_growth = np.random.normal(
        loc=expected_revenue_growth,
        scale=expected_revenue_growth * 0.1,
        size=simulations
    )
    simulated_costs = np.random.normal(
        loc=strategy_costs,
        scale=strategy_costs * 0.1,
        size=simulations
    )

    # Calculate simulated metrics
    simulated_roi = ((simulated_revenue_growth * simulated_costs / 100) - simulated_costs) / simulated_costs * 100
    simulated_breakeven = np.where(
        simulated_revenue_growth > 0,
        simulated_costs / ((simulated_revenue_growth * simulated_costs / 100) / strategy_timeline),
        float('inf')
    )
    simulated_risk_adjusted_growth = simulated_roi - (strategy_risk * 5)

    # Summary statistics
    mean_roi = np.mean(simulated_roi)
    mean_breakeven = np.mean(simulated_breakeven)
    mean_risk_adjusted_growth = np.mean(simulated_risk_adjusted_growth)

    st.write(f"- **Mean ROI:** {mean_roi:.2f}%")
    st.write(f"- **Mean Breakeven Point:** {mean_breakeven:.2f} months")
    st.write(f"- **Mean Risk-Adjusted Growth:** {mean_risk_adjusted_growth:.2f}%")

    # Step 3: Visualizations
    st.write("### Visualizations")
    
    # ROI Distribution
    fig_roi = px.histogram(
        simulated_roi,
        nbins=50,
        title="ROI Distribution",
        labels={"x": "ROI (%)", "y": "Frequency"}
    )
    st.plotly_chart(fig_roi)

    # Breakeven Distribution
    fig_breakeven = px.histogram(
        simulated_breakeven,
        nbins=50,
        title="Breakeven Point Distribution",
        labels={"x": "Breakeven Point (Months)", "y": "Frequency"}
    )
    st.plotly_chart(fig_breakeven)

    # Risk-Adjusted Growth Distribution
    fig_risk_adjusted = px.histogram(
        simulated_risk_adjusted_growth,
        nbins=50,
        title="Risk-Adjusted Growth Distribution",
        labels={"x": "Risk-Adjusted Growth (%)", "y": "Frequency"}
    )
    st.plotly_chart(fig_risk_adjusted)

    # Step 4: Add Strategy and Compare
    st.write("### Compare Strategies")
    if "strategies" not in st.session_state:
        st.session_state["strategies"] = []

    new_strategy_name = st.text_input("Enter Strategy Name")
    if st.button("Add Strategy", key="add_strategy_button"):
        if new_strategy_name:
            st.session_state["strategies"].append({
                "Name": new_strategy_name,
                "Mean ROI": mean_roi,
                "Mean Breakeven": mean_breakeven,
                "Mean Risk-Adjusted Growth": mean_risk_adjusted_growth
            })
            st.success(f"Strategy '{new_strategy_name}' added!")

    # Display saved strategies
    if st.session_state["strategies"]:
        st.write("### Saved Strategies")
        for strategy in st.session_state["strategies"]:
            st.write(f"- **{strategy['Name']}**: ROI = {strategy['Mean ROI']:.2f}%, "
                     f"Breakeven = {strategy['Mean Breakeven']:.2f} months, "
                     f"Risk-Adjusted Growth = {strategy['Mean Risk-Adjusted Growth']:.2f}%")

    # Comparative Visualization
    if st.session_state["strategies"]:
        names = [s["Name"] for s in st.session_state["strategies"]]
        rois = [s["Mean ROI"] for s in st.session_state["strategies"]]
        risk_adjusted = [s["Mean Risk-Adjusted Growth"] for s in st.session_state["strategies"]]

        fig_comparison = go.Figure()
        fig_comparison.add_trace(go.Bar(name="ROI", x=names, y=rois))
        fig_comparison.add_trace(go.Bar(name="Risk-Adjusted Growth", x=names, y=risk_adjusted))
        fig_comparison.update_layout(barmode="group", title="Comparison of Strategies", xaxis_title="Strategies", yaxis_title="Values")
        st.plotly_chart(fig_comparison)






def scenario_planning():

    st.subheader("Scenario Planning with Monte Carlo")
    st.write("Simulate and compare outcomes for best-case, worst-case, and most-likely scenarios.")

    # Step 1: Define Scenarios
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

    # Step 2: Monte Carlo Simulations
    simulations = 1000
    results = {"Scenario": [], "ROI": [], "Breakeven Point": [], "Risk-Adjusted Score": []}

    for scenario in scenarios:
        revenue = revenue_assumptions[scenario]
        cost = cost_assumptions[scenario]
        risk = risk_levels[scenario]

        if cost > 0:
            # Simulate variability
            simulated_revenues = np.random.normal(loc=revenue, scale=revenue * 0.1, size=simulations)
            simulated_costs = np.random.normal(loc=cost, scale=cost * 0.1, size=simulations)

            # Calculate metrics
            simulated_roi = ((simulated_revenues - simulated_costs) / simulated_costs) * 100
            simulated_breakeven = np.where(simulated_revenues > 0, simulated_costs / (simulated_revenues / 12), float('inf'))
            simulated_risk_adjusted = simulated_roi - (risk * 5)

            # Store results
            results["Scenario"].append(scenario)
            results["ROI"].extend(simulated_roi)
            results["Breakeven Point"].extend(simulated_breakeven)
            results["Risk-Adjusted Score"].extend(simulated_risk_adjusted)

            # Display summary statistics
            st.write(f"### {scenario} Scenario Results")
            st.write(f"- Mean ROI: {np.mean(simulated_roi):.2f}%")
            st.write(f"- Breakeven Point Range: {np.percentile(simulated_breakeven, 5):.2f} to {np.percentile(simulated_breakeven, 95):.2f} months")
            st.write(f"- Risk-Adjusted ROI Range: {np.percentile(simulated_risk_adjusted, 5):.2f}% to {np.percentile(simulated_risk_adjusted, 95):.2f}%")
        else:
            st.warning(f"Costs must be greater than zero for {scenario} to calculate metrics.")

    # Step 3: Visualization
    st.write("### Visualization")
    fig = go.Figure()
    for scenario in scenarios:
        fig.add_trace(go.Box(
            y=results["Risk-Adjusted Score"],
            name=f"{scenario} Risk-Adjusted",
            boxmean=True
        ))
    fig.update_layout(title="Risk-Adjusted Score Distribution Across Scenarios", xaxis_title="Scenarios", yaxis_title="Risk-Adjusted Score (%)")
    st.plotly_chart(fig)

    # Save Results
    st.write("### Save Results")
    if st.button("Save Scenario Results"):
        st.session_state["scenario_results"] = results
        st.success("Scenario results saved!")


import streamlit as st
import numpy as np
import plotly.express as px

def risk_adjusted_scaling():
    st.subheader("Risk-Adjusted Scaling with Monte Carlo")
    st.write("Analyze and integrate risk metrics into your scaling strategy.")

    # Step 1: Input Risk Factors
    st.write("### Step 1: Input Risk Factors")
    market_saturation = st.slider(
        "Market Saturation (%)", min_value=0, max_value=100, value=50,
        help="Percentage of the market already served by competitors."
    )
    competition_intensity = st.slider(
        "Competition Intensity (1-5)", min_value=1, max_value=5, value=3,
        help="Level of competition in the market, with 1 being low and 5 being high."
    )
    market_volatility = st.slider(
        "Market Volatility (1-5)", min_value=1, max_value=5, value=3,
        help="Market stability, with 1 being stable and 5 being highly volatile."
    )
    revenue_growth = st.number_input(
        "Projected Revenue Growth (%)", min_value=0.0, step=0.1,
        help="Expected revenue growth percentage from scaling."
    )
    scaling_costs = st.number_input(
        "Scaling Costs (\u00A3)", min_value=0.0, step=100.0,
        help="Costs associated with scaling operations."
    )

    # Step 2: Monte Carlo Simulations
    st.write("### Step 2: Monte Carlo Simulations")
    simulations = 1000

    # Simulate variability in risk factors
    simulated_market_saturation = np.random.normal(
        loc=market_saturation,
        scale=market_saturation * 0.1,
        size=simulations
    )
    simulated_competition_intensity = np.random.normal(
        loc=competition_intensity,
        scale=competition_intensity * 0.1,
        size=simulations
    )
    simulated_market_volatility = np.random.normal(
        loc=market_volatility,
        scale=market_volatility * 0.1,
        size=simulations
    )
    simulated_revenue_growth = np.random.normal(
        loc=revenue_growth,
        scale=revenue_growth * 0.1,
        size=simulations
    )
    simulated_scaling_costs = np.random.normal(
        loc=scaling_costs,
        scale=scaling_costs * 0.1,
        size=simulations
    )

    # Calculate Risk Scores and Risk-Adjusted ROI
    simulated_risk_scores = (
        simulated_market_saturation / 100
    ) * simulated_competition_intensity * simulated_market_volatility
    simulated_risk_adjusted_roi = (
        (simulated_revenue_growth - simulated_risk_scores) / simulated_scaling_costs
    ) * 100

    # Summary statistics
    mean_risk_score = np.mean(simulated_risk_scores)
    mean_risk_adjusted_roi = np.mean(simulated_risk_adjusted_roi)
    p5_risk_adjusted_roi = np.percentile(simulated_risk_adjusted_roi, 5)
    p95_risk_adjusted_roi = np.percentile(simulated_risk_adjusted_roi, 95)

    st.write(f"- **Mean Risk Score:** {mean_risk_score:.2f} (Higher = riskier)")
    st.write(f"- **Mean Risk-Adjusted ROI:** {mean_risk_adjusted_roi:.2f}%")
    st.write(f"- **Risk-Adjusted ROI Range (5th to 95th Percentile):** {p5_risk_adjusted_roi:.2f}% to {p95_risk_adjusted_roi:.2f}%")

    # Step 3: Visualizations
    st.write("### Visualizations")

    # Risk Score Distribution
    fig_risk_score = px.histogram(
        simulated_risk_scores,
        nbins=50,
        title="Risk Score Distribution",
        labels={"x": "Risk Score", "y": "Frequency"}
    )
    st.plotly_chart(fig_risk_score)

    # Risk-Adjusted ROI Distribution
    fig_risk_adjusted_roi = px.histogram(
        simulated_risk_adjusted_roi,
        nbins=50,
        title="Risk-Adjusted ROI Distribution",
        labels={"x": "Risk-Adjusted ROI (%)", "y": "Frequency"}
    )
    st.plotly_chart(fig_risk_adjusted_roi)

    # Recommendations
    st.write("### Recommendations")
    if mean_risk_adjusted_roi > 20 and mean_risk_score < 3:
        st.success("This scaling strategy appears low risk and profitable. Consider proceeding.")
    elif mean_risk_score >= 3:
        st.warning("This scaling strategy has significant risks. Consider mitigating risks before proceeding.")
    else:
        st.warning("This scaling strategy may not be profitable. Reassess your approach.")




def scaling_efficiency():
    st.subheader("Scaling Efficiency with Monte Carlo")
    st.write("Assess the efficiency and sustainability of your scaling strategy.")

    # Step 1: Input Efficiency Metrics
    st.write("### Step 1: Input Efficiency Metrics")
    revenue = st.number_input(
        "Projected Revenue (\u00A3)", min_value=0.0, step=100.0,
        help="Expected revenue after scaling."
    )
    scaling_resources = st.number_input(
        "Scaling Resources (e.g., Employees, Equipment)", min_value=1, step=1,
        help="Total number of resources used for scaling."
    )
    scaling_costs = st.number_input(
        "Scaling Costs (\u00A3)", min_value=0.0, step=100.0,
        help="Costs associated with scaling operations."
    )

    # Step 2: Monte Carlo Simulations
    st.write("### Step 2: Monte Carlo Simulations")
    simulations = 1000

    # Simulate variability in inputs
    simulated_revenue = np.random.normal(
        loc=revenue,
        scale=revenue * 0.1,
        size=simulations
    )
    simulated_scaling_resources = np.random.normal(
        loc=scaling_resources,
        scale=scaling_resources * 0.1,
        size=simulations
    )
    simulated_scaling_costs = np.random.normal(
        loc=scaling_costs,
        scale=scaling_costs * 0.1,
        size=simulations
    )

    # Calculate metrics
    simulated_revenue_per_resource = np.where(
        simulated_scaling_resources > 0,
        simulated_revenue / simulated_scaling_resources,
        0
    )
    simulated_cost_scaling_factor = np.where(
        simulated_scaling_costs > 0,
        simulated_revenue / simulated_scaling_costs,
        0
    )

    # Summary statistics
    mean_revenue_per_resource = np.mean(simulated_revenue_per_resource)
    mean_cost_scaling_factor = np.mean(simulated_cost_scaling_factor)
    p5_revenue_per_resource = np.percentile(simulated_revenue_per_resource, 5)
    p95_revenue_per_resource = np.percentile(simulated_revenue_per_resource, 95)
    p5_cost_scaling_factor = np.percentile(simulated_cost_scaling_factor, 5)
    p95_cost_scaling_factor = np.percentile(simulated_cost_scaling_factor, 95)

    st.write(f"- **Mean Revenue per Resource:** \u00A3{mean_revenue_per_resource:.2f}")
    st.write(f"- **Revenue per Resource Range (5th to 95th Percentile):** \u00A3{p5_revenue_per_resource:.2f} to \u00A3{p95_revenue_per_resource:.2f}")
    st.write(f"- **Mean Cost Scaling Factor:** {mean_cost_scaling_factor:.2f}")
    st.write(f"- **Cost Scaling Factor Range (5th to 95th Percentile):** {p5_cost_scaling_factor:.2f} to {p95_cost_scaling_factor:.2f}")

    # Step 3: Visualizations
    st.write("### Visualizations")

    # Revenue per Resource Distribution
    fig_revenue_per_resource = px.histogram(
        simulated_revenue_per_resource,
        nbins=50,
        title="Revenue per Resource Distribution",
        labels={"x": "Revenue per Resource (\u00A3)", "y": "Frequency"}
    )
    st.plotly_chart(fig_revenue_per_resource)

    # Cost Scaling Factor Distribution
    fig_cost_scaling_factor = px.histogram(
        simulated_cost_scaling_factor,
        nbins=50,
        title="Cost Scaling Factor Distribution",
        labels={"x": "Cost Scaling Factor", "y": "Frequency"}
    )
    st.plotly_chart(fig_cost_scaling_factor)

    # Recommendations
    st.write("### Recommendations")
    if mean_cost_scaling_factor > 2 and mean_revenue_per_resource > 5000:
        st.success("Your scaling strategy is efficient and sustainable. Keep scaling!")
    elif mean_cost_scaling_factor > 1:
        st.info("Your scaling strategy is acceptable, but there's room for improvement.")
    else:
        st.warning("Your scaling strategy is inefficient. Reassess your resources and costs.")



