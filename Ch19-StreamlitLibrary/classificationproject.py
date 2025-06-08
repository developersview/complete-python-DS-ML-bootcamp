import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.title("Iris Flower Classification")
st.write("This app classifies iris flowers based on their features.")

@st.cache_data
def load_data():
    """Load the iris dataset."""
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_names = load_data()

#---------------------------------------------------------
# Apply machine learning model and define input features
#---------------------------------------------------------
model = RandomForestClassifier()
model.fit(df.iloc[:,:-1], df['species'])

st.sidebar.header("User Input Features")
sepal_length = st.sidebar.slider("Sepal Length (cm)", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal Width (cm)", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal Length (cm)", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal Width (cm)", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))   

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

#-------------------
# Make prediction
#-------------------
if st.button("Predict"):
    st.write("Making prediction...")
    prediction = model.predict(input_data)
    prediction_species = target_names[prediction[0]]
    st.subheader("Prediction")
    st.write(f"The predicted species is: **{prediction_species}**")
