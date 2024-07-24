from datetime import datetime

def captureMonth(df):
    primeira_data = df.loc[0, 'DATA INCLUSÃO']
    data_obj = datetime.strptime(primeira_data, '%d/%m/%Y %H:%M:%S')
    mes = data_obj.month

    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro",
    }

    return meses[mes]