"""
page.py
A streamlit page
"""
from pathlib import Path
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
import black_scholes.model as model


# Utils
def load_markdown(file_name):
    file_path = Path(__file__).parent.joinpath('markdown', file_name + '.md')
    with open(file_path, 'r') as file:
        return file.read()


# Page Setup
st.title(':green[Black-Scholes Formula Intuition]')

# Simple Calculator
st.markdown(load_markdown('calculator-intro'), unsafe_allow_html=True)
st.divider()
model = model.BlackScholes()
model.isCall = 'Call' == st.selectbox('Option Type', ['Call', 'Put'],)
model.expiration_time = np.float64(st.slider('Time to Expiry (Days)', min_value=0.0, max_value=4*365.0, value=365.25))
model.price_underlying = np.float64(st.slider('Underlying Price ($)', min_value=1.0, max_value=200.0, value=100.0))
model.strike = np.float64(st.slider('Strike ($)', min_value=1.0, max_value=200.0, value=100.0))
model.risk_free_rate = np.float64(st.slider('Risk Free Rate (% Annualized)', min_value=0.0, max_value=50.0, value=5.0) / 100.0)
if st.checkbox('Infinite Volatility?', False):
    model.volatility = np.float64(1e9)
else:
    model.volatility = np.float64(st.slider('Volatility (% Annualized)', min_value=0.01, max_value=100.0, value=10.0) / 100.0)
st.header(f':green[{model.type_string} Price: ${model.option_price:.2f}]', anchor=False)
st.divider()
st.markdown(load_markdown('calculator-conclusions'), unsafe_allow_html=True)
st.divider()

# Sensitivity Study
st.title(':green[Model Sensitivities]')
st.markdown(load_markdown('sensitivity-intro'), unsafe_allow_html=True)
vol_range = np.float64(st.slider('Volatility Range (% Annualized)', min_value=1.0, max_value=100.0, value=5.0)) / 100
number_of_strikes = np.int8(st.slider('Number of Strikes', min_value=3, max_value=15, value=11))
number_of_strikes = number_of_strikes - number_of_strikes % 2 + 1
price_surface, strikes, vols = model.calculate_price_surface(vol_range, number_of_strikes)
# Heat map
st.header(f':green[{model.type_string} Price Surface: ${model.price_underlying:.2f} Spot]', anchor=False)
cmap = LinearSegmentedColormap.from_list('rg', ["r", "w", "g"], N=256)
annotation_size = 8 if number_of_strikes <= 9 else 6
ax = sns.heatmap(data=price_surface,
                 annot=True,
                 cmap=cmap,
                 fmt='.2f',
                 annot_kws={"fontsize": annotation_size},
                 cbar_kws={'format': '$%.2f', "label": 'Option Price ($)'}

                 )
fig = ax.get_figure()
plt.xlabel('Strike ($)')
plt.ylabel('Volatility (% Annualized)')
plt.xticks(rotation=90)
plt.yticks(rotation=0)
st.pyplot(fig)
# Surface plot
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(strikes, vols*100, price_surface.values, cmap=cmap)
plt.xlabel('Strike ($)', fontsize='8')
plt.ylabel('Volatility (% Annualized)', fontsize='8')
ax.set_zlabel('Option Price ($)', fontsize='8', labelpad=0)
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
ax.zaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
ax.tick_params(axis='both', which='major', labelsize=6)
ax.view_init(azim=290, elev=15)
plt.tight_layout()
st.pyplot(fig, bbox_inches='tight')
