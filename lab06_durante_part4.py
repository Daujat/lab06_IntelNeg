import xlrd
import pandas as pd
import openpyxl
import numpy as np
from pandas import ExcelWriter

archivo=pd.read_excel('BI_Clientes06.xlsx', sheet_name='Hoja1')
data=pd.DataFrame(archivo)

print('Resumen de valores perdidos totales')
r1=data.isna().sum()
print(r1)

print('\nValores duplicados')
r2=data.nunique()
print(r2)

print('\nCantidad de veces que un cliente aparece en la data')
r3 = data.groupby(by='CustomerKey').size().sort_values(ascending=False)
print(r3)

print('\nEliminando valores duplicados')
r4 = data.drop_duplicates()
print(r4)

destino = ExcelWriter('Resultados4.xlsx')
r4.to_excel(destino, index=False)
destino._save()
print('Archivo creado correctamente')