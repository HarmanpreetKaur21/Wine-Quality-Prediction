import streamlit as st
import numpy as np
import pickle

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the input fields for the features and their ranges
feature_names = [
    'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
    'pH', 'sulphates', 'alcohol'
]

feature_ranges = {
    'fixed acidity': '4.0 - 15.0 g/dm³',
    'volatile acidity': '0.1 - 1.5 g/dm³',
    'citric acid': '0.0 - 1.0 g/dm³',
    'residual sugar': '0.6 - 20.0 g/dm³',
    'chlorides': '0.01 - 0.2 g/dm³',
    'free sulfur dioxide': '1 - 72 mg/dm³',
    'total sulfur dioxide': '6 - 350 mg/dm³',
    'density': '0.990 - 1.003 g/cm³',
    'pH': '2.8 - 4.0',
    'sulphates': '0.2 - 1.0 g/dm³',
    'alcohol': '8.0 - 15.0 % (v/v)'
}

st.title("Wine Quality Prediction")

# Create input fields for each feature
input_values = []
for feature in feature_names:
    value = st.text_input(f"Enter {feature} ({feature_ranges[feature]}):", value="0.0")
    try:
        value = float(value)
    except ValueError:
        st.error(f"Invalid input for {feature}. Please enter a valid float.")
    input_values.append(value)

if st.button("Predict"):
    # Check if any value is not float
    if any(not isinstance(val, float) for val in input_values):
        st.error("All inputs must be valid floats.")
    else:
        # Show a processing circle
        with st.spinner('Predicting...'):
            # Convert input values to a numpy array and reshape for the model
            input_array = np.array(input_values).reshape(1, -1)
            
            # Predict using the model
            prediction = model.predict(input_array)
            
            # Display the result
            st.success(f"The predicted quality of the wine is: {prediction[0]:.2f}")
