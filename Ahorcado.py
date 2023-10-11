import random
import os
def menu():#Es un menu del juego
    print("------------------------MENU---------------------------")
    print("1.Jugador contra la maquina") #Se toma la palabra de un archivo aleatorio
    print("2.Salir")

def obtener_palabra():

    palabras = ["hola", "adios", "Complacer", "Coma", "Espumoso", "Mama", "Nuclear", "lugar",
                "Pesca", "Implicar", "Optimista", "Cero", "Pezuñas", "Desvanecimiento", "Cobre", "Explicación",
                "Retirar", "Zoom", "Innecesario", "Plano", "Desayuno", "Componer", "Problema", "Bovino",
                "Arcilla", "Cualquier momento", "Seda", "Raro", "Primero", "Minuto", "Equivocado", "Probado",
                "Diagonal", "Moneda", "Blanda", "Negro", "Estación", "Respaldar", "Lineal", "Examinador"]
    palabra = random.choice(palabras).lower()
    return palabra

def vida(pal): #Esta funcion devuelve la vida segun la mitad de la longitud de la palabra obtenida
    long=len(pal)
    vida= (long / 2)
    return vida 

def ahorcado(cantVida):
    #Funcion para definir el ascii del ahorcado
    pass


def juego():
    os.system('cls')
    jugar = True
    while jugar == True:
        print("------------Este es el juego de el ahorcado------------")
        menu()
        op = int(input("\nIngrese la opcion a elegir:\n-> "))

        if op == 1:
            palabra = obtener_palabra()
            vidas = int(vida(palabra))
            adivinada = ''
            letras_equivocada = []
            letras_ingresadas = []

            while vidas > 0:
                os.system('cls')
                fallas = 0
                print(f"Tienes {vidas} vidas")
                for letra in palabra:
                    if letra in adivinada:
                        print(letra, end="")
                    else:
                        print("_", end="")
                        fallas +=1

                if fallas == 0:
                    print("\n¡Ganaste! lograste adivinar la palabra")               
                    print(f"\nLetras incorrectas: {', '.join(letras_equivocada)}")
                    break 

                intento = input("\nIntroduce una letra o adivina la palabra completa (ingresa 'adivinar'): ").lower()

                if intento == 'adivinar':
                    palabra_intentada = input("\nIngresa la palabra completa: ").lower()
                    
                    if palabra_intentada == palabra:
                        print("\n¡Ganaste adivinando la palabra completa!")
                        break    
                    else:
                        print("\nPalabra incorrecta. Pierdes todas las vidas.")
                        vidas = 0
                        
                
                letra_ingresada = intento  #Le asigno el intento que seria la letra ingresada
                
                if letra_ingresada in letras_ingresadas:  #Si la letra que ingreso es la misma que la ingresada anteriormente entonces le pide que ingrese otra
                    print("\nYa has ingresado esa letra, intenta con una diferente.")
                    continue  # Vuelve al inicio del bucle sin restar vidas

                letras_ingresadas.append(letra_ingresada) 
                adivinada += letra_ingresada
            
                    
                if letra_ingresada not in palabra: 
                        vidas -= 1 #Resto uno a la vida si la letra que ingreso no esta en la palabra tomada de la lista
                        letras_equivocada.append(letra_ingresada)   
                        print(f"Letra equivocada . Te quedan {vidas} vidas restantes.") 

                #Si la vida del jugador es  0 entonces este perdio el juego, es decir no adivno la palabra
                if vidas == 0:
                    print(f"\nPerdiste!, La palabra era: {palabra}")
                    print(f"\nLetras equivocadas: {', '.join(letras_equivocada)}")

            juego = input("\nDeseas jugar otra vez y/n: ").lower()
            if juego == 'n':
                jugar = False
                print("Gracias por jugar")
            else:
                continue
        else:
            exit()

juego()


