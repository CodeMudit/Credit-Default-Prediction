# Credit Default Prediction System

An end-to-end Machine Learning application that predicts whether a customer is likely to default on a loan based on their financial information. The project combines an **XGBoost classification model**, a **FastAPI backend**, and a **Streamlit frontend** to provide real-time credit risk predictions.

---

## Overview

Financial institutions need to assess the likelihood of a customer defaulting on a loan before approving credit. This project uses historical financial data to predict whether a customer is likely to default, helping demonstrate how machine learning can support decision-making.

---

## Features

* Predicts whether a customer is likely to default on a loan.
* Displays the probability of default.
* Classifies customers into Low, Medium, or High Risk.
* Interactive web interface built with Streamlit.
* REST API powered by FastAPI.
* Machine Learning model built using XGBoost.
* Clean and user-friendly interface.

---

## Tech Stack

### Machine Learning

* Python
* XGBoost
* Scikit-learn
* Pandas
* NumPy

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Tools

* Git
* GitHub

---

## Project Structure

```text
Credit-Default-Prediction/
│
├── Backend/
│   ├── predictor.py
│   ├── predict.py
│   ├── schemas.py
│   └── models/
│
├── Frontend/
│   └── app.py
│
├── data/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

## How It Works

1. The user enters customer financial information.
2. Streamlit sends the data to the FastAPI backend.
3. The backend preprocesses the input using the trained scaler.
4. The XGBoost model predicts the customer's credit risk.
5. The API returns:

   * Prediction
   * Probability of Default
   * Risk Level
6. Streamlit displays the prediction in a simple dashboard.

---

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Credit-Default-Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶Running the Project

### Start the FastAPI Backend

```bash
uvicorn Backend.predict:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

### Start the Streamlit Frontend

```bash
streamlit run Frontend/app.py
```

---

## Model Information

* **Algorithm:** XGBoost Classifier
* **Task:** Binary Classification
* **Target Variable:** Loan Default (Yes / No)

---

## Prediction Output

The application provides:

* Default / No Default prediction
* Probability of Default
* Risk Category
* Model Accuracy

---

## Screenshots

Include screenshots here after deployment.

### Home Page

![alt text](<Screenshot From 2026-07-29 23-39-55.png>)

### Prediction Result

![alt text](<Screenshot From 2026-07-29 23-40-30.png>)


---

## Future Improvements

* Deploy the backend to a cloud platform.
* Add SHAP values for model explainability.
* Support batch predictions from CSV files.
* Improve the dashboard with charts and analytics.
* Add user authentication.

---

## Live Demo

Frontend:
https://credit-default-prediction-2.streamlit.app

Backend:
https://credit-default-prediction-2.onrender.com

API Docs:
https://credit-default-prediction-2.onrender.com/docs

## Author

**Mudit Sapra**

---


