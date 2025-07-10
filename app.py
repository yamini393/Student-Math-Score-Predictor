import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

st.title("🎓 Student Math Score Predictor")

# Collect user input
gender = st.selectbox("Gender", ['male', 'female'])
race = st.selectbox("Race/Ethnicity", ['group A', 'group B', 'group C', 'group D', 'group E'])
parent_edu = st.selectbox("Parental Level of Education", [
    "some high school", "high school", "some college", 
    "associate's degree", "bachelor's degree", "master's degree"
])
lunch = st.selectbox("Lunch", ['standard', 'free/reduced'])
prep = st.selectbox("Test Preparation Course", ['none', 'completed'])

# Encode input same as training
gender = 1 if gender == 'male' else 0
race = {'group A': 0, 'group B': 1, 'group C': 2, 'group D': 3, 'group E': 4}[race]
parent_edu = {
    "some high school": 5, "high school": 3, "some college": 4,
    "associate's degree": 0, "bachelor's degree": 1, "master's degree": 2
}[parent_edu]
lunch = 1 if lunch == 'standard' else 0
prep = 1 if prep == 'completed' else 0

# Predict
if st.button("Predict Math Score"):
    input_data = np.array([[gender, race, parent_edu, lunch, prep]])
    prediction = model.predict(input_data)[0]
    st.success(f"📊 Predicted Math Score: {int(prediction)} / 100")
