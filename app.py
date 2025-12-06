import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the model and the cleaned car data
try:
    pipe = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
    car = pd.read_csv('Cleaned Car.csv')
except FileNotFoundError:
    st.error("Model file or data file not found. Please make sure 'LinearRegressionModel.pkl' and 'Cleaned Car.csv' are in the correct directory.")
    st.stop()


# Get unique values for dropdowns
companies = sorted(car['company'].unique())
car_models = sorted(car['name'].unique())
years = sorted(car['year'].unique(), reverse=True)
fuel_types = car['fuel_type'].unique()

# Streamlit app layout
st.title("Car Price Predictor")
st.write("Enter the car details to get a price estimate.")

# Create columns for layout
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox("Select Company", companies)
    year = st.selectbox("Select Year of Purchase", years)
    kms_driven = st.number_input("Enter Kilometers Driven", min_value=0, step=1000)

with col2:
    # Filter models based on selected company
    available_models = sorted(car[car['company'] == company]['name'].unique())
    car_model = st.selectbox("Select Model", available_models)
    fuel_type = st.selectbox("Select Fuel Type", fuel_types)

# Prediction button
if st.button("Predict Price"):
    if kms_driven > 0:
        # Create a DataFrame from user inputs
        input_data = pd.DataFrame(
            [[car_model, company, year, kms_driven, fuel_type]],
            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
        )

        try:
            # Predict the price
            prediction = pipe.predict(input_data)
            
            # Display the result
            st.success(f"## Predicted Price: ₹ {prediction[0]:,.2f}")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
    else:
        st.warning("Please enter the kilometers driven.")

