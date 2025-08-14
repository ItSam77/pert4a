import streamlit as st
import pandas as pd
import pickle
import os
import joblib

# Load the trained model
@st.cache_resource
def load_model():
    model_path = 'attrition_prediction_model.pkl'
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file '{model_path}' not found. Please ensure the model file exists.")
    
    try:
        # Try joblib first (preferred for PyCaret models)
        return joblib.load(model_path)
    except Exception as joblib_error:
        try:
            # Fallback to pickle
            with open(model_path, 'rb') as file:
                return pickle.load(file)
        except Exception as pickle_error:
            raise RuntimeError(f"Failed to load model. Joblib error: {joblib_error}. Pickle error: {pickle_error}")

def main():
    st.title("Employee Attrition Prediction")
    st.write("Predict whether an employee will leave the company based on their characteristics.")
    
    try:
        # Load the model
        model = load_model()
        
        # Create input fields
        st.header("Employee Information")
        
        # Age input
        age = st.slider("Age", min_value=10, max_value=80, value=30)
        
        # Monthly Income input
        monthly_income = st.number_input("Monthly Income", min_value=0, value=5000, step=100)
        
        # Years at Company input
        years_at_company = st.slider("Years at Company", min_value=0, max_value=50, value=5)
        
        # Job Satisfaction input
        job_satisfaction = st.slider("Job Satisfaction", min_value=0, max_value=5, value=3)
        
        # Marital Status input
        marital_status_options = {
            "Single": 0,
            "Married": 1,
            "Divorced": 2
        }
        marital_status_text = st.selectbox("Marital Status", list(marital_status_options.keys()))
        marital_status = marital_status_options[marital_status_text]
        
        # Predict button
        predict_button = st.button("Predict Attrition")
        
        if predict_button:
            # Create input DataFrame with expected column names for the PyCaret pipeline
            input_df = pd.DataFrame([
                {
                    'Age': int(age),
                    'MonthlyIncome': int(monthly_income),
                    'YearsAtCompany': int(years_at_company),
                    'JobSatisfaction': int(job_satisfaction),
                    'MaritalStatus': int(marital_status),
                }
            ])

            # Make prediction
            prediction = model.predict(input_df)[0]
            prediction_proba = model.predict_proba(input_df)[0]

            # Get probability of leaving (class 1)
            prob_leaving = prediction_proba[1] if len(prediction_proba) > 1 else 0.5
            
            # Display results
            st.header("Prediction Results")
            
            if prediction == 1:
                st.error("🚨 High Risk: Employee is likely to leave")
            else:
                st.success("✅ Low Risk: Employee is likely to stay")
            
            # Show probability of leaving
            st.write(f"Probability of leaving: {prob_leaving:.1%}")
            
            # Display input summary
            st.subheader("Input Summary")
            st.write(f"**Age:** {age}")
            st.write(f"**Monthly Income:** ${monthly_income:,}")
            st.write(f"**Years at Company:** {years_at_company}")
            st.write(f"**Job Satisfaction:** {job_satisfaction}")
            st.write(f"**Marital Status:** {marital_status_text}")
    
    except Exception as e:
        st.error(f"Error loading model or making prediction: {str(e)}")
        st.error("Please ensure 'attrition_prediction_model.pkl' exists in the same directory.")

if __name__ == "__main__":
    main()
