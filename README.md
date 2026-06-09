# ✈️ Airline Passenger Satisfaction Prediction using Machine Learning

## 📌 Project Overview

This project aims to predict whether an airline passenger is **Satisfied** or **Not Satisfied** based on demographic information, travel details, and ratings of various airline services. The project follows a complete end-to-end Machine Learning lifecycle, from data preprocessing to deployment using Streamlit.

The final application provides real-time predictions through an interactive web interface.

---

## 🎯 Problem Statement

Airline companies strive to improve customer experience and retention. Identifying the factors that influence passenger satisfaction helps airlines make data-driven decisions to enhance their services.

The objective of this project is to build a machine learning model that accurately predicts passenger satisfaction.

---

## 📊 Dataset Information

The dataset contains passenger information such as:

* Gender
* Customer Type
* Type of Travel
* Class
* Age
* Flight Distance
* Departure Delay
* Arrival Delay
* Online Boarding
* Seat Comfort
* Leg Room Service
* In-flight Wi-Fi Service
* In-flight Entertainment
* On-board Service
* Food and Drink
* Cleanliness
* Baggage Handling
* Check-in Service
* Gate Location
* Ease of Online Booking
* Departure and Arrival Time Convenience

### Target Variable

* Satisfied
* Not Satisfied

---

## 🔬 Project Workflow

### 1. Data Understanding and Cleaning

* Explored dataset structure and data types.
* Checked for missing values.
* Removed unnecessary columns such as Passenger ID.
* Handled data inconsistencies.

### 2. Exploratory Data Analysis (EDA)

* Analyzed distributions of categorical and numerical features.
* Identified important patterns affecting satisfaction.
* Examined relationships between variables and target class.

### 3. Data Preprocessing

Applied different preprocessing techniques:

#### Categorical Features

* One-Hot Encoding

#### Numerical Features

* Robust Scaling
* Min-Max Scaling (used for Chi-Square feature selection)

Implemented preprocessing using **ColumnTransformer** and **Pipeline**.

---

## 🔍 Feature Selection

Performed multiple feature selection techniques to identify the most influential factors.

### Variance Threshold

* Removed low-variance features.

### Chi-Square Test

* Evaluated categorical feature importance.
* Applied after transforming features into non-negative values.

### Mutual Information

Identified highly informative features contributing to passenger satisfaction.

Top selected features included:

* Online Boarding
* In-flight Wi-Fi Service
* Type of Travel
* Travel Class
* In-flight Entertainment
* Seat Comfort
* Leg Room Service
* On-board Service
* Flight Distance
* Cleanliness

Removed features that provided little predictive value, such as Passenger ID.

---

## 🤖 Models Implemented

The following machine learning algorithms were trained and evaluated:

### Random Forest Classifier

* Ensemble learning approach.
* Used as one of the primary models.

### Logistic Regression

* Baseline linear classification model.

### Support Vector Machine (SVM)

* Effective for high-dimensional feature spaces.

### Naive Bayes

* Fast probabilistic classifier.

### Decision Tree Classifier

* Easy-to-interpret tree-based model.

---

## 📈 Model Evaluation

Models were evaluated using:

* Accuracy Score
* Training Accuracy
* Testing Accuracy
* Train-Test Gap Analysis

Special attention was given to balancing performance and avoiding overfitting by comparing training and testing scores.

The final model was selected based on:

* Predictive performance
* Generalization capability
* Stability across datasets

---

## 🌐 Deployment

Developed an interactive web application using **Streamlit**.

Features of the application:

* User-friendly interface.
* Accepts passenger details as input.
* Performs real-time satisfaction prediction.
* Displays whether the passenger is likely to be satisfied or not satisfied.

Deployment-ready for:

* Streamlit
* Hugging Face Spaces

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib
* Matplotlib
* Git
* GitHub
* Hugging Face Spaces

---

## 📂 Project Structure

Airline-Passenger-Satisfaction-Prediction-ML/

├── app.py

├── model.joblib

├── requirements.txt

├── README.md

├── data/

│   └── airline_passenger_satisfaction.csv

├── notebooks/

└── images/

---

## 🚀 How to Run the Project

Create a new Space on Hugging Face.
Select Streamlit as the SDK.
Upload the following files to the Space repository:
app.py
model.joblib
requirements.txt
README.md
dataset files (if required)
Ensure the requirements.txt file contains all required dependencies:

streamlit

pandas

numpy

scikit-learn==1.6.1

joblib

Hugging Face automatically installs the dependencies and builds the application.
Once the build is complete, the application becomes publicly accessible through the generated Hugging Face Space URL.

---

## 💡 Key Learnings

Through this project, I gained hands-on experience in:

* End-to-end Machine Learning workflow.
* Building preprocessing pipelines.
* Feature selection techniques.
* Comparing multiple classification algorithms.
* Evaluating and mitigating overfitting.
* Model serialization using Joblib.
* Streamlit application development.
* GitHub version control and deployment.

---

## 👩‍💻 Author

**Sireesha Peruri**

B.Tech in Information Technology

Aspiring Data Scientist | Machine Learning Enthusiast

GitHub: https://github.com/perurisiri

---

⭐ If you found this project useful, please consider giving it a star!
