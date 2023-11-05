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


class WebPizzeria:
    '''
    la clase encargada del registro y login de los usuarios a la página. 
    Donde llama a la clase usuario para guardar los datos de los usuarios y de las pizzas.
    '''
    def __init__(self):
        self.usuario = {}
        self.cargando_datos()

    def guardar_datos(self):
        with open('pizza_data.csv', mode='w', newline='') as file:
            escribir = csv.writer(file)
            for usuario in self.usuario.values(): #Recorremos el diccionario de usuarios
                for orden in usuario.ordenes: #Recorremos la lista de pizzas
                    escribir.writerow([usuario.nombre, usuario.contrasenia, orden])

    def cargando_datos(self):
        try:
            with open('pizza_data.csv', mode='r') as file:
                leer = csv.reader(file)
                for fila in leer:
                    #Añadimos al diccionario usuario el nombre (ya está registrado)
                    nombre, contrasenia, pedido = fila
                    if nombre not in self.usuario: #Si el nombre del usuario no está en el diccionario
                        self.usuario[nombre] = Usuario(nombre, contrasenia)#añadimos el usuario al diccionario
                    usuario = self.usuario[nombre] #Asociamos a la vaiable usuario el nombre del usuario
                    usuario.pedido_actual(pedido) #Vamos añadiendo las pizzas que tiene el usuario asociadas
        except FileNotFoundError:
            pass
        
    def registrar_usuario(self, nombre, contrasenia):
        if nombre not in self.usuario: #Si el nombre del usuario no está en el diccionario (no está registrado)
            self.usuario[nombre] = Usuario(nombre, contrasenia) #añadimos el usuario al diccionario

    def login(self, nombre, contrasenia):
        #Comprobamos que el nombre y la contraseña coinciden con los datos guardados y 
        #devolvemos el nombre del usuario
        if nombre in self.usuario and self.usuario[nombre].contrasenia == contrasenia: 
            return self.usuario[nombre]
        else:
            return None

    def usuario_registrado(self, nombre):
        return nombre in self.usuario


'''def main():
    web_pizza = WebPizzeria()
    controlador = True
    while controlador:
        print("\nBienvenido a la pizzería!")
        nombre = input("Por favor introduzca su nombre de usuario (0 para salir): ")

        if nombre == "0":
            controlador = False

        if web_pizza.usuario_registrado(nombre):
            ''
            Si el usuario ya está registrado, le pedimos la contraseña para que inicie sesión. 
            Si la contraseña es correcta, le damos la bienvenida y le mostramos su último pedido.
            ''
            contrasenia = input("Introduce contraseña: ")
            usuario = web_pizza.login(nombre, contrasenia)
            if usuario: #Si coincide el nombre y la contraseña (login correcto)
                ultimo_pedido = usuario.ultimo_pedido()
                if ultimo_pedido: #Si hay algún pedido registrado
                    print(f"Tu último pedido fue: {ultimo_pedido}")
                    pedir = input("Quieres pedir lo mismo? (Si/No) ")
                    if pedir == "Si":
                        usuario.pedido_actual(ultimo_pedido)
                        print('El pedido se ha realizado con éxito')
                        controlador = False
         
                else: #No hay ningún pedido registrado
                    print("Aún no tienes ningún pedido registrado")
                    

        else:
            ''
            El usuario no está registrado, por lo que le pedimos que cree una contraseña.
            Registramos al usuario y le damos la bienvenida.
            ''
            contrasenia = input("Crea una contraseña: ")
            web_pizza.registrar_usuario(nombre, contrasenia)
            usuario = web_pizza.login(nombre, contrasenia) #Abrir sesión
            print("Bienvenido!")


        while controlador:
            
            #Preparamos para el nuevo pedido
            director = Director() #Chef
            builder = ConcreteBuilder1() #Tipo de pizza
            director.builder = builder #Le decimos al chef que tipo de pizza queremos
            
            print("Pizza 1: ")
            director.build_pizza_prueba1() #Le decimos al chef los pasos a seguir para dicha pizza
            builder.pizza.list_parts() #Unimos todo
            a = builder.pizza.get_parts() #Lista con todos los datos de la pizza
            usuario.pedido_actual(a)
            builder.reset() #Reseteamos el builder para que no se acumulen los datos
            controlador = False

    print("\nHasta la próxima!")
    web_pizza.guardar_datos()


if __name__ == "__main__":
    main()
'''