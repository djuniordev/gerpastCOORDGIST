from repositories import SexoRepository

class SexoService():
    def __init__(self, sexoRepository: SexoRepository):
        self.sexoRepository = sexoRepository

    def execute(self):
        infoSexo = self.sexoRepository.countSexo()

        return infoSexo