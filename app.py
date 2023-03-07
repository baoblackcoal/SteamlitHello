import streamlit as st


def add_numbers(a, b):
    return a + b


def main():
    st.title("My Streamlit App")
    st.write("Enter two numbers to add:")

    a = st.number_input("First number")
    b = st.number_input("Second number")

    result = add_numbers(a, b)
    st.write("Result:", result)


if __name__ == "__main__":
    main()
