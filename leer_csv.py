#Leemos el csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
Interpretaremos los 0, 1 de las columnas gratuito y larga-duración como False y True respectivamente
'''

#Separamos el csv de datos numéicos y datos no numéricos, para hacer el análisis estadístico
datos_num = datos.select_dtypes(include=['int64', 'float64'])
datos_no_num = datos.select_dtypes(exclude=['int64', 'float64'])

def barras_col2(datos, columna1, columna2):
    '''
    Función que nos agrupa los datos de dos columnas y nos los representa en una gráfica de barras.
    '''
    plt.title('Gráfica de barras de ' + columna1 + ' y ' + columna2)
    datos_agrupados = datos.groupby([columna2, columna1]).size()
    datos_agrupados.plot(kind='bar')
    plt.xticks(rotation='horizontal')
    plt.show()

def barras_col1(datos, columna):
    '''
    Función que nos cuenta los datos de una columna y nos los representa en una gráfica de barras.
    '''
    plt.title('Gráfica de barras de ' + columna)
    datos_representar = datos[columna].value_counts()
    datos_representar.plot(kind='bar')
    plt.xticks(rotation='horizontal')
    plt.show()

barras_col2(datos, 'GRATUITO', 'NOMBRE-INSTALACION')
barras_col2(datos, 'FECHA', 'TITULO-ACTIVIDAD')
barras_col2(datos, 'LARGA-DURACION', 'TITULO')
barras_col1(datos, 'GRATUITO')

