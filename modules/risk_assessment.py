import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # Ensure this import is included
from modules.db_utils import save_risk_data, clear_data



def risk_assessment():
    st.header("Risk Assessment Tool")
    st.info("Evaluate and prioritize risks for your business.")

    # Step 1: Define Risks
    st.write("### Step 1: Define Risks")
    predefined_risks = {
        "Market Misalignment": 40,
        "Team Skill Gaps": 60,
        "Cash Flow Problems": 70,
        "Customer Churn": 50,
        "Regulatory Compliance": 30,
        "Supply Chain Disruption": 45,
        "Data Breach": 75,
        "Competitor Actions": 50,
        "Economic Downturn": 55,
        "Technology Failure": 65,
    }
    risk_data = []

    # Custom Risk Addition
    custom_risk = st.text_input("Add a Custom Risk", placeholder="Enter a custom risk name...")
    if custom_risk:
        predefined_risks[custom_risk] = 50  # Default likelihood for custom risks

    selected_risks = st.multiselect(
        "Select Risks to Assess",
        options=list(predefined_risks.keys()),
        default=list(predefined_risks.keys())
    )

    # Step 2: Input Likelihood, Impact, and Mitigation
    st.write("### Step 2: Input Likelihood, Impact, and Mitigation")
    for risk in selected_risks:
        st.subheader(risk)
        likelihood = st.slider(
            f"Likelihood of {risk} (%)",
            min_value=0,
            max_value=100,
            value=predefined_risks[risk]
        ) / 100
        min_impact = st.number_input(
            f"Minimum Impact (£) for {risk}",
            min_value=0.0,
            value=1000.0,
            step=100.0
        )
        most_likely_impact = st.number_input(
            f"Most Likely Impact (£) for {risk}",
            min_value=0.0,
            value=5000.0,
            step=100.0
        )
        max_impact = st.number_input(
            f"Maximum Impact (£) for {risk}",
            min_value=0.0,
            value=10000.0,
            step=100.0
        )
        mitigation_effectiveness = st.slider(
            f"Mitigation Effectiveness for {risk} (%)",
            min_value=0,
            max_value=100,
            value=50
        ) / 100
        mitigation_cost = st.number_input(
            f"Mitigation Cost (£) for {risk}",
            min_value=0.0,
            value=0.0,
            step=100.0
        )

        # Risk Score Calculation
        adjusted_impact = ((min_impact + (4 * most_likely_impact) + max_impact) / 6) * (1 - mitigation_effectiveness)
        risk_score = likelihood * adjusted_impact - mitigation_cost
        risk_data.append({
            "Risk": risk,
            "Likelihood (%)": likelihood * 100,
            "Adjusted Impact (£)": adjusted_impact,
            "Mitigation Cost (£)": mitigation_cost,
            "Risk Score": risk_score
        })

    # Convert data to DataFrame for better visualization
    df = pd.DataFrame(risk_data)

    # Step 3: Display Risk Scores
    st.write("### Step 3: Risk Scores and Prioritization")
    if not df.empty:
        st.write(df.sort_values(by="Risk Score", ascending=False))

        # Step 4: Visualization (Bar Chart)
        st.write("### Step 4: Risk Bar Chart")
        fig, ax = plt.subplots(figsize=(10, 6))  # This line should work now after importing matplotlib.pyplot
        df_sorted = df.sort_values(by="Risk Score", ascending=False)
        ax.barh(df_sorted["Risk"], df_sorted["Risk Score"], color='skyblue')
        ax.set_xlabel("Risk Score")
        ax.set_title("Risk Prioritization")
        st.pyplot(fig)

        # Step 5: Overall Risk Score
        overall_risk_score = np.mean(df["Risk Score"])
        st.write("### Step 5: Overall Risk Score")
        st.metric(label="Overall Risk Score", value=f"{overall_risk_score:.2f}")

        # Gauge-style visualization using a horizontal bar
        fig, ax = plt.subplots(figsize=(8, 2))
        ax.barh(["Overall Risk"], [overall_risk_score], color="orange")
        ax.set_xlim(0, 10)  # Assuming max score is 10
        ax.set_title("Overall Risk Score")
        st.pyplot(fig)

        # Top Risks
        st.write("### Top 3 Risks Contributing to Overall Risk")
        st.write(df_sorted.head(3))

    # Export to Database Button
    if st.button("Export to Other Modules"):
        risk_db_data = [
            (row["Risk"], row["Likelihood (%)"], row["Adjusted Impact (£)"], row["Mitigation Cost (£)"], row["Risk Score"])
            for _, row in df.iterrows()
        ]
        save_risk_data(risk_db_data)  # Save to database
        st.success("Risk data exported to the database!")

    # Clear Database Button
    if st.button("Clear Risk Data"):
        clear_data("risk_data")
        st.success("Risk data cleared from the database!")

    # Option to Download Results
    st.write("### Download Results")
    st.download_button(
        label="Download Risk Data as CSV",
        data=df.to_csv(index=False),
        file_name="risk_assessment.csv",
        mime="text/csv"
    )
