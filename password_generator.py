import streamlit as st
import random
import string

# --- Blacklisted common weak passwords
blacklist = ["password", "123456", "qwerty", "abc123", "password123", "admin", "letmein"]

# --- Function to generate password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# --- Function to calculate strength score
def calculate_strength(password):
    score = 0
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 2  # Special characters add more weight

    if password.lower() in blacklist:
        score = 0  # Completely reject blacklisted passwords

    return score

# --- Function to suggest a strong password
def suggest_strong_password():
    return generate_password(16, True, True)

# --- Streamlit UI
st.title("🔐 Password Generator & Strength Checker")

length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include digits", value=True)
use_special = st.checkbox("Include special characters", value=True)

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.code(password, language="text")

    if password.lower() in blacklist:
        st.error("⚠️ This password is too common. Try again!")
    else:
        score = calculate_strength(password)
        strength = "Weak"
        if score >= 7:
            strength = "Strong"
        elif score >= 4:
            strength = "Moderate"
        st.success(f"Password Strength: **{strength}** (Score: {score}/8)")

        # Progress bar
        st.progress(score / 8)

# --- Strong password suggestion
st.write("Need help?")
if st.button("Suggest a Strong Password"):
    strong_pass = suggest_strong_password()
    st.code(strong_pass)
    st.info("✅ This is a strong and secure password suggestion.")

st.write("---")
st.caption("Made with 💖 by [Kanwal Rafiqe](https://github.com/KanwalRafique)")
