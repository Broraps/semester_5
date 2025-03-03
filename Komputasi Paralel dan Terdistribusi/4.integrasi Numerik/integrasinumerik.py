import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Raffi Argianda Kelas Malam B
# Fungsi untuk metode trapesium
def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    jumlah = 0.5 * y[0] + 0.5 * y[-1] + np.sum(y[1:-1])
    integral = h * jumlah
    return integral, h, jumlah

# Fungsi parser untuk mengubah string menjadi fungsi (tanpa lambda)
def parse_function(function_str):
    try:
        def func(x):
            return eval(function_str, {"x": x, "np": np})
        return func
    except Exception as e:
        st.error(f"Error in function parsing: {e}")
        return None

# Judul aplikasi
st.title("Integrasi Numerik dengan Metode Trapesium")

# Input pengguna
function_str = st.text_input("Masukkan fungsi f(x) (contoh: x**2):", value="4*x + x**3")
a = st.number_input("Batas bawah integral (a):", value=1.0)
b = st.number_input("Batas atas integral (b):", value=4.0)
n = st.number_input("Jumlah subinterval (n):", min_value=1, step=1, value=4)

# Parsing fungsi
func = parse_function(function_str)

if func is not None:
    # Hitung integral
    integral_result, h, jumlah = trapezoidal_rule(func, a, b, n)

    # Tampilkan hasil
    st.latex(rf"""\int_{{{a}}}^{{{b}}} {function_str}, dx \text{{ dengan }} {n} \text{{ subinterval adalah: }} {integral_result:.6f}""")
    st.markdown("### Rumus Hasil Akhir:")
    st.latex(r"Hasil = \frac{h \cdot jumlah}{2}")
    st.markdown(f"""
    Dengan:
    - \( h = {h:.6f} \)
    - \( jumlah = {jumlah:.6f} \)
    
    Sehingga:
    """)
    st.latex(rf"Hasil = \frac{{{h:.6f} \cdot {jumlah:.6f}}}{{2}} = {integral_result:.6f}")

    # Plot fungsi
    x_plot = np.linspace(a, b, 500)
    y_plot = func(x_plot)

    fig, ax = plt.subplots()
    ax.plot(x_plot, y_plot, label="f(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    st.pyplot(fig)
else:
    st.warning("Masukkan fungsi yang valid untuk melanjutkan.")

