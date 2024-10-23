import math 
import streamlit as st
import pandas as pd
import numpy as np
#to start remember to activeate the venv  source .venv/bin/activate
#if there'isnt a venv -> python -m venv .venv,  within the directory 



"Hello world" #writes it on the page as it is st.write("Hello world")
"This is the rappresentation of a 1 header"
st.write("# Hello world") 
"This is the rappresentation of a 2 header"
st.write("## Hello world")
"This is the rappresentation of a 3 header"
st.write("### Hello world")
"This is the rappresentation of a 4 header"
st.write("#### Hello world")



if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")






