import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')
st.subheader('Number of pickups by hour')

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)