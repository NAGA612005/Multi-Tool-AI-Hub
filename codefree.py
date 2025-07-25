# codefree.py

import google.generativeai as genai
import re
import concurrent.futures

# ✅ Gemini API configuration
genai.configure(api_key="AIzaSyC2Z9xqIOx4BR4sjCX0Bt1sHYDZNGquMng")  # Replace with your actual Gemini API key
gemini_model = genai.GenerativeModel("gemini-2.0-flash")

def clean_html_response(raw_html):
    cleaned = re.sub(r"^(```)?html\s*", "", raw_html.strip(), flags=re.IGNORECASE)
    cleaned = re.sub(r"```$", "", cleaned.strip())
    return cleaned

# Shared timeout wrapper
def run_with_timeout(func, *args, timeout=25):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(func, *args)
        try:
            return future.result(timeout=timeout)
        except concurrent.futures.TimeoutError:
            return "⏰ Timeout: Gemini API took too long to respond."

# 🔍 Code explanation logic
def explain_code(code, language, style):
    prompt = f"""
🧑‍🏫 You are a helpful AI assistant.
Explain the following code line by line in {language}.
Make the explanation {style.lower()}.
Use diagrams if needed.

```{code}```
"""
    response = gemini_model.generate_content(prompt)
    return clean_html_response(response.text)

# 🚀 Code generation logic
def generate_code(description, lang):
    prompt = f"""
💡 Generate {lang} code from the following description:
{description}

"""
    response = gemini_model.generate_content(prompt)
    return clean_html_response(response.text)
