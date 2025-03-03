import streamlit as st 
import numpy as np 
import pickle
import plotly.express as px
import pandas as pd 

# Load the trainde KNN model
with open('knn_pinjam_mod.pkl', 'rb') as model_file:
    knn = pickle.load(model_file)
    
# Create a title for the web app
st.title('K-Nearest Neighbor (KNN) Loan Eligibility Prediction')

# Input Fields for new data
usia = st.sidebar.number_input('Usia', min_value = 18, max_value = 70, value = 30)
pendapatan = st.sidebar.number_input('Pendapatan', min_value = 10, max_value = 200, value = 50)
status_perkawinan = st.sidebar.selectbox('Status_Perkawinan', ['Belum Menikah', 'Menikah'])
if status_perkawinan == 'Belum Menikah' :
    status_perkawinan = 0
else : 
    status_perkawinan = 1

jumlah_pinjaman = st.sidebar.number_input('Jumlah_Pinjaman', min_value = 10, max_value = 500, value = 100)
durasi_pinjaman = st.sidebar.number_input('Durasi_Pinjaman', min_value = 1, max_value = 30, value = 10)
# status_pekerjaan = st.sidebar.number_input('Status_Pekerjaan', min_value = 0, max_value = 3, value = 0)
status_pekerjaan = st.sidebar.selectbox('Status_Pekerjaan', ['Karyawan Kontrakn', 'Karyawan Tetap', 'Pensiunan', 'Wirausaha'])
if status_pekerjaan == 'Karyawan Kontrak' :
    status_pekerjaan = 0
elif status_pekerjaan == 'Karyawan Tetap' :
    status_pekerjaan = 1
elif status_pekerjaan == 'Pensiunan' :
    status_pekerjaan = 2
elif status_pekerjaan == 'Wirausaha' :
    status_pekerjaan = 3

# New data for prediction
new_data = np.array([[usia, pendapatan, status_perkawinan, jumlah_pinjaman, durasi_pinjaman, status_pekerjaan]])

# Predict button
if st.sidebar.button('Predict') :
    # Predict the result
    prediction = knn.predict(new_data)
    result = 'Layak' if prediction == 0 else 'Tidak Layak'

    # Show the prediction result
    st.write(f'Hasil Prediksi : **{result}**')

    # 3D plot for KNN
    df = pd.DataFrame({
        'Usia' : np.random.randint(18, 70, size=60),
        'Pendapatan' : np.random.randint(10, 200, size=60),
        'Jumlah_Pinjaman' : np.random.uniform(10, 500, size=60),
        'Lulus_Kredit' : np.random.choice(['0','1'], size=60)
    })
    fig = px.scatter_3d(df, x = 'Usia', y = 'Pendapatan', z = 'Jumlah_Pinjaman', color = 'Lulus_Kredit', title = f'KNN Prediction')
    st.plotly_chart(fig)