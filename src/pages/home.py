import streamlit as st 

import streamlit as st

st.markdown("# Login")
st.sidebar.markdown("# Login")

with st.form(key="auth_user"): 
    input_name = st.text_input(label=" Nome de usuário")
    input_pwd = st.text_input(label="Senha")
    input_buttom_submit = st.form_submit_button("Enviar")