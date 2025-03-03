import pickle
import streamlit as st 
st.title('Prediksi Kalori')

st.header('Masukkan Data')
umur = st.number_input('Umur', min_value=25, max_value=55)
bb = st.number_input('Berat Badan (BB)', min_value=60, max_value=95)
tb = st.number_input('Tinggi Badan (TB)', min_value=155, max_value=180)
olahraga = st.number_input('Durasi Olahraga (Menit)', min_value=20, max_value=90)

if st.button('Prediksi'):
    loaded_model = pickle.load(open('regression_model.pkl', 'rb'))
    input_data = [[umur, bb, tb, olahraga]]
    prediction = loaded_model.predict(input_data)

    st.header('Hasil Prediksi')
    st.write(f'Kalori Yang diperkirakan : {prediction[0]:.2f}')