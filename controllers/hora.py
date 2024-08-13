import pandas as pd

def mostrarDadosHora(st, dadosUnidade):

    # Definindo os limites dos turnos como timedelta
    manha_inicio = pd.to_timedelta('06:00:00')  # Início do Turno Manhã
    manha_fim = pd.to_timedelta('11:59:00')     # Fim do Turno Manhã
    tarde_inicio = pd.to_timedelta('12:00:00')  # Início do Turno Tarde
    tarde_fim = pd.to_timedelta('17:59:00')     # Fim do Turno Tarde
    noite_inicio = pd.to_timedelta('18:00:00')  # Início do Turno Noite
    noite_fim = pd.to_timedelta('23:59:00')     # Fim do Turno Noite
    madrugada_inicio = pd.to_timedelta('00:00:00') # Início do Turno Madrugada
    madrugada_fim = pd.to_timedelta('05:59:00') # Fim do Turno Madrugada

    # Função para definir o turno com base no timedelta
    def definir_turno(timedelta):
        if manha_inicio <= timedelta <= manha_fim:
            return 'Manhã'
        elif tarde_inicio <= timedelta <= tarde_fim:
            return 'Tarde'
        elif noite_inicio <= timedelta <= noite_fim:
            return 'Noite'
        elif madrugada_inicio <= timedelta <= madrugada_fim:
            return 'Madrugada'
        else:
            return 'Fora do Período'

    dadosUnidade["TURNO"] = dadosUnidade["HORA DO ACIDENTE"].apply(definir_turno)
    # Converter timedelta para string no formato HH:MM
    dadosUnidade['HORA DO ACIDENTE'] = dadosUnidade['HORA DO ACIDENTE'].astype(str).str[7:16]
    print(dadosUnidade[["HORA DO ACIDENTE", "TURNO"]])
    # Caminho para o arquivo Excel que será criado
    caminho_arquivo = 'dados_unidade.xlsx'

    # Salvando o DataFrame em uma planilha Excel
    dadosUnidade.to_excel(caminho_arquivo, index=False, engine='openpyxl')