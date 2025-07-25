# streamlit_app.py (UI Entry Point for All Tools)
import streamlit as st
# from benormal import generate_nf_response, generate_er_diagram, export_to_pdf
from codefree import explain_code, generate_code, run_with_timeout

# 🌐 Streamlit UI Setup
st.set_page_config(page_title="Multi-Tool AI Hub", layout="wide", page_icon="🧠")
st.markdown("""
    <style>
    body, .stApp { background-color: #121212; color: #ffffff; font-family: 'Segoe UI', sans-serif; }
    .stTextInput > label, .stSelectbox > label, .stRadio > label, .stButton > button, .stMarkdown, .stExpanderHeader {
        color: #f0f0f0 !important;
    }
    .stButton > button {
        background-color: #4CAF50; color: white; border: none; padding: 0.5rem 1rem;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("🛠️ Choose a Tool")
tool = st.sidebar.radio("Select a model:", ["Code Explainer", "Code-Free"])

st.title(f"✨ {tool} Interface")

# if tool == "Be-Normal":
#     schema_input = st.text_area("📥 Enter SQL schema:", height=200, help="Paste a CREATE TABLE SQL schema")
#     nf_choice = st.multiselect("📊 Select Normal Form(s):", ["1NF", "2NF", "3NF", "BCNF", "4NF"], default=["1NF"])
#     language = st.selectbox("🌐 Choose Language:", ["English", "Hindi", "Tamil", "Telugu", "Tanglish"])
#     if st.button("🎯 Normalize and Explain"):
#         if schema_input:
#             with st.spinner("Analyzing schema and applying normalization laws..."):
#                 result = run_with_timeout(generate_nf_response, schema_input, nf_choice, language)
#                 html = f"""
#                 <div style='color: white; font-family: Segoe UI, sans-serif;'>
#                 <style>
#                 table {{border-collapse: collapse; width: 100%; color: white;}}
#                 th, td {{border: 1px solid #ccc; padding: 8px;}}
#                 th {{background-color: #333; color: white;}}
#                 </style>{result}</div>
#                 """
#                 st.components.v1.html(html, height=1000, scrolling=True)
#                 with st.expander("📊 ER Diagram"):
#                     st.markdown("""```mermaid\n""" + generate_er_diagram(schema_input) + "\n```", unsafe_allow_html=True)
#                 if st.download_button("📄 Download PDF", data=open(export_to_pdf("Be-Normal", f"Language: {language}, NFs: {', '.join(nf_choice)}", result), "rb"), file_name="be-normal.pdf"):
#                     st.success("PDF downloaded!")
#         else:
#             st.warning("❗ Please enter a valid schema to continue.")
if tool == "Code Explainer":
    code = st.text_area("🧾 Paste your code:", height=250, help="Python, JS, etc.")
    lang = st.selectbox("🌐 Explain in language:", ["English", "Tamil", "Tanglish", "Hindi"])
    style = st.radio("🎨 Style:", ["Beginner-friendly", "Visual + Steps", "Fun + Emoji"])
    if st.button("🔍 Explain Code"):
        if code:
            with st.spinner("Explaining line by line with visuals and insights..."):
                explanation = run_with_timeout(explain_code, code, lang, style)
                st.markdown(explanation, unsafe_allow_html=True)
        else:
            st.warning("❗ Please paste some code to explain.")

elif tool == "Code-Free":
    desc = st.text_area("🗒️ Describe what you want to code:", height=200, placeholder="Example: Create a login page in Flask")
    lang = st.selectbox("💻 Language:", ["Python", "JavaScript", "C++", "HTML", "Java"])

    if st.button("🚀 Generate and Explain"):
        if desc:
            with st.spinner("✨ Generating code and explanation..."):
                generated_code = run_with_timeout(generate_code, desc, lang)
                st.code(generated_code, language=lang.lower())
                st.markdown("<hr style='margin-top:2rem;margin-bottom:1rem;'>", unsafe_allow_html=True)
                st.markdown(f"<div style='color:white;'>{explanation}</div>", unsafe_allow_html=True)
        else:
            st.warning("❗ Please describe what you want to generate.")
