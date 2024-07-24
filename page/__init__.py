import streamlit as st
import time
from dataframe.read import read
from page.page import captureMonth
from controllers import *

def initializePage():
    st.set_page_config(layout="wide")
    st.sidebar.title("Importar planilha de Acidentes")
    planilha = st.sidebar.file_uploader("Clique aqui para importar...")

    with st.spinner("Aguardando..."):
        if planilha is None:
            time.sleep(5)
        else:
            st.success("Carregado!")
            df, month = read(planilha)
            st.title(month)
            st.dataframe(df)
            unidades = df["UNIDADE"].unique()
            unidade_selecionada = st.sidebar.selectbox("Selecionar a unidade:", unidades)

            dadosUnidade = df[df["UNIDADE"] == unidade_selecionada]

            st.title(unidade_selecionada)

            # Mostrar dados totais de Sexo
            sexoController = SexoController(st)
            sexoController.hideSexo(dadosUnidade)

