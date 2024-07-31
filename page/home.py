import streamlit as st
import time
from dataframe.read import read
from dataframe import meses
from controllers.veiculo import mostrarDadosVeiculo
from controllers.sexo import mostrarDadosSexo
from controllers.idade import mostrarDadosIdade
from controllers.municipio import mostrarDadosMunicipio
from filterpage.filterHomepage import filterDataframe
from datetime import datetime

def homePage():

    st.set_page_config(layout="wide")
    st.sidebar.title("Importar planilha de Acidentes")
    planilha = st.sidebar.file_uploader("Clique aqui para importar...")

    with st.spinner("Aguardando..."):
        if planilha is None:
            time.sleep(5)
        else:

            # Leitura do dataframe importado
            df = read(planilha)

            # Pegando os filtros selecionados pelo usuário

            dadosUnidade = filterDataframe(df, meses)
            # dadosUnidade = filtros.dadosUnidade
            # unidade_selecionada = filtros.unidade_selecionada
            # mes_selecionado = filtros.mes_selecionado
            # ano_selecionado = filtros.ano_selecionado
            # municipio_selecionado = filtros.municipio_selecionado


            # Criar duas colunas
            c1, c2, c3 = st.columns(3)
            c4, c5, c6 = st.columns(3)

            # Container para colocar as colunas em linha
            # with st.container():

                # Adicionando o Header de mês e unidade nas colunas
                # c1.header(f"Mês: {meses[mes_selecionado]}")
                # c2.header(f"Ano: {ano_selecionado}")
                # c3.header(f"Unidade: {unidade_selecionada}")
                # c4.header(f"Município: {municipio_selecionado}")

            # Colocar a tabela em um expander
            with st.expander("Mostrar tabela de acidentes"):
                # Mostrar a tabela
                st.dataframe(dadosUnidade, use_container_width=True, hide_index=True)

            # Mostrar dados totais de Sexo

            mostrarDadosSexo(st, dadosUnidade)

            # Mostrar dados veículo
            mostrarDadosVeiculo(st, dadosUnidade)

            # Mostrar dados de idade
            mostrarDadosIdade(st, dadosUnidade)

            # Mostrar dados município
            mostrarDadosMunicipio(st, dadosUnidade)