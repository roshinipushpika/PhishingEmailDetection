# PhishingEmailDetection
Machine Learning Phishing Email Detection Project using Flask and Scikit-learn

# Phishing Email Detection Model

## Project Overview

This project is a Machine Learning based Phishing Email Detection Model. It is built using Python, Scikit-learn, and Flask. The system analyzes email text and classifies the email as either **Phishing** or **Safe**.

Phishing emails are fake emails that try to steal sensitive information such as passwords, bank details, or personal data. This project helps identify such suspicious emails using text analysis and machine learning.



## Problem Statement

Build a machine learning model using Scikit-learn that can train on phishing and legitimate email data, extract useful features from email text, and classify emails as **Phishing** or **Safe**.

---

## Key Features

- Trains on a dataset of phishing and legitimate emails
- Extracts email text features using TF-IDF Vectorizer
- Analyzes suspicious words and URL-related patterns
- Classifies emails as **Phishing** or **Safe**
- Displays model accuracy
- Displays confusion matrix
- Provides a simple Flask web interface for testing emails



## Technologies Used

- Python
- Scikit-learn
- Pandas
- Flask
- HTML
- CSS
- Joblib



## Machine Learning Algorithm Used

The project uses **Logistic Regression** for classification.

The email text is converted into numerical features using **TF-IDF Vectorizer**. These features are then given to the Logistic Regression model to predict whether the email is phishing or safe.



## Project Structure

```text
PhishingEmailDetection/
│
├── app.py
├── train_model.py
├── emails.csv
├── phishing_model.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
