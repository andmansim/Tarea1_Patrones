'''
El cliente tiene que registrarse, ya sea con su clave o su nombre. 
Si es la primera vez que entra, se le pregunta que tipo de pizza quiere y se le guarda en su historial.
Si ya ha entrado antes, se le pregunta si quiere la misma pizza que la última vez o quiere otra.
Si quiere la misma, se le pregunta si quiere algún extra o algo diferente.
Si quiere otra, se le pregunta que tipo de pizza quiere y se le guarda en su historial.

Tiene que haber medidas de seguridad para que no se pueda acceder a los datos de otros clientes.
'''
import csv

class Pizza:
    def __init__(self, nombre, extras=None):
        self.nombre = nombre
        self.extras = extras if extras else []

    def add_extra(self, extra):
        self.extras.append(extra)

    def __str__(self):
        extras_str = ", ".join(self.extras)
        return f"{self.nombre} ({extras_str})" if self.extras else self.nombre


class Usuario:
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


class TiendaPizza:
    def __init__(self):
        self.usuario = {}
        self.load_data()

    def guardar_datos(self):
        with open('pizza_data.csv', mode='w', newline='') as file:
            escribir = csv.writer(file)
            for usuario in self.usuarios.values():
                for orden in usuario.ordenes:
                    escribir.writerow([usuario.nombre, usuario.contrasenia, orden.nombre, ', '.join(orden.extras)])

    def cargando_datos(self):
        try:
            with open('pizza_data.csv', mode='r') as file:
                leer = csv.reader(file)
                for fila in leer:
                    nombre, contrasenia, pizza_nombre, extras = fila
                    if nombre not in self.usuarios:
                        self.usuarios[nombre] = Usuario(nombre, contrasenia)
                    usuario = self.usuarios[nombre]
                    pizza = Pizza(pizza_nombre, extras.split(', '))
                    usuario.place_order(pizza)
        except FileNotFoundError:
            pass
    def registrar_usuario(self, nombre, contrasenia):
        if nombre not in self.usuarios:
            self.usuarios[nombre] = Usuario(nombre, contrasenia)

    def login(self, nombre, contrasenia):
        if nombre in self.usuarios and self.usuarios[nombre].contrasenia == contrasenia:
            return self.usuarios[nombre]
        else:
            return None

    def usuario_registrado(self, nombre):
        return nombre in self.usuarios


def main():
    tienda_pizza = TiendaPizza()

    while True:
        print("\nBienvenido a la pizzería!")
        nombre = input("Por favor introduzca su nombre de usuario (0 para salir): ")

        if nombre == "0":
            break

        if tienda_pizza.usuario_registrado(nombre):
            contrasenia = input("Introduce contraseña: ")
            usuario = tienda_pizza.login(nombre, contrasenia)
            if usuario:
                ultimo_pedido = usuario.ultimo_pedido()
                if ultimo_pedido:
                    print(f"Tu último pedido fue: {ultimo_pedido}")
                else:
                    print("You haven't placed any ordenes yet.")
        else:
            contrasenia = input("Crea una contraseña: ")
            tienda_pizza.usuario_registrado(nombre, contrasenia)
            usuario = tienda_pizza.login(nombre, contrasenia)
            print("Bienvenido!")

        while True:
            elegir = input("\nQué le gustaría hacer: pedir o salir? ")

            if elegir == "salir":
                break

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
                print(f"Order placed: {pizza}")

    print("Goodbye!")
    tienda_pizza.guardar_datos()


if __name__ == "__main__":
    main()
