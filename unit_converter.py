import streamlit as st
from pint import UnitRegistry


ureg = UnitRegistry()

# Streamlit App Title
st.title("Advanced Unit Converter 🔥")

# Available unit categories
unit_categories = {
    "Length": ["meters", "kilometers", "miles", "feet", "inches", "centimeters", "millimeters", "yards"],
    "Weight": ["grams", "kilograms", "pounds", "tons", "ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["seconds", "minutes", "hours", "days", "weeks"],
    "Speed": ["meters per second", "kilometers per hour", "miles per hour", "knots"],
    "Area": ["square meters", "square kilometers", "acres", "hectares"],
    "Volume": ["liters", "milliliters", "gallons", "cubic meters"],
    "Energy": ["joules", "calories", "kilowatt-hours"],
    "Pressure": ["pascals", "atmospheres", "bars"],
    "Data Storage": ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"]
}

unit_type = st.selectbox("Select Unit Type:", list(unit_categories.keys()))

available_units = unit_categories[unit_type]

value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From:", available_units)
to_unit = st.selectbox("To:", available_units)

# Convert function
def convert_units(value, from_unit, to_unit):
    try:
        if unit_type == "Temperature":
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                return (value - 32) * 5/9
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                return value + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                return value - 273.15
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
            else:
                return value
        else:
            result = (value * ureg(from_unit)).to(to_unit)
            return result.magnitude
    except:
        return "Invalid Conversion"

# Convert button
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"Converted Value: {result:.2f} {to_unit}")
