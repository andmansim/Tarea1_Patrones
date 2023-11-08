from . import manejardatos
from . import funciones_main

def main():
    web_pizza = manejardatos.WebPizzeria()
    controlador = True
    numero = 1
    while controlador:
        controlador, usuario = funciones_main.menu(web_pizza)
        while controlador:
            #Preparamos para el nuevo pedido
            funciones_main.crear_pizza(usuario, numero)
            numero += 1
            seguir = input("\nQuieres pedir otra pizza? (Si/No) ")
            if seguir == 'No' or seguir == 'no':
                controlador = False
    print("\nHasta la próxima!")
    web_pizza.guardar_datos()
    
if __name__ == "__main__":

    main()