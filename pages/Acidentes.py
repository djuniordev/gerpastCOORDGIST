import streamlit as st
from dataframe.read import read, mostrarDadosAcidente
from pages import configPage

def acidentesPage():
    configPage()

    st.sidebar.title("Importar planilha de Dados do Acidente")
    planilhaDeAcidentes = st.sidebar.file_uploader("Clique aqui para importar dados do acidente")
    
    # Processar as planilhas
    if planilhaDeAcidentes is not None:
        with st.spinner("Aguardando..."):
            try:
                df_acidentes = read(planilhaDeAcidentes, "Acidentes")
                mostrarDadosAcidente(df_acidentes)
            except Exception:
                st.warning("Ocorreu um erro durante o processamento.")

    # Mensagem caso nenhum arquivo seja carregado
    if planilhaDeAcidentes is None:
        st.write("Por favor, faça o upload de um arquivo.")

acidentesPage()