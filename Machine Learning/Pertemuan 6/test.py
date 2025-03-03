import streamlit as st
import pickle
import numpy as np 
import matplotlib.pyplot as plt

with open('cat_diabetes_mod.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title('Categorical Naive Bayes - Diabetes Prediction')

st.sidebar.header('Input Data Baru')
age = st.sidebar.selectbox('Age',['<30','30-40','40-50','50-60','60+'])
bmi = st.sidebar.selectbox('BMI',['<18.5','18.5-24.9','25-29.9','30+'])
blood_sugar = st.sidebar.selectbox('Blood Sugar Level',['<100','100-125','125-150','150'])
family_history = st.sidebar.selectbox('Family History Of diabetes',['No','Yes'])
diet = st.sidebar.selectbox('Diet',['Good','Moderate','Poor'])

age_map = {'<30':0, '30-40':1, '40-50':2, '50-60':3, '60+':4}
bmi_map = {'<18.5':0, '18.5-24.9':1, '25-29.9':2, '30+':3}
blood_sugar_map = {'<100':0, '100-125':1, '125-150':2, '150+':3}
family_history_map = {'No':0, 'Yes':1}
diet_map = {'Poor':0, 'Moderate':1, 'Good':2}

input_data = np.array([[age_map[age], bmi_map[bmi], blood_sugar_map[blood_sugar], family_history_map[family_history], diet_map[diet]]])

prediction = model.predict(input_data)
prediction_prob = model.predict_proba(input_data)

st.subheader('Prediction Result')
resul = 'Diabetes (Yes)' if prediction[0] == 1 else 'No Diabetes'
st.write(f'The model predicts : **{result}**')

fig, ax = plt.subplots()
labels = ['No Diabetes', 'Diabetes']
ax.bar(labels, prediction_prob[0], color = ['green', 'red'])
ax.set_ylabel('Probability')
ax.set_title('Prediction Probability')
st.pyplot(fig)

st.subheader('Input Summary')
st.write(f'**Age** : {age}')
st.write(f'**BMI** : {bmi}')
st.write(f'**Blood Sugar Level** : {blood_sugar}')
st.write(f'**Family History** : {family_history}')
st.write(f'**Diet** : {diet}')
