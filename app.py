import streamlit as st
import json
import urllib.request

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

# Sidebar
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Enter HuggingFace API Token (hf_...)", type="password")

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

def query_huggingface_router(system_prompt, user_prompt, token):
    url = "https://router.huggingface.co/hf-inference/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "Qwen/Qwen2.5-Coder-32B-Instruct",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "max_tokens": 1000
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers)
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        error_text = e.read().decode("utf-8")
        raise Exception(f"HTTP Error {e.code}: {error_text}")
    except Exception as e:
        raise Exception(f"Connection Error: {str(e)}")

# Generate Problem Button
st.subheader(f"Current Topic: {level}")

if st.button("✨ Generate Problem & Adaptive Guidance"):
    if not api_key:
        st.error("Please enter your HuggingFace API Token in the sidebar.")
    else:
        try:
            with st.spinner("Generating customized math problem..."):
                output = query_huggingface_router(
                    SYSTEM_PROMPTS[level],
                    "Generate one new math problem, its step-by-step solution, and key hints for the student.",
                    api_key
                )
            st.success("Problem generated successfully!")
            st.markdown(output)
        except Exception as e:
            st.error(f"Error: {e}")

# Interactive AI Hint / Assistant
st.markdown("---")
st.subheader("💡 Need Help or a Customized Hint?")
user_question = st.text_input("Ask the AI tutor a question about your problem:")

if st.button("Ask AI Tutor"):
    if not api_key:
        st.error("Please enter your HuggingFace API Token in the sidebar.")
    elif user_question:
        try:
            with st.spinner("AI Tutor is thinking..."):
                output = query_huggingface_router(
                    f"You are a math tutor helping a student with a {level} quadratic equation problem.",
                    f"Student question: {user_question}\nProvide a helpful hint without giving away the full answer immediately.",
                    api_key
                )
            st.info(output)
        except Exception as e:
            st.error(f"Error: {e}")
