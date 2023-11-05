from builder import *
from interf_usuario import *
from funciones_main import *

if __name__ == "__main__":
    web_pizza = WebPizzeria()
    controlador = True
    while controlador:
        controlador, usuario = menu(web_pizza)

        while controlador:
            #Preparamos para el nuevo pedido
            crear_pizza(usuario)
            controlador = False
    print("\nHasta la próxima!")
    web_pizza.guardar_datos()
