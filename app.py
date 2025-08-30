
import pickle
import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open('finalmodel.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("📚 Student Performance Predictor")
st.write("Enter the student's details below to predict their Performance Index:")

# Input fields
hours_studied = st.slider("Hours Studied", min_value=0.0, max_value=24.0, value=1.0)
previous_scores = st.number_input("Previous Scores", min_value=0.0, max_value=100.0, value=50.0)
sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=12.0, value=6.0)
sample_papers = st.number_input("Sample Question Papers Practiced", min_value=0, max_value=100, value=10)
extra = st.selectbox("Extracurricular Activities", ['Yes', 'No'])
extra_binary = 1 if extra == 'Yes' else 0

# Prepare input
input_data = np.array([[hours_studied, previous_scores, sleep_hours, sample_papers, extra_binary]])
scaled_input = scaler.transform(input_data)

# Predict
if st.button("Predict Performance Index"):
    prediction = model.predict(scaled_input)
    st.success(f"Predicted Performance Index: {prediction[0]:.2f}")
