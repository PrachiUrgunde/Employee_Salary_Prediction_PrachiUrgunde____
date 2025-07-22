import streamlit as st
import pandas as pd
import joblib


#Step 2: Download a background image
import requests
img_url = "https://media.istockphoto.com/id/1553638832/vector/business-coin-stock-and-arrow-up-technology-on-blue-background-investment-profit-income.jpg?s=612x612&w=0&k=20&c=X7ycYQgfKlMUnCeaLFR15NeywbQRF7nJZ-JLoBGYj24="
img_data = requests.get(img_url).content
with open("background.jpg", "wb") as f:
    f.write(img_data)

# Step 3: Create the Streamlit app (app.py)
app_code = ""
import streamlit as st
import base64

# Set background image
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://media.istockphoto.com/id/1553638832/vector/business-coin-stock-and-arrow-up-technology-on-blue-background-investment-profit-income.jpg?s=612x612&w=0&k=20&c=X7ycYQgfKlMUnCeaLFR15NeywbQRF7nJZ-JLoBGYj24=");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        
        .result-box {
            background-color: rgba(0, 0, 0, 0.6);
            border-radius: 12px;
            padding: 1rem;
            margin-top: 2rem;
            color: #fff;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
        }

        .blur {
            background-color: rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 20px;
            max-width: 800px;
            margin: auto;
            color: white;
        }

        /* Global input transparency fix */
        input, select, textarea {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: black !important;
            border: 1px solid rgba(255, 255, 255, 0.3) !important;
            border-radius: 10px !important;
        }

        /* Specifically target number inputs */
        div[data-testid="stNumberInput"] input {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: black !important;
        }

        /* Label color fix */
        label, .stTextInput label, .stNumberInput label, .stSelectbox label {
            color: white !important;
        }

        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            border: none;
            margin-top: 20px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


# Step 3: App layout
set_background()

st.markdown('<h1 style="color:white;">💼 Employee Salary Prediction</h1>', unsafe_allow_html=True)


pipeline = joblib.load('best_pipeline.pkl')

# Form inputs
with st.container():
    st.markdown('<div class="blur">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=17, max_value=90, value=30)
        workclass = st.selectbox("Workclass", ['Private', 'Self-emp-not-inc', 'Local-gov', 'State-gov'])
        education_num = st.slider("Educational-Num", 1, 16, 10)
        capital_gain = st.number_input("Capital Gain", min_value=0, value=0)
        capital_loss = st.number_input("Capital Loss", min_value=0, value=0)

    with col2:
        occupation = st.selectbox("Occupation", ['Prof-specialty', 'Exec-managerial', 'Tech-support', 'Sales'])
        gender = st.selectbox("Gender", ['Male', 'Female'])
        hours_per_week = st.slider("Hours per week", 1, 99, 40)
        race = st.selectbox("Race", ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'])
        relationship = st.selectbox("Relationship", ['Husband', 'Not-in-family', 'Own-child', 'Unmarried'])
        native_country = st.selectbox("Native Country", ['United-States', 'India', 'Mexico', 'Philippines'])

    st.markdown('</div>', unsafe_allow_html=True)


# Encode
gender = 1 if gender == 'Male' else 0
race_mapping = {'White': 4, 'Black': 1, 'Asian-Pac-Islander': 0, 'Amer-Indian-Eskimo': 2, 'Other': 3}
relationship_mapping = {'Husband': 0, 'Not-in-family': 1, 'Own-child': 2, 'Unmarried': 3}
workclass_mapping = {'Private': 3, 'Self-emp-not-inc': 4, 'Local-gov': 1, 'State-gov': 5}
occupation_mapping = {'Prof-specialty': 6, 'Exec-managerial': 0, 'Tech-support': 11, 'Sales': 9}
country_mapping = {'United-States': 38, 'India': 18, 'Mexico': 24, 'Philippines': 29}

# Prepare input
input_df = pd.DataFrame([{
    'age': age,
    'workclass': workclass_mapping[workclass],
    'educational-num': education_num,
    'occupation': occupation_mapping[occupation],
    'gender': gender,
    'hours-per-week': hours_per_week,
    'capital-gain': capital_gain,
    'capital-loss': capital_loss,
    'race': race_mapping[race],
    'relationship': relationship_mapping[relationship],
    'native-country': country_mapping[native_country]
}])

# Predict
if st.button("Predict Income"):
    prediction = pipeline.predict(input_df)[0]
    output = ">50K" if prediction == 1 else "<=50K"
    
    st.markdown(f"""
        <div class="result-box">
            Predicted Income: {output}
        </div>
    """, unsafe_allow_html=True)


