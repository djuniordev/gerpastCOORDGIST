import streamlit as st
import time
from dataframe.read import read
from page.page import captureMonth, meses
from controllers.veiculo import mostrarDadosVeiculo
from controllers.sexo import mostrarDadosSexo

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
            unidades = df["UNIDADE"].unique()
            unidade_selecionada = st.sidebar.selectbox("Selecionar a unidade:", unidades)
            mes_selecionado = st.sidebar.selectbox("Selecionar o mês:", meses)
            ano_selecionado = st.sidebar.selectbox("Selecionar o ano:", ['2024'])

            dadosUnidade = df[df["UNIDADE"] == unidade_selecionada]

            st.title(unidade_selecionada)

            st.dataframe(dadosUnidade)

            # Mostrar dados totais de Sexo

            mostrarDadosSexo(st, dadosUnidade)

            # Mostrar dados veículo
            mostrarDadosVeiculo(st, dadosUnidade)
