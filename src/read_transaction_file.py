import pandas as pd

def read_csv(file_path):
    """Читает операции из CSV-файла и возвращает список словарей."""
    df = pd.read_csv(file_path)
    return df.to_dict("records")


def read_excel(file_path):
    """Читает финансовые операции из Excel-файла и возвращает список словарей."""
    df = pd.read_excel(file_path)
    return df.to_dict("records")
