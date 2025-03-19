import streamlit as st
import requests

api_key = st.secrets['API_KEY']

# Where USD is the base currency you want to use
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

# Making our request
response = requests.get(url)
data = response.json()

conversion = data['conversion_rates']

# Extracting the keys into a list
currency_list = list(conversion.keys())


def convert_units(value, unit_from, unit_to):




    # Exchange rate of unit_from for the equivalent of 1 usd
    unit_from_exchange_rate = conversion[unit_from]

    # Exchange rate of unit_to for the equivalent of 1 usd
    unit_to_exchange_rate = conversion[unit_to]


    if unit_from and unit_to in conversion:
        amount_in_usd = value/unit_from_exchange_rate
        converted_amount = amount_in_usd * unit_to_exchange_rate    
        return converted_amount
    else:
        return "Conversion not supported"
    

st.title("GlobalXchange")
st.write("Easily convert between different currencies with real-time exchange rates.")

value = st.number_input("Enter the value...")

unit_from = st.selectbox("Convert from:", currency_list)
unit_to = st.selectbox("Convert to:", currency_list)

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value: {result:.2f}")