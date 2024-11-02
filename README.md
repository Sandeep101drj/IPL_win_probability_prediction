# IPL Win Probability Prediction

## Introduction
The Indian Premier League (IPL) is one of the most popular cricket leagues globally, drawing significant attention from fans and analysts alike. This project addresses the challenge of predicting match outcomes, particularly the win probability of the chasing team, by utilizing various match-specific features through machine learning.

## Overview
This project aims to develop a predictive model that evaluates the likelihood of the chasing team winning a match based on critical parameters such as batting scores, current run rate, and required run rate. By integrating the model into an interactive Streamlit web application, users can input relevant match data and receive real-time win probability predictions.

## Objective
- To create a machine learning model that predicts the win probability of the chasing team in IPL matches.
- To develop an interactive application using Streamlit that allows users to input match-specific data and receive predictions.
- To explore various machine learning algorithms, perform data preprocessing, and conduct hyperparameter tuning to optimize model performance.

## Description
The project involves several key steps:
1. **Data Collection**: The dataset is sourced from CSV files containing information on IPL matches and deliveries.
2. **Data Preprocessing**: Data is cleaned and transformed to extract meaningful features, such as total runs, wickets, balls left, and run rates.
3. **Exploratory Data Analysis (EDA)**: Analysis is performed to understand the data distribution, identify trends, and visualize relationships between features.
4. **Feature Engineering**: New features are created to improve the predictive capability of the model, including current score, runs left, balls left, wickets left, and run rates.
5. **Model Building**: Various machine learning algorithms, such as Logistic Regression, Random Forest, and Gradient Boosting, are employed to develop the predictive model.
6. **Hyperparameter Tuning**: Techniques such as Grid Search are used to fine-tune the model for better accuracy and reliability.
7. **Interactive Application Development**: An application is built using Streamlit, enabling users to input match data and obtain instant predictions on win probability.

## Results
- The accuracy scores of the models are evaluated, with Gradient Boosting and Logistic Regression showing promising results.
- The final model is exported for deployment, providing a user-friendly interface through the Streamlit application.

## Analysis
The project demonstrates the effectiveness of machine learning in sports analytics, particularly in predicting match outcomes based on historical data. The accuracy of the predictions varies across different models, highlighting the importance of feature selection and model tuning in achieving reliable results.

## Conclusion
This project showcases the potential of machine learning in the realm of sports analytics, particularly in cricket. By providing fans and analysts with real-time win probability predictions, the interactive application enhances the engagement and understanding of match dynamics. The integration of advanced analytics into sports can significantly inform decision-making for teams and fans alike.

## Future Work
- Expand the dataset to include more matches for improved model training.
- Explore additional features, such as player statistics and weather conditions, for better predictions.
- Enhance the Streamlit application with more user-friendly features and data visualizations.

