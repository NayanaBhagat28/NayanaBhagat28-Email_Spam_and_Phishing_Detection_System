import streamlit as st
import pandas as pd
import joblib
from utils.spam_utils import predict_spam

# Hide sidebar
st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

def spam_input_page():
    st.subheader("📧 Spam Email Detection")
    model = joblib.load("models/spam_model.pkl")

    input_type = st.radio("Choose input type:", ["Text", "Upload CSV"])

    if input_type == "Text":
        text = st.text_area("Enter email content:")
        if st.button("Predict"):
            prediction = predict_spam(text, model)
            st.session_state.spam_predictions = pd.DataFrame({
                'text': [text],
                'Prediction': [prediction]
            })
            return True

    elif input_type == "Upload CSV":
        file = st.file_uploader("Upload a CSV file with a 'text' column", type=["csv"])
        if file and st.button("Predict"):
            try:
                df = pd.read_csv(file, encoding='latin1')  # ✅ Encoding fix added here
                if "text" in df.columns:
                    df["Prediction"] = df["text"].apply(lambda x: predict_spam(x, model))
                    st.session_state.spam_predictions = df
                    return True
                else:
                    st.error("CSV must contain a 'text' column.")
            except Exception as e:
                st.error(f"Error reading file: {e}")

    return False
