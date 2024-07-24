from .columns import colunasOcultas, colunasRenomeadas
def configDataframe(df):
    df = df.drop(columns=colunasOcultas)
    df = df.rename(columns=colunasRenomeadas)

    # Excluir linhas onde a coluna "B" está vazia
    df = df.dropna(subset=['UNIDADE'])
    return df