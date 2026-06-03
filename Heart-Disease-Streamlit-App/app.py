import streamlit as st
import joblib
import numpy as np

# ---- Load Trained Model ----
model = joblib.load("heart1model.pkl")

st.title("Heart Disease Risk Prediction App ❤️")

st.write("Provide the following details to check your heart risk:")

# ---- Numeric Input for Age ----
age = st.number_input("Age", min_value=1, max_value=120, value=30)

# ---- Yes/No Inputs for Symptoms and Risk Factors ----
def yes_no_input(label):
    return 1 if st.radio(label, ["No", "Yes"]) == "Yes" else 0

chest_pain = yes_no_input("Chest Pain")
shortness_of_breath = yes_no_input("Shortness of Breath")
fatigue = yes_no_input("Fatigue")
palpitations = yes_no_input("Palpitations")
dizziness = yes_no_input("Dizziness")
swelling = yes_no_input("Swelling (Legs/Feet/Ankles)")
pain_arms_jaw_back = yes_no_input("Pain in Arms / Jaw / Back")
cold_sweats_nausea = yes_no_input("Cold Sweats / Nausea")
high_bp = yes_no_input("High Blood Pressure")
high_cholesterol = yes_no_input("High Cholesterol")
diabetes = yes_no_input("Diabetes")
smoking = yes_no_input("Smoking")
obesity = yes_no_input("Obesity")
sedentary_lifestyle = yes_no_input("Sedentary Lifestyle")
family_history = yes_no_input("Family History of Heart Disease")
chronic_stress = yes_no_input("Chronic Stress")

# ---- Gender Input ----
gender = 1 if st.radio("Gender", ["Male", "Female"]) == "Male" else 0

# ---- Collect All Inputs in Order ----
input_data = np.array([[chest_pain, shortness_of_breath, fatigue, palpitations,
                        dizziness, swelling, pain_arms_jaw_back, cold_sweats_nausea,
                        high_bp, high_cholesterol, diabetes, smoking, obesity,
                        sedentary_lifestyle, family_history, chronic_stress,
                        gender, age]])

# ---- Prediction ----
if st.button("Predict"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")

