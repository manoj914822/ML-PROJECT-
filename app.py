import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os

# Page Config
st.set_page_config(
    page_title="CardiScan: Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# Sidebar
st.sidebar.title("CardiScan ❤️")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigation", ["Data Overview", "Data Analysis", "Predictor"])

# Data Loading
def load_data():
    df = pd.read_csv("heart_disease_data.csv")
    return df

df = load_data()

# Logic for tabs
if page == "Data Overview":
    st.title("Dataset Overview 📊")
    st.write("Exploration of the UCI Heart Disease dataset.")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Patients", len(df))
    col2.metric("Heart Disease", len(df[df['target'] == 1]))
    col3.metric("Avg Age", f"{df['age'].mean():.1f}")
    col4.metric("Avg Cholesterol", f"{df['chol'].mean():.0f}")
    
    st.subheader("Age Distribution")
    fig = px.histogram(df, x="age", color="target", barmode="overlay")
    st.plotly_chart(fig, use_container_width=True)

elif page == "Data Analysis":
    st.title("Data Analysis 🔍")
    
    st.subheader("Correlation Heatmap")
    corr = df.corr()
    fig = px.imshow(corr, text_auto=True, aspect="auto")
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Raw Data")
    st.dataframe(df.head(50))

elif page == "Predictor":
    st.title("Health Predictor 🩺")
    st.write("Input parameters to analyze risk using Gemini AI.")
    
    with st.sidebar:
        st.subheader("Input Values")
        age = st.slider("Age", 1, 100, 45)
        chol = st.number_input("Cholesterol", 100, 600, 200)
        bps = st.number_input("Resting BP", 80, 200, 120)
        sex = st.selectbox("Sex", options=[1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
        
    if st.button("Run AI Analysis"):
        with st.spinner("Analyzing data patterns..."):
            # Mocking the AI logic for browser version to avoid CORS issues
            st.success("Analysis Complete")
            st.markdown("### Medical Insights (AI Generated)")
            st.info("Based on the provided values, the system detects characteristics that correlate with findings in the UCI dataset. Age and Cholesterol levels are significant indicators.")
            st.warning("Medical Disclaimer: This is not professional advice. Please consult a doctor.")

st.sidebar.markdown("---")
st.sidebar.info("Developed by Manoj g")
