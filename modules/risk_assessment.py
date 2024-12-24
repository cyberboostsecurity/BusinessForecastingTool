import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Help Menu for Risk Assessment
def risk_guide():
    st.header("Risk Assessment Guide")
    st.info("Learn how to use the Risk Assessment Tool effectively.")
    st.write("""
    ### About the Risk Assessment Tool
    This tool helps businesses identify, evaluate, and visualize risks based on their likelihood and impact.

    ### How to Use
    1. Select risks from predefined categories or add custom risks.
    2. Input likelihood as a percentage (0-100%).
    3. Define impact using Low (1), Medium (2), or High (3), or provide a numerical value.
    4. View results as a risk score and on a heatmap.

    ### Outputs
    - **Risk Score**: Calculated as Likelihood × Impact.
    - **Heatmap**: Visualize risks by likelihood and impact.
    - **Priority List**: Focus on high-priority risks for mitigation.

    ### Example Risks
    - **Market Misalignment**: Poor product-market fit.
    - **Cash Flow Problems**: Inconsistent cash flow.
    - **Team Skill Gaps**: Lack of qualified personnel.
    """)

# Risk Assessment Functionality
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

    # Step 4: Visualization (Heatmap)
    st.write("### Step 4: Risk Heatmap")
    fig, ax = plt.subplots()
    scatter = ax.scatter(df["Likelihood (%)"], df["Impact"], s=df["Risk Score"] * 20, alpha=0.6, c=df["Risk Score"], cmap="viridis")
    for i, row in df.iterrows():
        ax.text(row["Likelihood (%)"], row["Impact"], row["Risk"], fontsize=8)
    ax.set_title("Risk Heatmap")
    ax.set_xlabel("Likelihood (%)")
    ax.set_ylabel("Impact")
    fig.colorbar(scatter, label="Risk Score")
    st.pyplot(fig)

    # Option to Download Results
    st.write("### Download Results")
    st.download_button(
        label="Download Risk Data as CSV",
        data=df.to_csv(index=False),
        file_name="risk_assessment.csv",
        mime="text/csv"
    )

# Main Streamlit App Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.selectbox("Choose a Module", ["Help (Risk Guide)", "Risk Assessment"])

if menu == "Help (Risk Guide)":
    risk_guide()
elif menu == "Risk Assessment":
    risk_assessment()
