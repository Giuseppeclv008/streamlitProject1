import math 
import streamlit as st
import pandas as pd
import numpy as np

"# This is a dataframe"
if st.checkbox('Show dataframe'):
  
  df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
  })
  df 
  option = st.selectbox(
    'Which number do you like best?',
     df['second column'])

  'You selected: ', option

"## This is another dataframe"
if st.checkbox('Show another dataframe'):
  dataframe = np.random.randn(10,20)
  st.dataframe(dataframe)

'### This is another another dataframe'
if st.checkbox('Show another another dataframe'):
  dataframe1 = pd.DataFrame(
      np.random.randn(10,20),
      columns=('col %d' %i for i in range(20))
  )
  st.dataframe(dataframe1.style.highlight_max(axis=0)) #higlight_max highlights the max value in column

"# This is a line chart"
if st.checkbox('Show linechart'):
  chart_data = pd.DataFrame(
      np.random.randn(20, 5), #
      columns=['a', 'b', 'c', 'd', 'f'])

  st.line_chart(chart_data)