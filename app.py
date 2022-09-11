import streamlit as st

st.header('My Streamlit Dashboards')
hdick = {'Ferias Libres': '<A HREF="https://sergiolucero-feriaslibres-app-3aztis.streamlitapp.com/">%s</A>'}
for tit, html in hdick.items():
    st.markdown( html %tit, unsafe_allow_html=True)
