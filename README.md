# Spam-Mail-Prediction
The Spam Mail Detection project uses machine learning to classify emails as spam or not. It includes data cleaning, TF-IDF feature extraction, Logistic Regression for training, and evaluation using accuracy and F1-score. The model is deployed on the web using Streamlit for user interaction.
The Spam Mail Detection project focuses on identifying unwanted or harmful emails using machine learning, specifically the Logistic Regression algorithm. With the increasing volume of daily email traffic, automated spam detection has become essential for maintaining productivity and protecting users from scams and malicious content.

The project begins with data acquisition, typically using a public dataset that includes labeled email messages categorized as either "spam" or "ham" (non-spam). The dataset is explored and analyzed to understand the structure and class distribution. In most cases, spam messages are fewer than ham messages, requiring attention to class balance.

The next phase involves data preprocessing, where emails are cleaned by removing punctuation, special characters, stopwords, and HTML tags. The text is then tokenized and lemmatized to reduce words to their base form, ensuring that the model focuses on meaningful content. Once cleaned, the text data is converted into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency), which measures how important a word is in a message relative to the entire dataset.

Once features are extracted, the data is split into training and testing sets, and the Logistic Regression model is trained. Logistic Regression is effective for binary classification tasks like spam detection due to its simplicity and high performance. The model learns to distinguish between spam and non-spam messages based on the frequency and combination of words in the emails.

The model’s performance is evaluated using standard metrics like accuracy, precision, recall, and F1-score. These metrics help determine how well the model is able to correctly classify spam and avoid false positives.

To make the project interactive and user-friendly, it is deployed as a web application using Streamlit. Users can input an email message directly into the web interface, and the app will classify it as spam or not in real time, displaying the prediction instantly.

In conclusion, this project showcases the power of machine learning and natural language processing for building an effective, accessible, and deployable spam detection system.
