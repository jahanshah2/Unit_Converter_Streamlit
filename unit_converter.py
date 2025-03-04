import streamlit as st

st.title("Unit Converter")
st.write("Choose the unit you want to convert")

unit_type = st.selectbox("Select unit type:", ["Length", "Weight", "Temperature"])

def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "inches": 39.3701,
        "feet": 3.28084,
        "yards": 1.09361,
        "miles": 0.000621371
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "grams": 1,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "ounces": 0.035274
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    else:
        return value

value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

if unit_type == "Length":
    from_unit = st.selectbox("From:", ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards", "miles"])
    to_unit = st.selectbox("To:", ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards", "miles"])
    result = convert_length(value, from_unit, to_unit)

elif unit_type == "Weight":
    from_unit = st.selectbox("From:", ["grams", "kilograms", "pounds", "ounces"])
    to_unit = st.selectbox("To:", ["grams", "kilograms", "pounds", "ounces"])
    result = convert_weight(value, from_unit, to_unit)

elif unit_type == "Temperature":
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit"])
    result = convert_temperature(value, from_unit, to_unit)

st.write(f"Converted Value: {result:.2f} {to_unit}")
