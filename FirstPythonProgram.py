# Programa de TA-TE-TI (juego para dos personas)

def DarOpcionesParaContestar(Pregunta):
    print(Pregunta)
    ContestaMal = True

    while ContestaMal:
        SiONo = input()
        if SiONo == "S" or SiONo == "s" or SiONo == "Si" or SiONo == "sI" or SiONo == "SI" or SiONo == "si":
            print("\n" + "Sapeeee" + "\n")
            ContestaMal = False
        elif SiONo == "N" or SiONo == "n" or SiONo == "no" or SiONo == "No" or SiONo == "NO" or SiONo == "nO":
            print("\n" + "ANDATE A CAGAR" + "\n")
            ContestaMal = False
            exit()
        else:
            print("\n" + "CONTESTA CON LAS OPCIONES QUE TE DI PELOTUDO" + "\n")


def imprimirTemplateTaTeTi(lugar1,lugar2,lugar3,lugar4,lugar5,lugar6,lugar7,lugar8,lugar9):
    print("\n")
    print("     **     **   ")
    print("  " + lugar1 + "  **  " + lugar2 + "  **  " + lugar3 + "  ")
    print("     **     **   ")
    print("********************")
    print("********************")
    print("     **     **   ")
    print("  " + lugar4 + "  **  " + lugar5 + "  **  " + lugar6 + "  ")
    print("     **     **   ")
    print("********************")
    print("********************")
    print("     **     **   ")
    print("  " + lugar7 + "  **  " + lugar8 + "  **  " + lugar9 + "  ")
    print("     **     **   ")
    print("\n")

def SetearPosicionElegida(posicionElegida,Usuario,pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9):
    if int(posicionElegida) == 1:
        pos1 = Usuario
    elif int(posicionElegida) == 2:
        pos2 = Usuario
    elif int(posicionElegida) == 3:
        pos3 = Usuario
    elif int(posicionElegida) == 4:
        pos4 = Usuario
    elif int(posicionElegida) == 5:
        pos5 = Usuario
    elif int(posicionElegida) == 6:
        pos6 = Usuario
    elif int(posicionElegida) == 7:
        pos7 = Usuario
    elif int(posicionElegida) == 8:
        pos8 = Usuario
    elif int(posicionElegida) == 9:
        pos9 = Usuario
    
    return pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

def ChequeaSiGanoAlguno(Usuario,pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9):
    if pos1 == Usuario and pos2 == Usuario and pos3 == Usuario:     #Horizontal fila 1
        return True
    elif pos4 == Usuario and pos5 == Usuario and pos6 == Usuario:   #Horizontal fila 2
        return True
    elif pos7 == Usuario and pos8 == Usuario and pos9 == Usuario:   #Horizontal fila 3
        return True
    elif pos1 == Usuario and pos4 == Usuario and pos7 == Usuario:   #Vertical columna 1
        return True
    elif pos2 == Usuario and pos5 == Usuario and pos8 == Usuario:   #Vertical columna 2
        return True
    elif pos3 == Usuario and pos6 == Usuario and pos9 == Usuario:   #Vertical columna 3
        return True
    elif pos1 == Usuario and pos5 == Usuario and pos9 == Usuario:   #Diagonal 1
        return True
    elif pos3 == Usuario and pos5 == Usuario and pos7 == Usuario:   #Diagonal 2
        return True
    else:
        return False




def JuegoTaTeTi(Usuario1,Usuario2):     #Usuario1 y Usuario2 son "X" o "O"
    imprimirTemplateTaTeTi("1","2","3","4","5","6","7","8","9")
    pos1 = " "
    pos2 = " "
    pos3 = " "
    pos4 = " "
    pos5 = " "
    pos6 = " "
    pos7 = " "
    pos8 = " "
    pos9 = " "

    GanoAlguno = False
    LeTocaA1 = True
    Cantidad = 0

    while (not GanoAlguno) and Cantidad < 9:
        Cantidad += 1
        posicionElegidaCorrecta = False
        while (not posicionElegidaCorrecta):
            print("Elegi un numero entre el 1 y el 9 para determinar la posicion" + "\n")
            posicionElegida = input()
            if int(posicionElegida) == 1 or int(posicionElegida) == 2 or int(posicionElegida) == 3 or int(posicionElegida) == 4 or int(posicionElegida) == 5 or int(posicionElegida) == 6 or int(posicionElegida) == 7 or int(posicionElegida) == 8 or int(posicionElegida) == 9:
                posicionElegidaCorrecta = True
                

        if LeTocaA1:    #Caso que le toca a Usuario1
            pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9 = SetearPosicionElegida(posicionElegida,Usuario1,pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9)
            GanoAlguno = ChequeaSiGanoAlguno(Usuario1,pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9)
            LeTocaA1 = False
        else:           #Caso que le toca a Usuario2
            pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9 = SetearPosicionElegida(posicionElegida,Usuario2,pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9)
            GanoAlguno = ChequeaSiGanoAlguno(Usuario2,pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9)
            LeTocaA1 = True
        imprimirTemplateTaTeTi(pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9)

    if Cantidad == 9:   #Caso de empate
        return False, True
    else:
        if LeTocaA1:    #Caso que gana el Usuario2
            return False, False
        else:           #Caso que gana el Usuario1
            return True, False

    




##########################################################################################################################################################################
##################################  MAIN    ########################################################################################################################################
##########################################################################################################################################################################


DarOpcionesParaContestar("\n" + "********************************************" + "\n" + "Quieren jugar al TA-TE-TI (S/N):" + "\n" + "********************************************" + "\n")


#Si sigue aca abajo es porque quiere seguir jugando


salir = False

while not salir:

    print("Queres ser cruz (X) o circulo (O): (X/O):")

    ContestaMal = True

    while ContestaMal:
        CruzOCirculo = input()
        if CruzOCirculo == "X":
            print("Sos 'X' compadre" + "\n")
            ContestaMal = False
            Usuario1 = "X"
            Usuario2 = "O"
        elif CruzOCirculo == "O":
            print("Sos 'O' compadre" + "\n")
            ContestaMal = False
            Usuario1 = "O"
            Usuario2 = "X"
        else:
            print("Elegi 'X' o 'O' salame" + "\n")


    GanaUsuario1, Empate = JuegoTaTeTi(Usuario1,Usuario2)

    if Empate:
        print("\n" + "EMPATARON PAR DE GILES" + "\n")
    else:
        if GanaUsuario1:
            print("\n" + "GANA EL QUE ELIGIO " + Usuario1)
        else:
            print("\n" + "GANA EL QUE ELIGIO " + Usuario2)
    

    DarOpcionesParaContestar("\n" + "Jugar de nuevo? (S/N):" + "\n")
    
    






       



    
