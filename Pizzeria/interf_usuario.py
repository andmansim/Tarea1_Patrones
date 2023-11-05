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

'''class Pizza:
    def __init__(self, nombre, extras=None):
        self.nombre = nombre
        self.extras = extras if extras else []

    def add_extra(self, extra):
        self.extras.append(extra)

    def __str__(self):
        extras_str = ", ".join(self.extras)
        return f"{self.nombre} ({extras_str})" if self.extras else self.nombre'''


class Usuario:
    '''
    Esta clase se encarga de recoger el pedido actual y mirar si ha habido algún pedido anterior 
    con dicho usuario.
    '''
    def __init__(self, nombre, contrasenia):
        self.nombre = nombre
        self.contrasenia = contrasenia
        self.ordenes = []

    def pedido_actual(self, pizza, extras=None):
        if extras:
            pizza.add_extra(extras)
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
            for usuario in self.usuario.values():
                for orden in usuario.ordenes:
                    escribir.writerow([usuario.nombre, usuario.contrasenia, ', '.join(orden.extras)])

    def cargando_datos(self):
        try:
            with open('pizza_data.csv', mode='r') as file:
                leer = csv.reader(file)
                for fila in leer:
                    nombre, contrasenia, pedido = fila
                    if nombre not in self.usuario:
                        self.usuario[nombre] = Usuario(nombre, contrasenia)
                    usuario = self.usuario[nombre]
                    pizza = pedido.split(', ')
                    usuario.pedido_actual(pizza)
        except FileNotFoundError:
            pass
    def registrar_usuario(self, nombre, contrasenia):
        if nombre not in self.usuario:
            self.usuario[nombre] = Usuario(nombre, contrasenia)

    def login(self, nombre, contrasenia):
        if nombre in self.usuario and self.usuario[nombre].contrasenia == contrasenia:
            return self.usuario[nombre]
        else:
            return None

    def usuario_registrado(self, nombre):
        return nombre in self.usuario


def main():
    web_pizza = WebPizzeria()
    controlador = True
    while controlador:
        print("\nBienvenido a la pizzería!")
        nombre = input("Por favor introduzca su nombre de usuario (0 para salir): ")

        if nombre == "0":
            controlador = False

        if web_pizza.usuario_registrado(nombre):
            '''
            Si el usuario ya está registrado, le pedimos la contraseña para que inicie sesión. 
            Si la contraseña es correcta, le damos la bienvenida y le mostramos su último pedido.
            '''
            contrasenia = input("Introduce contraseña: ")
            usuario = web_pizza.login(nombre, contrasenia)
            if usuario:
                ultimo_pedido = usuario.ultimo_pedido()
                if ultimo_pedido:
                    print(f"Tu último pedido fue: {ultimo_pedido}")
                    pedir = input("Quieres pedir lo mismo? (Si/No) ")
                    if pedir == "Si":
                        usuario.pedido_actual(ultimo_pedido)
                        print('El pedido se ha realizado con éxito')
                        controlador = False
                    else: #No
                        director = Director() #Chef
                        builder = ConcreteBuilder1() #Tipo de pizza
                        director.builder = builder #Le decimos al chef que tipo de pizza queremos
                        
                        print("Pizza 1: ")
                        director.build_pizza_prueba1() #Le decimos al chef los pasos a seguir para dicha pizza
                        a = builder.pizza.get_parts()
                        builder.reset()
                        usuario.pedido_actual(a)
                        controlador = False
         
                else:
                    print("Aún no tienes ningún pedido registrado")
                    director = Director() #Chef
                    builder = ConcreteBuilder1() #Tipo de pizza
                    director.builder = builder #Le decimos al chef que tipo de pizza queremos
                    
                    print("Pizza 1: ")
                    director.build_pizza_prueba1() #Le decimos al chef los pasos a seguir para dicha pizza
                    builder.pizza.list_parts() #Unimos todo
                    controlador = False
        else:
            '''
            El usuario no está registrado, por lo que le pedimos que cree una contraseña.
            Registramos al usuario y le damos la bienvenida.
            '''
            contrasenia = input("Crea una contraseña: ")
            web_pizza.registrar_usuario(nombre, contrasenia)
            usuario = web_pizza.login(nombre, contrasenia)
            print("Bienvenido!")

        '''while controlador:
            elegir = input("\nQué quiere pedir? (0 para salir) ")

            if elegir == "0":
                controlador = False

            if elegir == "pedir":
                #Cambiar el código de aquí para que llame al otro lado
                    
                tipo_pizza = input("Choose a pizza (Margherita/Pepperoni): ")
                pizza = Pizza(tipo_pizza)

                extra_choice = input("Would you like any extras (e.g., mushrooms)? (yes/no): ")
                while extra_choice == "yes":
                    extra = input("Enter an extra: ")
                    pizza.add_extra(extra)
                    extra_choice = input("Would you like more extras (yes/no): ")

                usuario.pedido_actual(pizza)
                print(f"Order placed: {pizza}")'''

    print("\nHasta la próxima!")
    web_pizza.guardar_datos()


if __name__ == "__main__":
    main()
