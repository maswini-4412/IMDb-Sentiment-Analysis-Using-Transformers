import streamlit as st
from transformers import pipeline

# Load model
classifier = pipeline("sentiment-analysis")

st.title("IMDb Movie Review Sentiment Analysis")

review = st.text_area("Enter Movie Review")

if st.button("Predict"):

    if review != "":

        result = classifier(review[:512])

        label = result[0]['label']
        score = result[0]['score']

        st.write("Sentiment:", label)
        st.write("Confidence:", round(score, 2)) 