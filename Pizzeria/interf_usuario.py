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
    def __init__(self, name, extras=None):
        self.name = name
        self.extras = extras if extras else []

    def add_extra(self, extra):
        self.extras.append(extra)

    def __str__(self):
        extras_str = ", ".join(self.extras)
        return f"{self.name} ({extras_str})" if self.extras else self.name


class Customer:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.orders = []

    def place_order(self, pizza, extras=None):
        if extras:
            pizza.add_extra(extras)
        self.orders.append(pizza)

    def last_order(self):
        if self.orders:
            return self.orders[-1]
        else:
            return None


class PizzaShop:
    def __init__(self):
        self.customers = {}
        self.load_data()

    def save_data(self):
        with open('pizza_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for customer in self.customers.values():
                for order in customer.orders:
                    writer.writerow([customer.name, customer.password, order.name, ', '.join(order.extras)])

    def load_data(self):
        try:
            with open('pizza_data.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    name, password, pizza_name, extras = row
                    if name not in self.customers:
                        self.customers[name] = Customer(name, password)
                    customer = self.customers[name]
                    pizza = Pizza(pizza_name, extras.split(', '))
                    customer.place_order(pizza)
        except FileNotFoundError:
            pass
    def register_customer(self, name, password):
        if name not in self.customers:
            self.customers[name] = Customer(name, password)

    def login(self, name, password):
        if name in self.customers and self.customers[name].password == password:
            return self.customers[name]
        else:
            return None

    def is_customer_registered(self, name):
        return name in self.customers


def main():
    pizza_shop = PizzaShop()

    while True:
        print("\nBienvenido a la pizzería!")
        name = input("Por favor introduzca su nombre de usuario (0 para salir): ")

        if name == "0":
            break

        if pizza_shop.is_customer_registered(name):
            password = input("Enter your password: ")
            customer = pizza_shop.login(name, password)
            if customer:
                last_order = customer.last_order()
                if last_order:
                    print(f"Your last order was: {last_order}")
                else:
                    print("You haven't placed any orders yet.")
        else:
            password = input("Create a password: ")
            pizza_shop.register_customer(name, password)
            customer = pizza_shop.login(name, password)
            print("Welcome, new customer!")

        while True:
            choice = input("\nWhat would you like to do (order/quit)? ")

            if choice == "quit":
                break

            if choice == "order":
                pizza_type = input("Choose a pizza (Margherita/Pepperoni): ")
                pizza = Pizza(pizza_type)

                extra_choice = input("Would you like any extras (e.g., mushrooms)? (yes/no): ")
                while extra_choice == "yes":
                    extra = input("Enter an extra: ")
                    pizza.add_extra(extra)
                    extra_choice = input("Would you like more extras (yes/no): ")

                customer.place_order(pizza)
                print(f"Order placed: {pizza}")

    print("Goodbye!")
    pizza_shop.save_data()


if __name__ == "__main__":
    main()
