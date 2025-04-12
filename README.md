# 🔐 Password Generator & Strength Checker

This is a simple yet powerful **Streamlit** app that helps users generate secure passwords and evaluate their strength based on customizable options.

![Streamlit App Screenshot](https://img.shields.io/badge/Made%20With-Streamlit-red?style=for-the-badge&logo=streamlit)

## 🌟 Features

- ✅ Generate strong and random passwords
- 🛡️ Evaluate password strength with custom scoring
- 🚫 Block common/weak passwords (like `password123`)
- 💡 Suggest strong passwords automatically
- 🧠 Intuitive and beginner-friendly user interface

---

## 🚀 Getting Started

### 📦 Installation

Make sure you have Python installed. Then follow these steps:

# Clone the repository
git clone https://github.com/KanwalRafique/password-generator.git
cd password-generator

# Create a virtual environment and activate it (optional but recommended)
python -m venv .venv
.venv\Scripts\activate    # On Windows

# Install dependencies
pip install streamlit

▶️ Run the App
bash
Copy
Edit
streamlit run app.py

![image](https://github.com/user-attachments/assets/ec3e90e5-f060-42a7-8211-3eb8303d61c1)

![Password generator](![Screenshot 2025-04-13 034317](https://github.com/user-attachments/assets/67f7d608-5f8b-4393-9cdd-9a9e2e370e2b)
)


🧪 Password Strength Criteria
Each password is scored out of 8 based on:

✅ Length

🔠 Uppercase & lowercase letters

🔢 Numbers

🔣 Special characters

❌ Rejection if it's a blacklisted password

```bash
