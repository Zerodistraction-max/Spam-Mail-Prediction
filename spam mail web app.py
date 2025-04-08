# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 16:19:18 2025
@author: Asus
"""

import numpy as np
import pickle 
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('C:/Users/Asus/OneDrive/Desktop/PYPROJECT_Anaconda/Spam mail prediction project/trained_model.sav', 'rb'))

# Load the fitted vectorizer
feature_extraction = pickle.load(open('C:/Users/Asus/OneDrive/Desktop/PYPROJECT_Anaconda/Spam mail prediction project/vectorizer.sav', 'rb'))

# Prediction function
def spam_mail_prediction(input_mail):
    input_data_features = feature_extraction.transform(input_mail)
    prediction = loaded_model.predict(input_data_features)

    if prediction[0] == 1:
        return 'Ham mail'
    else:
        return 'Spam mail'

# Streamlit app
def main():
    st.title('Spam Mail Prediction Web App')
    Message = st.text_input('Enter mail content:')
    analysis = ''
    if st.button('Test the mail'):
        analysis = spam_mail_prediction([Message])
    st.success(analysis)

if __name__ == '__main__':
    main()
