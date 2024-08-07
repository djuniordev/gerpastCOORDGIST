import streamlit as st
from PIL import Image
from dataframe.read import read, mostrarDadosAcidente, mostrarDadosTratamento
im = Image.open("./page/favicon.ico")

def homePage():

    st.set_page_config(layout="wide", page_title="Sistema GERPAST", page_icon=im)
    with open('./page/style.css') as f:
        st.markdown(f'<style>{f.read()}</style', unsafe_allow_html=True)

    st.sidebar.title("Importar planilha de Dados do Acidente ou Dados do Tratamento")
    planilhaDeAcidentes = st.sidebar.file_uploader("Clique aqui para importar dados do acidente")
    planilhaDeTratamento = st.sidebar.file_uploader("Clique aqui para importar dados do tratamento")

    if planilhaDeAcidentes is not None or planilhaDeTratamento is not None:
        with st.spinner("Aguardando..."):
            if planilhaDeAcidentes:
                df = read(planilhaDeAcidentes, "Acidentes")
                mostrarDadosAcidente(df)
            elif planilhaDeTratamento:
                df = read(planilhaDeTratamento, "Tratamento")
                mostrarDadosTratamento(df)
    else:
        st.write("Por favor, faça o upload de um arquivo.")