from pandas import DataFrame

def countMunicipio(dadosUnidade: DataFrame):
    totalMunicipioUnidade = dadosUnidade["MUNICÍPIO ACIDENTE"].count()
    indicesVazios = dadosUnidade["MUNICÍPIO ACIDENTE"].isnull() | (dadosUnidade["MUNICÍPIO ACIDENTE"] == '')

    numerosSequenciaVazia = dadosUnidade.loc[indicesVazios, "SEQUÊNCIA"]

    contagemMunicipio = dadosUnidade['MUNICÍPIO ACIDENTE'].value_counts()

    infoMunicipio = {
        "TotalMunicipioAcidente": totalMunicipioUnidade,
        "NumeroSequenciaVazia": numerosSequenciaVazia.tolist(),
        "ContagemMunicipio": contagemMunicipio.to_dict()
    }

    return infoMunicipio

