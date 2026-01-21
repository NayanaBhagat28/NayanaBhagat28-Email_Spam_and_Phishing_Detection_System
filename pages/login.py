import streamlit as st

def login_page():
    st.set_page_config(page_title="Login", layout="centered")

    # Custom CSS for background and login box
    st.markdown("""
        <style>
        .stApp {
            background-image: url('https://img.freepik.com/free-vector/cyber-security-concept_23-2148532223.jpg');
            background-size: cover;
            background-position: center;
        }

        .login-box {
            background-color: rgba(255, 255, 255, 0.97);
            padding: 40px;
            border-radius: 10px;
            border: 2px solid black;
            width: 400px;
            margin: 100px auto;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
            text-align: center;
        }

        .login-title {
            font-size: 26px;
            font-weight: bold;
            color: #004aad;
            margin-bottom: 8px;
        }

        .login-subtitle {
            font-size: 18px;
            color: black;
            margin-bottom: 25px;
        }

        .stTextInput input {
            padding: 10px;
        }

        .stButton button {
            background-color: #004aad;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Create the styled login box
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown('<div class="login-title">Email Spam & Phishing Detection</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-subtitle">Login</div>', unsafe_allow_html=True)

    username = st.text_input("Username", key="username_input")
    password = st.text_input("Password", type="password", key="password_input")
    login_button = st.button("Login", key="login_button")

    if login_button:
        if username == "admin" and password == "admin":
            st.session_state.logged_in = True
            st.session_state.page = "home"
        else:
            st.error("Invalid credentials")

    st.markdown('</div>', unsafe_allow_html=True)
