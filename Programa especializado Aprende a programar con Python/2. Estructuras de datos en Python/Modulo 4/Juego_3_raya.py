# Matriz del tablero
tablero = [["COLUM: "," ","0"," ","1"," ","2"," "],
            ["FILA: 0","|","_","|","_","|","_","|"],
            ["FILA: 1","|","_","|","_","|","_","|"],
            ["FILA: 2","|","_","|","_","|","_","|"]]

# Inicio e introducción de los nombres en el juego
def menu():
    print(" ")
    print("             BIENVENIDO")
    print("        JUEGO DEL 3 EN RAYA")
    print(" ")
    nombre = True
    while nombre:
        jugador1 = input("Introduce el nombre de Jugador 1: ").capitalize()
        jugador2 = input("Introduce el nombre de Jugador 2: ").capitalize()
        if jugador1 == jugador2:
            print("\nNo pueden haber dos jugadores iguales. Vuelva a intrducir los nombres.\n")
        else:
            nombre = False 

    return jugador1, jugador2

# Pide la ficha al primer jugador
def pedir_ficha(jugador1):
    x = False
    while x is False:
        print("--------------------------------------")
        ficha = input("{}, selecciona que fichas quieres (X/O): ".format(jugador1))
        if ficha in ("X,x"):
            x = True
            ficha = "x"
        elif ficha in ("0,O,o"):
            x=True
            ficha = "o"
        else:
            print("Error.Selecciona una ficha correcta (X/O).")

    return ficha


# Imprime la matriz del tablero
def imprimir_tablero():
    print(" ")
    print("    TABLERO  ")
    for fila in tablero:
        for i in  range(len(fila)):
            if i == len(fila)-1:
                print(fila[i])
            else:
                print(fila[i],end='')

# Cuerpo del juego, donde esta todo el ciclo de turnos
def inicio_juego(jugador1, jugador2, ficha):
    print("--------------------------------------")
    print("        QUE EMPIECE LA PARTIDA")
    print("--------------------------------------")

    jugar= True
    contador_turno=1
    while jugar:
        
        jugador = turno_jugador(jugador1,jugador2,contador_turno)
        print("Turno {}.".format(contador_turno),"Es el turno de",jugador)
        imprimir_tablero()
        posicion_fila = input("\nSelecciona la fila: " )
        posicion_col = input("Selecciona la columna: ")

        if posicion_fila.isdigit() == True and posicion_col.isdigit() == True:
            posicion_col = int(posicion_col)
            posicion_fila = int(posicion_fila)
            if posicion_fila <= 2 and posicion_fila >=0 and posicion_col <= 2 and posicion_col>=0:
                ocupado = colocar_ficha(posicion_fila, posicion_col, ficha, jugador)
                if ocupado == True:
                    contador_turno = contador_turno -1
                print("--------------------------------------")
                print(" ")
                jugar = condicion_win(contador_turno)
                contador_turno = contador_turno+1
            else:
                print("--------------------------------------")
                print("POSICIONES ERRONEAS. PRUEBE DE NUEVO {}".format(jugador).upper())
                print("--------------------------------------")
        else:
            print("--------------------------------------")
            print("POSICIONES ERRONEAS. PRUEBE DE NUEVO {}".format(jugador).upper())
            print("--------------------------------------")




# Retorna un jugador segun si la tirada es par o impar
def turno_jugador(jugador1, jugador2,contador_turno):
    if contador_turno % 2 == 0:
        return jugador1
    else:
        return jugador2

# Coloca la ficha en la posicion seleccionada e imprime la ficha correcta
def colocar_ficha(posicion_fila, posicion_col, ficha, jugador):
    if posicion_fila <= 2 and posicion_fila >=0:
        posicion_fila = posicion_fila + 1

    if posicion_col == 0:
        posicion_col = 2
    elif posicion_col == 1:
        posicion_col = 4
    elif posicion_col == 2:
        posicion_col = 6

    if (tablero[posicion_fila][posicion_col] == "_"):
        if jugador == jugador1:
            tablero[posicion_fila][posicion_col] = ficha
        else:
            if ficha == "x":
                ficha = "o"
                tablero[posicion_fila][posicion_col] = ficha
            else:
                ficha = "x"
                tablero[posicion_fila][posicion_col] = ficha
        ocupado = False
    else:
        print("--------------------------------------")
        print("ESPACIO OCUPADO.")
        ocupado = True
    return ocupado
        

def condicion_win(contador_turno):
    jugar = True
    # Victoria horizontal
    if tablero[1][2] == tablero[1][4] == tablero[1][6] != "_" or tablero[2][2] == tablero[2][4] == tablero[2][6] != "_" or tablero[3][2] == tablero[3][4] == tablero[3][6] != "_":
        imprimir_tablero()
        print("\nFIN DE LA PARTIDA. VICTORIA PARA {}".format(turno_jugador(jugador1,jugador2,contador_turno).upper()))
        jugar = False

    # Victoria vertical
    if tablero[1][2] == tablero[2][2] == tablero[3][2] != "_"or tablero[1][4] == tablero[2][4] == tablero[3][4] != "_" or tablero[1][6] == tablero[2][6] == tablero[3][6] != "_":
        imprimir_tablero()
        print("\nFIN DE LA PARTIDA. VICTORIA PARA {}".format(turno_jugador(jugador1,jugador2,contador_turno).upper()))
        jugar = False


    # Victoria con diagonales
    if tablero[1][2] == tablero[2][4] == tablero[3][6] != "_" or tablero[1][6] == tablero[2][4] == tablero[3][2] != "_":
        imprimir_tablero()
        print("\nFIN DE LA PARTIDA. VICTORIA PARA {}".format(turno_jugador(jugador1,jugador2,contador_turno).upper()))
        jugar = False

    if contador_turno == 9:
        imprimir_tablero()
        print("\nFIN DE LA PARTIDA. EMPATE")
        jugar = False
    return jugar


# Llamamos las funciones principales
jugador1, jugador2= menu()
ficha = pedir_ficha(jugador1)
inicio_juego(jugador1, jugador2, ficha)




