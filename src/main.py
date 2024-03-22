import os
import glob
import pandas as pd

import utils.extract as extract
import utils.transform as transform
import utils.load as load


def main():
    folder_path = os.path.join('src', 'data', 'raw')
    output_file = os.path.join('src', 'data', 'ready', 'clean.xlsx')

    excel_files = extract.ler_arquivos_excel(folder_path)
    
    if not excel_files:
        print("Nenhum arquivo compatível encontrado")
        return

    dfs = []

    for excel_file in excel_files:
        df_temp = transform.processar_arquivo_excel(excel_file)
        if df_temp is not None:
            dfs.append(df_temp)

    result = load.concatenar_dataframes(dfs)
    load.salvar_arquivo_excel(result, output_file)

if __name__ == "__main__":
    main()