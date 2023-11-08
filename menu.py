import helpers
import SAMUR.main as samur
import Pizzeria.main as pizzeria
def iniciar():
     while True:
        helpers.limpiar_pantalla()
        
        print("========================")
        print(" BIENVENIDO AL Manager ")
        print("========================")
        print("[1] Ejercicio de SAMUR ")
        print("[2] Ejercicio de Pizzeria ")
        print("[3] Cerrar el Manager ")
        print("========================")
        
        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Ejercicio del SAMUR\n")
            samur.iniciar()
                
        if opcion == '2':
            print("Ejercicio de Pizzeria\n")
            pizzeria.iniciar()
        
        if opcion == '3':
            print("Saliendo...\n")
            break
       
        input("\nPresiona ENTER para continuar...")

