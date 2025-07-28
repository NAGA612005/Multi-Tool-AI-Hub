# 🧠 Code-Free + Code Explainer (Gemini-Powered AI Assistant)

Welcome to **Code-Free + Code Explainer**, a powerful developer companion built with **Streamlit + Python**, powered by **Gemini LLM** by Google.


## 🌐 Live App

👉 Try it live on Streamlit: [https://codetoolz.streamlit.app](https://codetoolz.streamlit.app)

✨ Whether you're a student or a pro, this tool helps you:
- 🧾 Explain any code line-by-line in multiple languages
- 💡 Generate full programs just by describing your idea

---

## 🚀 Features

### 🔍 Code Explainer
> Upload or paste any code → Get a detailed explanation.

- Language options: **Python, C++, JavaScript, HTML**
- Explanation styles:
  - Beginner-friendly
  - Visual + Steps
  - Fun + Emoji
- Multilingual support:
  - English, Hindi, Tamil, Tanglish
- Auto-formatting with styled HTML for clarity

---

### ⚡ Code-Free Generator
> Describe what you want to build → Get ready-to-use code.

- Just type: “Create a login system using Flask” or “Build a calculator in HTML”
- Choose your language: Python, JavaScript, HTML, etc.
- Gemini generates:
  - Clean, copyable code
  - Step-by-step explanation
- Perfect for rapid prototyping & learning

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) — clean Python UI
- [Google Gemini LLM](https://ai.google.dev/)
- Python 3.10+
- HTML + CSS for formatting output

---

## 📁 Project Structure

📦 code-hub/
├── streamlit_app.py # Main Streamlit interface
├── codefree.py # Handles LLM-based code generation & explanation
├── requirements.txt
└── README.md


---

## 🔧 Installation

```bash
git clone https://github.com/NAGA612005/codefree-hub.git
cd codefree-hub

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
