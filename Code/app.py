# Import required libraries
import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

# Load the TF-IDF vectorizer and the trained model from pickle files
tfidf = pickle.load(open("vectorizer.pkl",'rb'))
model = pickle.load(open("model.pkl",'rb'))

# Function to preprocess and transform input text
def Transform_text(text):
    # Convert the text to lowercase
    text = text.lower()
    # Tokenize the text into words
    text = nltk.word_tokenize(text)
    L = []

    # Filter out non-alphanumeric tokens
    for i in text:
        if i.isalnum():
            L.append(i)
            
    text = L[:]
    L.clear()
    
    # Remove stopwords and punctuation
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            L.append(i)
            
    text = L[:]
    L.clear()
    
    # Apply stemming to words
    for i in text:
        L.append(ps.stem(i)) 
        
    return " ".join(L)

# Streamlit app title
st.title("Emall/SMS Spam Classifier")

# Text input field for user to enter a message
input_sms = st.text_input("Enter Your Message")

# Button to trigger prediction
if st.button('Predict'):
    # Preprocess the input message
    trans_sms = Transform_text(input_sms)
    
    # Transform the preprocessed message using TF-IDF vectorizer
    vector_input = tfidf.transform([trans_sms])
    
    # Make a prediction using the trained model
    result = model.predict(vector_input)[0]
    
    # Display the prediction result
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
