💼 Employee Salary Prediction
A sleek and interactive machine learning web application that predicts whether an individual's salary is more than 50K or not based on their demographic and employment attributes. Built using **Streamlit** and deployed on **Streamlit Cloud**.

📊 Project Overview
This project uses the **UCI Adult Income dataset** to build a classification model that predicts whether an employee earns **more than $50K** annually. It uses features like:

- Age
- Workclass
- Education
- Occupation
- Sex
- Hours per week
- Capital Gain
- Capital Loss

 🖥️ Features

- 📈 Predict salary class using a trained ML model
- 🎨 Transparent input fields with blurred background UI
- ⚙️ Gradient Boosting Classifier for high accuracy
- 🌐 Streamlit Cloud deployment for global access
- 📁 Easily extendable and modular code structure


🚀 Live Demo

👉 [Click here to view the deployed app](https://employee-salary-prediction-prachiurgunde-73fv6gk8ae8vhod8u3bc7t.streamlit.app/)  


📦 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Joblib
- Streamlit (Frontend & Deployment)


🔍 Files in the Repository
 `app.py`  -  Main Streamlit app with UI and model prediction 
`best_pipeline.pkl`   -  Serialized ML pipeline (Gradient Boosting Classifier) 
`requirements.txt` -  Python dependencies for deployment 
`README.md'  -    Project documentation (this file) 




🧠 ML Model Details

- **Algorithm**: Gradient Boosting Classifier
- **Target**: `salary` (binary: >50K or ≤50K)
- **Accuracy Achieved**: ~87%
- **Preprocessing**: Categorical encoding, numerical scaling
- **Serialization**: Using `joblib`

👩‍💻 Author
Prachi Urgunde


