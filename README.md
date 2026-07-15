# 🚢 Titanic Survival Prediction

A Machine Learning web application that predicts whether a passenger would have survived the Titanic disaster using **Logistic Regression**.

The project includes data preprocessing, model training, evaluation, and deployment using **Streamlit**.

---

## 📌 Project Overview

The Titanic dataset is one of the most popular beginner Machine Learning datasets.

This project predicts passenger survival based on:

- Passenger Class
- Sex
- Age
- Fare
- Embarked Port

The trained model is deployed as an interactive Streamlit web application.

---

## 🚀 Live Demo

https://titanic-survival-prediction-bytaufiq.streamlit.app/

---

## 📸 Application Screenshot

> Add your screenshot inside the **images** folder.

```markdown
![Application Screenshot](images/screenshot.png)
```

---

## 📂 Project Structure

```
titanic-survival-prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── train.csv
│
├── models/
│   ├── logistic_model.pkl
│   └── metadata.pkl
│
└── images/
    └── screenshot.png
```

---

## 🧠 Machine Learning Workflow

1. Load Dataset
2. Exploratory Data Analysis (EDA)
3. Data Cleaning
4. Handle Missing Values
5. Encode Categorical Features
6. Train-Test Split
7. Train Logistic Regression Model
8. Evaluate Model
9. Save Model using Joblib
10. Deploy using Streamlit

---

## 📊 Features Used

| Feature | Description |
|----------|-------------|
| Pclass | Passenger Class |
| Sex | Gender |
| Age | Passenger Age |
| Fare | Ticket Fare |
| Embarked | Port of Embarkation |

---

## 🤖 Model Used

- Logistic Regression

---

## 📈 Model Performance

**Accuracy:** **~80%**

Evaluation Metrics:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Joblib
- Matplotlib
- Seaborn

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/taufiquerafique/titanic-survival-prediction.git
```

Move into the project directory

```bash
cd titanic-survival-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📊 Dataset

Dataset used:

**Titanic - Machine Learning from Disaster**

Available on Kaggle.

---

## 🎯 Future Improvements

- Feature Engineering
- Hyperparameter Tuning
- Random Forest Model
- XGBoost Model
- Better UI/UX
- Model Comparison Dashboard

---

## 👨‍💻 Author

**Taufique Rafique**

GitHub: https://github.com/taufiquerafique

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.