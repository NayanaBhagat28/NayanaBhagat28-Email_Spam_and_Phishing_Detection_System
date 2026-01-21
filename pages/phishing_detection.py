import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.phishing_utils import predict_phishing, load_phishing_model
from reports.report_generator import generate_phishing_report

def phishing_detection_page():
    st.header("🌐 Phishing Website Detection")
    model = load_phishing_model()

    input_type = st.radio("Input type:", ["Text", "Upload CSV"])

    if input_type == "Text":
        url = st.text_input("Enter URL:")
        if st.button("Check URL"):
            prediction = predict_phishing(url, model)
            st.success(f"Prediction: {prediction}")
            generate_phishing_report(url, prediction)

    else:
        file = st.file_uploader("Upload CSV", type=["csv", "txt", "xlsx"])
        if file and st.button("Check URLs"):
            try:
                df = pd.read_csv(file)
                if "url" not in df.columns:
                    st.error("Uploaded file must contain a 'url' column.")
                    return

                df["Prediction"] = df["url"].apply(lambda x: predict_phishing(x, model))
                st.dataframe(df)

                # Count predictions
                counts = df["Prediction"].value_counts()

                # 📊 Bar Chart
                st.subheader("📊 Phishing Detection - Bar Chart")
                st.bar_chart(counts)

                # 🥧 Pie Chart
                st.subheader("📈 Phishing Detection - Pie Chart")
                fig, ax = plt.subplots()
                ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
                ax.axis('equal')
                st.pyplot(fig)

            except Exception as e:
                st.error(f"Failed to process file: {e}")
