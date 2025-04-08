import numpy as np
import pickle

# Load the trained model
loaded_model = pickle.load(open('C:/Users/Asus/OneDrive/Desktop/PYPROJECT_Anaconda/Spam mail prediction project/trained_model.sav', 'rb'))

# Load the feature extraction (vectorizer)
feature_extraction = pickle.load(open('C:/Users/Asus/OneDrive/Desktop/PYPROJECT_Anaconda/Spam mail prediction project/vectorizer.sav', 'rb'))

# Input mail to test
input_mail = ["Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat..."]

# Transform input mail using loaded vectorizer
input_data_features = feature_extraction.transform(input_mail)

# Make prediction
prediction = loaded_model.predict(input_data_features)

# Output result
print(prediction)
if prediction[0] == 1:
    print('Ham mail')
else:
    print('Spam mail')
