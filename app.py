import os
import streamlit as st
import google.generativeai as genai

# Page configuration
st.set_page_config(
    page_title="AI Math Differentiator: Quadratic Equations",
    page_icon="🧮",
    layout="wide"
)

# App Title & Description
st.title("🧮 AI Math Differentiator — Quadratic Equations")
st.markdown("""
This web application uses AI to adapt **Quadratic Equations** into three distinct levels of difficulty for personalized, differentiated learning.
""")

# Sidebar for API Key and Level Selection
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

level = st.sidebar.radio(
    "Select Difficulty Level:",
    ["Level 1: Foundation", "Level 2: Standard", "Level 3: Advanced"]
)

# AI System Prompts tailored for Differentiated Learning
SYSTEM_PROMPTS = {
    "Level 1: Foundation": """
You are a helpful math tutor. Provide a basic quadratic equation with integer coefficients that factors easily (e.g., x^2 - 5x + 6 = 0).
Include a step-by-step breakdown, direct hints, and simplify the explanation to build foundational confidence.
""",
    "Level 2: Standard": """
You are a high school math teacher. Provide a standard curriculum quadratic equation requiring the quadratic formula or completing the square (e.g., 3x^2 + 5x - 2 = 0).
Provide standard guidance and clear step-by-step solutions suitable for grade-level practice.
""",
    "Level 3: Advanced": """
You are an advanced STEM educator. Provide a complex, real-world application problem involving quadratic functions (e.g., projectile motion, area maximization, or profit optimization).
Challenge the learner with multi-step logic, conceptual depth, and practical context.
"""
}

# Generate Problem Button
st.subheader(f"Current Topic: {level}")

if st.button("✨ Generate Problem & Adaptive Guidance"):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar to generate problems.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            
            prompt = f"{SYSTEM_PROMPTS[level]}\nGenerate one new math problem, its step-by-step solution, and key hints for the student."
            
            with st.spinner("Generating customized math problem..."):
                response = model.generate_content(prompt)
                
            st.success("Problem generated successfully!")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"Error generating response: {e}")

# Interactive AI Hint / Assistant
st.markdown("---")
st.subheader("💡 Need Help or a Customized Hint?")
user_question = st.text_input("Ask the AI tutor a question about your problem:")

if st.button("Ask AI Tutor"):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
    elif user_question:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            
            tutoring_prompt = f"The student is working on a {level} quadratic equation problem. Their question is: '{user_question}'. Provide an encouraging hint tailored to {level} without giving away the full answer immediately."
            
            with st.spinner("AI Tutor is thinking..."):
                response = model.generate_content(tutoring_prompt)
                
            st.info(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
