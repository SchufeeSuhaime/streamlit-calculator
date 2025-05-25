import streamlit as st
import math

# --- Page Setup ---
st.set_page_config(
    page_title="Super Calculator",
    page_icon="🧮",
    layout="centered"
)

# --- Custom Styling for Mobile ---
st.markdown("""
    <style>
    .block-container {
        max-width: 500px;
        margin: auto;
        padding-top: 1rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Name Input ---
name = st.text_input("👤 Enter your name to start:", key="username")

# --- Conditional Display ---
if name:
    st.markdown(f"### 👋 Welcome, **{name}**!")

    # --- Number Inputs ---
    num1 = st.number_input("Enter first number", key="first_number")
    num2 = st.number_input("Enter second number (ignored for Square Root)", key="second_number")

    # --- Operation Selection ---
    operation = st.selectbox(
        "Select operation",
        ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)",
         "Power (x^y)", "Square Root (√x)", "Percentage (x%)"]
    )

    # --- Initialize History ---
    if "history" not in st.session_state:
        st.session_state.history = []

    # --- Calculation ---
    if st.button("Calculate", key="calc_button"):
        result = None
        if operation == "Addition (+)":
            result = num1 + num2
            op_str = f"{num1} + {num2} = {result}"
        elif operation == "Subtraction (-)":
            result = num1 - num2
            op_str = f"{num1} - {num2} = {result}"
        elif operation == "Multiplication (×)":
            result = num1 * num2
            op_str = f"{num1} × {num2} = {result}"
        elif operation == "Division (÷)":
            if num2 != 0:
                result = num1 / num2
                op_str = f"{num1} ÷ {num2} = {result}"
            else:
                result = "Error: Division by zero"
                op_str = f"{num1} ÷ {num2} = Error"
        elif operation == "Power (x^y)":
            result = num1 ** num2
            op_str = f"{num1} ^ {num2} = {result}"
        elif operation == "Square Root (√x)":
            if num1 >= 0:
                result = math.sqrt(num1)
                op_str = f"√{num1} = {result}"
            else:
                result = "Error: Negative number"
                op_str = f"√{num1} = Error"
        elif operation == "Percentage (x%)":
            result = (num1 / 100) * num2
            op_str = f"{num1}% of {num2} = {result}"

        if result is not None:
            st.success(f"✅ {name}, your result is: {result}")

        st.session_state.history.append(op_str)

    # --- History Section ---
    if st.session_state.history:
        st.subheader("📜 Calculation History")
        for h in reversed(st.session_state.history):
            st.write(h)

        # --- Download History ---
        history_text = "\n".join(st.session_state.history)
        st.download_button("📤 Download History as .txt", history_text, file_name="calculator_history.txt")

    # --- Clear Button ---
    if st.button("Clear All", key="clear_button"):
        st.session_state.first_number = 0.0
        st.session_state.second_number = 0.0
        st.session_state.history = []
        st.experimental_rerun()

else:
    st.warning("❗ Please enter your name to use the calculator.")

# --- Developer Credit ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 0.9em; padding-top: 2rem;'>
        🔧 Developed by <strong>Schufee Suhaime</strong>
    </div>
    """,
    unsafe_allow_html=True
)
