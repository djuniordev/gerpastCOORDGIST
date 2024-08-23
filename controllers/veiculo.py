import plotly.express as px
import pandas as pd
from repositories.veiculo import countVeiculo

def mostrarDadosVeiculo(st, dadosUnidade):

    # Dados para o gráfico
    veiculo_counts = dadosUnidade["VEÍCULOS ENVOLVIDOS"].value_counts().reset_index()
    veiculo_counts.columns = ['Veículo', 'Total']

    # Criar gráfico com plotly
    fig = px.bar(veiculo_counts, x='Veículo', y='Total',
                 color='Veículo',
                 title="Número de Acidentes por Veículo",
                 color_discrete_map={"Carro": "#40E0D0", "Motocicleta": "#FF007F", "Bicicleta": "#FFD700",
                                     "Caminhão": "#FF4500", "Caminhonete": "#00FF00"},
                 )  # Define o tamanho do buraco no meio para criar o efeito de donut
    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Adicionar informações adicionais (comentado, mas você pode descomentar se necessário)
    infoVeiculo = countVeiculo(dadosUnidade)
    #
    st.header("Veículos:")
    st.write(f"Total: {infoVeiculo['TotalVeiculoUnidade']}")
    st.write(f"Sequência vazia: {infoVeiculo['NumeroSequenciaVazia']}")
    st.write(f"Bicicleta: {infoVeiculo['TotalBicicleta']}")
    st.write(f"Caminhão: {infoVeiculo['TotalCaminhao']}")
    st.write(f"Caminhonete: {infoVeiculo['TotalCaminhonete']}")
    st.write(f"Motocicleta: {infoVeiculo['TotalMotocicleta']}")
    st.write(f"Carro: {infoVeiculo['TotalCarro']}")
def dadosDetalhadosVeiculos(st, dadosUnidade):
     infoVeiculo = countVeiculo(dadosUnidade)
     st.header("Veículos:")
     st.write(f"Total: {infoVeiculo['TotalVeiculoUnidade']}")
     st.write(f"Sequência vazia: {infoVeiculo['NumeroSequenciaVazia']}")
     st.write(f"Bicicleta: {infoVeiculo['TotalBicicleta']}")
     st.write(f"Caminhão: {infoVeiculo['TotalCaminhao']}")
     st.write(f"Caminhonete: {infoVeiculo['TotalCaminhonete']}")
     st.write(f"Motocicleta: {infoVeiculo['TotalMotocicleta']}")
     st.write(f"Carro: {infoVeiculo['TotalCarro']}")
