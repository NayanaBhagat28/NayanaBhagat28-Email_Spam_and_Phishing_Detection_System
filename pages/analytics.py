import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from reports.report_generator import generate_spam_report, generate_phishing_report

def analytics_page():
    st.title("📊 Prediction Results & Analysis")

    prediction_type = st.session_state.get("prediction_type")

    # ---------- SPAM ANALYTICS ----------
    if prediction_type == "spam":
        data = st.session_state.get("spam_predictions")

        if data is not None and not data.empty:
            st.subheader("📋 Spam Report")

            texts = data["text"].astype(str).tolist()
            predictions = data["Prediction"].astype(str).tolist()
            true_labels = data.get("TrueLabel", predictions)  # fallback if no true labels

            generate_spam_report(texts, predictions)

            # Pie chart
            st.subheader("📈 Spam Prediction Distribution")
            pie_data = data["Prediction"].value_counts()
            fig1, ax1 = plt.subplots()
            ax1.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=90)
            ax1.axis("equal")
            st.pyplot(fig1)

            # Bar chart
            st.subheader("📊 Spam Prediction Count")
            fig2, ax2 = plt.subplots()
            pie_data.plot(kind="bar", ax=ax2)
            ax2.set_xlabel("Prediction")
            ax2.set_ylabel("Count")
            st.pyplot(fig2)

            # Confusion matrix and metrics
            if "TrueLabel" in data.columns:
                st.subheader("🧮 Spam Confusion Matrix")
                cm = confusion_matrix(true_labels, predictions, labels=list(pie_data.index))
                fig3, ax3 = plt.subplots()
                sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", 
                            xticklabels=pie_data.index, yticklabels=pie_data.index, ax=ax3)
                ax3.set_xlabel("Predicted")
                ax3.set_ylabel("Actual")
                st.pyplot(fig3)

                # Metrics
                st.subheader("📊 Spam Performance Metrics")
                accuracy = accuracy_score(true_labels, predictions)
                precision = precision_score(true_labels, predictions, average='weighted', zero_division=0)
                recall = recall_score(true_labels, predictions, average='weighted', zero_division=0)
                f1 = f1_score(true_labels, predictions, average='weighted', zero_division=0)

                st.write(f"**Accuracy:** {accuracy:.2f}")
                st.write(f"**Precision:** {precision:.2f}")
                st.write(f"**Recall:** {recall:.2f}")
                st.write(f"**F1-Score:** {f1:.2f}")

            else:
                st.info("No ground truth labels available for metrics and confusion matrix.")

        else:
            st.warning("No spam prediction data found.")

    # ---------- PHISHING ANALYTICS ----------
    elif prediction_type == "phishing":
        data = st.session_state.get("phishing_predictions")

        if data is not None and not data.empty:
            st.subheader("📋 Phishing Report")

            urls = data["url"].astype(str).tolist()
            predictions = data["Prediction"].astype(str).tolist()
            true_labels = data.get("TrueLabel", predictions)

            generate_phishing_report(urls, predictions)

            # Pie chart
            st.subheader("📈 Phishing Prediction Distribution")
            pie_data = data["Prediction"].value_counts()
            fig1, ax1 = plt.subplots()
            ax1.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=90)
            ax1.axis("equal")
            st.pyplot(fig1)

            # Bar chart
            st.subheader("📊 Phishing Prediction Count")
            fig2, ax2 = plt.subplots()
            pie_data.plot(kind="bar", ax=ax2)
            ax2.set_xlabel("Prediction")
            ax2.set_ylabel("Count")
            st.pyplot(fig2)

            # Confusion matrix and metrics
            if "TrueLabel" in data.columns:
                st.subheader("🧮 Phishing Confusion Matrix")
                cm = confusion_matrix(true_labels, predictions, labels=list(pie_data.index))
                fig3, ax3 = plt.subplots()
                sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", 
                            xticklabels=pie_data.index, yticklabels=pie_data.index, ax=ax3)
                ax3.set_xlabel("Predicted")
                ax3.set_ylabel("Actual")
                st.pyplot(fig3)

                # Metrics
                st.subheader("📊 Phishing Performance Metrics")
                accuracy = accuracy_score(true_labels, predictions)
                precision = precision_score(true_labels, predictions, average='weighted', zero_division=0)
                recall = recall_score(true_labels, predictions, average='weighted', zero_division=0)
                f1 = f1_score(true_labels, predictions, average='weighted', zero_division=0)

                st.write(f"**Accuracy:** {accuracy:.2f}")
                st.write(f"**Precision:** {precision:.2f}")
                st.write(f"**Recall:** {recall:.2f}")
                st.write(f"**F1-Score:** {f1:.2f}")

            else:
                st.info("No ground truth labels available for metrics and confusion matrix.")

        else:
            st.warning("No phishing prediction data found.")

    else:
        st.info("Please complete a prediction first.")
