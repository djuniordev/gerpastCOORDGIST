from pandas import DataFrame

def countSexo(dadosUnidade: DataFrame):
    indicesVazios = dadosUnidade["SEXO"].isnull() | (dadosUnidade["SEXO"] == '')
    numerosSequenciaVazia = dadosUnidade.loc[indicesVazios, "SEQUÊNCIA"]

    totalSexoUnidade = dadosUnidade["SEXO"].count()
    contagemPorSexo = dadosUnidade["SEXO"].value_counts()
    totalMasculino = contagemPorSexo.get("Masculino", 0)
    totalFeminino = contagemPorSexo.get("Feminino", 0)

    infoSexo = {
        "TotalSexoUnidade": totalSexoUnidade,
        "NumeroSequenciaVazia": numerosSequenciaVazia.tolist(),
        "TotalMasculino": totalMasculino,
        "TotalFeminino": totalFeminino,
    }

    return infoSexo