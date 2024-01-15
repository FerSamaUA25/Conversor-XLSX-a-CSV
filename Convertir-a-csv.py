import pandas as pd

# Ruta del archivo XLSX
xlsx_file_path = 'C:/Users/fernando.samaniego/OneDrive - americana.edu.py/Documentos/XLSX a CSV/CRM-Dataverse.xlsx'

# Ruta donde quieres guardar el archivo CSV
csv_output_path = 'C:/Users/fernando.samaniego/OneDrive - americana.edu.py/Documentos/XLSX a CSV/CRM-Dataverse.csv'

# Leer el archivo XLSX
df = pd.read_excel(xlsx_file_path)

# Guardar como archivo CSV delimitado por comas
df.to_csv(csv_output_path, index=False, encoding='utf-8', sep=',')

print("Archivo convertido y guardado como:", csv_output_path)