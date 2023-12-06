import pandas as pd

def excel_to_csv(filename, path):
    """
    Función para convertir el archivo de entrada de Excel a CSV.
    """
    archivo = pd.read_excel(filename)
    all_csv = []

    for sheet in archivo:
        df = archivo[sheet]

        csv_name = sheet.replace(' ', '_').upper()

        df.to_csv(f'{path}/{csv_name}.csv')

        all_csv.append(f'{path}/{csv_name}.csv')

    return all_csv
