from repositories.veiculo import countVeiculo

def mostrarDadosVeiculo(st, dadosUnidade):

        infoVeiculo = countVeiculo(dadosUnidade)

        st.header("Veículos:")
        st.write(f"Total: {infoVeiculo["TotalVeiculoUnidade"]}")
        st.write(f"Sequência vazia: {infoVeiculo["NumeroSequenciaVazia"]}")
        st.write(f"Carro: {infoVeiculo["TotalCarro"]}")
        st.write(f"Bicicleta: {infoVeiculo["TotalBicicleta"]}")
        st.write(f"Caminhão: {infoVeiculo["TotalCaminhao"]}")
        st.write(f"Caminhonete: {infoVeiculo["TotalCaminhonete"]}")
        st.write(f"Motocicleta: {infoVeiculo["TotalMotocicleta"]}")
