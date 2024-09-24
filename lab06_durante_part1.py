import xlrd
import pandas as pd
import openpyxl
from pandas import ExcelWriter

archivo=pd.read_excel('BI_Clientes06.xlsx', sheet_name='Hoja1')
data=pd.DataFrame(archivo, columns=['CustomerKey', 'FirstName','TotalChildren'])
resultados1=data.dropna(axis=0)

destino=ExcelWriter('Resultados1.xlsx')
resultados1.to_excel(destino)
destino._save()
print('Archivo creado correctamente')