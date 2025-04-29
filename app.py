import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv('predicted_risk_levels.csv')

# Title
st.title("HIV Outbreak Risk Prediction Dashboard")

# Show dataset
st.subheader("Predicted Risk Levels")
st.dataframe(data)

# Add a score for graphing
data['RiskScore'] = data['PredictedRisk'].apply(lambda x: 1 if x == 'High Risk' else 0)

# Visualize
fig = px.bar(data, x='District', y='RiskScore', color='PredictedRisk',
             color_discrete_map={"High Risk": "red", "Low Risk": "green"},
             title="District Risk Levels")
st.plotly_chart(fig)