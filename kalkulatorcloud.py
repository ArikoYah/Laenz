import streamlit as st

#Header
st.header('Nugroho :sparkles:')
st.subheader('Plot')

c1, c2 = st.columns(2)

with c1:
  x = st.number_input('',value=100)
  st.write('=>: ')
  with c2:
    satuan = st.selectbox(
      'Satuan',
      ('+','-','x',':'),key='k1')
    with c3:
  x = st.number_input('',value=100)
  st.write('=>: ')
    st.write(':sparkle:')
    st.write(x,'',satuan,'=','')
st.caption('Copyright @ Ariko Yahya 2024')
