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

    def place_order(self, pizza, extras=None):
        if extras:
            pizza.add_extra(extras)
        self.ordenes.append(pizza)

    def last_order(self):
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
    pizza_shop = TiendaPizza()

    while True:
        print("\nBienvenido a la pizzería!")
        nombre = input("Por favor introduzca su nombre de usuario (0 para salir): ")

        if nombre == "0":
            break

        if pizza_shop.is_customer_registered(nombre):
            contrasenia = input("Enter your contrasenia: ")
            usuario = pizza_shop.login(nombre, contrasenia)
            if usuario:
                last_order = usuario.last_order()
                if last_order:
                    print(f"Your last order was: {last_order}")
                else:
                    print("You haven't placed any ordenes yet.")
        else:
            contrasenia = input("Create a contrasenia: ")
            pizza_shop.register_customer(nombre, contrasenia)
            customer = pizza_shop.login(nombre, contrasenia)
            print("Welcome, new customer!")

        while True:
            choice = input("\nWhat would you like to do (order/quit)? ")

            if choice == "0":
                break

            if choice == "order":
                pizza_type = input("Choose a pizza (Margherita/Pepperoni): ")
                pizza = Pizza(pizza_type)

                extra_choice = input("Would you like any extras (e.g., mushrooms)? (yes/no): ")
                while extra_choice == "yes":
                    extra = input("Enter an extra: ")
                    pizza.add_extra(extra)
                    extra_choice = input("Would you like more extras (yes/no): ")

                usuario.place_order(pizza)
                print(f"Order placed: {pizza}")

    print("Goodbye!")
    pizza_shop.save_data()


if __name__ == "__main__":
    main()
