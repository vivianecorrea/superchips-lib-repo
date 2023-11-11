# streamlit_app.py

import streamlit as st
import sqlalchemy


# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from usuarios;', ttl=600)
conn.close

st.dataframe(df) 
