from pandas import DataFrame

def countVeiculo(dadosUnidade: DataFrame):
    totalVeiculoUnidade = dadosUnidade["VEÍCULOS ENVOLVIDOS"].count()
    indicesVazios = dadosUnidade["VEÍCULOS ENVOLVIDOS"].isnull() | (dadosUnidade["VEÍCULOS ENVOLVIDOS"] == '')

    numerosSequenciaVazia = dadosUnidade.loc[indicesVazios, "SEQUÊNCIA"]

    totalCarro = (dadosUnidade["VEÍCULOS ENVOLVIDOS"] == "Carro").sum()
    totalBicicleta = (dadosUnidade["VEÍCULOS ENVOLVIDOS"] == "Bicicleta").sum()
    totalCaminhao = (dadosUnidade["VEÍCULOS ENVOLVIDOS"] == "Caminhão").sum()
    totalCaminhonete = (dadosUnidade["VEÍCULOS ENVOLVIDOS"] == "Caminhonete").sum()
    totalMotocicleta = (dadosUnidade["VEÍCULOS ENVOLVIDOS"] == "Motocicleta").sum()
    totalCarroPasseio = (dadosUnidade["VEÍCULOS ENVOLVIDOS"] == "Carro de Passeio").sum()

    infoVeiculo = {
        "TotalVeiculoUnidade": totalVeiculoUnidade,
        "NumeroSequenciaVazia": numerosSequenciaVazia.tolist(),
        "TotalCarro": totalCarro,
        "TotalBicicleta": totalBicicleta,
        "TotalCaminhao": totalCaminhao,
        "TotalCaminhonete": totalCaminhonete,
        "TotalMotocicleta": totalMotocicleta,
        "TotalCarroPasseio": totalCarroPasseio
    }

    return infoVeiculo

