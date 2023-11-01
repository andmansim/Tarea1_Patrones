from __future__ import annotations
from abc import ABC, abstractmethod


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
        return ConcreteProductB2()


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
        return f"La media es: {media}"
    def calculo_mediana(self, datos) -> str:
        mediana = datos.median()
        return f"La mediana es: {mediana}"
    def calculo_moda(self, datos) -> str:
        moda = datos.mode()
        return f"La moda es: {moda}"
    def calculo_varianza(self, datos) -> str:
        varianza = datos.var()
        return f"La varianza es: {varianza}"
    def calculo_desviacion_tipica(self, datos) -> str:
        desviacion_tipica = datos.std()
        return f"La desviación típica es: {desviacion_tipica}"


class AbstractProductB(ABC):
    """
    Es igual que el abstract factory, pero para los productos. Es decir, es una clase abstracta A que solo 
    nos declara los métodos. 
    AbstractProductB nos declara los métodos que vamos a usar para la representación estadística.
    """

    @abstractmethod
    



class ConcreteProductB1(AbstractProductB):
    '''
    Clase B1 que contiene los métodos que hacen cosas concretas del producto B.
    Ponemos el código que queramos y lo retornamos.
    '''
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    La variante, Producto B1, solo puede funcionar correctamente con la variante,
    Producto A1. Sin embargo, acepta cualquier instancia de AbstractProductA como
    argumento. 
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    '''
    Clase B2 que contiene los métodos que hacen cosas concretas del producto B.
    Ponemos el código que queramos y lo retornamos.
    '''
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
       La variante, Producto B2, solo puede funcionar correctamente con la variante,
        Producto A2. Sin embargo, acepta cualquier instancia de AbstractProductA como
        argumento. 
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


    
def client_code(factory: AbstractFactory) -> None:
    """
    El código del cliente funciona con fábricas y productos solo a través de tipos abstractos:
    AbstractFactory y AbstractProduct. Esto le permite pasar cualquier subclase de fábrica o 
    producto al código del cliente sin romperlo.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")



if __name__ == "__main__":
    """
    El código cliente puede funcionar con cualquier clase de fábrica concreta.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())