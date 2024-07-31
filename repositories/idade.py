from pandas import DataFrame


def countIdade(dadosUnidade: DataFrame):
    totalIdadeUnidade = dadosUnidade["IDADE"].count()
    indicesVazios = dadosUnidade["IDADE"].isnull() | (dadosUnidade["IDADE"] == '')

    numerosSequenciaVazia = dadosUnidade.loc[indicesVazios, "SEQUÊNCIA"]

    totalMenosde10anos = (dadosUnidade["CATEGORIA IDADE"] == "Menos de 10").sum()
    total10a19anos = (dadosUnidade["CATEGORIA IDADE"] == "10 a 19").sum()
    total20a29anos = (dadosUnidade["CATEGORIA IDADE"] == "20 a 29").sum()
    total30a39anos = (dadosUnidade["CATEGORIA IDADE"] == "30 a 39").sum()
    total40a49anos = (dadosUnidade["CATEGORIA IDADE"] == "40 a 49").sum()
    total50a59anos = (dadosUnidade["CATEGORIA IDADE"] == "50 a 59").sum()
    total60a69anos = (dadosUnidade["CATEGORIA IDADE"] == "60 a 69").sum()
    total70a79anos = (dadosUnidade["CATEGORIA IDADE"] == "70 a 79").sum()
    total80AnosOuMais = (dadosUnidade["CATEGORIA IDADE"] == "80 ou mais").sum()

    infoIdade = {
        "TotalIdadeUnidade": totalIdadeUnidade,
        "NumeroSequenciaVazia": numerosSequenciaVazia.tolist(),
        "Total -10": totalMenosde10anos,
        "Total 10 a 19": total10a19anos,
        "Total 20 a 29": total20a29anos,
        "Total 30 a 39": total30a39anos,
        "Total 40 a 49": total40a49anos,
        "Total 50 a 59": total50a59anos,
        "Total 60 a 69": total60a69anos,
        "Total 70 a 79": total70a79anos,
        "Total 80 ou +": total80AnosOuMais
    }

    return infoIdade