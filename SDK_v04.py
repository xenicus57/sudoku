"""
SDK_v04.py
Version 04
En esta version se pondran en marcha una nueva estrategia antes de pasar a fuerza bruta.
Estrategia PAR DESNUDO o DOBLE PAREJA

******************
*** FINALIZADO ***
******************
"""
import sys
import copy
from datetime import datetime

#*************************
def alert(pipo=""):
#*************************
    """
    Funcion parada, información y continuacion. Funcion de control del desarrollador para provocar paradas y recabar información
    
    - Argumentos 
    pipo (opcional) -> char 

    """
    input(pipo+" Pulse Enter para continuar")
    return None

#*************************
def presenta(aVar):
#************************
    """
        Función que nos permite ver la situación del sudoku insertando la función < presenta() > en cualquier lugar del modulo de resolución,
        por tanto su función principal es de apoyo al desarrollador en el chequeo del código que vamos construyendo.

        Argumentos:
            aVar -> Lista multidimensional

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

        2º Sudoku 3 por 3 en proceso de resolucion, el que haya mas de un numero por casillas indica que son candidatos a ser la solucion de la casilla.

        !    67| 45678|  4678!  3689|     2|  3489! 35689|     1|345678!
        !     9|  4568| 12468!  1368|  1348|     7! 23568| 23568| 34568!
        !     3|  4678|124678!     5|   148|   489!  2689|  2678|  4678!
        ---------------------------------------------------------------
        !   167|     3| 14678!     2|    48|    48!   568|  5678|     9!
        !     5|    89|    89!     7|     6|     1!     4|     3|     2!
        !  1267|  4678|124678!    38|     9|     5!   368|  3678| 13678!
        ---------------------------------------------------------------
        !     4|     2|     5!   138|   138|     6!     7|     9|    38!
        !    67|   679|  3679!   389|   378|  2389!     1|     4|  3568!
        !     8|     1|  3679!     4|     5|   239!   236|   236|    36!
        ---------------------------------------------------------------

    """
    nmax = 0
    nhor = 0
    # Calcular de la lista, la casilla con mas candidatos
    for i in aVar:
        for j in i:
            if len(j) > nmax :
                nmax = len(j)

    for i in aVar:

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
    alert()


#************************
def ini_congruen(cSum):
#************************
    """
    Funcion que verifica la congruencia del sudoku cargado.
    Congruencia indica: que para cualquier fila,columna o cuadro, no hay ningun elemento repetido.

    Argumentos:
        cSum -> cadena de caracteres de cualquier fila, columna o cuadro.

    Devuelve:
    True -> Si a encontrado un elemento repetido
    False -> en caso contrario
    """

    for i in cSDK:
        if cSum.count(i) > 1:
            return True

    return False

#************************
def ini_comp(aVar,aFil,aCol,aInt):
#************************
    """
    El objetivo de esta funcion es crear para cada fila, columna y cuadro una cadena con los elementos ya resueltos (como maximo los nSDK valores posibles)

    Argumentos:
    Se pasan las cuatro listas (aVar,aFil,aCol,aInt) por referencia de las cuales las tres ultimas en base a aVAR se modificaran.
    
    Devuelve:
    None
     """

    # Inicializamos aFil,aCol,aInt a ""
    for i in range(0,nSDK):
        aFil[i] = ""
        aCol[i] = ""
        aInt[i] = ""

    # cargamos las filas
    for i in range(0,nSDK):
       for j in range(0,nSDK):
           if len(aVar[i][j]) == 1 :
               aFil[i] += aVar[i][j]

    # cargamos las columnas
    for i in range(0,nSDK):
       for j in range(0,nSDK):
           if len(aVar[j][i]) == 1 :
                aCol[i] += aVar[j][i]

    # cargamos los cuadros
    for i in range(0,nSDK):

        nFil = (int(i/nRSDK)*nRSDK) - 1
        for j in range(0,nRSDK):
            nFil += 1
            nCol = ((i%nRSDK)*nRSDK) -1

            for k in range(0,nRSDK):
                nCol +=1
                if len (aVar[nFil][nCol]) == 1 :
                    aInt[i] += aVar[nFil][nCol]

    return None

#************************
def ele_Int(i,j):
#************************
    """
    Esta funcion nos calculara, conociendo posicion de fila y columna que cuadro tiene asociado
    ej: para [5,3] -> cuadro 4

    Argumentos:
    i -> integer posicion de fila
    j -> integer posicion de columna

    Devuelve:
    Un integer que nos informa sobre la posicion del cuadro
    """
    nf = int((i)/nRSDK)
    nc = int((j)/nRSDK)
    return (nRSDK*nf)+nc

#************************
def est_Smp(cFil,cCol,cInt):
#************************
    """
    Recibido 3 cadenas y sumadas se trata de averiguar que elementos faltan en nuestra cadena Maestra (cSDK)

    Argumentos:
    cFil -> cadena de caractres de la Fila
    cCol -> cadena de caractres de la Columa
    cInt -> cadena de caractres del Cuadro

    Devuelve:
    Una cadena con los elementos que faltan en la Maestra

    Ej:
    Cadena Maestra : "123456789"
    cFil -> "946"
    cCol -> "7"
    cInt -> "2"
    La funcion devolverá -> "1358"
    """

    cSum = cFil+ cCol + cInt
    cSal = ""

    for i in cSDK:
        if  not(i in cSum):
            cSal += i

    return cSal

#************************
def ele_comp(cele,i,j,nInt,aFil,aCol,aInt):
#************************
    """
    Encontrado un elemento de una casilla nos permite reajustar las listas: fila, columna y cuadro con dicho elemento añadiendolo

    Argumentos:
    cele -> elemento encontrado
    i -> Numero de fila
    j -> Numero de columna
    nInt -> numero de cuadro
    aFil -> lista de cadena de caractres de la Fila
    aCol -> lista de cadena de caractres de la Columa
    aInt -> lista de cadena de caractres del Cuadro

    Devuelve nada. Las listas pasadas por referencia son alimentadas con el nuevo valor encontrado
    """
    aFil[i] += cele
    aCol[j] += cele
    aInt[nInt] += cele

    return None

#************************
def Bucle1(aVar,aFil,aCol,aInt,nvuelta):
#************************
    """
    Funcion Estrategia Simple (UNICO DESNUDO)
    Esta funcion tratara de buscar elementos que faltan en el sudoku con el algoritmo Estrategia Simple. 
    Sobre una casilla ver, de la suma de los elementos hallados de fila, columna y cuadro, cuantos faltan de la cadena base (cSDK)
    Si solo nos falta uno es el definitivo para dicha casilla.

    Argumentos:
    Se pasan las cuatro listas (aVar,aFil,aCol,aInt) por referencia.
    nvuelta -> integer

    Devuelve:
    Siempre  True, a no ser que interrumpa el programa al encontrar que es irresoluble o una incogruencia (de su paso por Fuerza Bruta) 
    """
    nInt = 0
    lsigue =True

    while lsigue:
        lsigue = False

        for i in range(0,nSDK):
            for j in range(0,nSDK):
                """
                En primera vuelta habrá casillas (las que hay que resolver) de aVar que estaran vacias y en las siguientes vueltas
                con un solo caracter (SOLUCION DE CASILLA) o mas caracteres (CANDIDATOS/PENDIENTE), estos caracteres de mas nos indican
                que son candidatos para ser la solucion de dicha casilla
                Cada vez que consiga solucionar una casilla. Se reinicia el bucle FOR
                """

                # en primera vuelta entraran los que esten vacios y en siguientes los que tengan mas de un candidato
                if len(aVar[i][j]) != 1:

                    #print(aVar[i][j])
                    #alert()

                    # Para este elemento de la matriz, necesitamos conocer a que fila, columna y cuadrado pertenece
                    # fila -> i, columna -> j, ¿ cuadro ?
                    # calcular a que cuadro pertenece
                    nInt = ele_Int(i,j)
                    # estrategia 1º
                    aVar[i][j] = est_Smp(aFil[i],aCol[j],aInt[nInt])

                    """"
                    Si en primera vuelta nvuelta = 0 y ademas nos encontramos que no se ha asignado nada a alguna casilla de la matriz
                    El sudoku es irresoluble. 

                    EJEMPLO: Irresoluble
                    Estudio de cuadros [1,2] y [9,2] en ambos falta un 7 lo que daria  lugar a la columna 2 con 2 sietes.
                    1| |4| | | | | | |
                    2|3|5| | | | | | |
                    8|6|9| | | | | | |
                    ------------------
                    6| | | | | | | | |
                    7| | | | | | | | |
                    3| | | | | | | | |
                    ------------------
                    4|8|2| | | | | | |
                    5|1|3| | | | | | |
                    9| |6| | | | | | |
                    ------------------

                    """
                    if nvuelta == 0 and len(aVar[i][j]) == 0:
                        print(aFil[i])
                        print(aCol[j])
                        print(aInt[nInt])
                        alert('SUDOKU Irresoluble: '+'Casilla:'+str(i)+','+str(j))
                        presenta(aVar)
                        sys.exit(0)

                    if len(aVar[i][j]) == 0:
                        # Hallamos una INCONGRUENCIA 
                        # La incongruencia hallada nos llevará a Fuerza Bruta probando con el siguiente candidato o si fuera el ultimo
                        # a quitar el ultimo elemento de aBruta (deshacemos la pila) y probar con los anteriores
                        #presenta(aVar)
                        return False

                    # Hemos encontrado solo 1 es por tanto la solucion de esa casilla
                    if len(aVar[i][j]) == 1:
                        
                        # si queremos ver por pantalla como se generan las soluciones, modificar el fichero de configuración <sdk.ini>
                        if apar["SOLEST1"]:
                            quien("1º Estrategia: ", i, j, aVar[i][j])
                       
                        
                        # Hallada solución de casilla repercutir en las listas que mantienen los
                        # encontrados por fila, columna, cuadrado, añadiendo el hallado
                        ele_comp(aVar[i][j],i,j,nInt,aFil,aCol,aInt)

                        # volvemos a iniciar el ciclo

                        lsigue = True
        #check
        #print(lsigue)
        #presenta(aVar)


    return True

#************************
def est_Cmp(aVar,aTmp,aFil,aCol,aInt):
#************************
    """
    (UNICO OCULTO)
    Que valor es unico en '123456789' de la suma de los no hallados
    Ejemplo: Estado dada la fila 1->   1267|127  |3   |1245  |8   |245   |9   |1245|257
    las casillas [1,3]:='3' [1,5]:='8' [1,7]:='9' no estaria en aTmp al tener un solo valor
    el resto si con indicacion de fila y columna
    de un vistazo vemos que el 6 de la casilla [1,1]:='1267' no se repite en ninguna mas
    lo que nos indica que hemos hallado el valor de esa casilla aVar[1,1]:='6'

    Argumentos:
    aVar -> matriz de nSDK x nSDK
    aTmp -> Lista que recoge por elemento otra lista de la forma [posicion fila, posicion columna, cadena de caracteres]
    aFil -> lista de cadena de caractres de la Fila
    aCol -> lista de cadena de caractres de la Columa
    aInt -> lista de cadena de caractres del Cuadro

    Devuelve:
    False -> si no encontramos ninguno
    True  -> si encontramos uno 
    """

    cSum = ""
    
    # Check
    """
    for kk in aTmp:
        if len(aTmp[2]) == 1:
            print("aTmp:",aTmp)
            alert()
    """
    
    
    for i in aTmp:
        cSum += i[2]

    for i in cSDK:

        if cSum.count(i) == 1: # he encontrado uno, es el valido

            # a que elemento de la lista corresponde
            for j in aTmp:
                if i in j[2]:
                    
                    # si queremos ver por pantalla como se generan las soluciones, modificar el fichero de configuración <sdk.ini>
                    if apar["SOLEST2"]:
                        quien("2º Estrategia: ", j[0], j[1], i)
                    
                    
                    aVar[j[0]][j[1]] = i
                    return True
 
    return False

#************************
def Bucle2(aVar,aFil,aCol,aInt):
#************************
    """
    Esta funcion tratara de buscar los elementos que faltan en el sudoku de la siguiente manera:
    Se basa en un estudio de filas, columnas o cuadros, establecer, por ejemplo para una columna cuantas  casillas estan sin resolver y
    cuales son sus posibles valores, si de la suma de todos ellos hay alguno que sólo se repita una vez ese valor es el único posible.
    Ejemplo:
    casilla[1,4]:='3456' valores posibles
    casilla[6,4]:='36'   valores posibles
    casilla[9,4]:='34'   valores posibles
    El valor de la casilla[1,4] es el 5.

    Argumentos:
    Se pasan las cuatro listas (aVar,aFil,aCol,aInt) por referencia.

    Devuelve:
    False -> si no encontramos ninguno
    True  -> si encontramos uno 
    """

    #Estudio de FILAS
    for i in range(0,nSDK):
        aTmp = []
        for j in range(0,nSDK):
            if len(aVar[i][j]) > 1 :
                aTmp.append([i,j,aVar[i][j]] )
                #print(aTmp)
                #alert()

        #print(aTmp)
        #alert()
        if len(aTmp) > 1 and est_Cmp(aVar,aTmp,aFil,aCol,aInt):
            return True

    #Estudio de COLUMNAS
    for i in range(0,nSDK):
        aTmp = []
        for j in range(0,nSDK):
            if len(aVar[j][i]) > 1 :
                aTmp.append([j,i,aVar[j][i]])

        if len(aTmp) > 1 and est_Cmp(aVar,aTmp,aFil,aCol,aInt):
            return True

    # Estudio de cuadros
    for i in range(0,nSDK):

        nFil = (int(i/nRSDK)*nRSDK) - 1
        aTmp = []
        for j in range(0,nRSDK):
            nFil += 1
            nCol = ((i%nRSDK)*nRSDK) -1

            for k in range(0,nRSDK):
                nCol +=1
                if len(aVar[nFil][nCol]) > 1:
                    aTmp.append([nFil,nCol,aVar[nFil][nCol]])

        if len(aTmp) > 1 and est_Cmp(aVar,aTmp,aFil,aCol,aInt):
            return True

    return False

#************************
def situacion(aVar):
#************************
    """
    Esta funcion devolvera una Lista de los elementos no conseguidos con el siguiente formato:
    [Fila,Columna,Nº de candidatos ]

    Argumentos:
    aVar -> matriz de nSDK x nSDK

    Devuelve una lista

    """
    aTmp = []
    for i in range(0,nSDK):
        for j in range(0,nSDK):
            if len(aVar[i][j]) > 1 :
                aTmp.append([i,j,len(aVar[i][j])])

    return aTmp

#************************
def congruen(cSum):
#************************
    """
    Esta funcion verifica que dada una cadena de numeros (repetidos o no) al menos alguno esta en otra cadena. 
    Si se cumple devolvera True, en caso contrario False

    Argumentos:
    cSum -> cadena de caracteres

    Devuelve:
    Un booleano

    """
    for i in cSDK:
        if not i in cSum:
            return False
    
    return True

#************************
def congru_fil(aVar):
#************************
    """
    Esta funcion recoge por fila todos los valores posibles de aVar: conseguidos y candidatos y apoyandose en la funcion congruen() verifica
    que dada una cadena de numeros (repetidos o no) al menos alguno esta en otra cadena. 
    Si se cumple devolvera True, en caso contrario False
    
    Argumentos:
    aVar -> matriz de nSDK x nSDK

    Devuelve:
    Un booleano

    """
    
    for i in range(0,nSDK):

        cTmp = ""
        for j in range(0,nSDK):
            cTmp += aVar[i][j]
        if not congruen(cTmp):
            return False

    return True

#************************
def congru_col(aVar):
#************************
    """
    Esta funcion recoge por columna todos los valores posibles de aVar: conseguidos y candidatos y apoyandose en la funcion congruen() verifica
    que dada una cadena de numeros (repetidos o no) al menos alguno esta en otra cadena. 
    Si se cumple devolvera True, en caso contrario False
    
    Argumentos:
    aVar -> matriz de nSDK x nSDK

    Devuelve:
    Un booleano

    """
    
    for i in range(0,nSDK):

        cTmp = ""
        for j in range(0,nSDK):
            cTmp += aVar[j][i]
        if not congruen(cTmp):
            return False

    return True

#************************
def congru_cua(aVar):
#************************
    """
    Esta funcion recoge por cuadro todos los valores posibles de aVar: conseguidos y candidatos y apoyandose en la funcion congruen() verifica
    que dada una cadena de numeros (repetidos o no) al menos alguno esta en otra cadena. 
    Si se cumple devolvera True, en caso contrario False
    
    Argumentos:
    aVar -> matriz de nSDK x nSDK

    Devuelve:
    Un booleano

    """
    nFil = 0
    nCol = 0

    for i in range(0,nSDK):
        cTmp = ""
        nFil = (int(i/nRSDK)*nRSDK) - 1

        for j in range(0,nRSDK):
            nFil += 1
            nCol = ((i%nRSDK)*nRSDK) -1

            for k in range(0,nRSDK):
                nCol +=1
                cTmp += aVar[nFil][nCol]
        
        if not congruen(cTmp):
            return False

    return True    


#************************
def loadpar(apar,clin):
#************************
    """
    Funcion que cargara en un dicionario (apar) los diferentes parametros de configuracion:
    
    Argumentos:
    apar -> Diccionario de parametros de configuracion de sudoku a resolver
    clin -> Cadena de caracteres (linea del fichero de configuracion)
    
    Devuelve:
    Actualiza el diccionario, devuelve None

    """
    
    clin = clin.strip()
    
    if "CADSDK" in clin:
        pos = clin.find("=")
        apar["CADSDK"] = clin[pos+1:]

    elif "FILEIN" in clin:
        pos = clin.find("=")
        apar["FILEIN"] = clin[pos+1:]

    elif "FILEOUT" in clin:
        pos = clin.find("=")
        apar["FILEOUT"] = clin[pos+1:]

    elif "NUMSOL" in clin:
        pos = clin.find("=")
        apar["NUMSOL"] = int(clin[pos+1:])

    elif "PRESSOL" in clin:
        pos = clin.find("=")
        tmp = True if clin[pos+1:] == "S" else False
        apar["PRESSOL"] = tmp

    elif "SOLEST1" in clin:
        pos = clin.find("=")
        tmp = True if clin[pos+1:] == "S" else False
        apar["SOLEST1"] = tmp
      
    elif "SOLEST2" in clin:
        pos = clin.find("=")
        tmp = True if clin[pos+1:] == "S" else False
        apar["SOLEST2"] = tmp        

    elif "SOLEST3" in clin:
        pos = clin.find("=")
        tmp = True if clin[pos+1:] == "S" else False
        apar["SOLESTS3"] = tmp

    elif "FUERBRT" in clin:
        pos = clin.find("=")
        tmp = True if clin[pos+1:] == "S" else False
        apar["FUERBRT"] = tmp

    elif "VERALTARB" in clin:
        pos = clin.find("=")
        tmp = True if clin[pos+1:] == "S" else False
        apar["VERALTARB"] = tmp

    return None

#************************
def writesol(aSol,aVar,lmas):
#************************
    """
    Funcion que escribira en una lista (aSol) las soluciones que vaya encontrando
    
    Argumentos:
    aSol -> Lista para cargar solucion en fichero
    aVar -> Lista de sudoku a resolver o resuelto
    lmas -> Booleano que nos indica:
            False ->  Sudoku a resolver (cargar en elemento de aSol posicion 11)
    
    
    Devuelve:
    None

    """
    cTmp = ""
    for i in range(0,nSDK):
            for j in range(0,nSDK):
                cTmp += " " if len(aVar[i][j]) == 0 else aVar[i][j]

    cTmp += "\n"
    
    if lmas:
        aSol.append(cTmp)
    else:
        aSol[12] = cTmp
    
    
    return None

#************************
def presCompl(aTm):
#************************
    """
    Funcion que nos dara una representacion de la complejidad del SUDOKU antes de entrar en Fuerza Bruta
    
    Argumentos:
    aTm ->    Lista de sudoku para presentar su complejidad
    
    
    Devuelve:
    Una cadena formateada

    """
    if len(aTm) == 0:
       return "* Combinaciones Posibles: NO NECESARIO "  + N_LIN

    cTot =  "* Combinaciones Posibles:  "  + N_LIN
    for i in range(0,nSDK):
        cTmp = ""
        for j in range(0,nSDK):
            cTmp += str(len(aTm[i][j])).rjust(2)+"|" if len(aTm[i][j]) > 1 else  "  |"

        cTot += cTmp + N_LIN
        if (i+1)%nRSDK == 0:
            cTot += "-" * nSDK * 3 + N_LIN
        
    return cTot

#************************
def quien(cTmp,i,j,cvar):
#************************
    """
    Funcion presentara en pantalla una solucion de casilla
    
    Argumentos:
    cTmp -> cadena de texto
    i ->    entero que nos indica posicion de fila
    i ->    entero que nos indica posicion de columna
    cvar -> cadena, la solucion de la casilla 
    
    
    Devuelve:
    None

    """
    alert(cTmp + " Fila:" + str(i).rjust(2) + " Columna:" +  str(j).rjust(2) + " Solución:" + cvar +"\n")
    return None

#************************
def cargar_solucion(handle,aSol):
#************************
    """
    Funcion que escribira en el fichero de soluciones informe y soluciones
    
    Argumentos:
    handle -> puntero al fichero de salida (manejador)
    aSol ->   Lista con el informe y soluciones
    
        
    Devuelve:
    None

    """
    for i in aSol:
        f_out.write(i)
    f_out.write("\n\n\n")
        
    return None

#********************************
def est_Dpareja_Fil(parj,nFil,nCol,mCol):
#********************************
    """
    Funcion que aplicará en aVar la estrategia de Par Desnudo/Doble Pareja a una fila
    
    Argumentos: 
    parj -> pareja de 2 caracteres
    nFil -> Int Entero que nos indica en que fila se ha encontrado la doble pareja igual
    nCol -> Int Entero que nos indica una de las columnas
    mCol -> Int Entero que nos indica la otra columna
    
    Devuelve:
    Actualiza aVar 
    0 -> No hemos conseguido reducir
    1 -> Hemos conseguido reducir a un 1 candidato
    2 -> Hemos reducido pero tenemos mas de un candidato
    3 -> INCONGRUENCIA
    
    """
    # recojo cada elemento de la pareja
    n1 = parj[0]
    n2 = parj[1]
    nsal = 0

    #check
    #print("Entrada Fila:",parj)
    #presenta(aVar)


    for j in range(0,nSDK):
        # Evito las columnas donde se encuentra las parejas
        if j != nCol and j != mCol:
            if len(aVar[nFil][j]) >= 2:
                # cuantos elementos tenia la casilla a tratar 
                nini = len(aVar[nFil][j])
                aVar[nFil][j] = aVar[nFil][j].replace(n1,"")
                aVar[nFil][j] = aVar[nFil][j].replace(n2,"")
                
                # cuantos al finalizar
                nfin = len(aVar[nFil][j])
                # hemos reducido
                if nfin != nini:
                    if nfin == 0: 
                        #INCONGRUENCIA 
                        return 3
                    if nfin == 1:
                        # si queremos ver por pantalla como se generan las soluciones, modificar el fichero de configuración <sdk.ini>
                        if apar["SOLEST3"]:
                            quien("3º Estrategia: ", nFil, j, aVar[nFil][j])

                    if nsal != 1:   # Si ya obtuvimos una reduccion al 1 no entramos
                        if nfin == 1:
                            nsal = 1
                        else:
                            nsal = 2

    #check
    #print("Salida Fila:")
    #presenta(aVar)

    return nsal 

#********************************
def est_Dpareja_Col(parj,nCol,nFil,mFil):
#********************************
    """
    Funcion que aplicará en aVar la estrategia de Par Desnudo/Doble Pareja a una Columna
    
    Argumentos: 
    parj -> pareja de 2 caracteres
    nCol -> Int Entero que nos indica en que columna se ha encontrado la doble pareja igual
    nFil -> Int Entero que nos indica una de las filas
    mFil -> Int Entero que nos indica la otra fila
    
    Devuelve:
    Actualiza aVar 
    0 -> No hemos conseguido reducir
    1 -> Hemos conseguido reducir a un 1 candidato
    2 -> Hemos reducido pero tenemos mas de un candidato  
    3 -> INCONGRUENCIA
    
    """
    # recojo cada elemento de la pareja
    n1 = parj[0]
    n2 = parj[1]
    nsal = 0

    #check
    #print("Entrada Columna",parj)
    #presenta(aVar)

    for j in range(0,nSDK):
        if j != nFil and j != mFil:
            if len(aVar[j][nCol]) >= 2:
                # cuantos elementos tenia la casilla a tratar 
                nini = len(aVar[j][nCol])
                aVar[j][nCol] = aVar[j][nCol].replace(n1,"")
                aVar[j][nCol] = aVar[j][nCol].replace(n2,"")
                
                # cuantos al finalizar
                nfin = len(aVar[j][nCol])
                # hemos reducido
                if nfin != nini:
                    if nfin == 0: 
                        #INCONGRUENCIA 
                        return 3
                    
                    if nfin == 1:
                        # si queremos ver por pantalla como se generan las soluciones, modificar el fichero de configuración <sdk.ini>
                        if apar["SOLEST3"]:
                            quien("3º Estrategia: ", nFil, j, aVar[j][nCol])

                    if nsal != 1: # Si ya obtuvimos una reduccion al 1 no entramos
                        if nfin == 1:
                            nsal = 1
                        else:
                            nsal = 2


    #check
    #print("Salida Columna")
    #presenta(aVar)
    return nsal

#********************************
def est_Dpareja_Cua(parj,ncua,ni,nj,mi,mj):
#********************************
    """
    Funcion que aplicará en aVar la estrategia de Par Desnudo/Doble Pareja a un Cuadro/Region
    
    Argumentos: 
    parj -> pareja de 2 caracteres
    ncua -> Int Entero que nos indica el cuadro afectado 
    ni -> Int Entero que nos indica en que fila se ha encontrado una pareja igual
    nj -> Int Entero que nos indica en que columna se ha encontrado una pareja igual
    mi -> Int Entero que nos indica en que fila se ha encontrado la otra pareja igual
    mj -> Int Entero que nos indica en que columna se ha encontrado la otra pareja igual
    
    Devuelve:
    Actualiza aVar 
    0 -> No hemos conseguido reducir
    1 -> Hemos conseguido reducir a un 1 candidato
    2 -> Hemos reducido pero tenemos mas de un candidato
    3 -> INCONGRUENCIA  
    
    """
    # recojo cada elemento de la pareja
    n1 = parj[0]
    n2 = parj[1]
    nsal = 0

    #check
    #print("Entrada Region",ncua,parj)
    #presenta(aVar)

    nFil = (int(ncua/nRSDK)*nRSDK) - 1
    for j in range(0,nRSDK):
        nFil += 1
        nCol = ((ncua%nRSDK)*nRSDK) -1

        for k in range(0,nRSDK):
            nCol +=1
            if not ( (nFil == ni and nCol == nj) or (nFil == mi or nCol == mj) ):  # ninguna de las casillas que son iguales
               if len(aVar[nFil][nCol]) >= 2:

                    # cuantos elementos tenia la casilla a tratar 
                    nini = len(aVar[nFil][nCol])
                    aVar[nFil][nCol] = aVar[nFil][nCol].replace(n1,"")
                    aVar[nFil][nCol] = aVar[nFil][nCol].replace(n2,"") 

                    # cuantos al finalizar
                    nfin = len(aVar[nFil][nCol])
                    # hemos reducido
                    if nfin != nini:
                        if nfin == 0: 
                            #INCONGRUENCIA 
                            return 3

                        if nfin == 1:
                        # si queremos ver por pantalla como se generan las soluciones, modificar el fichero de configuración <sdk.ini>
                            if apar["SOLEST3"]:
                                quien("3º Estrategia: ", nFil, j, aVar[nFil][nCol])

                        if nsal != 1: # Si ya obtuvimos una reduccion al 1 no entramos
                            if nfin == 1:
                                nsal = 1
                            else:
                                nsal = 2

    #check
    #print("Salida Region",ncua)
    #presenta(aVar)

    return nsal  

#************************
def Bucle3(aVar,aFil,aCol,aInt,aPend):
#************************
    """
    Esta funcion tratara de aplicar la estrategia de Par desnudo/doble pareja. Repetiremos el proceso mientras logremos reducir candidatos, si en algun
    momento logramos encontrar el candidato unico de una casilla, al finalizar todo el proceso de reduccion de candidatos iniciaremos el proceso
     desde la 1º estrategia
    Ejemplo:
    Fijemonos en el cuadro de mas a la derecha, tenemos una pareja de candidatos repetida "28", nos idica que dichos valores solo pueden estar en 
    dichas casillas, lo que nos permite quitar cualquiera de estos dos candidatos en el resto.
    ------------------------------------------------------
    !  349|    5|  246! 2389| 2368|    7!    1|   28| 2469!
    !    1| 2368|   26! 2389|    4|    5!    7|   28|  269!
    !  479|  268| 2467!    1|  268|  689!    5|    3| 2469!
    -------------------------------------------------------
    Despues de aplicar dicha estrategia el cuadro quedaria:
    ------------------------------------------------------
    !  349|    5|  246! 2389| 2368|    7!    1|   28|  469!
    !    1| 2368|   26! 2389|    4|    5!    7|   28|   69!
    !  479|  268| 2467!    1|  268|  689!    5|    3|  469!
    -------------------------------------------------------
    En nuestro caso el candidato "2" desaparece del resto de casillas.

    Argumentos:
    Se pasan las listas (aVar,aFil,aCol,aInt,aPend) por referencia.

    Devuelve: Un entero
    0 -> No conseguimos reducir
    1 -> Redujimos una casilla a 1 solo
    2 -> Redujimos
    3 -> INCONGRUENCIA 

    """

    aPend.sort(key=lambda tup:tup[2])
    n = 0
    m = 0
    salEst = 0
    nEst = 0
    # la siguiente variable nos permite seguir analizando mientras tengamos exito
    lexito = False

    while len(aPend) > n and aPend[n][2] == 2:

        m = n + 1
        while len(aPend) > m and aPend[m][2] == 2:
            
            if aVar[aPend[n][0]][aPend[n][1]] == aVar[aPend[m][0]][aPend[m][1]] :
                
                # recojo la doble pareja
                pareja = aVar[aPend[n][0]][aPend[n][1]]
                
                if aPend[m][0] == aPend[n][0]:  # Están en la misma fila
                    # proceso
                    nEst = est_Dpareja_Fil(pareja,aPend[n][0],aPend[n][1],aPend[m][1])
                    
                    if nEst == 3:
                        return 3 # INCONGRUENCIA
                    elif nEst != 0:
                        if nEst ==1:
                           salEst = 1 
                        lexito = True
                        break
                
                if aPend[m][1] == aPend[n][1]:  # Están en la misma columna
                    # proceso
                    nEst =  est_Dpareja_Col(pareja,aPend[n][1],aPend[n][0],aPend[m][0])
                    
                    if nEst == 3:
                        return 3 # INCONGRUENCIA
                    elif nEst != 0:
                        if nEst ==1:
                            salEst = 1 
                        lexito = True
                        break
                
                # Calcular a que Cuadro/Region pertenece
                nReg = ele_Int(aPend[n][0],aPend[n][1])
                mReg = ele_Int(aPend[m][0],aPend[m][1])
                if mReg  == nReg: # estan en el mismo Cuadro/Región 
                    # proceso 
                    nEst = est_Dpareja_Cua(pareja,nReg,aPend[n][0],aPend[n][1],aPend[m][0],aPend[m][1])
                  
                    if nEst == 3:
                        return 3 # INCONGRUENCIA
                    elif nEst != 0:
                        if nEst ==1:
                           salEst = 1 
                        lexito = True
                        break
                    
            m += 1

        # si conseguimos reducir, recalcularemos y volveremos a iniciar el proceso
        if lexito:
            aPend = situacion(aVar)
            aPend.sort(key=lambda tup:tup[2])
            lexito = False
            n = -1
            m= 0

        n += 1

    return salEst

#*************************
#*************************
# MODULO DE RESOLUCION
#*************************
#*************************
N_LIN= "\n" #nueva linea

"""
***************************************
Variables CRITICAS . Sus contenidos
***************************************
aVar ->  Lista de 9x9 los valores de las casillas, todas en formato de Char
         contendran por casilla: la soluciones (una) o las posibles soluciones (varias)
         ejemplo aVar[3,4]->'6' solucion valida al ser única
         otro  aVar[5,6]->'2457' los posibles candidatos a ser la solucion de la casilla

aFil -> Lista de filas, contiene para cada fila una cadena con las casillas halladas en la fila (solucion unica)

aCol -> Lista de las columnas, contiene para cada columna una cadena con las casillas halladas en la columna (solucion unica)

aInt -> Lista de cuadros, contiene para cada cuadro una cadena con las casillas halladas en el cuadro (solucion unica)

aPend ->Lista de ?x3 de las casillas no conseguidas (?) todas en formato -> int
        [Fila, Columna, Número de candidatos posibles]
        Ejemplo: si aPend[6]->[5,6,4]
        aPend[6,1] -> 5ª fila
        aPend[6,2]-> 6ª columna
        aPend[6,3]-> tiene 4 posibles candidatos

aBruta ->   array de ?x3 con el siguiente contenido {aVar,aPend,contador} como vemos
            contiene 2 arrays ya comentados y un entero que se utiliza de contador.
nvuelta -> Entero que cuando es distinto de cero nos indica que estamos tratando la solucion con Fuerza Bruta
            que no es mas que una especulacion que puede ser cierta o falsa.
lsal -> Booleano que controla la salida de las estrategias de resolucion, mientras sea True, vamos bien,
        si nos devuelve False, es porque en algun momento entramos en fuerza bruta y hemos hallado una incongruencia
        no hay solucion para una casilla y hemos de dar pasos atras.
"""

#******************************************************************************
# Apertura del fichero de parametros de configuracion y carga para tratamiento

# Diccionario que contendrá los parametros de configuracion
apar = {"CADSDK":""  ,    
        "FILEIN":"sdk"  ,    
        "FILEOUT":"sal_sdk.txt" ,    
        "NUMSOL": 1  ,
        "PRESSOL":False ,
        "SOLEST1":False ,   
        "SOLEST2":False ,    
        "SOLEST3":False ,
        "FUERBRT":False ,
        "VERALTARB":False, }

try:
    f_ini = open("sdk.ini", mode="r", encoding="utf-8")

except:
    alert("No puedo abrir el fichero <sdk.ini> de carga de configuracion del sudoku")
    sys.exit(0)

for i in f_ini:
    if i[0] != "#" :
        loadpar(apar,i)

f_ini.close()


# Conjunto de caracteres indicativos del tipo de Sudoku, tamaño y su raiz 
cSDK = apar["CADSDK"]
nSDK = len(cSDK)
nRSDK = int(nSDK**(1/2)) # raiz cuadrada

# Creacion de la matriz de elementos vacios del sudoku a resolver 
aVar = [[""] * nSDK for i in range(nSDK)]

# matriz de filas
aFil = [""] * nSDK
# matriz de columnas
aCol = [""] * nSDK
# matriz de cuadro
aInt = [""] * nSDK

# apertura del fichero de donde recogeremos el sudoku a resolver por defecto  < sdk >
try:
    f_in = open(apar["FILEIN"], mode="r", encoding="utf-8")

except:
    alert("No puedo abrir el fichero de carga del sudoku")
    sys.exit(0)

cbuff=f_in.read()
f_in.close()

# Carga del sudoku a resolver leyendo nSDK*nSDK caracteres VALIDOS (definidos en la variable: cSDK)
"""
Es interesante saber como podemos pasarle el sudoku a resolver a programa, ejemplos:

1º Aspecto visual conocido:
 | | | |2| | |1| |
9| | | | |7| | | |
3| | |5| | | | | |
------------------
 |3| |2| | | | |9|
 | | |7|6|1|4| |2|
 | | | |9|5| | | |
------------------
4| |5| | |6|7|9| |
 | | | | | |1|4| |
8|1| |4|5| | | | |
------------------

2º Como una sola fila
      5     35 2    61   9   743   23    1 8665  2  17 61           2  9 4   

3º Otra forma
1    7 9 
 3  2   8
  96  5  
  53  9  
 1  8   2
6    4   
3      1
 4      7
  7   3   

La carga solo entiende la cadena numerica: cSDK (123456789 caso 9x9) y el caracter " " como casilla a resolver,
por tanto tratara de leer tantos caracteres validos como casillas tenga el sudoku. 81 en el caso de un sudoku de 9x9,
asi que podemos pasar el sudoku a resolver como mas nos apetezca conocida como es la lectura. 
"""

m=0
for i in range(0,nSDK):

    for j in range(0,nSDK):

        # extraer verificando contenido
        while True:
            ctmp = cbuff[m:m+1]
            
            if ctmp in (" "+cSDK) or len(ctmp)==0:
                break
            else:
                m +=1
                continue  #loop

        m +=1

        aVar[i][j]= "" if ctmp==" " else ctmp

# vacio cbuff
cbuff = ""

# apertura del fichero en donde recogeremos las soluciones del sudoku, por defecto <sal_sdk.txt >
try:
    f_out = open(apar["FILEOUT"], mode="a", encoding="utf-8")

except:
    alert("No puedo abrir el fichero de soluciones del sudoku")
    sys.exit(0)

# Preparando la Solucion que al final escribiremos en fichero
aSol = [ N_LIN + "*" * 40 + N_LIN ,                                             # 0
         "* Fecha-Hora: " + str(datetime.now()) + N_LIN ,                        # 1
         "* Tipo: " + str(nSDK) + "x" + str(nSDK) + N_LIN ,                      # 2
         "* Elementos Base: " + cSDK + N_LIN ,                                   # 3
         "* Nº Max. de Soluciones Buscadas: " +str(apar["NUMSOL"]) + N_LIN ,     # 4
         "*" + "-" * 40 + N_LIN,                                                # 5
         "" ,                                                                   # 6 Altura Maxima Probable
         "" ,                                                                   # 7 Altura Maxima Alcanzada
         "" ,                                                                   # 8 Combinaciones posibles
         "" ,                                                                   # 9 Combinaciones probadas
         "" ,                                                                   #10 Soluciones Halladas
         "*" * 40 + N_LIN ,                                                     #11 
         "" ]                                                                   #12 Sudoku a resolver
         # esta lista ira creciendo con las soluciones encontradas

# cargar sudoku a resolver
writesol(aSol,aVar,False)

print("PRESENTACION del sudoku cargado para resolver")
presenta(aVar)

#*************************
# Verificacion de la congruencia del sudoku
# Que no se ha cargado algun elemento repetido tanto por fila / columna / cuadro
#*************************
# POR FILA
for i in range(0,nSDK):
    cTmp = ""
    for j in range(0,nSDK):
        cTmp += aVar[i][j]

    if ini_congruen(cTmp):
        alert("Fila:"+str(i)+" No congruente")
        sys.exit(0)

# POR COLUMNA
for i in range(0,nSDK):
    cTmp = ""
    for j in range(0,nSDK):
        cTmp += aVar[j][i]

    if ini_congruen(cTmp):
        alert("Columna:"+str(i)+" No congruente")
        sys.exit(0)


# POR CUADRO
"""
OJO no olvidar, estamos en python y nuestros recorridos empiezan en 0 para que no le sorprenda lo siguiente, solo indica orden:
Para el recorrido de cuadros se establece el siguiente órden (izquierda a derecha y de arriba abajo)
 1 2 3
 4 5 6
 7 8 9
 ------
 Dentro de cada cuadrado el recorrido es igual (izquierda a derecha y de arriba abajo)
 Caso cuadrado nº 6 el recorrido de sus casillas sería coordenadas: filas (4,5,6) y columnas (7,8,9)
 las siguentes coordenadas
  4,7 | 4,8 | 4,9
  5,7 | 5,8 | 5,9
  6,7 | 6,8 | 6,9
"""
for i in range(0,nSDK):
    cTmp = ""
    nFil = (int(i/nRSDK)*nRSDK) - 1

    for j in range(0,nRSDK):
        nFil += 1
        nCol = ((i%nRSDK)*nRSDK) -1

        for k in range(0,nRSDK):
            nCol +=1
            # Activese las siguientes lineas si tiene interes en observar como se va construyendo.
            # print("Fila:", nFil,"Col:",nCol)
            # alert()
            cTmp += aVar[nFil][nCol]

    if ini_congruen(cTmp):
        alert("Cuadro:"+str(i)+" No congruente")
        sys.exit(0)

#*************************
# INICIO PROCESO DE RESOLUCION
# OJO entramos en un Bucle infinito        
#*************************
nSol = 0 # numero de soluciones
nvuelta = 0
check = 0 # varible para chequeo del programador
aBruta = []
nArbReal = 0
nArbMax = 0
aComMax = []

while True:

    # el objetivo es agrupar las casillas resueltas por fila columa y cuadrado.
    ini_comp(aVar,aFil,aCol,aInt)

    # Check
    #print("Estado del sudoku al inicio de su resolucion y su evolucion. Vemos casillas resueltas y candidatos de las no resueltas.")
    #presenta(aVar)
    
    """
    if check ==1 :
        presenta(aVar)
        print("Fil",aFil)
        alert()
        print("Col",aCol)
        alert()
        print("Cuad",aInt)
        alert()
    """

    # Variable de control, para pasar a 2º ó 3º estrategia si no encontramos mas elementos con la estrategia 1º
    lsal = True

    #***********************
    # Estrategia SIMPLE (UNICO DESNUDO)**

    lsal = Bucle1(aVar,aFil,aCol,aInt,nvuelta)

    # Si no hallamos mas elementos en las casillas la variable lsal:=.T.
    # Para ir a la siguiente estrategia

    # FIN estrategia SIMPLE (UNICO DESNUDO)
    #***********************


    #***************************************************
    # Estrategia SOLO PUDE SER ESE, porque es el unico (UNICO OCULTO)**

    if lsal:

        if Bucle2(aVar,aFil,aCol,aInt):
            #check += 1
            #print(check)
            #alert()
            continue

    # FIN estrategia SOLO PUDE SER ESE, poque es el unico (UNICO OCULTO)**
    #*******************************************************


    #***************************************************
    # Estrategia Par Desnudo o Doble Pareja **
    
    if lsal:
        aPend = situacion(aVar)
        #presenta(aVar)
        nEst3 = Bucle3(aVar,aFil,aCol,aInt,aPend)
        # analizamos la salida
        if nEst3 == 3:
            lsal = False # Entre en fuerza bruta a deshacer
        elif nEst3 == 1:
            continue    
    
    # FIN estrategia Par Desnudo o Doble Pareja **
    #*******************************************************


    #Estado de situación
    # Con la entrada de la 3º estrategia posiblemente el if siguiente no sea necesario
    # Posiblemente tampoco los procesos de ordenacion de Fuerza Bruta
    if lsal:
        aPend = situacion(aVar)
        #presenta(aVar)
        #print(aPend)
        #alert()

    # Si entramos en ereordenaremosl if siguiente hemos encontrado al menos una solucion, si entramos con: ( nvuelta = 0 ) se ha resuelto entre 1º, 2º y  3º Estrategia
    # y la solucion es unica. Si tuvo que resolverse por Fuerza Bruta ( nvuelta > 0 ) y la solucion puede ser unica o multiple.
    
    if lsal and len(aPend) == 0:
        # alert('¡¡¡¡ RESUELTO !!!!!')
        # presenta(aVar)
        
        # carga en fichero de salida de solucion
        writesol(aSol,aVar,True)
        
        # contador del numero de soluciones
        nSol += 1

        if nSol == apar["NUMSOL"]: # Hemos llegado al tope de soluciones que queriamos, modificar el fichero de configuración <sdk.ini> si queremos cambiarlo
            break
                  
        if nvuelta == 0:    # salida del While no hay mas soluciones
            break
        else:               # hay mas soluciones
            lsal = False


    """
    OJOJOJOJO
    Antes de seguir adelante y antes de primera vuelta
    verificar con aVar que sumando todos los elementos por filas,columnas, cuadrados
    al menos estan todos los de la cadena maestra(4,9,16,25..)
    es posible forzar algun ejemplo interesante: el sudoku mas grande del mundo
    colocando en [1,2]:=4

    """    

    if nvuelta == 0:
        if not congru_fil(aVar) and not congru_col(aVar) and not congru_cua(aVar):
            alert("NO TIENE SOLUCIONES")
            sys.exit(0)

        # Inicio de estadisticas -> carga de trabajo
        # maxima altura arborea prevista
        nArbMax = len(aPend)

        # Maximas combinaciones posibles
        aComMax = copy.deepcopy(aVar)
        l1Pas = False
        

    # Estado antes de entrar en resolucion arborea (Fuerza Bruta) si queremos verlo modificar el fichero de configuración <sdk.ini>
    if apar["VERALTARB"]:
        presenta(aVar)


    """
    *************************************************     
    ****** LLegar a solucion por FUERZA BRUTA *******   
    *************************************************
    Crearemos una lista que trabajrá como una pila <aBruta> que contendrá una matriz de ?x3 con los siguientes elementos: 
    - Situación de aVar (tendremos casillas con solucion y casillas con candidatos)
    - La tabla asociada aPend, que contiene solo las casillas con candidatos [fila,columna,nº de candidatos] se cargará en aBruta ordenandolo
      previamente por el tercer elemento (nº de candidatos) de menor a mayor
    - Un contador de aBruta

     Empezaremos con el primer elemento de aPend, el de menor numero de candidatos, tomaremos el primer candidato como si fuese la solución y le haremos 
     que circule por la 1º, 2º y 3º  estrategia tratando de encontrar la solución, si no lo conseguimos y nos vemos forzados a entrar en fuerza bruta
     volveremos a  cargar aBruta como lo hicimos anteriormente como un nuevo elemento en la pila, con la situacion de aVar, aPend y el contador de aBruta,   

    """
    # alert("Entramos en Fuerza Bruta")

    
    # Ojo en primera vuelta siempre entrará por el (else) de este (if)
    if not lsal:

        # Bucle de pasos atras
        while True:
            
            # carga del estado anterior
            aVar = copy.deepcopy(aBruta[-1][0])
            aPend = copy.deepcopy(aBruta[-1][1])
             
            #check
            """
            for i in aBruta:
                presenta(i[0])
            alert("*******************")
            """

            """
            ¿Es el ultimo elemento tratado de los pendientes?
            siempre toma  el primero siendo sus coordenadas aPend[0,0],aPend[0,1]  el aPend[0,2]=nº de posibles candidatos
            se estudia sobres el ultimo añadido -> LEN(aBruta) 
            se verifica si recorrimos todos los posibles valores
            """
            # Siempre trabajamos con el primero de aPend despues de ordenarlos
            # Nuestro contador en aBruta es igual al tercer elemento de aPend (nº de candidatos) -> eliminar el ultimo
            
            #check
            #print("Pos. Abruta",aBruta[-1][2],"Tam.aPend",aPend[0])
            #presenta(aBruta[-1] [0])
            #presenta(aVar)
                        
            if aBruta[-1][2] == aPend[0][2]:
                nTmp = aBruta[-1][2] 
                aBruta.pop() 

                # Salida de este bucle infinito
                if len(aBruta) == 0 :
                    
                    aSol[6] = "* Altura Maxima Probable:  " + str(nArbMax).rjust(4) + N_LIN
                    aSol[7] = "* Altura Maxima Alcanzada:  " + str(nArbReal).rjust(4) + N_LIN
                    aSol[8] = presCompl(aComMax)
                    aSol[9] = "* Combinaciones Probadas:  "+str(nvuelta).rjust(6)  + N_LIN
                    aSol[10] = "* Soluciones Halladas:  "+str(nSol).rjust(6)  + N_LIN
                    
                    alert('Soluciones: '+str(nSol))
                    cargar_solucion(f_out,aSol)
                    
                    # cierre
                    f_out.close()

                    sys.exit(0)

            else:
                break

        # recoger el siguiente elemento de los posibles aumentando posteriormente el contador
        
        nTmp = aBruta[-1][2] 


        # asignamos ese posible valor a la casilla
        # Cambiamos esta sintaxis:   aVar[aPend[0][0]][aPend[0][1]] = aVar[aPend[0][0]][aPend[0][1]][nTmp] por la siguiente 
        
        nFil = aPend[0][0]
        nCol = aPend[0][1]
        
        # print("Pos.",nFil,nCol,"Casilla",aVar[nFil][nCol])
        
        
        
        aVar[nFil][nCol] = aVar[nFil][nCol][nTmp]

        # aumentamos el contador
        aBruta[-1][2] = nTmp +1

        # si queremos ver por pantalla como se generan las soluciones modificar el fichero de configuración <sdk.ini>
        if apar["FUERBRT"]:
            quien("Fuerza Bruta: ", aPend[0][0],aPend[0][1], aVar[aPend[0][0]][aPend[0][1]] )

    # han quedado elementos por resolver, otro elemento a la pila de aBruta
    else:
        # reordenamos aPend por el menor numero de cadidatos casilla 3º
        aPend.sort(key=lambda tup:tup[2])
        
        # añadir elementos a aBruta
        
        # He tenido que crear un punto intermedio para cargar <aVar> se esta cargando por referencia y no se porqué
        # Vaya tela hasta que que me he dado cuenta -> un recorrido por la pila aBruta presentado los primeros elementos (estados de aVar)
        # sorpresa todos son iguales ¿alguien que sepa porqué?. He probado la funcion <deepcopy> de módulo <copy> y si funciona.
        """
        vyt = []
        for i in range(0,nSDK):
            lvyt = []
            for j in range(0,nSDK):
                lvyt.append(aVar[i][j])
            vyt.append(lvyt)

        aBruta.append([vyt.copy(),aPend.copy(),1])
        """
        aBruta.append([copy.deepcopy(aVar),aPend.copy(),1])
        
                

        """
        # Check -> Pila de aVar cargados en aBruta
        for i in aBruta:
                presenta(i[0])
        alert("*******************")
        """
        """  
        # Check -> Pila de aPend cargados en aBruta
        for i in aBruta:
                print(i[1])
                print()
        alert("*******************")
        """

        # Coger el primer candidato y probar fila=aPend[1,1], columna=aPend[1,2]
        # Cambiamos esta sintaxis:  aVar[aPend[0][0]][aPend[0][1]] = aVar[aPend[0][0]][aPend[0][1]][0] por la siguiente
        nFil = aPend[0][0]
        nCol = aPend[0][1]
        # asigno el primer candidato a esta casilla (especulo)
        aVar[nFil][nCol] = aVar[nFil][nCol][0]

        # si queremos ver por pantalla como se generan las soluciones
        if apar["FUERBRT"]:
            quien("Fuerza Bruta: ", aPend[0][0],aPend[0][1], aVar[aPend[0][0]][aPend[0][1]] )


    # estadisticas de altura maxima real del arbol alcanzado
    nArbReal =  len(aBruta) if len(aBruta) > nArbReal else nArbReal

    nvuelta += 1
    
# Carga y escritura en el fichero de soluciones
aSol[6] = "* Altura Maxima Probable:  " + str(nArbMax).rjust(4) + N_LIN
aSol[7] = "* Altura Maxima Alcanzada:  " + str(nArbReal).rjust(4) + N_LIN
aSol[8] = presCompl(aComMax)
aSol[9] = "* Combinaciones Probadas:  "+str(nvuelta).rjust(6)  + N_LIN
aSol[10] = "* Soluciones Halladas:  "+str(nSol).rjust(6)  + N_LIN
                    
alert('Soluciones: '+str(nSol))
cargar_solucion(f_out,aSol)
# cierre
f_out.close()

sys.exit(0)






