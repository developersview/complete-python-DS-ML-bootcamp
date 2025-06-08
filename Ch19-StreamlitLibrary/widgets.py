import streamlit as st
import pandas as pd


st.title("Streamlit Widgets Example")
st.write("This application demonstrates various Streamlit widgets.")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")


age = st.slider("Select your age:", 0, 100, 25)
if age:
    st.write(f"You are {age} years old.")

options = ["Python", "JavaScript", "Java", 'R', "C++", "Go"]
choice = st.selectbox("Choose a programming language:", options)
if choice:
    st.write(f"You selected: {choice}")


data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
st.write("Here is a sample DataFrame:")
if st.button("Show DataFrame"):
    st.dataframe(df)

if st.button("Convert to csv"):
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="data.csv",
        mime="text/csv"
    )
    st.write("DataFrame converted to CSV and saved as 'data.csv'.")



# File uploader widget
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    uploaded_df = pd.read_csv(uploaded_file)
    st.write("Uploaded DataFrame:")
    st.dataframe(uploaded_df)

    if st.button("Show Summary"):
        st.write(uploaded_df.describe())
