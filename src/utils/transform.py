import pandas as pd
import os


def processar_arquivo_excel(excel_file):
    try:
        df_temp = pd.read_excel(excel_file)
        file_name = os.path.basename(excel_file)
        df_temp['filename'] = file_name

        if 'brasil' in file_name.lower():
            df_temp['location'] = 'br'
        elif 'france' in file_name.lower():
            df_temp['location'] = 'fr'
        elif 'italian' in file_name.lower():
            df_temp['location'] = 'it'

        df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')
        return df_temp
    except Exception as e:
        print(f"Erro ao ler o arquivo {excel_file}: {e}")
        return None