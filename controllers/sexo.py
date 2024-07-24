from repositories import SexoRepository
from services import SexoService

class SexoController():
    def __init__(self, st):
        self.st = st

    def hideSexo(self, dadosUnidade):
        sexoRepository = SexoRepository(dadosUnidade)
        sexoService = SexoService(sexoRepository)

        infoSexo = sexoService.execute()

        self.st.header("Sexo:")
        self.st.write(f"Total: {infoSexo["TotalSexoUnidade"]}")
        self.st.write(f"Masculino: {infoSexo["TotalMasculino"]}")
        self.st.write(f"Feminino: {infoSexo["TotalFeminino"]}")

