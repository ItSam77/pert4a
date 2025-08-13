import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the trained model
@st.cache_resource
def load_model():
    with open('decision_tree_attrition.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def main():
    st.title("Employee Attrition Prediction")
    st.write("Predict whether an employee will leave the company based on their characteristics.")
    
    # Load the model
    model = load_model()
    
    # Create input fields
    st.header("Employee Information")
    
    # Age input (18-60)
    age = st.slider("Age", min_value=18, max_value=60, value=30)
    
    # Monthly Income input
    monthly_income = st.number_input("Monthly Income", min_value=0, value=5000, step=100)
    
    # Marital Status input
    marital_status_options = {
        "Single": 0,
        "Married": 1,
        "Divorced": 2
    }
    marital_status_text = st.selectbox("Marital Status", list(marital_status_options.keys()))
    marital_status = marital_status_options[marital_status_text]
    
    # Predict button
    if st.button("Predict Attrition"):
        # Create input array for prediction
        input_data = np.array([[age, monthly_income, marital_status]])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        prediction_proba = model.predict_proba(input_data)[0]
        
        # Display results
        st.header("Prediction Results")
        
        if prediction == 1:  # Assuming 1 means "Yes" for attrition
            st.error("🚨 High Risk: Employee is likely to leave")
            st.write(f"Probability of leaving: {prediction_proba[1]:.2%}")
        else:
            st.success("✅ Low Risk: Employee is likely to stay")
            st.write(f"Probability of staying: {prediction_proba[0]:.2%}")
        
        # Display input summary
        st.subheader("Input Summary")
        st.write(f"**Age:** {age}")
        st.write(f"**Monthly Income:** ${monthly_income:,}")
        st.write(f"**Marital Status:** {marital_status_text}")

if __name__ == "__main__":
    main()
