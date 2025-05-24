import streamlit as st
import math

# Set page config
st.set_page_config(page_title="Super Calculator", layout="centered")

# Title
st.markdown("## 🧮 Super Calculator")

# --- Theme Toggle ---
theme = st.selectbox("Select Theme", ["🌑 Dark", "☀️ Light"])
if theme == "☀️ Light":
    st.markdown(
        """
        <style>
        body {
            background-color: white;
            color: black;
        }
        </style>
        """, unsafe_allow_html=True
    )

# --- Inputs ---
num1 = st.number_input("Enter first number", key="first_number")
num2 = st.number_input("Enter second number (ignored for Square Root)", key="second_number")

# --- Operation ---
operation = st.selectbox(
    "Select operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)",
     "Power (x^y)", "Square Root (√x)", "Percentage (x%)"]
)

# --- History State ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Result Calculation ---
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

    # Display result
    if result is not None:
        st.success(f"Result: {result}")

    # Add to history
    st.session_state.history.append(op_str)

# --- History Display ---
if st.session_state.history:
    st.subheader("📜 Calculation History")
    for h in reversed(st.session_state.history):
        st.write(h)

    # Export history
    history_text = "\n".join(st.session_state.history)
    st.download_button("📤 Download History as .txt", history_text, file_name="calculator_history.txt")

# --- Clear Button ---
if st.button("Clear All", key="clear_button"):
    st.session_state.first_number = 0.0
    st.session_state.second_number = 0.0
    st.session_state.history = []
    st.experimental_rerun()
