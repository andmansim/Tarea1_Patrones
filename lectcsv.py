#Leemos el csv
import pandas as pd

datos = pd.read_csv('datos-emergencias.csv', sep=';', encoding='ISO-8859-1')

#Examinamos los datos del csv
print ('Información del csv')
print(datos.info())
print('\n Columnas del csv')
print(datos.columns)
'''
Observacón: 
Hay 3 columnas vacias (precio, dias-excluidos y descripción).
Columnas numéricas son: id evento, gratuito, larga-duración, num-instalación, código postal-instalación, latitud, longitud, coord-x, coord-y)
El resto son no numéricas. 
'''

#Limpiamos y organizamos los datos

datos_copia = datos.copy() #realizamos primero una copia de los datos

#Eliminamos las columnas vacias
datos = datos.drop(['precio', 'dias-excluidos', 'descripción'], axis=1)
print(datos.info())