import streamlit as st
import numpy as np

# Fungsi untuk menyelesaikan matriks dengan metode Gauss-Jordan
def gauss_jordan(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        # Normalisasi diagonal
        factor = matrix[i][i]
        for j in range(m):
            matrix[i][j] /= factor
        
        # Eliminasi baris lain
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(m):
                    matrix[k][j] -= factor * matrix[i][j]
    
    return matrix

# Judul aplikasi Streamlit
st.title("Penyelesaian Matriks dengan Metode Gauss-Jordan")

# Input jumlah baris dan kolom matriks
rows = st.number_input("Masukkan jumlah baris:", min_value=1, max_value=10, value=3, step=1)
cols = st.number_input("Masukkan jumlah kolom:", min_value=1, max_value=10, value=4, step=1)

# Membuat matriks input dari pengguna
matrix = []
st.write("Masukkan elemen matriks:")
for i in range(rows):
    row = []
    for j in range(cols):
        value = st.number_input(f"Elemen [{i+1},{j+1}]:", key=f"elem_{i}_{j}")
        row.append(value)
    matrix.append(row)

# Mengonversi ke numpy array untuk komputasi
matrix = np.array(matrix, dtype=float)

# Tombol untuk melakukan perhitungan
if st.button("Selesaikan Matriks"):
    try:
        result = gauss_jordan(matrix)
        st.write("Hasil Matriks setelah Gauss-Jordan:")
        st.write(result)
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
