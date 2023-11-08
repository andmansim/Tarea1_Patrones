'''
El cliente tiene que registrarse, ya sea con su clave o su nombre. 
Si es la primera vez que entra, se le pregunta que tipo de pizza quiere y se le guarda en su historial.
Si ya ha entrado antes, se le pregunta si quiere la misma pizza que la última vez o quiere otra.
Si quiere la misma, se le pregunta si quiere algún extra o algo diferente.
Si quiere otra, se le pregunta que tipo de pizza quiere y se le guarda en su historial.

Tiene que haber medidas de seguridad para que no se pueda acceder a los datos de otros clientes.
'''
import csv
from builder import *


class Usuario:
    '''
    Esta clase se encarga de recoger el pedido actual y mirar si ha habido algún pedido anterior 
    con dicho usuario.
    '''
    def __init__(self, nombre, contrasenia):
        self.nombre = nombre
        self.contrasenia = contrasenia
        self.ordenes = []

    def pedido_actual(self, pizza):
        self.ordenes.append(pizza)

    def ultimo_pedido(self):
        if self.ordenes:
            return self.ordenes[-1]
        else:
            return None


