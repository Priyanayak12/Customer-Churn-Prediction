import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("customer_churn_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊"
)

# Application title
st.title("Customer Churn Prediction")

st.write(
    "Enter customer details to predict whether "
    "the customer is likely to leave."
)

# Customer details
tenure = st.number_input(
    "Tenure (Months)", min_value=0, max_value=72, value=12
)

monthly_charges = st.number_input(
    "Monthly Charges", min_value=0.0, value=70.0
)

total_charges = st.number_input(
    "Total Charges", min_value=0.0, value=840.0
)

senior_citizen = st.selectbox(
    "Senior Citizen", [0, 1]
)

gender = st.selectbox("Gender", ["Male", "Female"])

partner = st.selectbox("Partner", ["Yes", "No"])

dependents = st.selectbox("Dependents", ["Yes", "No"])

phone_service = st.selectbox("Phone Service", ["Yes", "No"])

multiple_lines = st.selectbox(
    "Multiple Lines", ["Yes", "No", "No phone service"]
)

internet_service = st.selectbox(
    "Internet Service", ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security", ["Yes", "No", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup", ["Yes", "No", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection", ["Yes", "No", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support", ["Yes", "No", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV", ["Yes", "No", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies", ["Yes", "No", "No internet service"]
)

contract = st.selectbox(
    "Contract", ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.selectbox(
    "Paperless Billing", ["Yes", "No"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

# Prediction button
if st.button("Predict Churn"):

    customer = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }])

    prediction = model.predict(customer)[0]

    probability = model.predict_proba(customer)[0][1]

    if prediction == 1:
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is likely to stay.")

    st.write(
        f"Churn Probability: {probability * 100:.2f}%"
    )