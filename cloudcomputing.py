import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('Nugroho :sparkles:')
st.subheader('Plot')

x = np.linspace(-2 * np.pi, 2 * np.pi,1000)
y = np.sin(x)
z = np.cos(x)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x, y, label='sin(x)', color='b')
ax.plot(x, y, label='cos(x)', color='g')
ax.set_ylabel("")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(),rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)

# subheader
st.subheader("Plot Sin & Cos")

co11,co12 = st.coloumn(2)

  with col1:
  st.caption('Plot Sin')
  x = np.linspace(-2 * np.pi, 2 * np.pi, 1000) # Generating x values from -2*pi to 2*pi
  y = np.sin(x) # Calculating sin(x) values
  fig, ax = plt.subplots(figsize=(16, 8))
  ax.plot(x, y, label='sin(x)', color='b') # plotting sin(x) curve
  ax.set_ylabel("Sin x")
  ax.set_xlabel("x")
  ax.tick_params(axis='y', labelsize=20)
  ax.set_xticklabels(ax.get_sticklabels(), rotation=30, ha='right')
  ax.tick_params(axis='x', labelsize=15)
  st.pyplot(fig)

with col2:
  st.caption('Plot Cos')
  x = np.linspace(-2 * np.pi, 2 * np.pi, 1000) #Generating x values from -2*pi to 2*pi
  y = np.cos(x) # Calculating sin(x) values
  
  fig, ax = plt.subplots(figsize=(16, 8))
  ax.plot(x, y, label='cos(x)', color='g') # plotting sin(x) curve
  ax.set_ylabel("Cos x")
  ax.set_xlabel("x")
  ax.tick_params(axis='y', labelsize=20)
  ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
  ax.tick_params(axis='x', labelsize=15)
  
  st.pyplot(fig)

st.caption('Copyright @ Ariko Yahya 2024')
