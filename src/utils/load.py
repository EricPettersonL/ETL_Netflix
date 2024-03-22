import pandas as pd

def concatenar_dataframes(dfs):
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        return None

def salvar_arquivo_excel(result, output_file):
    if result is not None:
        writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
        result.to_excel(writer, index=False)
        writer._save()
    else:
        print("Nenhum dado para ser salvo.")