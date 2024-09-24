import xlrd
import pandas as pd
import openpyxl
import numpy as np
from pandas import ExcelWriter

archivo=pd.read_excel('BI_Clientes06.xlsx', sheet_name='Hoja1')
data=pd.DataFrame(archivo, columns=['TotalChildren'])
media_total=data['TotalChildren'].mean()

resultados3 = data['TotalChildren'].replace(np.nan, media_total)
destino=ExcelWriter('Resultados3.xlsx')

resultados3.to_excel(destino, index=False)
destino._save()
print('Archivo creado correctamente')