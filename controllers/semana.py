import plotly.express as px
import numpy as np
def mostrarDadosSemana(st, dadosUnidade):

    dadosUnidade = dadosUnidade.dropna(subset=['DATA DO ACIDENTE']).copy()
    dadosUnidade['Dia'] = dadosUnidade["DATA DO ACIDENTE"].dt.day
    dadosUnidade['Mês'] = dadosUnidade['DATA DO ACIDENTE'].dt.month
    dadosUnidade['Ano'] = dadosUnidade['DATA DO ACIDENTE'].dt.year

    mes_counts = dadosUnidade['Mês'].value_counts().reset_index().astype(int)
    ano_counts = dadosUnidade['Ano'].value_counts().reset_index().astype(int)

    dadosUnidade['Dia da Semana'] = dadosUnidade['DATA DO ACIDENTE'].dt.day_name()

    dia_counts = dadosUnidade['Dia'].value_counts().reset_index()

    # Extrai o nome do dia da semana
    dia_counts.columns = ['Dia', 'Total']

    fig = px.bar(dia_counts, x='Dia', y='Total', orientation="v",
                 title='Distribuição por Dia da Semana')
    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)
    dia_mais_acidentes = dia_counts.loc[dia_counts['Total'].idxmax(), 'Dia']
    mais_acidentes = dia_counts['Total'].max()
    if int(dia_mais_acidentes) < 10:
        dia_mais_acidentes = "0"+str(dia_mais_acidentes)

    for item in mes_counts["Mês"]:
        if item < 10:
            mes = "0"+str(item)

    # Calcular o ano com mais acidentes
    ano_counts.columns = ['Ano', 'Total']
    ano_mais_acidentes = ano_counts.loc[ano_counts['Total'].idxmax(), 'Ano']

    st.write(f"OBS: o(s) dia(s) que mais ocorreu acidente(s) foi no dia {dia_mais_acidentes}/{mes}/{ano_mais_acidentes} com {mais_acidentes} acidente(s)")

    # Dicionário para tradução dos dias da semana
    diasDaSemana = {
        'Monday': 'Segunda-feira',
        'Tuesday': 'Terça-feira',
        'Wednesday': 'Quarta-feira',
        'Thursday': 'Quinta-feira',
        'Friday': 'Sexta-feira',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    }

    # (Opcional) Exibe o DataFrame com as novas colunas
    dadosUnidade['Dia da Semana'] = dadosUnidade['Dia da Semana'].map(diasDaSemana)

    # Dados
    semana_counts = dadosUnidade["Dia da Semana"].value_counts().reset_index()
    semana_counts.columns = ['Dia da Semana', 'Total']

    fig = px.bar(semana_counts, x='Dia da Semana', y='Total',
                 color='Dia da Semana', orientation="v",
                 category_orders={'Dia da Semana': diasDaSemana.values()},  # Definir a ordem do eixo X
                 title='Distribuição por Dia da Semana')
    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

    return dadosUnidade
