import streamlit as st
from dataframe.read import readPlanilhas, mostrarDadosAcidentesTratamento
from pages import configPage

def acidentesTratamentoPage():
    configPage()
    st.sidebar.title("Importar planilha de Dados do Acidente")
    planilhaDeAcidentes = st.sidebar.file_uploader("Clique aqui para importar dados do acidente")
    planilhaDeTratamento = st.sidebar.file_uploader("Clique aqui para importar dados do tratamento")
    
    # Processar as planilhas
    if planilhaDeAcidentes is not None and planilhaDeTratamento is not None:
        with st.spinner("Aguardando..."):
            try:
                df_acidentesTratamento = readPlanilhas(planilhaDeAcidentes, planilhaDeTratamento)
                #mostrarDadosAcidente(df_acidentes)
                mostrarDadosAcidentesTratamento(df_acidentesTratamento)
            except Exception:
                st.warning("Ocorreu um erro durante o processamento.")

    # Mensagem caso nenhum arquivo seja carregado
    if planilhaDeAcidentes is None and planilhaDeTratamento is None:
        st.write("Por favor, faça o upload de um arquivo.")

acidentesTratamentoPage()