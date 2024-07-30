import pandas as pd
from .dataframe import configDataframe
def read(planilha):

    df = pd.read_excel(planilha)
    df = configDataframe(df)

    return df
