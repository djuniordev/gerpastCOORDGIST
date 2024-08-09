from pandas import DataFrame

def countInternacao(dadosUnidade: DataFrame):
    totalInternacaoUnidade = dadosUnidade["INICIO INTERNACAO"].count()
    #indicesVazios = dadosUnidade["MUNICÍPIO ACIDENTE"].isnull() | (dadosUnidade["MUNICÍPIO ACIDENTE"] == '')

    #numerosSequenciaVazia = dadosUnidade.loc[indicesVazios, "SEQUÊNCIA"]

    #contagemMunicipio = dadosUnidade['MUNICÍPIO ACIDENTE'].value_counts()

    infoMunicipio = {
        "TotalInfoInternacao": totalInternacaoUnidade,
        #"NumeroSequenciaVazia": numerosSequenciaVazia.tolist(),
        #"ContagemMunicipio": contagemMunicipio.to_dict()
    }

    return infoMunicipio

