import streamlit as st
import pickle

# "/app/{repository name}/ {file.extension}"
pkl_filename = "/app/pickle-demo/Model.pkl"

# Load the pickled model
model = pickle.load(open(pkl_filename, 'rb'))

# Title
st.title('Salary Predictor')

# Year of Experience
exp = st.slider("Years of Experience", 0, 20, 1)

# Predict button
if st.button('Predict'):
    # Predict the salary
    salary = model.predict([[exp]])

    # Format the salary
    salary = round(salary[0], 2)

    # Display the salary
    st.write('The predicted salary is $', salary)
