import streamlit as st

# Create session state to store expression and result
session_state = st.session_state
if "expression" not in session_state:
    session_state.expression = ""
if "result" not in session_state:
    session_state.result = ""

# Define the UI components
st.write("## Calculator")

expression = st.text_input("Expression", value=session_state.expression, key="expression")
result = st.text_input("Result", value=session_state.result, key="result", disabled=True)

col1, col2, col3, col4 = st.columns(4)

# Define the button functions
def add_digit(digit):
    session_state.expression += str(digit)

def add_operator(operator):
    session_state.expression += operator

def calculate():
    try:
        session_state.result = str(eval(session_state.expression))
    except ZeroDivisionError:
        session_state.result = "Error: Division by zero"
    except:
        session_state.result = "Error: Invalid input"
    # session_state.expression = ""

def clear():
    session_state.expression = ""
    session_state.result = ""

# Add the number buttons
with col1:
    button_7 = st.button("7", on_click=add_digit, args=(7,))
with col2:
    button_8 = st.button("8", on_click=add_digit, args=(8,))
with col3:
    button_9 = st.button("9", on_click=add_digit, args=(9,))
with col4:
    button_divide = st.button(" D/ ", on_click=add_operator, args=("/"))

with col1:
    button_4 = st.button("4", on_click=add_digit, args=(4,))
with col2:
    button_5 = st.button("5", on_click=add_digit, args=(5,))
with col3:
    button_6 = st.button("6", on_click=add_digit, args=(6,))
with col4:
    button_multiply = st.button(" M* ", on_click=add_operator, args=("*"))

with col1:
    button_1 = st.button("1", on_click=add_digit, args=(1,))
with col2:
    button_2 = st.button("2", on_click=add_digit, args=(2,))
with col3:
    button_3 = st.button("3", on_click=add_digit, args=(3,))
with col4:
    button_minus = st.button(" S- ", on_click=add_operator, args=("-"))

with col1:
    button_0 = st.button("0", on_click=add_digit, args=(0,))
with col2:
    button_clear = st.button(" C ", on_click=clear)
with col3:
    button_equal = st.button(" = ", on_click=calculate)
with col4:
    button_plus = st.button(" A+ ", on_click=add_operator, args=("+"))

# # Display the expression and result
# st.write("### Output")
# st.write("Expression: ", session_state.expression)
# st.write("Result: ", session_state.result)
