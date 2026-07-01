import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Page configuration
st.set_page_config(
    page_title="Raisin Classification",
    page_icon="🍇",
    layout="centered"
)

# Title
st.title("🍇 Raisin Classification using Random Forest")

st.write("""
Enter the raisin measurements below and click **Predict**.
""")

# Sidebar
st.sidebar.header("About")
st.sidebar.write("""
Machine Learning Algorithm:
- Random Forest Classifier

Dataset:
- Raisin Dataset
""")

# Input fields
area = st.number_input("Area", min_value=0.0)

major_axis = st.number_input("Major Axis Length", min_value=0.0)

minor_axis = st.number_input("Minor Axis Length", min_value=0.0)

eccentricity = st.number_input(
    "Eccentricity",
    min_value=0.0,
    max_value=1.0,
    value=0.80
)

convex_area = st.number_input("Convex Area", min_value=0.0)

extent = st.number_input(
    "Extent",
    min_value=0.0,
    max_value=1.0,
    value=0.70
)

perimeter = st.number_input("Perimeter", min_value=0.0)

# Prediction button
if st.button("Predict"):

    features = np.array([[area,
                          major_axis,
                          minor_axis,
                          eccentricity,
                          convex_area,
                          extent,
                          perimeter]])

    prediction = model.predict(features)[0]

    # If your labels are encoded as 0 and 1
    if prediction == 0:
        st.success("Predicted Class: Kecimen 🍇")
    else:
        st.success("Predicted Class: Besni 🍇")
        