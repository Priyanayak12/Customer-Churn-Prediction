
# Customer Churn Prediction

## Project Overview
This project uses Machine Learning to predict whether a telecom customer is likely to leave the company (churn) based on their service usage, contract details, and payment information.

A Streamlit web application allows users to enter customer details and receive a churn prediction with its estimated probability.

## Dataset
- Dataset: IBM Telco Customer Churn
- Original records: 7,043
- Records after cleaning: 7,032
- Features: 19
- Target variable: Churn

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

## Project Workflow
1. Data loading and cleaning
2. Exploratory Data Analysis (EDA)
3. Feature preparation and encoding
4. Train-test splitting
5. Model training
6. Model evaluation and comparison
7. Model saving and loading
8. Streamlit application development

## Machine Learning Models
- Logistic Regression
- Balanced Logistic Regression
- Random Forest Classifier

## Model Evaluation

| Model | Accuracy | Churn Recall |
|---|---:|---:|
| Logistic Regression | 80.38% | 57% |
| Balanced Logistic Regression | 73% | 80% |
| Random Forest | 76.76% | 65% |

Balanced Logistic Regression was selected for the application because identifying more customers who may churn was an important objective.

## Run the Project

### 1. Clone the repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder
```bash
cd Customer-Churn-Prediction
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application
```bash
streamlit run notebooks/app.py
```

## Sample Predictions
- Higher-risk sample customer: 90.17% churn probability
- Lower-risk sample customer: 3.97% churn probability

## Future Improvements
- Improve model performance
- Experiment with additional machine learning algorithms
- Deploy the application online

## Author
Priya Rajesh Nayak
