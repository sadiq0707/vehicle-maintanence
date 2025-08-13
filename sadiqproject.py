import streamlit as st

import joblib

gb_model=joblib.load("vehicle_maintenance_data_final1_model.pkl")
l1=joblib.load("encoder1.pkl")
l2=joblib.load("encoder2.pkl")
l3=joblib.load("encoder3.pkl")
l4=joblib.load("encoder4.pkl")
l5=joblib.load("encoder5.pkl")
l6=joblib.load("encoder6.pkl")
l7=joblib.load("encoder7.pkl")
s=joblib.load("scaler.pkl")

st.title("vehicle_maintenance")
st.write("Enter Data Description")

Maintenance_History=st.selectbox(' Enter Your Maintenance_History ',['Good','Average','Poor'])
Reported_Issues=st.number_input(' Enter Your Reported_Issues ')
Vehicle_Age=st.number_input(' Enter Vehicle_Age')
Fuel_Type=st.selectbox('Enter Fuel_Type',['Electric','Petrol','Diesel'])
Transmission_Type=st.selectbox('Ener Transmission_Type',['Automatic','Manual')
Engine_Size=st.number_input('Enter Engine_Size')
Odometer_Reading=st.number_input(' Enter Odometer_Reading')
Owner_Type=st.selectbox('Enter Owner_Type',['First','Second','Third'])
Insurance_Premium=st.number_input(" Enter Insurance_Premium")
Service_History=st.number_input("Enter Service_History")
Accident_History=st.number_input("Accident_History")
Fuel_Efficiency=st.number_input("Enter Fuel_Efficiency")
Tire_Condition=st.selectbox('Enter Tire_Condition',['New','Good','Worn out'])
Brake_Condition=st.selectbox('Enter Brake_Condition',['New','Good','Worn out'])
Battery_Status=st.selectbox('Enter Battery_Status',['New','Good','Weak'])




Maintenance_History=l1.fit_transform(data[Maintenance_History])[0]
Fuel_Type=l2.fit_transform(data[Fuel_Type])[0]
Transmission_Type=l3.fit_transform(data[Transmission_Type])[0]
Owner_Type=l4.fit_transform(data[Owner_Type])[0]
Tire_Condition=l5.fit_transform(data[Tire_Condition])[0]
Brake_Condition=l6.fit_transform(data[Brake_Condition])[0]
Battery_Status=l7.fit_transform(data[Battery_Status])[0]
if st.button("predict"):
    result=model.predict(s.transform([[Maintenance_History,Reported_Issues,Vehicle_Age,Fuel_Type,Transmission_Type,Engine_Size,Odometer_Reading,Owner_Type,
                                       Insurance_Premium,Service_History,Accident_History,Fuel_Efficiency,Tire_Condition,Brake_Condition,Battery_Status]]))[0]
    st.success('the output is {}'.format(result))



