import streamlit as st

def largest_number(a, b, c):
    """
    Returns the largest number among a, b, and c.
    """
    largest = max(a, b, c)
    return largest

# Streamlit app
def app():
    st.set_page_config(page_title="Find the Largest Number")

    st.write("# Find the Largest Number")

    st.write("Enter three numbers below:")

    a = st.number_input("First number:")
    b = st.number_input("Second number:")
    c = st.number_input("Third number:")

    if st.button("Find the Largest Number"):
        largest = largest_number(a, b, c)
        st.write(f"The largest number is: {largest}")
