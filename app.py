import streamlit as st
import pandas as pd
import numpy as np
#to start remember to activeate the venv  source .venv/bin/activate
#if there'isnt a venv -> python -m venv .venv,  within the directory 

"# Hello world" #writes it on the page as it is st.write("Hello world")
st.write("# Hello world")
st.write("## Hello world")
st.write("### Hello world")
st.write("#### Hello world")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df 

dataframe = np.random.randn(10,20)
st.dataframe(dataframe)

dataframe1 = pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d' %i for i in range(20))
)
st.dataframe(dataframe1.style.highlight_max(axis=0)) #higlight_max highlights the max value in column

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)