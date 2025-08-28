import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("weight_loss_model.pkl", "rb"))

st.title("🏋️ Personalized Fitness Predictor")

# Input fields
age = st.number_input("Enter your age", min_value=10, max_value=100, value=25)
weight = st.number_input("Enter your current weight (kg)", min_value=20, max_value=200, value=70)
height = st.number_input("Enter your height (cm)", min_value=100, max_value=220, value=170)

if st.button("Predict Weight Loss"):
    input_data = np.array([[age, weight, height]])
    prediction = model.predict(input_data)
    st.success(f"Predicted weight loss: {prediction[0]:.2f} kg")
