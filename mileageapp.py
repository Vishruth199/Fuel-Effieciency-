import streamlit as st
import pandas as pd
import joblib
import webbrowser


model=joblib.load('mileage_model.pkl') 
st.title(' MILEAGE PREDICTION ')

st.write("Details Required")
no_cylinder=st.number_input('Enter the number of cylinders')
hp=st.number_input('Enter the Horsepower')
acceleration=st.number_input('Time it takes to reach 0-100 kmph in seconds (Acceleration) ')
model_year=st.number_input('Enter the model year')
if model_year <2000:
    model_year=model_year%100
else:
    model_year=100

origin_country = st.selectbox('Select the origin of the car',['india'])

if(origin_country=='india'):
    origin=1


displacement=st.number_input('Enter the engine displacement in cc')

weight=st.number_input('Enter the weight in kg()')

mileage=model.predict([[no_cylinder,hp,acceleration,model_year,origin,displacement,weight]])

Button = st.button("Calculate Mileage")


if Button:    
    st.title(f""" Mileage of the vehicle is""")
    st.title(f"""{round(mileage[0]*1.6,2)} kmpl """)

st.write("    ")
st.write("    ")
