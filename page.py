from pathlib import Path

import numpy as np
import streamlit as st
import black_scholes.model as model


# Utils
def load_markdown(file_name):
    file_path = Path(__file__).parent.joinpath('markdown', file_name)
    with open(file_path, 'r') as file:
        return file.read()


# Page Setup
st.title(':green[Black-Scholes Formula Intuition]')

# Simple Calculator
st.markdown(load_markdown('calculator-intro.md'), unsafe_allow_html=True)
st.divider()
model = model.BlackScholes()
model.isCall = 'Call' == st.selectbox('Option Type', ['Call', 'Put'],)
model.expiration_time = st.slider('Days to Expiry', min_value=0.0, max_value=4*365.0, value=365.25)
model.price_underlying = st.slider('Underlying Price', min_value=1.0, max_value=200.0, value=100.0)
model.strike = st.slider('Strike', min_value=1.0, max_value=200.0, value=100.0)
model.risk_free_rate = st.slider('Annualized Risk Free Rate', min_value=0.0, max_value=50.0, value=5.0) / 100.0
if st.checkbox('Infinite Volatility?', False):
    model.volatility = 1e9
else:
    model.volatility = st.slider('Volatility', min_value=0.0, max_value=100.0, value=10.0) / 100.0
if model.isCall:
    st.header(f':green[Call Price: ${model.option_price:.2f}]', anchor=False)
else:
    st.header(f':green[Put Price: ${model.option_price:.2f}]', anchor=False)
st.divider()
st.markdown(load_markdown('calculator-conclusions.md'), unsafe_allow_html=True)
st.divider()

# Sensitivity Study
st.title(':green[Model Sensitivities]')
st.markdown(load_markdown('sensitivity-intro.md'), unsafe_allow_html=True)