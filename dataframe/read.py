import pandas as pd
from .dataframe import configDataframe
from page.page import captureMonth
def read(planilha):

    df = pd.read_excel(planilha)
    mes = captureMonth(df)
    df = configDataframe(df)

    return df, mes
