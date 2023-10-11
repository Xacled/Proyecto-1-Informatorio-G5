import random
dibujosAhorcado = [
'''
     +---+
     |   |
         |
         |
         |
         |
    ------
''',
'''
     +---+
     |   |
     O   |
         |
         |
         |
    ------
''',
'''
     +---+
     |   |
     O   |
     |   |
         |
         |
    ------
''',
'''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    ------
''',
'''
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    ------
''',
'''
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    ------
''',
'''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    ------
'''
]

palabras = ['EJECUTIVA', 'IMPULSAR', 'MEDIANO', 'PLAZO', 'ALEJARSE', 'CONTEXTO', 'FURIOSO', 'PANTALLAS', 'HOMBRES', 'MUJERES', 'NEGOCIOS', 'TRANSITAN', 'PASILLOS', 'SHERATON.', 'CHARLAS', 'DECISIONES', 'EMPRESAS', 'PUEDEN', 'ESPERAR', 'CONTEXTO', 'ALGUNOS', 'FRENARON', 'COMENTAR', 'ESPERAN', 'TERMINADO', 'GOBIERNO', 'EMPIECE', 'MANDO']

intentosPermitidos = 6
intentosFallidos = 0
indicesAciertos = []
caracteresIngresados = []
palabraElegida = palabras[random.randint(0,len(palabras)-1)]
estado = list("-" * len(palabraElegida))  #lista que mantiene el estado del juego (lo adivinado), se inicializa a [----]

def formatearLista(lista):    
    # recibe una lista y devuelve una cadena con espacios entre caracteres, para mejor visualización

    return " ".join((i) for i in lista)

def comprobarStringIngresado(cadena):     
    # verifica que lo ingresado cumpla con las condiciones para afectar al estado del juego

    letras="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    #retorno tupla con código y mensaje de error
    if len(cadena) > 1: # se ingresó más de un caracter
       return((1,"Ingresó más de un caracter"))
    
    elif len(cadena) == 0: # no se ingresó un caracter
       return ((2, "No ingresó un caracter"))
    
    elif not cadena in letras: # verifica en la lista de caracteres
       return((3,"Ingresó un caracter no válido"))
    
    elif cadena in caracteresIngresados: # ingresó un caracter que ya había ingresado
       return((4, "Ya ingresó ese caracter"))
    
    else:
       return((0,"OK")) # código de error 0 corresponde a no hubo error
    
def mostrarEnPantalla(momentoDelJuego, indiceAhorcado ):
    # muestra en pantalla el estado del juego
    if momentoDelJuego == "Inicio":

      print("\nBIENVENIDO AL JUEGO DEL AHORCADO\n")
      print(f'Intenta adivinar la palabra secreta, tiene {len(palabraElegida)} caracteres')
      print("La palabra es: ",formatearLista(estado))
      print(f'Tienes {intentosPermitidos-intentosFallidos} intentos')
      print(dibujosAhorcado[0])

    elif momentoDelJuego == "Continuar":

      print(dibujosAhorcado[indiceAhorcado])
      print(formatearLista(estado))
      print(f'Te quedan {intentosPermitidos-intentosFallidos} intentos')
      print(f'Letras ingresadas: {formatearLista(caracteresIngresados)}')
      print("")

      
   
mostrarEnPantalla("Inicio",0)

while intentosFallidos < intentosPermitidos and palabraElegida != ''.join(estado):
    
    c = input("Ingrese un caracter: ").upper()
    
    if comprobarStringIngresado(c)[0] == 0: # verifica si lo ingresado pasa el control

      caracteresIngresados.append(c)

      # obtengo indices de la letra ingresada en la palabraElegida
      for i in range(len(palabraElegida)):
        if c.upper() == palabraElegida[i]:
          indicesAciertos.append(i)

      # reemplazo en estado las letras encontradas en este intento
      for indice in indicesAciertos:
        estado[indice] = c

      # si no aparece ninguna vez la letra ingresada, incremento el contador de intentos fallidos
      if len(indicesAciertos) == 0:
        intentosFallidos += 1
      
      indicesAciertos=[] # re inicializo lista de índices de la letra ingresada en la palabraElegida

      mostrarEnPantalla("Continuar",intentosFallidos)

    else: # si comprobarStringIngresado(c) ha retornado un código de error
       print(f'******* Error: {comprobarStringIngresado(c)[1]} ********') # muestro el error
       mostrarEnPantalla("Continuar",intentosFallidos)
    
    

if palabraElegida == ''.join(estado):
    print("FELICITACIONES, HAS GANADO")
else:
    print("HAS PERDIDO, SE TE TERMINARON LOS INTENTOS")
    print(f'La palabra secreta era: {palabraElegida}')
