import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function definition
def f(x):
    """Defines the function f(x) = x^2 + 17x + 9."""
    return x**2 + 17*x + 9

# Function to compute integral using trapezoidal method
def trapezoidal_integral(f, a, b, n):
    """Computes the integral of a function f over the interval [a, b] using the trapezoidal method."""
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    integral_value = h * (np.sum(y) - 0.5 * (y[0] + y[-1]))
    return integral_value

# Streamlit app
st.title('Integral Trapesium untuk Fungsi f(x) = x^2 + 17x + 9')
st.write('Gunakan slider di bawah untuk memilih rentang nilai x:')

# Slider for selecting the range of x values
x_range = st.slider('Rentang nilai x', -20.0, 5.0, (-20.0, 5.0))
st.write('Rentang nilai x:', x_range)

# Calculate function values within the selected range
x_vals = np.linspace(x_range[0], x_range[1], 1000)
y_vals = f(x_vals)

# Calculate integral value using trapezoidal method
integral_value = trapezoidal_integral(f, x_range[0], x_range[1], 1000)

# Plot the function and shaded region
fig, ax = plt.subplots(2, 1, figsize=(16, 12), sharex=True)

# Plot the function
ax[0].plot(x_vals, y_vals, label='f(x) = x^2 + 17x + 9', color='b')
ax[0].fill_between(x_vals, y_vals, color='skyblue', alpha=0.3)  # Color the area under the curve
ax[0].set_ylabel("f(x)")
ax[0].tick_params(axis='y', labelsize=20)
ax[0].grid(color='green', linestyle='-.', linewidth=.5)

# Plot the integral approximation
integral_approximation = np.linspace(x_range[0], x_range[1], 10)
integral_approximation_y = f(integral_approximation)
ax[1].plot(integral_approximation, integral_approximation_y, marker='o', linestyle='-', color='r')
ax[1].fill_between(integral_approximation, 0, integral_approximation_y, color='salmon', alpha=0.3)  # Color the area under the curve
ax[1].set_ylabel("Integral Approximation")
ax[1].set_xlabel("x")
ax[1].tick_params(axis='y', labelsize=20)
ax[1].tick_params(axis='x', labelsize=15)
ax[1].grid(color='green', linestyle='-.', linewidth=.5)

plt.tight_layout()
st.pyplot(fig)

# Display integral value
st.write('Nilai integral menggunakan metode trapesium:', integral_value)
