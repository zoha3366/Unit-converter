import streamlit as st
from converter import convert, load_units

# Load units from JSON
units = load_units()

# Streamlit App Title
st.title("Unit Converter")

# Select Category
category = st.selectbox("Select a category", list(units.keys()))

# Special case for temperature conversion
if category == "temperature":
    from_unit = st.selectbox("Convert from", ["celsius", "fahrenheit"])
    to_unit = st.selectbox("Convert to", ["celsius", "fahrenheit"])
else:
    from_unit = st.selectbox("Convert from", list(units[category].keys()))
    to_unit = st.selectbox("Convert to", list(units[category].keys()))

# User Input
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

# Convert Button
if st.button("Convert"):
    try:
        result = convert(value, from_unit, to_unit, category)
        st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
    except ValueError as e:
        st.error(f"Error: {e}")
