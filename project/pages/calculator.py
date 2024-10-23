
import math 
import streamlit as st
import pandas as pd
import numpy as np


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
st.write(x, 'square root is', math.sqrt(x))


st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name