# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 00:00:10 2024

@author: DELL
"""

import streamlit as st
import pickle

@st.cache
def load_model():
    with open('classifier.pkl', 'rb') as pickle_in:
        model = pickle.load(pickle_in)
    return model

def main():
    html_temp = """
    <div style="background-color: grey; padding: 16px;">
    <h2 style="color: black; text-align: center;">
        Health Insurance Cost Predictor
    </h2>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Load the model
    model = load_model(model_joblib_gr)
    
    # Input fields
    p1 = st.slider("Enter Your Age", 18, 100)
 
    s1 = st.selectbox("Sex", ("Male", "Female"))
    p2 = 1 if s1 == "Male" else 0

    p3 = st.number_input("Enter Your BMI Value")
    p4 = st.slider("Enter Number of Children", 0, 4) 
 
    s2 = st.selectbox("Smoker", ("Yes", "No"))
    p5 = 1 if s2 == "Yes" else 0
     
    p6 = st.slider("Enter Your Region [1-4]", 1, 4)
 
    # Prediction button
    if st.button('Predict'):
        prediction = model.predict([[p1, p2, p3, p4, p5, p6]])
        st.balloons()
        st.success('Insurance Amount is ${:.2f}'.format(prediction[0])) 
    
if __name__ == '__main__':
    main()
