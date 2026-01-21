import streamlit as st

def feature_selection_page():
    st.title("Choose Detection Feature")
    choice = st.radio("Select what you want to detect:", ["Email Spam Detection", "Website Phishing Detection"])

    if st.button("Continue"):
        if choice == "Email Spam Detection":
            st.session_state.current_page = "spam_detection"
        else:
            st.session_state.current_page = "phishing_detection"
