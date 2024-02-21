import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Definisi fungsi
def f(x):
    return x**2 + 17*x + 9

# Persiapan data untuk plotting
x_vals = np.linspace(-20, 5, 1000)  # 1000 titik dari -20 sampai 5

# Streamlit app
st.title('Grafik Fungsi f(x) = x^2 + 17x + 9')
st.write('Gunakan slider di bawah untuk memilih rentang nilai x:')

# Slider untuk memilih rentang nilai x
x_range = st.slider('Rentang nilai x', min_value=-20.0, max_value=5.0, value=(-20.0, 5.0))

# Menghitung nilai fungsi untuk rentang yang dipilih
y_vals = f(x_vals)

# Membuat plot dengan rentang yang dipilih
plt.plot(x_vals, y_vals)
plt.xlim(x_range[0], x_range[1])
plt.title('Grafik Fungsi f(x) = x^2 + 17x + 9')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# Menampilkan plot di Streamlit
st.pyplot(plt)
