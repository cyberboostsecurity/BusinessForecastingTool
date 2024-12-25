import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

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

    # Step 2: Input Likelihood and Impact
    st.write("### Step 2: Input Likelihood and Impact")
    for risk in selected_risks:
        st.subheader(risk)
        likelihood = st.slider(
            f"Likelihood of {risk} (%)", 
            min_value=0, 
            max_value=100, 
            value=predefined_risks[risk]
        ) / 100
        impact = st.number_input(
            f"Impact of {risk} (Numerical Value, e.g., 1 for Low, 2 for Medium, 3 for High)", 
            min_value=1, 
            max_value=5, 
            value=3
        )
        risk_score = likelihood * impact
        risk_data.append({"Risk": risk, "Likelihood (%)": likelihood * 100, "Impact": impact, "Risk Score": risk_score})

    # Convert data to DataFrame for better visualization
    df = pd.DataFrame(risk_data)

    # Step 3: Display Risk Scores
    st.write("### Step 3: Risk Scores and Prioritization")
    st.write(df.sort_values(by="Risk Score", ascending=False))

    # Step 4: Visualization (Bar Chart)
    st.write("### Step 4: Risk Bar Chart")
    fig, ax = plt.subplots(figsize=(10, 6))
    df_sorted = df.sort_values(by="Risk Score", ascending=False)
    ax.barh(df_sorted["Risk"], df_sorted["Risk Score"], color='skyblue')
    ax.set_xlabel("Risk Score")
    ax.set_title("Risk Prioritization")
    st.pyplot(fig)

    # Step 5: Overall Risk Score
    if not df.empty:
        overall_risk_score = df["Risk Score"].mean()
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

    # Option to Download Results
    st.write("### Download Results")
    st.download_button(
        label="Download Risk Data as CSV",
        data=df.to_csv(index=False),
        file_name="risk_assessment.csv",
        mime="text/csv"
    )
