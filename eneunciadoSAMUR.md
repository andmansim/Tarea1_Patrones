1. Lectura de Datos: Acceda y lea el archivo CSV directamente desde el enlace proporcionado: Activaciones del SAMUR-Protección Civil. A continuación, te dejo un código que realiza la lectura del archivo CSV:
    import pandas as pd

    URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

    # Leer CSV desde la URL

    data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

    print(data.head())  # Mostrar las primeras filas para visualizar los datos

    
2. Modelado de Datos: Modela y estructura la información para su análisis.

3. Abstract Factory: Diseña un "Abstract Factory" que permita crear diferentes tipos de análisis o representaciones de los datos. Por ejemplo:
    -Una fábrica que genere análisis estadísticos (media, moda, mediana).
    -Una fábrica que produzca visualizaciones gráficas (histogramas, gráficos de barras).

Cada fábrica debe tener al menos dos productos concretos (e.g., histograma de activaciones por tipo de emergencia, gráfico de barras de activaciones por mes).

4. Análisis y Representación: Utiliza las fábricas creadas para generar distintos análisis y representaciones de los datos. Muestra la media de activaciones por día, y un histograma de las activaciones