import streamlit as st
import random

# Page configuration
st.set_page_config(
    page_title="AI Math Differentiator: Quadratic Equations",
    page_icon="🧮",
    layout="wide"
)

# App Title & Description
st.title("🧮 AI Math Differentiator — Quadratic Equations")
st.markdown("""
This web application uses AI logic to adapt **Quadratic Equations** into three distinct levels of difficulty for personalized, differentiated learning.
""")

# Sidebar
st.sidebar.header("Settings")
level = st.sidebar.radio(
    "Select Difficulty Level:",
    ["Level 1: Foundation", "Level 2: Standard", "Level 3: Advanced"]
)

# Pre-generated dataset simulating AI Differentiated Outputs
PROBLEMS_DATA = {
    "Level 1: Foundation": [
        {
            "problem": "Solve for $x$: $x^2 - 5x + 6 = 0$",
            "steps": "1. Find two numbers that multiply to $6$ and add up to $-5$ (they are $-2$ and $-3$).\n2. Factor the equation: $(x - 2)(x - 3) = 0$.\n3. Set each factor to zero: $x - 2 = 0$ or $x - 3 = 0$.",
            "solution": "$x_1 = 2, \\quad x_2 = 3$",
            "hint": "Try factoring the constant term (6) into two integers whose sum equals the middle coefficient (-5)."
        },
        {
            "problem": "Solve for $x$: $x^2 - 7x + 12 = 0$",
            "steps": "1. Look for factors of $12$ that sum to $-7$ ($-3$ and $-4$).\n2. Rewrite as: $(x - 3)(x - 4) = 0$.\n3. Solve for $x$.",
            "solution": "$x_1 = 3, \\quad x_2 = 4$",
            "hint": "Since the constant term is positive and the middle term is negative, both roots must be negative numbers inside the brackets."
        }
    ],
    "Level 2: Standard": [
        {
            "problem": "Solve for $x$: $2x^2 + 5x - 3 = 0$",
            "steps": "1. Use the quadratic formula: $x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$ with $a=2, b=5, c=-3$.\n2. Calculate discriminant: $D = 5^2 - 4(2)(-3) = 25 + 24 = 49$.\n3. Compute roots: $x = \\frac{-5 \\pm 7}{4}$.",
            "solution": "$x_1 = 0.5, \\quad x_2 = -3$",
            "hint": "Calculate the discriminant $b^2 - 4ac$ first to verify if real solutions exist."
        },
        {
            "problem": "Solve for $x$: $3x^2 - 2x - 5 = 0$",
            "steps": "1. Apply formula with $a=3, b=-2, c=-5$.\n2. $D = (-2)^2 - 4(3)(-5) = 4 + 60 = 64$.\n3. $x = \\frac{2 \\pm 8}{6}$.",
            "solution": "$x_1 = 1.67, \\quad x_2 = -1$",
            "hint": "Be careful with negative signs when evaluating $b^2 - 4ac$."
        }
    ],
    "Level 3: Advanced": [
        {
            "problem": "A projectile is launched from a height of 10 meters with an initial velocity of 20 m/s. Its height $h(t)$ in meters after $t$ seconds is modeled by: $$h(t) = -5t^2 + 20t + 10$$ Find the exact time $t$ when the projectile hits the ground ($h = 0$).",
            "steps": "1. Set equation to zero: $-5t^2 + 20t + 10 = 0$.\n2. Simplify by dividing by $-5$: $t^2 - 4t - 2 = 0$.\n3. Use quadratic formula: $t = \\frac{4 \\pm \\sqrt{16 - 4(1)(-2)}}{2} = \\frac{4 \\pm \\sqrt{24}}{2} = 2 \\pm \\sqrt{6}$.\n4. Discard negative time solution.",
            "solution": "$t = 2 + \\sqrt{6} \\approx 4.45 \\text{ seconds}$",
            "hint": "In real-world physical models, reject negative time values as extraneous roots."
        }
    ]
}

st.subheader(f"Current Topic: {level}")

if "current_problem" not in st.session_state:
    st.session_state.current_problem = None

if st.button("✨ Generate Problem & Adaptive Guidance"):
    problem_choice = random.choice(PROBLEMS_DATA[level])
    st.session_state.current_problem = problem_choice

if st.session_state.current_problem:
    p = st.session_state.current_problem
    st.success("Problem Generated!")
    st.markdown(f"### **Problem:**\n{p['problem']}")
    st.markdown(f"### **Step-by-step Solution:**\n{p['steps']}")
    st.markdown(f"### **Final Answer:**\n{p['solution']}")

st.markdown("---")
st.subheader("💡 Need Help or a Customized Hint?")
user_question = st.text_input("Ask the AI tutor a question about your problem:")

if st.button("Ask AI Tutor"):
    if st.session_state.current_problem:
        st.info(f"**AI Tutor Hint:** {st.session_state.current_problem['hint']}")
    else:
        st.warning("Please generate a problem first!")
