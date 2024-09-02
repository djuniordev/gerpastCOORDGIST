from repositories.idade import countIdade
import plotly.express as px
from dataframe import listaCategorias
from repositories.idade import countIdade
def mostrarDadosIdade(st, dadosUnidade):
    idade_counts = dadosUnidade["CATEGORIA IDADE"].value_counts().reset_index()
    idade_counts.columns = ['Categoria Idade', 'Total']

    # Criar gráfico com plotly
    fig = px.bar(idade_counts, x='Total', y='Categoria Idade', orientation="h",
                 color='Categoria Idade',
                 category_orders={'Categoria Idade': listaCategorias},  # Definir a ordem do eixo X
                 title='Distribuição por Categoria de Idade')
    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # infoIdade = countIdade(dadosUnidade)
    #
    # st.header("Idade:")
    # st.write(f"Total: {infoIdade["TotalIdadeUnidade"]}")
    # st.write(f"Sequência vazia: {infoIdade["NumeroSequenciaVazia"]}")
    # st.write(f"Menos de 10 anos: {infoIdade["Total -10"]}")
    # st.write(f"10 a 19 anos: {infoIdade["Total 10 a 19"]}")
    # st.write(f"20 a 29 anos: {infoIdade["Total 20 a 29"]}")
    # st.write(f"30 a 39 anos: {infoIdade["Total 30 a 39"]}")
    # st.write(f"40 a 49 anos: {infoIdade["Total 40 a 49"]}")
    # st.write(f"50 a 59 anos: {infoIdade["Total 50 a 59"]}")
    # st.write(f"60 a 69 anos: {infoIdade["Total 60 a 69"]}")
    # st.write(f"70 a 79 anos: {infoIdade["Total 70 a 79"]}")
    # st.write(f"80 anos ou mais: {infoIdade["Total 80 ou +"]}")
def dadosIdadeDetalhados(st, dadosUnidade):
     infoIdade = countIdade(dadosUnidade)
     st.header("Idade:")
     st.write(f"Total: {infoIdade["TotalIdadeUnidade"]}")

     mostrar_tudo2 = st.checkbox("Mostrar sequência vazia idade")

     if mostrar_tudo2:
         st.write(f"Sequência vazia: {infoIdade['NumeroSequenciaVazia']}")

     st.write(f"Menos de 10 anos: {infoIdade["Total -10"]}")
     st.write(f"10 a 19 anos: {infoIdade["Total 10 a 19"]}")
     st.write(f"20 a 29 anos: {infoIdade["Total 20 a 29"]}")
     st.write(f"30 a 39 anos: {infoIdade["Total 30 a 39"]}")
     st.write(f"40 a 49 anos: {infoIdade["Total 40 a 49"]}")
     st.write(f"50 a 59 anos: {infoIdade["Total 50 a 59"]}")
     st.write(f"60 a 69 anos: {infoIdade["Total 60 a 69"]}")
     st.write(f"70 a 79 anos: {infoIdade["Total 70 a 79"]}")
     st.write(f"80 anos ou mais: {infoIdade["Total 80 ou +"]}")