import os
import glob

def ler_arquivos_excel(folder_path):
    excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))
    return excel_files