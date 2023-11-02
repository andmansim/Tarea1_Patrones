from __future__ import annotations
from abc import ABC, abstractmethod
from leer_csv import datos_num, datos_no_num


class AbstractFactory(ABC):
    """
    Esta clase nos declara métodos que retornan los diferentes objetos abstractos. Estos están vacios. 
    Las subclases serán las que implementen los métodos y retornen los objetos concretos.
    El método crea_calculos_estadisticos() es para calcular la media, moda, mediana, etc.
    El método crea_representaciones_estadisticas() es para representar los datos en gráficas.
    """
    
    @abstractmethod #reservamos el espacio de memoria
    def crea_calculos_estadisticos(self) -> AbstractProductA: 
        pass
    @abstractmethod
    def crea_representaciones_estadisticas(self) -> AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):
    """
    Aquí le indicamos que nos retorne los productos concretos que necesitemos para el Factory 1.
    Factory 1 es para los cálculos estadísticos.
    Donde aunque le pasemos uno en concreto nos devolverá un producto abstracto.
    Si alguno de los métodos no se usa, no se modifica, se pone return None.
    """

    def crea_calculos_estadisticos(self) -> AbstractProductA: 
        return ConcreteProductA1()

    def crea_representaciones_estadisticas(self) -> AbstractProductB:
        return None


class ConcreteFactory2(AbstractFactory):
    """
    Aquí le indicamos que nos retorne los productos concretos que necesitemos para el Factory 2.
    Factory 2 es para las representaciones estadísticas.
    Donde aunque le pasemos uno en concreto nos devolverá un producto abstracto.
    Si alguno de los métodos no se usa, no se modifica, se pone return None.
    """

    def crea_calculos_estadisticos(self) -> AbstractProductA:
        return None

    def crea_representaciones_estadisticas(self) -> AbstractProductB:
        return ConcreteProductB1()


class AbstractProductA(ABC):
    """
    Es igual que el abstract factory, pero para los productos. Es decir, es una clase abstracta A que solo 
    nos declara los métodos. 
    AbstractProductA nos declara los métodos que vamos a usar para el análisis estadístico.
    """

    @abstractmethod
    def calculo_media(self) -> str: 
        pass
    @abstractmethod
    def calculo_mediana(self) -> str:
        pass
    @abstractmethod
    def calculo_moda(self) -> str:
        pass
    @abstractmethod
    def calculo_varianza(self) -> str:
        pass
    @abstractmethod
    def calculo_desviacion_tipica(self) -> str:
        pass

    


class ConcreteProductA1(AbstractProductA): 
    '''
    En este clase implementamos la lógica y lo que queremos hacer con los métodos de AbstractProductA. (Cálculo estadísitico)

    '''
    def calculo_media(self, datos) -> str:
        media = datos.mean()
        return f"La media es: \n {media}"
    def calculo_mediana(self, datos) -> str:
        mediana = datos.median()
        return f"La mediana es: \n {mediana}"
    def calculo_moda(self, datos) -> str:
        moda = datos.mode()
        return f"La moda es: \n {moda}"
    def calculo_varianza(self, datos) -> str:
        varianza = datos.var()
        return f"La varianza es: \n {varianza}"
    def calculo_desviacion_tipica(self, datos) -> str:
        desviacion_tipica = datos.std()
        return f"La desviación típica es: \n {desviacion_tipica}"


class AbstractProductB(ABC):
    """
    Es igual que el abstract factory, pero para los productos. Es decir, es una clase abstracta A que solo 
    nos declara los métodos. 
    AbstractProductB nos declara los métodos que vamos a usar para la representación estadística.
    """

    @abstractmethod
    def representacion_grafica(self) -> str:
        pass



class ConcreteProductB1(AbstractProductB):
    '''
    En este clase implementamos la lógica y lo que queremos hacer con los métodos de AbstractProductA. (Cálculo estadísitico)

    '''
    def representacion_grafica(self, datos) -> str:
        pass #Aquí iría la representación gráfica de los datos. PENSAR


    
def client_code(factory: AbstractFactory, datos) -> None:
    """
    ns 
    """
    calculos_estadisticos = factory.crea_calculos_estadisticos()
    representaciones_estadisticas = factory.crea_representaciones_estadisticas()
    
    print(calculos_estadisticos.calculo_media(datos))
    print(calculos_estadisticos.calculo_mediana(datos))
    print(calculos_estadisticos.calculo_moda(datos))
    print(calculos_estadisticos.calculo_varianza(datos))
    print(calculos_estadisticos.calculo_desviacion_tipica(datos))
    #print(representaciones_estadisticas.representacion_grafica(datos))
    #Está comentado porque no está implementado.
    
    


if __name__ == "__main__":
    
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1(), datos_num)
    #Da error porque falta dividir el csv en dados numéricos y no numéricos.

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    #client_code(ConcreteFactory2(), datos_no_num)
    #Está comentado porque no está implementado.