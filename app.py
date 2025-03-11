import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔄")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔄 Unit Conversion Application</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #1E88E5;'>This is a simple and colorful unit conversion application.</p>", unsafe_allow_html=True)

category = st.selectbox("📊 Select the category of conversion", ["📏 Length", "🌡️ Temperature", "⚖️ Weight", "� Pressure"])

if "📏 Length" in category:
    input_unit = st.selectbox("📥 Select input unit", ["Meters", "Feet", "Inches", "Kilometers"])
    output_unit = st.selectbox("📤 Select output unit", ["Meters", "Feet", "Inches", "Kilometers"])
    value = st.number_input("🔢 Enter the value to convert", value=0.0, step=0.1)

    if st.button("🔄 Convert"):
        if input_unit == output_unit:
            st.success(f"{value} {input_unit} is equal to {value} {output_unit}")
        else:
            # Conversion logic for length
            conversions = {
                "Meters": 1,
                "Feet": 0.3048,
                "Inches": 0.0254,
                "Kilometers": 1000
            }
            result = value * conversions[input_unit] / conversions[output_unit]
            st.success(f"{value} {input_unit} is equal to {result:.4f} {output_unit}")

elif "🌡️ Temperature" in category:
    input_unit = st.selectbox("📥 Select input unit", ["Celsius", "Fahrenheit", "Kelvin"])
    output_unit = st.selectbox("📤 Select output unit", ["Celsius", "Fahrenheit", "Kelvin"])
    value = st.number_input("🔢 Enter the value to convert", value=0.0, step=0.1)

    if st.button("🔄 Convert"):
        if input_unit == output_unit:
            st.success(f"{value} {input_unit} is equal to {value} {output_unit}")
        else:
            # Conversion logic for temperature
            if input_unit == "Celsius" and output_unit == "Fahrenheit":
          
                result = (value * 9/5) + 32
            elif input_unit == "Celsius" and output_unit == "Kelvin":
                result = value + 273.15
            elif input_unit == "Fahrenheit" and output_unit == "Celsius":
                result = (value - 32) * 5/9
            elif input_unit == "Fahrenheit" and output_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif input_unit == "Kelvin" and output_unit == "Celsius":
                result = value - 273.15
            elif input_unit == "Kelvin" and output_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            st.success(f"{value} {input_unit} is equal to {result:.2f} {output_unit}")

elif "⚖️ Weight" in category:
    input_unit = st.selectbox("📥 Select input unit", ["Kilograms", "Pounds", "Ounces", "Grams"])
    output_unit = st.selectbox("📤 Select output unit", ["Kilograms", "Pounds", "Ounces", "Grams"])
    value = st.number_input("🔢 Enter the value to convert", value=0.0, step=0.1)

    if st.button("🔄 Convert"):
        if input_unit == output_unit:
            st.success(f"{value} {input_unit} is equal to {value} {output_unit}")
        else:
            # Conversion logic for weight
            conversions = {
                "Kilograms": 1,
                "Pounds": 0.453592,
                "Ounces": 0.0283495,
                "Grams": 0.001
            }
            result = value * conversions[input_unit] / conversions[output_unit]
            st.success(f"{value} {input_unit} is equal to {result:.4f} {output_unit}")

elif "�pressure" in category:
    input_unit = st.selectbox("📥 Select input unit", ["Pascal", "Bar", "PSI", "Atmosphere"])
    output_unit = st.selectbox("📤 Select output unit", ["Pascal", "Bar", "PSI", "Atmosphere"])
    value = st.number_input("🔢 Enter the value to convert", value=0.0, step=0.1)

    if st.button("🔄 Convert"):
        if input_unit == output_unit:
            st.success(f"{value} {input_unit} is equal to {value} {output_unit}")
        else:
            # Conversion logic for pressure
            conversions = {
                "Pascal": 1,
                "Bar": 100000,
                "PSI": 6894.76,
                "Atmosphere": 101325
            }
            result = value * conversions[input_unit] / conversions[output_unit]
            st.success(f"{value} {input_unit} is equal to {result:.6f} {output_unit}")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9E9E9E;'>Made with ❤️ by Asghar Zaheer</p>", unsafe_allow_html=True)
