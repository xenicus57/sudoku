

def presenta(avar):
    """
    Función que nos permite ver la situación del sudoku insertando la función < presenta() > en el modulo de resolución
    La función principal es para chequeo del código.

    Ejemplos de salidas:
    1º Sudoku 3 por 3 (recien cargado en el modulo de resolución)
    el signo: ! en la salida nos ayuda a no mezclar cuadros.

    !1| | ! | |7! |9| !
    ! |3| ! |2| ! | |8!
    ! | |9!6| | !5| | !
    ------------------
    ! | |5!3| | !9| | !
    ! |1| ! |8| ! | |2!
    !6| | ! | |4! | | !
    ------------------
    !3| | ! | | ! |1| !
    ! |4| ! | | ! | |7!
    ! | |7! | | !3| | !
    ------------------

    2º Sudoku 3 por 3
    PENDIENTE


    """
    nmax = 0
    nhor = 0
    # Calcular de la lista, la casilla con mas valores
    for i in avar:
        for j in i:
            if len(j) > nmax :
                nmax = len(j)
    #print(nmax)
    #input("parada")

    for i in avar:

        ctmp = "!"
        nhor += 1
        nver = 1
        for j in i:
            ctmp += (" " * nmax) if len(j) == 0 else (" " * (nmax-len(j)))
            ctmp += j
            ctmp += "!" if nver%nRSDK == 0 else "|"
            nver +=1

        print(ctmp)
        if nhor%nRSDK == 0:
            print("-"*(nSDK*(nmax+1)))


# *******************************************

nSDK=4
nRSDK=2
# avar = [["24"]*nSDK]*nSDK  OJO crea referencias no es correcto en la creacion de esta matriz bidimnesional
#forma correcta
avar = [["24"] * nSDK for i in range(nSDK)]

avar[3][2]="1234"

presenta(avar)

"""
**************
FUNCTION presenta(aVar)
**************
LOCAL cTmp,i,j,nmax:=0

 //calculo del maximo numero de valores en una casilla
 FOR i:=1 TO nSDK
     FOR j:=1 TO nSDK
         IF LEN(aVar[i,j]) > nmax
            nmax:=LEN(aVar[i,j])
         ENDIF
     NEXT
 NEXT

 FOR i:=1 TO nSDK
     cTmp:=''
     FOR j:=1 TO nSDK
         cTmp += IIF(LEN(aVar[i,j])=0,SPACE(nmax),SPACE(nmax-LEN(aVar[i,j]))+aVar[i,j]) +'|'
         //cTmp += IIF(LEN(aVar[i,j])=0,' ',aVar[i,j]) +'|'
         //cTmp := SPACE(nmax+1-LEN(cTmp))+cTmp
     NEXT
     ? cTmp
     IF i%nRSDK=0
        ? REPLICATE('-',(nSDK*nmax)+nSDK)
     ENDIF

 NEXT
 ? 'pulse una tecla para seguir'
 inkey(0)
 ? 'EN MARCHA...'

RETURN nil
"""
