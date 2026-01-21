import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.spam_utils import predict_spam, load_spam_model

def spam_detection_page():
    st.header("📧 Spam Email Detection")
    model = load_spam_model()

    file = st.file_uploader("Upload CSV (must have 'text' column)", type="csv")
    
    if file:
        df = pd.read_csv(file)
        if "text" not in df.columns:
            st.error("File must contain a 'text' column.")
            return

        df["Prediction"] = df["text"].apply(lambda x: predict_spam(x, model))
        st.dataframe(df)

        counts = df["Prediction"].value_counts()
        st.write("Prediction counts:", counts)

        st.subheader("📊 Bar Chart")
        st.bar_chart(counts)

        st.subheader("🥧 Pie Chart")
        fig, ax = plt.subplots()
        ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
