import pandas as pd
from .dataframe import configDataframeAcidentes, configDataframeTratamento, configDataframeAcidentesTratamento
from dataframe import meses
from controllers.veiculo import mostrarDadosVeiculo,dadosDetalhadosVeiculos
from controllers.sexo import mostrarDadosSexo,sexoDetalhado
from controllers.idade import mostrarDadosIdade,dadosIdadeDetalhados
from controllers.municipio import mostrarDadosMunicipio, dadosDetalhadosMunicipio
from controllers.internacao import mostrarDadosInternacao
from controllers.semana import mostrarDadosSemana
from controllers.mes import mostrarDadosMes
from controllers.hora import mostrarDadosHora

from filterpage.filterHomepage import filterDataframeAcidentes, filterDataframeTratamento, filterDataframeAcidentesTratamento
import streamlit as st

def read(planilha, tipo):

    df = pd.read_excel(planilha)

    if tipo == "Acidentes":
        df = configDataframeAcidentes(df)
    if tipo == "Tratamento":
        df = configDataframeTratamento(df)

    return df

def readPlanilhas(planilha1, planilha2):
    df1 = pd.read_excel(planilha1)
    
    df2 = pd.read_excel(planilha2)

    # Merge dos DataFrames pela coluna 'CPF'
    df = pd.merge(df1, df2[['CARTÃO SUS_8', 'INÍCIO INTERNAÇÃO_7']], on='CARTÃO SUS_8', how='left')  # 'inner' para o merge interno, 'outer' para o externo
    df = configDataframeAcidentesTratamento(df)
    return df

def mostrarDadosAcidente(df):
    # Pegando os filtros selecionados pelo usuário

    dadosUnidade = filterDataframeAcidentes(df, meses)

    # Colocar a tabela em um expander
    #with st.expander("Mostrar tabela de acidentes"):
        # Mostrar a tabela
        #st.dataframe(dadosUnidade, use_container_width=True, hide_index=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total de Acidentes", value=dadosUnidade["UNIDADE"].count())

    with col2:
        sexo_counts = dadosUnidade["SEXO"].value_counts()

        # Determinar o número máximo de acidentes
        max_count = sexo_counts.max()

        # Obter todos os sexos com o número máximo de acidentes
        sexos_max = sexo_counts[sexo_counts == max_count].index.tolist()

        if len(sexos_max) > 1:
            # Se houver mais de um sexo com a mesma quantidade máxima de acidentes
            message = "Igual"
        else:
            # Caso contrário, exibe o gênero com o maior número de acidentes
            message = sexos_max[0]

        st.metric(label="Sexo c/ mais acidentes", value=message)

    with col3:
        veículo_counts = dadosUnidade["VEÍCULOS ENVOLVIDOS"].value_counts()
    
        # Determinar o sexo com o maior número de acidentes
        veiculo_max = veículo_counts.idxmax()
        st.metric(label="Veículo c/ mais acidentes", value=veiculo_max)
    with st.expander("Dados Detalhados"):
        st.write(''' Tabela de Dados ''')
        st.dataframe(dadosUnidade, use_container_width=True, hide_index=True)
        sexoDetalhado(st, dadosUnidade)
        dadosDetalhadosVeiculos(st, dadosUnidade)
        dadosIdadeDetalhados(st, dadosUnidade)
        dadosDetalhadosMunicipio(st, dadosUnidade)
    #with col4:
        #st.metric(label="Total Municípios", value=dadosUnidade["MUNICÍPIO ACIDENTE"].count())
    mostrarDadosMes(st, dadosUnidade)
    col6, col7, col8 = st.columns(3)
    # Mostrar dados totais de Sexo

    with col6:
        mostrarDadosIdade(st, dadosUnidade)

    with col7:
        # Mostrar dados veículo
    #with st.expander("Mostrar dados de veículo"):
        mostrarDadosVeiculo(st, dadosUnidade)
    with col8:
        mostrarDadosSexo(st, dadosUnidade)

    #with col6:
    #with st.expander("Mostrar dados de sexo"):
        #mostrarDadosSexo(st, dadosUnidade)

    # Mostrar dados de idade
    #with st.expander("Mostrar dados de idade"):
    #mostrarDadosIdade(st, dadosUnidade)

    # Mostrar dados município
    #with st.expander("Mostrar dados de município"):
    #mostrarDadosMunicipio(st, dadosUnidade)

    mostrarDadosSemana(st, dadosUnidade)
    mostrarDadosHora(st, dadosUnidade)

def mostrarDadosAcidentesTratamento(df):
    dadosUnidade = filterDataframeAcidentesTratamento(df, meses)
    st.dataframe(dadosUnidade)
    mostrarDadosVeiculo(st, dadosUnidade)

def mostrarDadosTratamento(df):
    # Pegando os filtros selecionados pelo usuário

    dadosUnidade = filterDataframeTratamento(df, meses)

    # Colocar a tabela em um expander
    with st.expander("Mostrar tabela de tratamento"):
        # Mostrar a tabela
        st.dataframe(dadosUnidade, use_container_width=True, hide_index=True)

    # Mostrar dados totais de Sexo

    with st.expander("Mostrar dados de sexo"):
        mostrarDadosSexo(st, dadosUnidade)

    # Mostrar dados de idade
    with st.expander("Mostrar dados de idade"):
        mostrarDadosIdade(st, dadosUnidade)

    with st.expander("Mostrar dados de internação"):
        mostrarDadosInternacao(st, dadosUnidade)