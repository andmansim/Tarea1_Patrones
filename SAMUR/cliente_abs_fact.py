from abstract_factory import AbstractFactory

def client_code(factory: AbstractFactory, datos, numero) -> None:
    """
    Función donde instanciamos todas las clases y los métodos que necesitemos.
     
    """
    calculos_estadisticos = factory.crea_calculos_estadisticos()
    representaciones_estadisticas = factory.crea_representaciones_estadisticas()
    
    if numero == 1:
        print(calculos_estadisticos.calculo_media(datos))
        print(calculos_estadisticos.calculo_mediana(datos))
        print(calculos_estadisticos.calculo_moda(datos))
        print(calculos_estadisticos.calculo_varianza(datos))
        print(calculos_estadisticos.calculo_desviacion_tipica(datos))
    else:
        representaciones_estadisticas.barras_2columnas(datos, 'GRATUITO', 'LARGA-DURACION')
        representaciones_estadisticas.barras_2columnas(datos, 'LARGA-DURACION', 'TIPO')
        representaciones_estadisticas.barras_1columna(datos, 'GRATUITO')
        representaciones_estadisticas.barras_1columna(datos, 'DISTRITO-INSTALACION')
        representaciones_estadisticas.barras_1columna(datos, 'TIPO')
    