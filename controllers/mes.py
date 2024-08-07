import pandas as pd
import plotly.express as px
import streamlit as st

def mostrarDadosMes(st, dadosUnidade):
    # Garantir que a coluna 'DATA DO ACIDENTE' seja do tipo datetime
    dadosUnidade['DATA DO ACIDENTE'] = pd.to_datetime(dadosUnidade['DATA DO ACIDENTE'], errors='coerce')

    # Filtrar linhas com datas válidas
    dadosUnidade = dadosUnidade.dropna(subset=['DATA DO ACIDENTE']).copy()  # Usar .copy() para evitar o SettingWithCopyWarning

    # Extrair mês e ano
    dadosUnidade['Mês'] = dadosUnidade['DATA DO ACIDENTE'].dt.month
    dadosUnidade['Ano'] = dadosUnidade['DATA DO ACIDENTE'].dt.year

    # Agregar os dados por mês e ano
    dados_por_mes = dadosUnidade.groupby(['Mês', 'Ano']).size().reset_index(name='Total')

    # Criar uma coluna 'Mês' no formato desejado para o eixo X
    dados_por_mes['Mês'] = dados_por_mes['Mês'].astype(int)

    # Criar gráfico de linha com plotly
    fig = px.line(dados_por_mes, x='Mês', y='Total', color='Ano',
                  title='Número de Acidentes por Mês e Ano',
                  labels={'Mês': 'Mês', 'Total': 'Número de Acidentes', 'Ano': 'Ano'},
                  markers=True)

    # Ajustar o formato do eixo X para mostrar apenas os meses
    fig.update_xaxes(
        tickmode='array',
        tickvals=list(range(1, 13)),  # Meses de 1 a 12
        ticktext=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']  # Nome dos meses
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)
