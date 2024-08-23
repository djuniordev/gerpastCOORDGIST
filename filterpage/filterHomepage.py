import pandas as pd
import streamlit as st
from dataframe import listaCategorias
def filterDataframeAcidentes(df, meses):
    unidades = df["UNIDADE"].unique().tolist()
    unidades = ["Todas as unidades"] + unidades
    unidade_selecionada = st.sidebar.selectbox("Selecionar a unidade:", unidades)
    mes_selecionado_label = st.sidebar.selectbox("Selecionar o mês:", meses.values())

    for id, mes in meses.items():
        if mes == mes_selecionado_label:
            mes_selecionado = id
            break
    anos = df["DATA DO ACIDENTE"].dt.year.dropna().astype(int).unique().tolist()
    anos = sorted(anos, reverse=True)
    anos = ["Todos os anos"] + anos
    ano_selecionado = st.sidebar.selectbox("Selecionar o ano:", anos)

    municipios = df["MUNICÍPIO ACIDENTE"].dropna().unique().tolist()
    municipios = ["Todos os municípios"] + municipios
    municipio_selecionado = st.sidebar.selectbox("Selecionar o município", municipios)

    sexos = df["SEXO"].dropna().unique().tolist()
    sexos = ["Todos os sexos"] + sexos
    sexo_selecionado = st.sidebar.selectbox("Selecionar o sexo", sexos)

    veiculos = df["VEÍCULOS ENVOLVIDOS"].dropna().unique().tolist()
    veiculos = ["Todos os veículos"] + veiculos
    veiculo_selecionado = st.sidebar.selectbox("Selecionar o veículo", veiculos)

    categorias_idade = ["Todas as categorias"] + listaCategorias
    categoria_idade_selecionado = st.sidebar.selectbox("Selecionar a categoria de idade", categorias_idade)

    condicoes = []

    if unidade_selecionada != "Todas as unidades":
        condicoes.append(df["UNIDADE"] == unidade_selecionada)
    if ano_selecionado != "Todos os anos":
        condicoes.append(df["DATA DO ACIDENTE"].dt.year == ano_selecionado)
    if mes_selecionado != 0:
        condicoes.append(df["DATA DO ACIDENTE"].dt.month == mes_selecionado)
    if municipio_selecionado != "Todos os municípios":
        condicoes.append(df["MUNICÍPIO ACIDENTE"] == municipio_selecionado)
    if sexo_selecionado != "Todos os sexos":
        condicoes.append(df["SEXO"] == sexo_selecionado)
    if veiculo_selecionado != "Todos os veículos":
        condicoes.append(df["VEÍCULOS ENVOLVIDOS"] == veiculo_selecionado)
    if categoria_idade_selecionado != "Todas as categorias":
        condicoes.append(df["CATEGORIA IDADE"] == categoria_idade_selecionado)

    dadosUnidade = df.copy()

    if condicoes:
        condicao_final = condicoes[0]
        for condicao in condicoes[1:]:
            condicao_final &= condicao

        dadosUnidade = df[condicao_final]

    return dadosUnidade

def filterDataframeTratamento(df, meses):
    unidades = df["UNIDADE"].unique().tolist()
    unidades = ["Todas as unidades"] + unidades
    unidade_selecionada = st.sidebar.selectbox("Selecionar a unidade:", unidades, key="unidade_tratamento")
    
    mes_selecionado_label = st.sidebar.selectbox("Selecionar o mês:", meses.values(), key="mes_tratamento")
    mes_selecionado = next((id for id, mes in meses.items() if mes == mes_selecionado_label), 0)
    
    anos = df["INICIO INTERNACAO"].dt.year.dropna().astype(int).unique().tolist()
    anos = sorted(anos, reverse=True)
    anos = ["Todos os anos"] + anos
    ano_selecionado = st.sidebar.selectbox("Selecionar o ano:", anos, key="ano_tratamento")

    sexos = df["SEXO"].dropna().unique().tolist()
    sexos = ["Todos os sexos"] + sexos
    sexo_selecionado = st.sidebar.selectbox("Selecionar o sexo", sexos, key="sexo_tratamento")

    categorias_idade = ["Todas as categorias"] + listaCategorias
    categoria_idade_selecionado = st.sidebar.selectbox("Selecionar a categoria de idade", categorias_idade, key="categoria_idade_tratamento")

    condicoes = []
    if unidade_selecionada != "Todas as unidades":
        condicoes.append(df["UNIDADE"] == unidade_selecionada)
    if ano_selecionado != "Todos os anos":
        condicoes.append(df["INICIO INTERNACAO"].dt.year == ano_selecionado)
    if mes_selecionado != 0:
        condicoes.append(df["INICIO INTERNACAO"].dt.month == mes_selecionado)
    if sexo_selecionado != "Todos os sexos":
        condicoes.append(df["SEXO"] == sexo_selecionado)
    if categoria_idade_selecionado != "Todas as categorias":
        condicoes.append(df["CATEGORIA IDADE"] == categoria_idade_selecionado)

    dadosUnidade = df.copy()
    if condicoes:
        condicao_final = condicoes[0]
        for condicao in condicoes[1:]:
            condicao_final &= condicao
        dadosUnidade = df[condicao_final]

    return dadosUnidade

def filterDataframeAcidentesTratamento(df, meses):
    unidades = df["UNIDADE"].unique().tolist()
    unidades = ["Todas as unidades"] + unidades
    unidade_selecionada = st.sidebar.selectbox("Selecionar a unidade:", unidades)
    mes_selecionado_label = st.sidebar.selectbox("Selecionar o mês:", meses.values())

    for id, mes in meses.items():
        if mes == mes_selecionado_label:
            mes_selecionado = id
            break
    # Extrair anos de 'DATA DO ACIDENTE'
    anos_acidente = df['DATA DO ACIDENTE'].dt.year.dropna().astype(int).unique()

    # Extrair anos de 'INICIO INTERNACAO'
    anos_internacao = df['INICIO INTERNACAO'].dt.year.dropna().astype(int).unique()

    # Combinar e obter anos únicos
    anos = sorted(set(anos_acidente).union(set(anos_internacao)), reverse=True)

    # Adicionar a opção 'Todos os anos'
    anos = ["Todos os anos"] + anos
    ano_selecionado = st.sidebar.selectbox("Selecionar o ano:", anos)

    municipios = df["MUNICÍPIO ACIDENTE"].dropna().unique().tolist()
    municipios = ["Todos os municípios"] + municipios
    municipio_selecionado = st.sidebar.selectbox("Selecionar o município", municipios)

    sexos = df["SEXO"].dropna().unique().tolist()
    sexos = ["Todos os sexos"] + sexos
    sexo_selecionado = st.sidebar.selectbox("Selecionar o sexo", sexos)

    veiculos = df["VEÍCULOS ENVOLVIDOS"].dropna().unique().tolist()
    veiculos = ["Todos os veículos"] + veiculos
    veiculo_selecionado = st.sidebar.selectbox("Selecionar o veículo", veiculos)

    categorias_idade = ["Todas as categorias"] + listaCategorias
    categoria_idade_selecionado = st.sidebar.selectbox("Selecionar a categoria de idade", categorias_idade)

    condicoes = []

    if unidade_selecionada != "Todas as unidades":
        condicoes.append(df["UNIDADE"] == unidade_selecionada)
    if ano_selecionado != "Todos os anos":
        ano_selecionado = int(ano_selecionado)
        condicao_ano_internacao = (df['INICIO INTERNACAO'].dt.year == ano_selecionado)
        condicoes.append(condicao_ano_internacao)
    if mes_selecionado != 0:
        mes_selecionado = int(mes_selecionado)
        condicao_mes_internacao = (df['INICIO INTERNACAO'].dt.month == mes_selecionado)
        condicoes.append(condicao_mes_internacao)
    if municipio_selecionado != "Todos os municípios":
        condicoes.append(df["MUNICÍPIO ACIDENTE"] == municipio_selecionado)
    if sexo_selecionado != "Todos os sexos":
        condicoes.append(df["SEXO"] == sexo_selecionado)
    if veiculo_selecionado != "Todos os veículos":
        condicoes.append(df["VEÍCULOS ENVOLVIDOS"] == veiculo_selecionado)
    if categoria_idade_selecionado != "Todas as categorias":
        condicoes.append(df["CATEGORIA IDADE"] == categoria_idade_selecionado)

    dadosUnidade = df.copy()

    if condicoes:
        condicao_final = condicoes[0]
        for condicao in condicoes[1:]:
            condicao_final &= condicao

        dadosUnidade = df[condicao_final]

    return dadosUnidade