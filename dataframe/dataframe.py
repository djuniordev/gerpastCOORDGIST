import pandas as pd
from datetime import datetime
from .columns import colunasDesejadasAcidente, colunasRenomeadasAcidente, colunasDesejadasTratamento, colunasRenomeadasTratamento, colunasDesejadasAcidenteTratamento, colunasRenomeadasAcidenteTratamento
def configDataframeAcidentes(df):
    df = df.rename(columns=colunasRenomeadasAcidente)

    # Excluir linhas onde a coluna "B" está vazia
    df = df.dropna(subset=['UNIDADE'])

    df['DATA DO ACIDENTE'] = pd.to_datetime(df['DATA DO ACIDENTE'], dayfirst=True)

    df['HORA DO ACIDENTE'] = df['HORA DO ACIDENTE'].str.replace(' H', '', regex=False)
    df['HORA DO ACIDENTE'] = pd.to_timedelta(df['HORA DO ACIDENTE']+':00')
    #df['DATA DO ACIDENTE'] = df['DATA DO ACIDENTE'].dt.strftime('%d/%m/%Y')

    df["VEÍCULOS ENVOLVIDOS"] = df["VEÍCULOS ENVOLVIDOS"].str.replace('Veículo de Passeio', 'Carro')

    def agregar_veiculos(row, termos):
        if not isinstance(row, str):
            return None

        # Verificar se algum termo está presente em row
        for termo in termos:
            if termo in row:
                return termo

        return None

    # Lista de termos para categorização
    termos = ['Bicicleta', 'Caminhão', 'Caminhonete', 'Motocicleta', 'Carro']

    # Aplicar a função para agregar os dados
    df['VEÍCULOS ENVOLVIDOS'] = df['VEÍCULOS ENVOLVIDOS'].apply(lambda x: agregar_veiculos(x, termos))

    def calcular_idade(data_nascimento):
        data = datetime.strptime(data_nascimento, "%d/%m/%Y")
        ano_data = data.year

        ano_atual = datetime.now().year

        idade = ano_atual - ano_data

        return idade

    # Função para categorizar a idade
    def categorizar_idade(idade):
        if idade < 10:
            return 'Menos de 10'
        elif 10 <= idade < 20:
            return '10 a 19'
        elif 20 <= idade < 30:
            return '20 a 29'
        elif 30 <= idade < 40:
            return '30 a 39'
        elif 40 <= idade < 50:
            return '40 a 49'
        elif 50 <= idade < 60:
            return '50 a 59'
        elif 60 <= idade < 70:
            return '60 a 69'
        elif 70 <= idade < 80:
            return '70 a 79'
        else:
            return '80 ou mais'

    # Calcula a idade e categoriza para cada linha
    df['IDADE'] = df['DATA NASCIMENTO'].apply(calcular_idade)
    df['CATEGORIA IDADE'] = df['IDADE'].apply(categorizar_idade)
    df = df[colunasDesejadasAcidente]

    return df

def configDataframeTratamento(df):
    df = df.rename(columns=colunasRenomeadasTratamento)

    # Excluir linhas onde a coluna "B" está vazia
    df = df.dropna(subset=['UNIDADE'])

    df['DATA DO ACIDENTE'] = pd.to_datetime(df['DATA DO ACIDENTE'], dayfirst=True)
    df['DATA DO TRATAMENTO'] = pd.to_datetime(df['DATA DO TRATAMENTO'], dayfirst=True)
    df['INICIO INTERNACAO'] = pd.to_datetime(df['INICIO INTERNACAO'], dayfirst=True)

    def calcular_idade(data_nascimento):
        data = datetime.strptime(data_nascimento, "%d/%m/%Y")
        ano_data = data.year

        ano_atual = datetime.now().year

        idade = ano_atual - ano_data

        return idade

    # Função para categorizar a idade
    def categorizar_idade(idade):
        if idade < 10:
            return 'Menos de 10'
        elif 10 <= idade < 20:
            return '10 a 19'
        elif 20 <= idade < 30:
            return '20 a 29'
        elif 30 <= idade < 40:
            return '30 a 39'
        elif 40 <= idade < 50:
            return '40 a 49'
        elif 50 <= idade < 60:
            return '50 a 59'
        elif 60 <= idade < 70:
            return '60 a 69'
        elif 70 <= idade < 80:
            return '70 a 79'
        else:
            return '80 ou mais'

    # Calcula a idade e categoriza para cada linha
    df['IDADE'] = df['DATA NASCIMENTO'].apply(calcular_idade)
    df['CATEGORIA IDADE'] = df['IDADE'].apply(categorizar_idade)
    df = df[colunasDesejadasTratamento]

    return df

def configDataframeAcidentesTratamento(df):
    df = df.rename(columns=colunasRenomeadasAcidenteTratamento)

    # Excluir linhas onde a coluna "B" está vazia
    df = df.dropna(subset=['UNIDADE'])

    df['DATA DO ACIDENTE'] = pd.to_datetime(df['DATA DO ACIDENTE'], dayfirst=True)

    df['HORA DO ACIDENTE'] = df['HORA DO ACIDENTE'].str.replace(' H', '', regex=False)
    df['HORA DO ACIDENTE'] = pd.to_timedelta(df['HORA DO ACIDENTE']+':00')
    df['INICIO INTERNACAO'] = pd.to_datetime(df['INICIO INTERNACAO'], dayfirst=True)
    #df['DATA DO ACIDENTE'] = df['DATA DO ACIDENTE'].dt.strftime('%d/%m/%Y')

    df["VEÍCULOS ENVOLVIDOS"] = df["VEÍCULOS ENVOLVIDOS"].str.replace('Veículo de Passeio', 'Carro')

    def agregar_veiculos(row, termos):
        if not isinstance(row, str):
            return None

        # Verificar se algum termo está presente em row
        for termo in termos:
            if termo in row:
                return termo

        return None

    # Lista de termos para categorização
    termos = ['Bicicleta', 'Caminhão', 'Caminhonete', 'Motocicleta', 'Carro']

    # Aplicar a função para agregar os dados
    df['VEÍCULOS ENVOLVIDOS'] = df['VEÍCULOS ENVOLVIDOS'].apply(lambda x: agregar_veiculos(x, termos))

    def calcular_idade(data_nascimento):
        data = datetime.strptime(data_nascimento, "%d/%m/%Y")
        ano_data = data.year

        ano_atual = datetime.now().year

        idade = ano_atual - ano_data

        return idade

    # Função para categorizar a idade
    def categorizar_idade(idade):
        if idade < 10:
            return 'Menos de 10'
        elif 10 <= idade < 20:
            return '10 a 19'
        elif 20 <= idade < 30:
            return '20 a 29'
        elif 30 <= idade < 40:
            return '30 a 39'
        elif 40 <= idade < 50:
            return '40 a 49'
        elif 50 <= idade < 60:
            return '50 a 59'
        elif 60 <= idade < 70:
            return '60 a 69'
        elif 70 <= idade < 80:
            return '70 a 79'
        else:
            return '80 ou mais'

    # Calcula a idade e categoriza para cada linha
    df['IDADE'] = df['DATA NASCIMENTO'].apply(calcular_idade)
    df['CATEGORIA IDADE'] = df['IDADE'].apply(categorizar_idade)
    df = df[colunasDesejadasAcidenteTratamento]


    return df