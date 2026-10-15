# Individual Assignment: Web-Based AI Math Differentiator

## Topic: AI for Differentiated Learning (Quadratic Equations)

### 1. Overview & Objective
This project demonstrates how Artificial Intelligence can personalize educational content by adapting a core mathematical concept—**Quadratic Equations**—into three distinct levels of difficulty. By tailoring prompt engineering, the application delivers scaffolding, hints, and problem complexity matched to diverse learner capabilities.

---

### 2. Differentiated Learning Levels
* **Level 1 (Foundation):** Focuses on basic equations with simple integer roots (e.g., $x^2 - 5x + 6 = 0$). Includes detailed step-by-step breakdowns and direct conceptual hints to build confidence.
* **Level 2 (Standard):** Covers standard curriculum-level problems requiring the quadratic formula ($x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$) or completing the square.
* **Level 3 (Advanced):** Features multi-step, real-world application tasks (e.g., physics projectile motion equations $h(t) = -16t^2 + v_0 t + h_0$) requiring high-level logical reasoning and modeling.

---

### 3. AI System Prompts & Differentiation Strategy
The dynamic differentiation is achieved by passing specialized system prompts to the LLM (Gemini API):

1. **Foundation Prompt:** Instructs the model to use scaffolded explanations, limit complex terminology, and highlight basic factoring rules.
2. **Standard Prompt:** Directs the model to follow official curriculum standards, encouraging procedural correctness and algorithm verification.
3. **Advanced Prompt:** Orders the model to contextualize the algebraic concept into practical modeling, challenging the student to extract parameters from text before solving.

---

### 4. How to Run Locally
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `streamlit run app.py`
4. Enter your Gemini API key in the sidebar.
