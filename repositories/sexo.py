from pandas import DataFrame

class SexoRepository():
    def __init__(self, dadosUnidade: DataFrame):
        self.dadosUnidade = dadosUnidade

    def countSexo(self):

        totalSexoUnidade = self.dadosUnidade["SEXO"].count()
        contagemPorSexo = self.dadosUnidade["SEXO"].value_counts()
        totalMasculino = contagemPorSexo.get("Masculino", 0)
        totalFeminino = contagemPorSexo.get("Feminino", 0)

        infoSexo = {
            "TotalSexoUnidade": totalSexoUnidade,
            "TotalMasculino": totalMasculino,
            "TotalFeminino": totalFeminino,
        }

        return infoSexo