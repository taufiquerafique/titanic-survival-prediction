import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢",
    layout="wide"
)

# -----------------------------
# Load Model & Metadata
# -----------------------------
model = joblib.load("models/logistic-model.pkl")
metadata = joblib.load("models/metadata.pkl")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🚢 Titanic Survival Predictor")

st.sidebar.info(
    """
Predict whether a passenger would survive
based on passenger information.

Model: Logistic Regression
"""
)

st.sidebar.success(
    f"Model Accuracy: {metadata['accuracy']*100:.2f}%"
)

# -----------------------------
# Title
# -----------------------------
st.title("🚢 Titanic Survival Prediction")

st.write(
    "Enter passenger details and click **Predict**."
)

# -----------------------------
# Layout
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    st.subheader("Passenger Details")

    pclass = st.selectbox(
        "Passenger Class",
        [1, 2, 3]
    )

    sex = st.selectbox(
        "Sex",
        ["Male", "Female"]
    )

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=100,
        value=25
    )

    fare = st.number_input(
        "Fare",
        min_value=0.0,
        value=20.0
    )

    embarked = st.selectbox(
        "Embarked",
        ["C", "Q", "S"]
    )

    predict = st.button(
        "🚀 Predict"
    )

# -----------------------------
# Prediction
# -----------------------------
with col2:

    st.subheader("Prediction")

    if predict:

        sex = 1 if sex == "Female" else 0

        embarked_q = 1 if embarked == "Q" else 0
        embarked_s = 1 if embarked == "S" else 0

        input_df = pd.DataFrame({
            "Pclass": [pclass],
            "Sex": [sex],
            "Age": [age],
            "Fare": [fare],
            "Embarked_Q": [embarked_q],
            "Embarked_S": [embarked_s]
        })

        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0]

        if prediction == 1:
            st.success("✅ Passenger is likely to Survive")
        else:
            st.error("❌ Passenger is unlikely to Survive")

        st.subheader("Prediction Probability")

        st.write(
            f"Survive: **{probability[1]*100:.2f}%**"
        )

        st.progress(float(probability[1]))

        st.write(
            f"Not Survive: **{probability[0]*100:.2f}%**"
        )