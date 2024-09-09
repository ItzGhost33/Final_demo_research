import streamlit as st
import pickle
import numpy as np

with open('model_folder/xgboost_ckd_model.pkl', 'rb') as file:
    model_ckd = pickle.load(file)

with open('model_folder/xgboost_ckd_model_no_scr.pkl', 'rb') as file:
    model_other = pickle.load(file)

def predict_ckd(features):
    prediction = model_ckd.predict([features])
    return prediction[0]

#     prediction = model_other.predict([features])
#     return prediction[0]

st.title("CKD Predictor")
model_choice = st.selectbox("Which model would you like to use?", ("xgboost_ckd_model", "xgboost_ckd_model_no_scr"))

if model_choice == "xgboost_ckd_model":
    st.header("xgboost_ckd_model - Input Features")
    
    cr = st.number_input("Serum Creatinine", min_value=0.0, max_value=4000.0, step=0.1)
    age = st.number_input("Age", min_value=0.0, max_value=100.0,step =0.1)
    weight = st.number_input("Weight", min_value=0.0, max_value=200.0,step =0.1)
    al = st.number_input("Albumin", min_value=0.0, max_value=1000.0, step=0.1)
    # gender = st.number_input("Gender--- If male put 1 else 0", min_value=0.0, max_value=1.0, step=0.1)
    option = st.selectbox(
        'Select the gender',
        ('Male', 'Female'))
    if option=='Male':
        gender=1.0
    elif option =='Female':
        gender =0.0

    
    na = st.number_input("Sodium", min_value=0.0, max_value=1000.0, step=0.1)
    gl = st.number_input("Glucose", min_value=0.0, max_value=1000.0, step=0.1)
    ca = st.number_input("Calcium", min_value=0.0, max_value=1000.0, step=0.1)
    cl = st.number_input("Chloride", min_value=0.0, max_value=1000.0, step=0.1)
    k = st.number_input("Pottasium", min_value=0.0, max_value=1000.0, step=0.1)
    
    if st.button("Predict CKD"):
        features = [cr,age, weight,al,gender,na,gl,ca,cl,k]
        result = predict_ckd(features)
        st.success(f"Prediction: {'CKD Positive' if result == 1 else 'CKD Negative'}")
        # st.success(result)
        
elif model_choice == "xgboost_ckd_model_no_scr":
    st.header("xgboost_ckd_model_no_scr - Input Features")
    
    age = st.number_input("Age", min_value=0, max_value=100)
    weight = st.number_input("Blood Pressure", min_value=0, max_value=200)
    # cr = st.number_input("Serum Creatinine", min_value=0.0, max_value=10.0, step=0.1)
    al = st.number_input("Albumin", min_value=0.0, max_value=10.0, step=0.1)
    gender = st.number_input("Gender--- If male put 1 else 0", min_value=0, max_value=1, step=1)
    na = st.number_input("Sodium", min_value=0.0, max_value=10.0, step=0.1)
    gl = st.number_input("Glucose", min_value=0.0, max_value=10.0, step=0.1)
    ca = st.number_input("Calcium", min_value=0.0, max_value=10.0, step=0.1)
    cl = st.number_input("Chloride", min_value=0.0, max_value=10.0, step=0.1)
    k = st.number_input("Pottasium", min_value=0.0, max_value=10.0, step=0.1)
    
    if st.button("Predict with Other Model"):
        features = [age, weight,al,gender,na,gl,ca,cl,k]  
        result = predict_ckd(features)
        st.success(f"Prediction: {'CKD Positive' if result == 1 else 'CKD Negative'}")

