## Hello Everyone My Name is S.Dinesh Kumar This My First Website by Integrating the trained Machine Learning model and Classify Predictions 

# Sentiment Analysis with Manually Collected Data and Flask Integration

This repository contains code for a sentiment analysis project where sentiment data has been manually collected. The project involves training a machine learning model to analyze the sentiment of text data and deploying it using a Flask web application.

## Results:
![Screenshot 2024-02-27 222833](https://github.com/SDineshKumar1304/Data_Science/assets/125432987/b956f999-e2a4-4ee0-8f80-7dd14a627fe2)
![Screenshot 2024-02-27 222907](https://github.com/SDineshKumar1304/Data_Science/assets/125432987/3962437a-e92c-40ec-88c0-3a7ac6a1d880)
![Screenshot 2024-02-27 222914](https://github.com/SDineshKumar1304/Data_Science/assets/125432987/094f18f8-7648-4c50-a62b-a64f82d6e62f)


## Overview

The goal of this project is to develop a sentiment analysis model capable of classifying text into different sentiment categories. The sentiment data used for training and testing the model has been manually collected to ensure a diverse and representative dataset. The model is integrated into a Flask web application, allowing users to interact with it through a user-friendly interface.

## Data Collection

The sentiment data used in this project was collected manually. The dataset, stored in an Excel file (`Sentiment.xlsx`), includes text samples with corresponding sentiment labels. Details about the manual data collection process, sources, and criteria are explained in the data collection section of the code.

## Data Cleaning

Before training the sentiment analysis model, the collected data undergoes a cleaning process. The `clean_text` function is applied to each text sample, which includes tasks such as lowercasing, HTML tag removal, punctuation removal, and lemmatization. The cleaned data is then used for model training.

## Model Training

The sentiment analysis model is trained using a Support Vector Machine (SVM) classifier with a linear kernel. The cleaned text data is transformed into a bag-of-words representation using the CountVectorizer. The trained model is saved as `Sentiment_classifier_model.joblib`, and the corresponding TF-IDF vectorizer is saved as `vectorizer_model.joblib`.

## Flask Integration

The sentiment analysis model is deployed using a Flask web application. The Flask app (`app.py`) includes routes for user interaction, allowing users to input text through a web interface and receive sentiment predictions in real-time.

## HTML and CSS

The web interface is designed using HTML and CSS to create a visually appealing and intuitive user experience. The structure and styles are defined in the `templates` and `static` directories, respectively.
## Sql Database 

The Sql Database is created for Registration form in the flask

