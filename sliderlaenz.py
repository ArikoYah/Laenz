import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Definisi fungsi
def f(x):
    return x**2 + 17*x + 9

# Fungsi untuk menghitung integral menggunakan metode trapesium
def trapezoidal_integral(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    integral_value = h * (np.sum(y) - 0.5 * (y[0] + y[-1]))
    return integral_value

# Streamlit app
st.title('Integral Trapesium untuk Fungsi f(x) = x^2 + 17x + 9')
st.write('Gunakan slider di bawah untuk memilih rentang nilai x:')

# Slider untuk memilih rentang nilai x
x_range = st.slider('Rentang nilai x', -20.0, 5.0, (-20.0, 5.0))
st.write('Rentang nilai x:', x_range)

# Menampilkan nilai rentang integral
st.write('Rentang integral:', x_range[0], 'hingga', x_range[1])

# Menghitung nilai fungsi untuk rentang yang dipilih
x_vals = np.linspace(x_range[0], x_range[1], 1000)
y_vals = f(x_vals)

# Membuat plot dengan rentang yang dipilih
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x_vals, y_vals, label='f(x) = x^2 + 17x + 9', color='b')
ax.fill_between(x_vals, y_vals, color='skyblue', alpha=0.3)  # Warna daerah di bawah kurva
ax.set_ylabel("")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)

# Menampilkan integral trapesium
integral_value = trapezoidal_integral(f, x_range[0], x_range[1], 1000)
st.write('Nilai integral menggunakan metode trapesium:', integral_value)
