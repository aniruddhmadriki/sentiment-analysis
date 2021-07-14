import streamlit as st
from PIL import Image
import nltk
import re
import string
import pickle
from nltk.tokenize.toktok import ToktokTokenizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.tokenize.toktok import ToktokTokenizer
import nltk
model = pickle.load(open('SentimentAnalysis.p','rb'))
st.title("Sentiment Analysis")
st.subheader("Enter Text to analyise: ")
text = st.text_input(" ")
text = [text]
y_out = model.predict(text)

if st.button("Predict"):
        

        if (y_out == "Positive"):
            image = Image.open("happy.jpeg")
            st.image(image,width = 250)
            st.header("WOW!! That's Positive review")
        else:
            image = Image.open("sad.jpeg")
            st.image(image,width = 250)
            st.header("That's Negative review")
