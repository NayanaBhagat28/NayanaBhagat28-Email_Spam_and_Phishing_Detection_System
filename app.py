import streamlit as st
from pages.spam_input import spam_input_page
from pages.phishing_input import phishing_input_page
from pages.analytics import analytics_page

# =======================
# Initialize Session State
# =======================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'page' not in st.session_state:
    st.session_state.page = "login"  # Changed from "home" to "login"
if 'input_done' not in st.session_state:
    st.session_state.input_done = False
if 'prediction_type' not in st.session_state:
    st.session_state.prediction_type = None


# =======================
# Hide Sidebar Everywhere & Set Background
# =======================
st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="collapsedControl"] {
            display: none !important;
        }

        .stApp {
            background-color: #FFFF00;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }

        .login-box {
            background-color: rgba(255, 255, 255, 0.95);
            padding: 50px 40px;
            border-radius: 12px;
            max-width: 400px;
            margin: 150px auto;
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.3);
        }

        .main-title {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            color: #004aad;
            margin-bottom: 25px;
        }
    </style>
""", unsafe_allow_html=True)

# =======================
# Login Page
# =======================
def login():
    st.markdown("""
        <style>
            body {
                background-color: #2c3e50;
            }
            .login-box {
                margin: 100px auto;
                width: 350px;
                padding: 40px;
                background: #fff;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
                text-align: center;
            }
            .login-title {
                font-size: 30px;
                font-weight: bold;
                margin-bottom: 25px;
                color: #333;
                align:center;
            }
            .input-icon {
                position: absolute;
                font-size: 20px;
                padding: 10px;
                pointer-events: none;
                color: #004aad;
            }
            .stTextInput>div>div>input {
                padding-left: 40px;
            }
            .stTextInput {
                position: relative;
                margin-bottom: 20px;
            }
            .stButton>button {
                width: 100%;
                background-color: #004aad;
                color: white;
                font-weight: bold;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
        </style>
    """, unsafe_allow_html=True)

   
    st.markdown("<h1 class='main-title'>Email Spam & Phishing Detection</h1>", unsafe_allow_html=True)
    
    st.markdown('<div class="login-title">Login</div>', unsafe_allow_html=True)
    st.markdown('<div class="input-icon">👤</div>', unsafe_allow_html=True)
    username = st.text_input("Username", key="username")

    st.markdown('<div class="input-icon">🔒</div>', unsafe_allow_html=True)
    password = st.text_input("Password", type="password", key="password")

    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state.logged_in = True
            st.session_state.page = "home"
        else:
            st.error("Incorrect username or password")

    st.markdown('</div>', unsafe_allow_html=True)


# =======================
# Feature Selection Page
# =======================
def feature_selection():
    st.markdown("## Select a Feature")
    col1, col2, col3 = st.columns(3)
    with col2:
        choice = st.radio("What would you like to do?", [
            "Spam Email Detection",
            "Phishing Website Detection"])

        if st.button("Continue"):
            if choice == "Spam Email Detection":
                st.session_state.page = "spam_input"
            elif choice == "Phishing Website Detection":
                st.session_state.page = "phishing_input"

# =======================
# Page Routing Logic
# =======================
if not st.session_state.logged_in:
    login()

elif st.session_state.page == "home":
    feature_selection()

elif st.session_state.page == "spam_input":
    if st.button("⬅ Back", key="back_from_spam"):
        st.session_state.page = "home"
    else:
        if spam_input_page():
            st.session_state.input_done = True
            st.session_state.prediction_type = "spam"
            st.session_state.page = "analytics"

elif st.session_state.page == "phishing_input":
    if st.button("⬅ Back", key="back_from_phishing"):
        st.session_state.page = "home"
    else:
        if phishing_input_page():
            st.session_state.input_done = True
            st.session_state.prediction_type = "phishing"
            st.session_state.page = "analytics"

elif st.session_state.page == "analytics":
    if st.button("⬅ Back to Input", key="back_from_analytics"):
        if st.session_state.prediction_type == "spam":
            st.session_state.page = "spam_input"
        elif st.session_state.prediction_type == "phishing":
            st.session_state.page = "phishing_input"
    else:
        analytics_page()
