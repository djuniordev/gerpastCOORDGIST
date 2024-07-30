import streamlit as st
import time
from dataframe.read import read
from page.page import captureMonth, meses
from controllers.veiculo import mostrarDadosVeiculo
from controllers.sexo import mostrarDadosSexo
from controllers.idade import mostrarDadosIdade
from controllers.municipio import mostrarDadosMunicipio

def initializePage():
    st.set_page_config(layout="wide")
    st.sidebar.title("Importar planilha de Acidentes")
    planilha = st.sidebar.file_uploader("Clique aqui para importar...")

    with st.spinner("Aguardando..."):
        if planilha is None:
            time.sleep(5)
        else:
            st.success("Carregado!")
            df = read(planilha)

            unidades = df["UNIDADE"].unique().tolist()
            unidades = ["Todas"] + unidades
            unidade_selecionada = st.sidebar.selectbox("Selecionar a unidade:", unidades)
            mes_selecionado_label = st.sidebar.selectbox("Selecionar o mês:", meses.values())

            for id, mes in meses.items():
                if mes == mes_selecionado_label:
                    mes_selecionado = id
                    break

            ano_selecionado = st.sidebar.selectbox("Selecionar o ano:", ["Todos", 2024, 2023])

            condicoes = []

            if unidade_selecionada != "Todas":
                condicoes.append(df["UNIDADE"] == unidade_selecionada)
            if ano_selecionado != "Todos":
                condicoes.append(df["DATA DO ACIDENTE"].dt.year == ano_selecionado)
            if mes_selecionado != 0:
                condicoes.append(df["DATA DO ACIDENTE"].dt.month == mes_selecionado)

            dadosUnidade = df.copy()

            if condicoes:
                condicao_final = condicoes[0]
                for condicao in condicoes[1:]:
                    condicao_final &= condicao

                dadosUnidade = df[condicao_final]


            # dadosUnidade = df[
            #     (df["UNIDADE"] == unidade_selecionada) &
            #     (df["DATA DO ACIDENTE"].dt.year == ano_selecionado) &
            #     (df["DATA DO ACIDENTE"].dt.month == mes_selecionado)
            #
            #     ]

            st.title(meses[mes_selecionado])
            st.title(unidade_selecionada)

            st.dataframe(dadosUnidade)

            # Mostrar dados totais de Sexo

            mostrarDadosSexo(st, dadosUnidade)

            # Mostrar dados veículo
            mostrarDadosVeiculo(st, dadosUnidade)

            # Mostrar dados de idade
            #mostrarDadosIdade(st, dadosUnidade)

            # Mostrar dados município
            mostrarDadosMunicipio(st, dadosUnidade)