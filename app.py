
import streamlit as st
import pandas as pd

# Título da aplicação
st.title("CRM Básico com Streamlit")

# Inicializando a lista de contatos como um DataFrame
if 'contacts' not in st.session_state:
    st.session_state.contacts = pd.DataFrame(columns=['Nome', 'Email', 'Telefone'])

# Função para adicionar um novo contato
def add_contact(name, email, phone):
    new_contact = pd.DataFrame({'Nome': [name], 'Email': [email], 'Telefone': [phone]})
    st.session_state.contacts = pd.concat([st.session_state.contacts, new_contact], ignore_index=True)

# Formulário para entrada de novo contato
with st.form("Adicionar Contato"):
    name = st.text_input("Nome")
    email = st.text_input("Email")
    phone = st.text_input("Telefone")
    submitted = st.form_submit_button("Adicionar")
    if submitted:
        add_contact(name, email, phone)
        st.success("Contato adicionado com sucesso!")

# Exibindo a lista de contatos
st.subheader("Lista de Contatos")
st.table(st.session_state.contacts)

camera=st.camera_input("Take a picture", disabled="not enable")