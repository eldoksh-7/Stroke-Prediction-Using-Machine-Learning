import streamlit as st
import joblib
import numpy as np

model = joblib.load("stroke_model.pkl")

st.title("Stroke Prediction App")

age = st.number_input("Age")
hypertension = st.number_input("Hypertension (0 or 1)")
heart_disease = st.number_input("Heart Disease (0 or 1)")
avg_glucose_level = st.number_input("Avg Glucose Level")
bmi = st.number_input("BMI")
risk_score = st.number_input("Risk Score")

if st.button("Predict"):
    data = np.array([[age, hypertension, heart_disease,
                      avg_glucose_level, bmi, risk_score]])

    result = model.predict(data)

    if result[0] == 1:
        st.error("High Risk of Stroke ⚠️")
    else:
        st.success("Low Risk of Stroke ✅")