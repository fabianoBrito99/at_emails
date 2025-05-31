import os
import pandas as pd

def carregar_registro(caminho):
    if os.path.exists(caminho):
        return pd.read_excel(caminho, dtype=str, engine='openpyxl')
    else:
        return pd.DataFrame(columns=['mes', 'agencia', 'arquivo'])

def salvar_registro(caminho, df):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    df.to_excel(caminho, index=False, engine='openpyxl')
