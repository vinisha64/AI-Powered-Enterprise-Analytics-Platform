import pandas as pd

def load_data(file_path):

    if file_path.endswith(".csv"):
        try:
            df = pd.read_csv(file_path, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, encoding="latin1")

    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)

    else:
        raise ValueError("Unsupported file format")

    return df