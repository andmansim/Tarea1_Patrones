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
Hay 5 columnas vacias : precio, dias-excluidos, descripción, unnamed: 29 y audiencia. 
La audiencia solo tiene un dato por eso la podemos considerar una columna vacia.
Columnas numéricas son: id evento, gratuito, larga-duración, num-instalación, código postal-instalación, latitud, longitud, coord-x, coord-y)
El resto son no numéricas. 
'''

#Limpiamos y organizamos los datos

datos_copia = datos.copy() #realizamos primero una copia de los datos

#Eliminamos las columnas vacias
datos = datos.drop(['PRECIO', 'DIAS-EXCLUIDOS', 'DESCRIPCION', 'Unnamed: 29', 'AUDIENCIA'], axis=1)
print(datos.info())

#Examinamos cada columna por separado
print(datos.head())
'''
Al observar cada columna nos damos cuenta que no podemos completar los espacios en blanco con la media o la mediana. 
'''
#Interpretaremos los 0, 1 de las columnas gratuito y larga-duración como False y True respectivamente

