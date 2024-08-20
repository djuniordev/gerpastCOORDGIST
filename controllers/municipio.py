import plotly.express as px
from repositories.municipio import countMunicipio
def mostrarDadosMunicipio(st, dadosUnidade):
        municipio_counts = dadosUnidade["MUNICÍPIO ACIDENTE"].value_counts().reset_index()
        municipio_counts.columns = ['Município', 'Total']

        # Criar gráfico com plotly
        fig = px.bar(municipio_counts, x='Município', y='Total',
                     color='Município',
                     )  # Define o tamanho do buraco no meio para criar o efeito de donut
        # Mostrar o gráfico no Streamlit
        st.plotly_chart(fig, use_container_width=True)

        # infoMunicipio = countMunicipio(dadosUnidade)
        #
        # st.header("Município:")
        # st.write(f"Total: {infoMunicipio["TotalMunicipioAcidente"]}")
        # st.write(f"Sequência vazia: {infoMunicipio["NumeroSequenciaVazia"]}")
        # for municipio in infoMunicipio["ContagemMunicipio"]:
        #         st.write(f"{municipio}: {infoMunicipio["ContagemMunicipio"][municipio]}")
def dadosDetalhadosMunicipio(st, dadosUnidade):
        infoMunicipio = countMunicipio(dadosUnidade)
        st.header("Município:")
        st.write(f"Total: {infoMunicipio["TotalMunicipioAcidente"]}")
        st.write(f"Sequência vazia: {infoMunicipio["NumeroSequenciaVazia"]}")
        for municipio in infoMunicipio["ContagemMunicipio"]:
                st.write(f"{municipio}: {infoMunicipio["ContagemMunicipio"][municipio]}")