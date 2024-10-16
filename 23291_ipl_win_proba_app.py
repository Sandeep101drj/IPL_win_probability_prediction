import streamlit as st
import pickle
import pandas as pd

# CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f0f5;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 10px;
    }
    .stNumberInput input, .stSelectbox select, .stTextInput input, .stSlider, .stTextArea textarea {
        background-color: white !important;
        border-radius: 8px;
        border: 1px solid #ccc !important;
        padding: 10px !important;
        color: #333;
    }
    .stSelectbox div {
        background-color: transparent !important;
    }
    footer {
        visibility: hidden;
    }
    .footer-text {
        font-size: 12px;
        text-align: center;
        padding: 10px;
        color: grey;
    }
    .css-1v3fvcr {
        background-color: #f5f5f5 !important;
        color: black !important;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
    }
    .block-container {
        max-width: 800px;
        margin: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# Load model
pipe = pickle.load(open('best_model_tuned.pkl', 'rb'))

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["🏏 Prediction", "ℹ️ About"])

if page == "🏏 Prediction":
    # App title
    st.title("🏏 Sandeep's IPL Win Predictor")

    # Teams and cities
    teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
             'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
             'Rajasthan Royals', 'Delhi Capitals']

    cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
              'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
              'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
              'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
              'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
              'Sharjah', 'Mohali', 'Bengaluru']

    # Center match inputs
    with st.container():
        st.subheader(" Match Details")  

        # Select Batting and Bowling Teams
        batting_team = st.selectbox('🏏 Select the batting team', sorted(teams))
        bowling_team = st.selectbox(' Select the bowling team', sorted(teams))  

        # Select City
        selected_city = st.selectbox('🌍 Select host city', sorted(cities))

        # Match details
        target = st.number_input('🎯 Target Score', min_value=1, step=1)
        score = st.number_input('📊 Current Score', min_value=0, step=1)
        overs = st.number_input('⏱️ Overs completed', min_value=1.0, step=0.1)
        wickets = st.number_input('🚫 Wickets out', min_value=0, max_value=10, step=1)

    # Prediction button
    if st.button('🔮 Predict Win Probability'):
        runs_left = target - score
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets
        crr = score / overs
        rrr = (runs_left * 6) / balls_left

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [wickets_left],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        # Predict win probabilities
        result = pipe.predict_proba(input_df)
        win = result[0][1]
        loss = result[0][0]

        # Display result
        st.header(f"🏏 {batting_team} vs {bowling_team}")

        st.subheader(f"💪 Win Probability for {batting_team}:")
        st.progress(win)

        st.subheader(f"💔 Win Probability for {bowling_team}:")
        st.progress(loss)

        st.success(f"{batting_team}: {round(win * 100)}% chance of winning")
        st.error(f"{bowling_team}: {round(loss * 100)}% chance of winning")

elif page == "ℹ️ About":
    st.title("ℹ️ About")
    st.write("""
         
        **IPL Win Probability Prediction**

**Project Overview**

The Indian Premier League (IPL) is one of the most popular cricket leagues worldwide, drawing millions of fans and generating a huge amount of interest in match predictions. However, the dynamic nature of cricket makes it difficult to accurately predict match outcomes, as various factors influence the results, such as team composition, player performance, batting and bowling strengths, and match conditions.

This project aims to tackle this challenge by developing a machine learning model that predicts the win probability of the chasing team based on crucial features such as batting scores, current run rate, required run rate, and more. The model has been trained using historical IPL match data to ensure reliable predictions.


**Features**

Machine Learning Model: Uses historical IPL data to predict the win probability of the chasing team.
Interactive Streamlit App: A user-friendly web application that allows users to input match-specific data and receive real-time win probability predictions.
Key Predictors: Factors like current run rate, required run rate, batting scores, and other match conditions are taken into account.
Engagement and Insights: Aims to enhance fan engagement and provide valuable insights to cricket analysts and enthusiasts.
             
**Data**

The model is trained using IPL match data, focusing on the factors that significantly impact the outcome of a match. The data includes details like match scores, run rates, and other relevant match conditions.


**Technologies Used**

Python: For data processing, model training, and deployment.
Streamlit: For creating the interactive web app.
scikit-learn: For building the machine learning model.
Pandas: For data manipulation and analysis.            
    """)

# Footer
st.markdown("""
    <div class="footer-text">
    Made by Sandeep Pradhan
    </div>
    """, unsafe_allow_html=True)
