#Leemos el csv
import pandas as pd

datos = pd.read_csv('datos-emergencias.csv', sep=';', encoding='ISO-8859-1')

print(datos.head())