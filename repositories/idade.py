from pandas import DataFrame

def countIdade(dadosUnidade: DataFrame):
    totalIdadeUnidade = dadosUnidade["IDADE"].count()
    indicesVazios = dadosUnidade["IDADE"].isnull() | (dadosUnidade["IDADE"] == '')

    numerosSequenciaVazia = dadosUnidade.loc[indicesVazios, "SEQUÊNCIA"]

    totalMenosde10anos = (dadosUnidade["CATEGORIA IDADE"] == "Carro").sum()
    total10a19anos = (dadosUnidade["CATEGORIA IDADE"] == "Bicicleta").sum()
    total20a29anos = (dadosUnidade["CATEGORIA IDADE"] == "Caminhao").sum()
    total30a39anos = (dadosUnidade["CATEGORIA IDADE"] == "Caminhonete").sum()
    total40a49anos = (dadosUnidade["CATEGORIA IDADE"] == "Motocicleta").sum()
    total50a59anos = (dadosUnidade["CATEGORIA IDADE"] == "Motocicleta").sum()
    total60a69anos = (dadosUnidade["CATEGORIA IDADE"] == "Motocicleta").sum()
    total70a79anos = (dadosUnidade["CATEGORIA IDADE"] == "Motocicleta").sum()
    total80AnosOuMais = (dadosUnidade["CATEGORIA IDADE"] == "Motocicleta").sum()

    infoIdade = {
        "TotalVeiculoUnidade": totalVeiculoUnidade,
        "NumeroSequenciaVazia": numerosSequenciaVazia.tolist(),
        "TotalCarro": totalCarro,
        "TotalBicicleta": totalBicicleta,
        "TotalCaminhao": totalCaminhao,
        "TotalCaminhonete": totalCaminhonete,
        "TotalMotocicleta": totalMotocicleta
    }

    return infoIdade

