import streamlit as st
import pandas as pd
import numpy as np

#title of the application
st.title("Hello World!")

##Display a text
st.write("This is a simple Streamlit application.")

#create a dataframe
df = pd.DataFrame({
    'first column': np.random.uniform(0, 100, 10),
    'second column': np.random.uniform(0, 100, 10),
    'third column': np.random.uniform(0, 100, 10),
    'fourth column': np.random.uniform(0, 100, 10),
    'fifth column': np.random.uniform(0, 100, 10)
})

st.write("Here is a dataframe with random numbers:")
st.dataframe(df)

#create a button
if st.button('Click me!'):
    chart_data6 = df[['first column', 'second column', 'third column']]
    st.line_chart(chart_data6)
    chart_data4 = df[['fourth column', 'fifth column']]
    st.line_chart(chart_data4)
    