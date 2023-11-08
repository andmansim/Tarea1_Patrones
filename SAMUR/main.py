from . import abstract_factory
from . import cliente_abs_fact
from . import leer_csv
def main():
    
    print("Datos estadísticos")
    cliente_abs_fact.client_code(abstract_factory.ConcreteFactory1(), leer_csv.datos_num, 1)

    print("\n")

    print("Representación gráfica de algunos datos")
    cliente_abs_fact.client_code(abstract_factory.ConcreteFactory2(), leer_csv.datos, 2)

if __name__ == "__main__":
    main()