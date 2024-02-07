import streamlit as st

# Header
st.header('Nugroho :sparkles:')
st.subheader('Plot')

c1, c2 = st.columns(2)

with c1:
    x = st.number_input('Masukkan angka:', value=100)
    st.write('=>: ')

with c2:
    satuan = st.selectbox('Satuan', ('+', '-', 'x', ':'), key='k1')
    st.write(':sparkle:')
    st.write(x, satuan, '=', end=' ')

# Operasi matematika
if satuan == '+':
    y = st.number_input('Masukkan angka kedua:', value=0)
    st.write(x + y)
elif satuan == '-':
    y = st.number_input('Masukkan angka kedua:', value=0)
    st.write(x - y)
elif satuan == 'x':
    y = st.number_input('Masukkan angka kedua:', value=1)
    st.write(x * y)
elif satuan == ':':
    y = st.number_input('Masukkan angka kedua (tidak boleh nol):', value=1)
    if y != 0:
        st.write(x / y)
    else:
        st.write("Tidak bisa melakukan pembagian dengan nol")

st.caption('Copyright @ Ariko Yahya 2024')
