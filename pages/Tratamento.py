import streamlit as st
from dataframe.read import mostrarDadosTratamento, read
from pages import configPage

def tratamentoPage():
    configPage()

    st.sidebar.title("Importar planilha de Dados do Tratamento")

    planilhaDeTratamento = st.sidebar.file_uploader("Clique aqui para importar dados do tratamento")
    if planilhaDeTratamento is not None:
        with st.spinner("Aguardando..."):
            try:
                df_tratamento = read(planilhaDeTratamento, "Tratamento")
                mostrarDadosTratamento(df_tratamento)
            except Exception:
                st.warning("Ocorreu um erro durante o processamento.")

    if planilhaDeTratamento is None:
        st.write("Por favor, faça o upload de um arquivo.")

tratamentoPage()