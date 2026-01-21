import streamlit as st
import pandas as pd
import joblib
from utils.phishing_utils import predict_phishing

# Hide sidebar
st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

def phishing_input_page():
    st.subheader("🌐 Phishing Website Detection")
    model = joblib.load("models/phishing_model.pkl")

    input_type = st.radio("Choose input type:", ["URL Text", "Upload CSV"])

    if input_type == "URL Text":
        url = st.text_input("Enter a URL:")
        if st.button("Predict"):
            prediction = predict_phishing(url, model)
            st.session_state.phishing_predictions = pd.DataFrame({
                'url': [url],
                'Prediction': [prediction]
            })
            return True

    elif input_type == "Upload CSV":
        file = st.file_uploader("Upload a CSV with a 'url' column", type=["csv"])
        if file and st.button("Predict"):
            df = pd.read_csv(file)
            if "url" in df.columns:
                df["Prediction"] = df["url"].apply(lambda x: predict_phishing(x, model))
                st.session_state.phishing_predictions = df
                return True
            else:
                st.error("CSV must contain a 'url' column.")

    return False
