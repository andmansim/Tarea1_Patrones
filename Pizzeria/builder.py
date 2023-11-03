from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any #tipado dinámigo 


class Builder(ABC):
    """
    Es una clase abstracta que contiene la estructura básica de una pizza. 
    Teniendo el propio producto (la pizza) y los métodos para construir las distintas 
    partes de la pizza, como la masa, la salsa, la presentación etc.
    """

    @property #nos genera los getter y setter de los de abajo
    @abstractmethod
    def pizza(self) -> None:
        pass

    @abstractmethod
    def tipo_masa(self) -> None:
        pass
    
    @abstractmethod
    def salsa_base(self) -> None:
        pass
    
    @abstractmethod
    def ingr_principales(self) -> None: #ingredientes principales
        pass
    
    @abstractmethod
    def tec_coccion(self) -> None: #técnica de cocción
        pass
    
    @abstractmethod
    def presentacion(self) -> None:
        pass
    
    @abstractmethod
    def maridajes(self)-> None: #maridajes recomendados
        pass
    
    @abstractmethod
    def extras(self) -> None:
        pass
    
class ConcreteBuilder1(Builder): #Es un tipo de pizza, donde personaliza los métodos de la clase Builder
    """
    Implementa la interfaz del Builder y proporciona implementaciones concretas de los métodos para construir las partes del objeto. 
    Cada builder concreto puede crear un objeto con una representación específica.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = Product1() #pizza final

    @property
    def pizza(self) -> Product1:
        pizza = self._pizza
        self.reset()
        return pizza

    def tipo_masa(self) -> None:
        masa = input("¿Qué tipo de masa quieres? (fina, normal, gruesa): ")
        self._pizza.add(masa)
    
    def salsa_base(self) -> None:
        salsa = input("¿Qué salsa quieres? (tomate, barbacoa, carbonara): ")
        self._pizza.add(salsa)
    
    def ingr_principales(self) -> None:
        while True:
            ingrediente = input("¿Qué ingrediente quieres? (pulsa 0 para salir): ")
            if ingrediente == "0":
                break
            else:
                self._pizza.add(ingrediente)
    
    def tec_coccion(self) -> None:
        coccion = input("¿Qué técnica de cocción quieres? (horno de leña, horno eléctrico, horno de gas): ")
        self._pizza.add(coccion)
    
    def presentacion(self) -> None:
        presentacion = input("¿Cómo quieres que se presente? (en caja de cartón, en plato de barro): ")
        self._pizza.add(presentacion)
    
    def maridajes(self) -> None:
        while True:
            maridaje = input("¿Qué maridaje quieres? (Vino tinto, cerveza, etc.)(pulsa 0 para salir): ")
            if maridaje == "0":
                break
            else:
                self._pizza.add(maridaje)
        
    
    def extras(self) -> None:
        while True:
            extra = input("¿Qué extra quieres? (bordes especiales, ingrediente extra, etc.)(pulsa 0 para salir): ")
            if extra == "0":
                break
            else:
                self._pizza.add(extra)
        
    


class Product1(): #Es el producto final, en este caso la pizza, donde se almacenan las partes de la pizza
    """
    Solo se utiliza cuando el producto es complejo y requiere una configuración extensa. 
    Los resultados de varios builder pueden que no sigan la misma interfaz. 
    Puede ser una clase única o una estructura de datos compleja.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director: #Chef
    """
    Es el único responsable de la ejecución de los pasos de construcción en una secuencia particular.
    Es útil cuando se producen productos de acuerdo con un orden o configuración específicos.
    La clase Director es opcional, ya que el código del cliente puede controlar los builders directamente.
    """

    def __init__(self) -> None:
        self._builder = None 

    @property
    def builder(self) -> Builder: #getter del builder
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None: #setter del builder
        self._builder = builder

    #Construimos el producto según el tipo de pizza que queramos
    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_semi_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

    def build_full_featued_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()
        self.builder.produce_part_d()
        self.builder.produce_part_e()

if __name__ == "__main__":

    director = Director() #Chef
    builder = ConcreteBuilder1() #Tipo de pizza
    director.builder = builder #Le decimos al chef que tipo de pizza queremos

    print("Standard basic product: ")
    director.build_minimal_viable_product() #Le decimos al chef los pasos a seguir para dicha pizza
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    print("Custom product: ") #Esto no lo entiendo
    builder.produce_part_a() 
    builder.produce_part_b()
    builder.produce_part_c()
    builder.produce_part_d() 
    builder.product.list_parts()
    