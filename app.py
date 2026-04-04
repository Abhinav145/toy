import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Page config
st.set_page_config(page_title="Placement Predictor", layout="centered")

# Title
st.title("Placement Predictor")

st.markdown("### Enter student details")

# Input fields
iq = st.number_input(
    "Enter IQ of the student",
    min_value=0.0,
    max_value=200.0,
    value=50.0,
    step=1.0
)

cgpa = st.number_input(
    "Enter CGPA of the student",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

# Predict button
if st.button("Predict"):
    # Prepare input
    input_data = np.array([[cgpa, iq]])

    # Prediction
    prediction = model.predict(input_data)

    # Output
    st.markdown("## Result:")

    if prediction[0] == 1:
        st.success("Placement Ho Jaayega 🎉")
    else:
        st.error("Placement Nahi Hoga 😢")