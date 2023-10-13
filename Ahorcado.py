import random  # Libreria de python que en este caso me permitira escoger una palabra random de mi lista de palabras
import os  # Libreria de python que me permitira limpiar la consola


def menu():  # Es un menu del juego donde elegiras entre jugar o salir del programa en cuestion
    print("------------------------MENU---------------------------")
    # Para jugar solo tendras que elegir entre este menu de opcion 1 o 2, 1 para jugar
    # Se toma la palabra de un archivo aleatorio
    print("1.Jugador contra la maquina")
    print("2.Instrucciones")
    print("3.Salir")


def dificultad():
    print("Seleccione una dificultad:")
    print("========================")
    print("1.Facil")
    print("2.Medio")
    print("3.Dificil")


def obtener_palabra(dificultad):

    palabras = ["hola", "adios", "Complacer", "Coma", "Espumoso", "Mama", "Nuclear", "lugar",
                "Pesca", "Implicar", "Optimista", "Cero", "Pezuñas", "Desvanecimiento", "Cobre", "Explicación",
                "Retirar", "Zoom", "Innecesario", "Plano", "Desayuno", "Componer", "Problema", "Bovino",
                "Arcilla", "Cualquier", "momento", "Seda", "Raro", "Primero", "Minuto", "Equivocado", "Probado",
                "Diagonal", "Moneda", "Blanda", "Negro", "Estación", "Respaldar", "Lineal", "Examinador"]
    # Utilizo el random para que sea aleatorio y choice para elegir la palabra, lower para que sea minuscula
    # separo la lista de palabras por nivel
    facil = []
    medio = []
    dificil = []
    for palabra in palabras:
        letras_difrentes = len(set(palabra))
        if letras_difrentes <= 4:
            facil.append(palabra)
        elif letras_difrentes <= 8:
            medio.append(palabra)
        else:
            dificil.append(palabra)
    if dificultad == 1:
        palabra = random.choice(facil).lower()
    elif dificultad == 2:
        palabra = random.choice(medio).lower()
    else:
        palabra = random.choice(dificil).lower()
    return palabra


def ahorcado(cantVida):
    # Funcion para definir el ascii del ahorcado
    dibujo = [
        '''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
              |
              |
              |
        ========''',
        '''
          +---+
          |   |
              |
              |
              |
              |
        ========'''
    ]

    print(dibujo[cantVida])


def juego():
    # Limpio la consola al iniciar el juego
    jugar = True
    while jugar == True:  # Primer control del flujo del programa mientras jugar sea true  podra seguir adivinando palabras
        # corri esto aca abajo para que despues de volver a jugar limpie bien
        os.system('cls')
        print("-------------Este es el juego del ahorcado-------------")
        menu()
        op = int(input("\nIngrese la opcion a elegir:\n-> "))
        op_deseada = [1, 2, 3]  # chequeo que elija una de las 3 opciones
        while op not in op_deseada:
            print("opcion no valida vuelva a intentarlo")
            op = int(input("\nIngrese la opcion a elegir otra vez:\n-> "))

        # apartir de aqui comienza el juego, tendras que adivinar una palabra aleatoria, ingresando letra por letra o en su defecto
        # arriesgar la palabra si estas muy seguro de saber que palabra es ,
        # con cada intento si es incorrecta la letra te resta una vida, si es la palabra completa perdes toda tus vidas.
        os.system('cls')
        if op == 1:
            dificultad()
            op_dif = int(input("\nIngrese una opcion: "))
            op_dif_deseada = [1, 2, 3]
            while op_dif not in op_dif_deseada:
                print("opcion no valida vuelva a intentarlo")
                op_dif = int(input("\nIngrese una opcion valida: "))

            palabra = obtener_palabra(op_dif)
            vidas = 6
            adivinada = ''  # Letras por adivinar
            # Lista donde se guardaran las letras ingresadas y que son incorrectas
            letras_equivocada = []
            letras_repetidas = []  # Lista donde se guardaran las letras ingresadas repetidas

            def letras_equivocadas():  # Funcion para mostrar letras equivocadas/incorrectas
                if letras_equivocada == []:
                    print("\nNo te equivocaste en ninguna letra :D")
                else:
                    print(
                        f"\nLetras equivocadas: {', '.join(letras_equivocada)}")
            mensaje = ''  # inicalizo este mensaje en vacio y lo asigno despues pq sino la limpieza de consola no lo muestra
            while vidas > 0:  # Segundo while controla el flujo del programa mientras las vidas > 0 seguira jugando
                os.system("clear" if os.name == "posix" else "cls")

                print(f"\nTienes {vidas} vidas")
                ahorcado(vidas)
                letras_adivinidas = 0
                for letra in palabra:
                    if letra in adivinada:
                        print(letra, end="")
                    else:
                        print("_ ", end="")
                        letras_adivinidas += 1

                print(f"\nQuedan {letras_adivinidas} letras")

                if letras_adivinidas == 0:
                    print("\n┌(ㆆ㉨ㆆ)ʃ¡Ganaste! lograste adivinar la palabra┌(ㆆ㉨ㆆ)ʃ")
                    letras_equivocadas()
                    break

                if letras_adivinidas <= 2 and vidas > 0:
                    opc = input(
                        "\nQuiere arriesgar la palabra completa? y/n: ").lower()
                    if opc == "y":
                        palabra_intentada = input(
                            "\nIngresa la palabra completa: ").lower()
                        if palabra_intentada == palabra:
                            print("\n┌(ㆆ㉨ㆆ)ʃ¡Ganaste!┌(ㆆ㉨ㆆ)ʃ")

                            break
                        else:
                            print(
                                "\nPalabra incorrecta. Pierdes todas las vidas (╯°□°）╯︵ ┻━┻")
                            print(f"\nLa palabra era: {palabra}")
                            if len(letras_equivocada) > 0:
                                letras_equivocadas()  # pongo esto adentro del if pq si arriesgas hasta el momento sin equivocacciones al perder muestra como que no te equivocaste
                            vidas = 0
                            break
                if vidas < 6:
                    letras_equivocadas()
                print(mensaje)
                letrain = input("\nIntroduce una letra: ").lower()

                # .isalpha debuelve true si los caracteres ingresado son letras
                if len(letrain) != 1 or not letrain.isalpha():
                    mensaje = '\nEl caracter ingresado no es una letra o es mas de una letra,Ingrese nuevamente una letra'
                    continue

                letra_ingresada = letrain  # Le asigno el intento que seria la letra ingresada

                # Si la letra que ingreso es la misma que la ingresada anteriormente entonces le pide que ingrese otra
                if letra_ingresada in letras_repetidas:
                    print(
                        "\n ''⌐(ಠ۾ಠ)¬''' Ya has ingresado esa letra, intenta con una diferente.")
                    continue  # Vuelve al inicio del bucle sin restar vidas

                # Añado a la lista de letras repetidas
                letras_repetidas.append(letra_ingresada)
                adivinada += letra_ingresada

                if letra_ingresada not in palabra:
                    vidas -= 1  # Resto uno a la vida si la letra que ingreso no esta en la palabra tomada de la lista
                    letras_equivocada.append(letra_ingresada)
                    print(
                        f"Letra equivocada . Te quedan {vidas} vidas restantes.")
                    letras_equivocadas()
                # Si la vida del jugador es  0 entonces este perdio el juego, es decir no adivno la palabra
                if vidas == 0:
                    os.system('cls')
                    ahorcado(vidas)
                    print(
                        f"\nPerdiste!, La palabra era: {palabra} (╯°□°）╯︵ ┻━┻")
                    if len(letras_equivocada) > 0:
                        letras_equivocadas()
                    # elimino esto para mostrarlo siempre letras_equivocadas()
                # Limpio la consola mientras mis vidas sean > 0

            juego = input("\nDeseas jugar otra vez y/n: ").lower()
            if juego == 'n':
                jugar = False
                # Limpio la consola mientras mis vidas sean > 0
                os.system('cls')
                print("---Gracias por jugar!---")
            else:
                continue
        elif op == 2:
            print("las instrucciones de este juego")
            input("presione enter para volver al menu inicial.....")
            os.system('cls')
        else:
            exit()


juego()


# hola
# este es el segundo commit
