import random
import os
def menu():#Es un menu del juego
    print("Este es el juego de el ahorcado")
    print("----MENU----")
    print("1.Jugador contra la maquina") #Se toma la palabra de un archivo aleatorio
    print("2.Salir")

def obtener_palabra():

    palabras = ["hola", "adios", "Complacer", "Coma", "Espumoso", "Mama", "Nuclear", "lugar",
                "Pesca", "Implicar", "Optimista", "Cero", "Pezuñas", "Desvanecimiento", "Cobre", "Explicación",
                "Retirar", "Zoom", "Innecesario", "Primer plano", "Desayuno", "Componer", "Problema", "Bovino",
                "Arcilla", "Cualquier momento", "Seda", "Raro", "Grin", "Minuto", "Equivocado", "Probado",
                "Diagonal", "Moneda", "Blanda", "Negro", "Estación", "Respaldar", "Lineal", "Examinador"]
    palabra = random.choice(palabras).lower()
    return palabra

def ahorcado():
    pass

def juego():
    print("Bienvenido al juego de adivinanza de palabras.")
    menu()
    op = int(input("Ingrese el modo de juego:\n-> "))

    if op == 1:
        palabra = obtener_palabra()
        vidas = 6
        adivinada = ''
        letras_equivocada = []
        letras_ingresadas = []

        while vidas > 0:
            fallas = 0

            for letra in palabra:
                if letra in adivinada:
                    print(letra, end="")
                else:
                    print("_", end="")
                    fallas +=1

            if fallas == 0:
                print("\n¡Ganaste! lograste adivinar la palabra")               
                print(f"Letras incorrectas: {', '.join(letras_equivocada)}")
                break 

            intento = input("\nIntroduce una letra o adivina la palabra completa (ingresa 'adivinar'): ").lower()

            if intento == 'adivinar':
                palabra_intentada = input("Ingresa la palabra completa: ").lower()
                
                if palabra_intentada == palabra:
                    print("¡Ganaste adivinando la palabra completa!")
                    break    
                else:
                    print("Palabra incorrecta. Pierdes todas las vidas.")
                    vidas = 0
                    
            
            letra_ingresada = intento

            if letra_ingresada in letras_ingresadas:
                print("Ya has ingresado esa letra. Intenta con una diferente.")
                continue  # Vuelve al inicio del bucle sin restar vidas
            
            letras_ingresadas.append(letra_ingresada) 
            adivinada += letra_ingresada
            
            if vidas == 0:
                print(f"Perdiste. La palabra era: {palabra}")
                print(f"Letras incorrectas: {', '.join(letras_equivocada)}")

                
            if letra_ingresada not in palabra: 
                    vidas -= 1
                    letras_equivocada.append(letra_ingresada)   
                    print(f"Letra incorrecta. Te quedan {vidas} vidas restantes.") 


juego()

def vida ():
 pass
