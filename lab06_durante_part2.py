import xlrd
import pandas as pd
import openpyxl
from pandas import ExcelWriter

archivo=pd.read_excel('BI_Clientes06.xlsx', sheet_name='Hoja1')
data=pd.DataFrame(archivo, columns=['CustomerKey', 'FirstName','TotalChildren'])
resultados2=data.dropna(subset=['TotalChildren'],axis=0)

destino=ExcelWriter('Resultados2.xlsx')
resultados2.to_excel(destino, index=False)
destino._save()
print('Archivo creado correctamente')