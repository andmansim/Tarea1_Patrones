from abstract_factory import *
from cliente_abs_fact import *


if __name__ == "__main__":
    
    print("Datos estadísticos")
    client_code(ConcreteFactory1(), datos_num, 1)

    print("\n")

    print("Representación gráfica de algunos datos")
    client_code(ConcreteFactory2(), datos, 2)