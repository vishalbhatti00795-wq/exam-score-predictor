# 🎯 EXAMAI — Exam Score Predictor
[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-View%20App-success?style=for-the-badge)](https://vishal-exam-score-predictor.streamlit.app/#predict-your-exam-scorewith-ai)

> **AI-powered academic performance prediction using XGBoost Regression**

EXAMAI is a Machine Learning-based **Exam Score Predictor** that estimates a student's exam score based on academic, lifestyle, and learning-environment factors.

The project uses a trained **XGBoost Regressor** model and provides an interactive **Streamlit web application** with a modern black and crimson-red interface for real-time predictions.

---

## 📌 Project Overview

Student performance can be influenced by several factors such as study time, attendance, sleep, study methods, and the quality of the learning environment.

This project applies **Supervised Machine Learning** to learn relationships between these factors and exam scores.

The trained XGBoost model takes the student's profile as input and produces an estimated exam score on a **0–100 scale**.

### Prediction Pipeline

```text
Student Information
        ↓
Data Preprocessing
        ↓
Categorical Encoding
        ↓
Feature Preparation
        ↓
Trained XGBoost Model
        ↓
Predicted Exam Score
        ↓
Performance Interpretation
```

---

## ✨ Features

* 🎯 Exam score prediction
* 🤖 XGBoost Regression model
* 📊 Interactive Streamlit dashboard
* 🌙 Premium black & crimson-red UI
* 📈 Prediction score visualization
* 🏆 Automatic performance categorization
* 📋 Student prediction breakdown
* 🔍 XGBoost feature importance visualization
* ⚡ Cached model loading for efficient inference
* 🛡️ Error handling for model and preprocessing issues
* 🔐 Uses saved model and label encoders without retraining

---

## 🧠 Machine Learning Model

The project uses **XGBoost Regressor** for predicting continuous exam scores.

XGBoost is an ensemble learning algorithm based on gradient boosting decision trees. It is well suited for structured/tabular data and can capture nonlinear relationships between input features and the target variable.

### Model Configuration

The best model configuration obtained during hyperparameter tuning:

| Hyperparameter       |               Value |
| -------------------- | ------------------: |
| Algorithm            |   XGBoost Regressor |
| Learning Rate        |                0.05 |
| Maximum Depth        |                   3 |
| Number of Estimators |                 300 |
| Subsample            |                 0.8 |
| Cross Validation     | 3-Fold GridSearchCV |

---

## 📊 Model Performance

The selected XGBoost model achieved the following performance on the project evaluation:

| Metric       |      Score |
| ------------ | ---------: |
| **R² Score** | **0.7290** |
| **RMSE**     | **9.8454** |

### R² Score

An R² score of **0.7290** indicates that the model explains approximately **72.9% of the variance** in the target exam scores on the evaluated data.

### RMSE

The model achieved an **RMSE of 9.8454**, meaning the typical prediction error is on the order of roughly 9.85 score points under the evaluation used in the project.

---

## 📥 Input Features

The prediction model uses the following six features:

| Feature            | Description                                 |
| ------------------ | ------------------------------------------- |
| `study_hours`      | Average study hours                         |
| `class_attendance` | Student class attendance                    |
| `sleep_hours`      | Average sleep duration                      |
| `sleep_quality`    | Quality of the student's sleep              |
| `study_method`     | Student's study method                      |
| `facility_rating`  | Rating of the available learning facilities |

Categorical variables are processed using the saved label encoders before being passed to the trained model.

---

## 📈 Feature Importance

The application provides a feature-importance visualization extracted directly from the trained XGBoost model.

This helps understand which input variables contribute most strongly to the model's predictions.

The feature-importance values shown in the application are obtained from:

```python
model.feature_importances_
```

rather than being manually assigned.

---

## 🖥️ Streamlit Application

The project includes a complete interactive Streamlit interface called **EXAMAI**.

### Dashboard Sections

**1. Hero Section**

Introduces the Exam Score Predictor and its AI-powered prediction capabilities.

**2. Student Profile**

Users enter the academic, lifestyle, and learning-environment information required by the model.

**3. AI Prediction**

Displays the predicted exam score prominently on a 0–100 scale.

**4. Performance Category**

The predicted score is interpreted into categories:

|    Score | Category          |
| -------: | ----------------- |
|   90–100 | Outstanding       |
|    80–89 | Excellent         |
|    70–79 | Good              |
|    60–69 | Average           |
| Below 60 | Needs Improvement |

**5. Prediction Breakdown**

Displays a summary of the values submitted for prediction.

**6. Model Information**

Displays information about the XGBoost model, task type, and selected hyperparameters.

**7. Feature Importance**

Visualizes the relative importance of the model's input features.

---

## 🎨 UI Design

The Streamlit application uses a premium **black + rich crimson-red** theme.

### Design Characteristics

* Dark cinematic background
* Crimson-red accents
* Glassmorphism-inspired cards
* Rounded UI components
* Red glow effects
* Interactive score gauge
* Responsive two-column layout
* Minimal visual clutter
* Modern typography
* Subtle hover animations

The goal is to make the application feel more like a **professional AI/EdTech product** than a conventional Machine Learning demo.

---

## 🛠️ Technologies Used

### Programming Language

* **Python**

### Machine Learning

* **XGBoost**
* **Scikit-learn**

### Data Processing

* **Pandas**
* **NumPy**

### Visualization

* **Plotly**

### Web Application

* **Streamlit**

### Model Persistence

* **Pickle**

---

## 📁 Project Structure

```text
exam-score-predictor/
│
├── app.py
├── best_xgb_model.pkl
├── label_encoders.pkl
├── requirements.txt
└── README.md
```

### File Description

| File                 | Purpose                          |
| -------------------- | -------------------------------- |
| `app.py`             | Streamlit web application        |
| `best_xgb_model.pkl` | Trained XGBoost model            |
| `label_encoders.pkl` | Saved categorical label encoders |
| `requirements.txt`   | Python dependencies              |
| `README.md`          | Project documentation            |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/exam-score-predictor.git
```

Navigate into the project directory:

```bash
cd exam-score-predictor
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔮 How It Works

When a user enters the required student information:

```text
Input
 ↓
Categorical Encoding
 ↓
Pandas DataFrame
 ↓
XGBoost Model
 ↓
Score Prediction
 ↓
Performance Category
```

The application loads the trained model using Streamlit resource caching, applies the saved categorical encoders, prepares the input in the required feature order, and sends it to the XGBoost model.

The model then returns a continuous predicted exam score.

---

## 🔒 Model Usage

The Streamlit application **does not retrain the Machine Learning model**.

Instead, it loads the previously trained artifacts:

```text
best_xgb_model.pkl
label_encoders.pkl
```

This makes the application focused on **model inference and deployment**.

---

## ⚠️ Disclaimer

The predicted exam score is an **estimate generated by a Machine Learning model** based on the provided inputs.

It should not be interpreted as a guaranteed examination result or a definitive assessment of a student's academic ability.

---

## 👨‍💻 Author

**Vishal Bhatti**

B.Tech — Artificial Intelligence & Robotics Engineering

Interested in:

* Machine Learning
* Artificial Intelligence
* Data Science
* Computer Vision
* Python
* Predictive Analytics

---

## ⭐ Project

If you find this project useful or interesting, consider giving the repository a **star ⭐** on GitHub.
