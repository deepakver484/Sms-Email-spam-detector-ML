import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

tfidf = pickle.load(open("vectorizer.pkl",'rb'))
model = pickle.load(open("model.pkl",'rb'))

def Transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    L = []

    for i in text:
        if i.isalnum():
            L.append(i)
            
    text = L[:]
    L.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            L.append(i)
            
    text = L[:]
    L.clear()
    for i in text:
        L.append(ps.stem(i)) 
        
    return " ".join(L)


st.title("Emall/SMS Spam Classifier")

input_sms = st.text_input("Enter Your Message")
if st.button('Predict'):
    trans_sms = Transform_text(input_sms)

    vector_input = tfidf.transform([trans_sms])

    result = model.predict(vector_input)[0]

    if result==1:
        st.header("Spam")
    else:
        st.header("Not Spam")