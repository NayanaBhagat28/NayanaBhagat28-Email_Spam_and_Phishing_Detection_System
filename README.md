# 📧 Email Spam and Phishing Detection System

**Machine Learning based Email Security Application using Python & Streamlit**

---

## 🌟 Overview
The **Email Spam and Phishing Detection System** is a machine learning powered web application
designed to identify and classify emails as **Spam**, **Phishing**, or **Safe**.
It helps users protect themselves from malicious emails and online scams.

---

## ✨ Key Features

### 📩 Email Spam Detection
- Detects unwanted and promotional spam emails
- Uses trained machine learning models for accurate classification
- Real-time prediction based on email content

### 🎣 Phishing Email Detection
- Identifies phishing attempts and malicious email content
- Protects users from fake links and credential theft
- High accuracy using NLP-based feature extraction

### 🌐 Interactive Web Application
- User-friendly interface built with Streamlit
- Instant predictions with confidence scores
- Clean and responsive design

### 📊 Analytics & Visualization
- Visual representation of prediction results
- Model performance insights
- Confusion matrix and accuracy metrics

---

## 🏗️ Project Structure

Email-Spam-and-Phishing-Detection/
├── app.py
├── pages/
│ ├── spam_input.py
│ ├── phishing_input.py
│ ├── analytics.py
│ └── login.py
├── model/
│ ├── spam_model.pkl
│ ├── phishing_model.pkl
│ └── vectorizer.pkl
├── dataset/
│ └── emails.csv
├── requirements.txt
├── .gitignore
└── README.md

## 🛠 Technologies Used
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 🚀 Installation & Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt

Step 2: Run the Application
streamlit run app.py


The application will start at:

http://localhost:8501

📖 How to Use

Open the application in your browser

Navigate to Spam Detection or Phishing Detection

Paste the email content into the text box

Click Predict

View the classification result (Spam / Phishing / Safe)

🎯 Use Cases

Personal email security

Educational and academic projects

Demonstration of NLP & ML concepts

Awareness of phishing and cyber scams

🔐 Security & Reliability

Uses trained ML models for prediction

Local execution ensures data privacy

No email content is stored permanently

👩‍💻 Author

Nayana Bhagath

📧 Stay alert. Stay safe from email threats.
