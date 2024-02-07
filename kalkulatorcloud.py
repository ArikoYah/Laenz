import streamlit as st

# Header
st.header('Nugroho :sparkles:')
st.subheader('Kalkulator')

c1, c2, c3 = st.columns(3)

with c1:
    x = st.number_input('angka pertama:', value=100)
    st.write('=>: ')

with c2:
    satuan = st.selectbox('Operasi Matematika:', ('+', '-', 'x', ':'), key='k1')
    st.write(':sparkle:')

with c3:
    y = st.number_input('angka kedua:', value=1)

# Operasi matematika dan penampilan hasil
with st.expander('Hasil'):
    if satuan == '+':
        result = x + y
    elif satuan == '-':
        result = x - y
    elif satuan == 'x':
        result = x * y
    elif satuan == ':':
        if y != 0:
            result = x / y
        else:
            result = "Tidak bisa melakukan pembagian dengan nol"

  st.write(x,satuan,y,' = ',result)

st.caption('Copyright @ Ariko Yahya 2024')
