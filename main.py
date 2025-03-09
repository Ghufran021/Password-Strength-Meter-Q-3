import streamlit as st
import re

def evaluate_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number")

    special_chars = "!@#$%^&*"
    if any(char in special_chars for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&*)")

    if score <= 3:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return score, strength, feedback, color


def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="logo.jpg", layout="centered")

    st.title("Password Strength Meter")
    st.write ("Made by MUHAMMD GHUFRAN")
    st.write("Enter a password to check its strength and get improvement suggestions.")

    password = st.text_input(
        "Enter your password", type="password", help="Password is hidden for security")

    if st.button("Check Strength"):
        if password:
            score, strength, feedback, color = evaluate_password(password)

            st.subheader("Results")
            st.markdown(
                f"**Strength:** <span style='color:{color}'>{strength}</span>", unsafe_allow_html=True)
            st.write(f"**Score:** {score}/7")

            st.progress(score / 7.0)

            if strength != "Strong":
                st.warning("Suggestions to improve:")
                for suggestion in feedback:
                    st.write(f"- {suggestion}")
            else:
                st.success("Great job! This is a secure password.")
        else:
            st.error("Please enter a password to analyze.")

    with st.expander("Password Strength Rules"):
        st.write("""
        A strong password should:
        - Be at least 9 characters long
        - Contain uppercase letters (A-Z)
        - Contain lowercase letters (a-z)
        - Include at least one digit (0-9)
        - Have at least one special character (!@#$%^&*)
        """)


if __name__ == "__main__":
    main()