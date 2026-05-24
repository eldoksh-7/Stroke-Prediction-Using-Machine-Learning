# Stroke Prediction Using Machine Learning

A Machine Learning project for predicting stroke risk using healthcare data analysis and predictive modeling techniques.

---

# 👨‍💻 Project Information

### Project Author:
Mohamed Ashour

### Project Supervisor:
Dr. Mohamed Elsayeh

### Presentation Video:
:contentReference[oaicite:0]{index=0}

---

# 📌 Project Overview

Stroke is considered one of the leading causes of death worldwide. Early prediction can help reduce complications and improve healthcare decision-making.

The main objective of this project is to build a Machine Learning model capable of predicting stroke risk based on patient medical and lifestyle information.

---

# 📊 Dataset

The project uses a large synthetic healthcare dataset containing approximately 50,000 records with multiple medical features such as:

- Age
- BMI
- Average Glucose Level
- Hypertension
- Heart Disease
- Smoking Status
- Work Type
- Residence Type

---

# ⚙️ Project Workflow

## 1. Data Cleaning
- Handling missing values
- Data preprocessing
- Encoding categorical variables
- Converting target variable into binary classification

---

## 2. Exploratory Data Analysis (EDA)

Several visualizations and analyses were performed including:
- Count Plots
- Histograms
- Heatmaps
- Boxplots
- Correlation Analysis

---

## 3. Feature Engineering

New features were created to improve model performance:
- Age Group
- BMI Category
- Risk Score

---

## 4. Machine Learning Models

The following Machine Learning models were trained and compared:
- Logistic Regression
- Decision Tree
- Random Forest

---

## 5. Hyperparameter Tuning

GridSearchCV was applied to optimize model parameters and improve prediction performance.

---

## 6. Model Deployment

The final model was deployed using Flask / Streamlit as a simple web application for real-time stroke prediction.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Flask / Streamlit

---

# 📈 Evaluation Metrics

The models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score

Random Forest achieved the best overall performance.

---

# 📂 Project Structure

```text
stroke_project/
│
├── app.py
├── stroke_model.pkl
├── Stroke_Project.ipynb
├── templates/
│   └── index.html
├── README.md
