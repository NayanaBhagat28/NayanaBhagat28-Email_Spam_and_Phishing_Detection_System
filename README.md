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
```
Email-Spam-and-Phishing-Detection/
│
├── app.py                       # Main Streamlit application
│
├── pages/                       # Application pages
│ ├── spam_input.py              # Spam email detection page
│ ├── phishing_input.py          # Phishing email detection page
│ ├── analytics.py               # Analytics & visualization
│ └── login.py                   # User login page
│
├── model/                       # Trained machine learning models
│ ├── spam_model.pkl             # Spam detection model
│ ├── phishing_model.pkl         # Phishing detection model
│ └── vectorizer.pkl             # Text vectorizer
│
├── dataset/                    # Dataset files
│ └── emails.csv                # Email dataset
│
├── requirements.txt            # Project dependencies
├── .gitignore                  # Git ignore file
└── README.md                   # Project documentation
```

## 🛠 Technologies Used
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 🚀 Quick Start Guide

### Step 1: Install Dependencies
Install all required Python packages using:

```bash
python -m pip install -r requirements.txt
```

## Required Packages:

Streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib

### Step 2: Prepare Dataset

Ensure the following file exists in the dataset/ folder:
emails.csv – Email dataset used for spam and phishing detection

📌 The dataset contains email text used for training and testing the models.

### Step 3: Model Files

Ensure the following trained model files are present in the model/ folder:
spam_model.pkl – Spam classification model
phishing_model.pkl – Phishing detection model
vectorizer.pkl – Text vectorizer for feature extraction

⚠️ If these files are missing, the application will not run correctly.

### Step 4: Run the Application

Start the Streamlit web application using:
```bash
python -m streamlit run app.py

```
You should see the application running at:
```
http://localhost:8501
```
### Step 5: Access the Application

Open your web browser and navigate to:
```
http://localhost:8501
```
## 📖 How to Use

1. Open the application in your browser.
2. Navigate to Spam Detection or Phishing Detection.
3. Paste the email content into the text box.
4. Click the Predict button.
5. View the classification result (Spam / Phishing / Safe).

## 🎯 Use Cases

• Personal email security.

• Educational and academic projects.

• Demonstration of NLP and Machine Learning concepts.

• Awareness of phishing and cyber scams.


## 🔐 Security & Reliability

✅Uses trained ML models for prediction

✅Local execution ensures data privacy

✅No email content is stored permanently

## 👩‍💻 Author

Nayana Bhagath

## 📧 Stay alert. Stay safe from email threats.
