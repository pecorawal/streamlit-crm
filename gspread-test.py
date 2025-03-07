import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Read Google Sheet as DataFrame")

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/121rUFMr0o9AEtDii717xJONdUFZJ9wQ0XYXfidk7IDc/edit?gid=896099711#gid=896099711", ttl="10m", nrows=20,worksheet="aliquotas")

st.dataframe(df)