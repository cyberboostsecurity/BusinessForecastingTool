import streamlit as st

def growth_scaling():
    st.header("Growth & Scaling Strategy")
    st.info("Analyze market expansion, customer metrics, and partnership benefits.")

    sub_module = st.selectbox("Select a Sub-Module", [
        "Market Expansion", "Customer Metrics", "Partnership Projections"
    ])

    # Market Expansion
    if sub_module == "Market Expansion":
        st.subheader("Market Expansion")
        st.write("Analyze ROI for entering new markets.")

        target_market_costs = st.number_input(
            "Target Market Entry Costs (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the estimated costs for entering the target market."
        )
        target_market_revenue = st.number_input(
            "Expected Revenue from Target Market (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the expected revenue from the target market."
        )

        if st.button("Calculate ROI"):
            if target_market_costs > 0:
                roi = ((target_market_revenue - target_market_costs) / target_market_costs) * 100
                st.write(f"**Return on Investment (ROI):** {roi:.2f}%")
            else:
                st.warning("Entry costs must be greater than zero.")

    # Customer Metrics
    elif sub_module == "Customer Metrics":
        st.subheader("Customer Metrics")
        st.write("Calculate Customer Lifetime Value (CLV) and Customer Acquisition Cost (CAC).")

        customer_retention_rate = st.slider(
            "Customer Retention Rate (%)", min_value=0, max_value=100, value=80,
            help="Enter the percentage of customers retained annually."
        )
        customer_acquisition_cost = st.number_input(
            "Customer Acquisition Cost (CAC, \u00A3)", min_value=0.0, step=10.0,
            help="Enter the average cost of acquiring a new customer."
        )
        average_customer_revenue = st.number_input(
            "Average Revenue per Customer (\u00A3)", min_value=0.0, step=10.0,
            help="Enter the average annual revenue per customer."
        )

        if st.button("Calculate Customer Metrics"):
            clv = average_customer_revenue * (customer_retention_rate / 100)
            st.write(f"**Customer Lifetime Value (CLV):** \u00A3{clv:.2f}")
            st.write(f"**Customer Acquisition Cost (CAC):** \u00A3{customer_acquisition_cost:.2f}")

    # Partnership Projections
    elif sub_module == "Partnership Projections":
        st.subheader("Partnership Projections")
        st.write("Estimate the revenue contribution from partnerships.")

        partnership_cost = st.number_input(
            "Partnership Costs (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the cost of forming and maintaining the partnership."
        )
        partnership_benefits = st.number_input(
            "Expected Revenue from Partnerships (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the expected revenue generated from the partnership."
        )

        if st.button("Calculate Partnership ROI"):
            if partnership_cost > 0:
                partnership_roi = ((partnership_benefits - partnership_cost) / partnership_cost) * 100
                st.write(f"**Partnership ROI:** {partnership_roi:.2f}%")
            else:
                st.warning("Partnership costs must be greater than zero.")
