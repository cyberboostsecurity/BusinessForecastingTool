import streamlit as st

def risk_assessment():
    st.header("Risk Assessment")
    st.info("Identify key risks and plan for different financial scenarios.")

    sub_module = st.selectbox("Select a Sub-Module", [
        "Risk Identification", "Scenario Planning"
    ])

    # Risk Identification
    if sub_module == "Risk Identification":
        st.subheader("Risk Identification")
        st.write("Identify internal and external risks affecting your business.")

        internal_risks = st.text_area(
            "Internal Risks",
            help="List risks within your organization (e.g., staff turnover, outdated systems)."
        )
        external_risks = st.text_area(
            "External Risks",
            help="List external risks (e.g., economic downturn, new competitors)."
        )

        if st.button("Analyze Risks"):
            st.write("### Risk Summary")
            if internal_risks.strip():
                st.write("**Internal Risks:**")
                st.write(internal_risks)
            else:
                st.write("No internal risks identified.")

            if external_risks.strip():
                st.write("**External Risks:**")
                st.write(external_risks)
            else:
                st.write("No external risks identified.")

    # Scenario Planning
    elif sub_module == "Scenario Planning":
        st.subheader("Scenario Planning")
        st.write("Analyze best-case, worst-case, and likely financial outcomes.")

        revenue = st.number_input(
            "Monthly Revenue (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the current monthly revenue."
        )
        costs = st.number_input(
            "Monthly Costs (\u00A3)", min_value=0.0, step=100.0,
            help="Enter the current monthly costs."
        )
        best_case_growth = st.slider(
            "Best-Case Growth Rate (%)", min_value=0, max_value=100, value=20,
            help="Enter the expected revenue growth rate in the best-case scenario."
        )
        worst_case_reduction = st.slider(
            "Worst-Case Reduction Rate (%)", min_value=0, max_value=100, value=20,
            help="Enter the expected revenue reduction rate in the worst-case scenario."
        )

        if st.button("Calculate Scenarios"):
            # Best-case scenario
            best_case_revenue = revenue * (1 + best_case_growth / 100)
            best_case_profit = best_case_revenue - costs

            # Worst-case scenario
            worst_case_revenue = revenue * (1 - worst_case_reduction / 100)
            worst_case_profit = worst_case_revenue - costs

            # Likely scenario (average of best and worst)
            likely_revenue = (best_case_revenue + worst_case_revenue) / 2
            likely_profit = likely_revenue - costs

            # Display results
            st.write("### Scenario Outcomes")
            st.write(f"- **Best-Case Revenue:** \u00A3{best_case_revenue:.2f}, **Profit:** \u00A3{best_case_profit:.2f}")
            st.write(f"- **Worst-Case Revenue:** \u00A3{worst_case_revenue:.2f}, **Profit:** \u00A3{worst_case_profit:.2f}")
            st.write(f"- **Likely Revenue:** \u00A3{likely_revenue:.2f}, **Profit:** \u00A3{likely_profit:.2f}")

            if likely_profit < 0:
                st.warning("Likely scenario indicates a potential loss. Consider mitigating risks.")


