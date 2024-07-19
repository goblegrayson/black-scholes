import streamlit as st
import black_scholes.model as model

# Time-value of money parameters:
st.title('Black-Scholes Model Intuition')
model = model.BlackScholes()
model.time = 0.0  # Days
model.expiration_time = st.slider('Days to Expiry', min_value=1.0, max_value=4*365.0, value=365.25)
model.risk_free_rate = st.slider('Annualized Risk Free Rate', min_value=0.0, max_value=50.0, value=5.0) / 100.0
# Underlying parameters
model.price_underlying = st.slider('Underlying Price', min_value=1.0, max_value=1000.0, value=100.0)
model.drift_rate = st.slider('Drift Rate', min_value=-100.0, max_value=100.0, value=0.0)
model.volatility = st.slider('Volatility', min_value=0.0, max_value=100.0, value=10.0) / 100.0
# Option parameters
model.isCall = st.checkbox('Is Call? (Uncheck for Put)', value=True)
model.strike = st.slider('Strike', min_value=1.0, max_value=1000.0, value=100.0)
# Print price
if model.isCall:
    st.header(f'Call Price: ${model.option_price}')
else:
    st.header(f'Put Price: ${model.option_price}')
