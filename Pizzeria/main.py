from builder import *
from interf_usuario import *
from funciones_main import *

if __name__ == "__main__":
    web_pizza = WebPizzeria()
    controlador = True
    numero = 1
    while controlador:
        controlador, usuario = menu(web_pizza)
        while controlador:
            #Preparamos para el nuevo pedido
            crear_pizza(usuario, numero)
            numero += 1
            seguir = input("\nQuieres pedir otra pizza? (Si/No) ")
            if seguir == 'No' or seguir == 'no':
                controlador = False
    print("\nHasta la próxima!")
    web_pizza.guardar_datos()
