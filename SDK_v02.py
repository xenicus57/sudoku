"""
SDK_v02.py
Version 02
En esta version se implementara la configuracion a través de fichero <sdk.ini>
"""
import sys

#*************************
def alert(pipo=""):
#*************************
    """
    Funcion parada, información y continuacion.
    
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
        por tanto su función principal es de apoyo en el chequeo del código que vamos costruyendo.

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
        cSum -> cadena de caracteres de cualquier fila, columna, cuadro.

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

    Argumento:
    Se pasan las cuatro listas (aVar,aFil,aCol,aInt) por referencia de las cuales las tres ultimas en base a aVAR se modificaran.
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
    Esta funcion nos calculara, conociendo posicion de fila y columna de que cuadro se trata
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
    Encontrado un elemento de una casilla nos permite reajustar las listas: fila columna y cuadro con dicho elemento añadiendolo

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
    Funcion Estrategia Simple
    Esta funcion tratara de buscar elementos que faltan en el sudoku con el algoritmo Estrategia Simple. 
    Sobre una casilla ver, de la suma de los elementos hallados de fila, columna y cuadro, cuantos faltan de la cadena base (cSDK)
    Si solo nos falta uno es el definitivo para dicha casilla.

    Argumentos:
    Se pasan las cuatro listas (aVar,aFil,aCol,aInt) por referencia.
    nvuelta -> integer

    Devuelve:
    Siempre  True, a no ser que interrumpa el programa al encontrar que es irresoluble
    """
    nInt = 0
    lsigue =True

    while lsigue:
        lsigue = False

        for i in range(0,nSDK):
            for j in range(0,nSDK):
                """
                En primera vuelta habrá casillas (las que hay que resolver) de aVar que estaran vacias y en las siguientes vueltas
                con un solo caracter (SOLUCION DE CASILLA) o mas caracteres (PENDIENTE), estos caracteres de mas nos indican
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
                        print (aFil[i])
                        print(aCol[j])
                        print(aInt[nInt])
                        alert('SUDOKU Irresoluble: '+'Casilla:'+str(i)+','+str(j))
                        presenta(aVar)
                        sys.exit(0)

                    # tengo dudas que entre por aquí poner checks
                    if len(aVar[i][j]) == 0:
                        alert("Creo que nuncaca saldrá este msg.")
                        return False

                    # Hemos encontrado solo 1 es portanto la solucion de esa casilla
                    if len(aVar[i][j]) == 1:
                        print("1º Estrategia" )
                        print("Fil.",i,"Col.",j,"  Valor",aVar[i][j])
                        alert()
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
                    # check
                    print("2º Estrategia" )
                    print("Fil.",j[0],"Col.",j[1],"  Valor",i)
                    alert()
                    
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

#*************************
#*************************
# MODULO DE RESOLUCION
#*************************
#*************************
"""
***************************************
Variables CRITICAS . Sus contenidos
***************************************
aVar ->  Lista de 9x9 los valores de las casillas, todas en formato de Char
         contendran por casilla: la soluciones (una) o las posibles soluciones (varias)
         ejemplo aVar[3,4]->'6' solucion valida al ser única
         otro  aVar[5,6]->'2457' los posibles candidatos a ser la solucion de la casilla

aFil -> Lista de filas, contiene para cada fila una cadena con las casillas halladas en la fila (solucion unica)

aCol -> Lista de las columnas, contiene cada columna una cadena con las casillas halladas en la columna (solucion unica)

aInt -> Lista de cuadros, cada cuadro una cadena con las casillas halladas en el cuadro (solucion unica)

aPend ->Lista de ?x3 de las casillas no conseguidas (?) todas en formato Num
        [Fila, Columna, Número de valores posibles]
        Ejemplo: si aPend[6]->[5,6,4]
        aPend[6,1] -> 5ª fila
        aPend[6,2]-> 6ª columna
        aPend[6,3]-> tiene 4 valores posibles

aBruta ->   array de ?x3 con el siguiente contenido {aVar,aPend,contador} como vemos
            contiene 2 arrays ya comentados y un contador.
"""

#******************************************************************************
# Apertura del fichero de parametros de configuracion y carga para tratamiento

apar = [None] * nSDK


try:
    f_ini = open("sdk.ini", mode="r", encoding="utf-8")

except:
    alert("No puedo abrir el fichero <sdk.ini> de carga de configuracion del sudoku")
    sys.exit(0)

for i in f_ini:
    if i[0] != "#"
        loadpar(apar,i)






"""

 // apertura del fichero de parametros de configuracion y carga para tratamiento
 //*****************************************************************************
 nManiConf := FOPEN("sdk.ini",FO_READ) 
 IF nManiConf = -1  
    // error en la apertura 
    ALERT('ERROR no puedo localizar <sdk.ini> ')
    QUIT

 ENDIF

 // carga en buffer (cBuff) del fichero
 nBuff:=FSIZE(nManiConf)                    //tamaño del fichero
 cBuff:=SPACE(nBuff)                        // establezco tamaño a blancos
 FREAD(nManiConf,@cBuff,nBuff)              // cargo los valores


 // Recogida de parametros de fichero sdk.ini
 //******************************************
 // cargado en buffer todo el fichero .ini se van buscando CHR(13)+CHR(10)
 // saltos de linea
 // bucle de recorrido y carga de parametros
 DO WHILE ( n := AT( N_LIN, cBuff ) ) > 0   // busca saltos de linea
    cTmp := LEFT( cBuff, n-1 )                        // corte menos la parada en CHR(13)
    
    // desechamos lo que recogimos en ctmp
    cBuff := SUBSTR( cBuff, n+2)              // saltamos al siguiente pasando de chr(13)+chr(10)

    // tratamiento de los cortes
    IF SUBSTR(cTmp,1,1) <> '#' // por igual-> comentario, paso a siguiente linea
       // funcion de recogida de parametros del fichero ini
       loadpar(aPar,cTmp) 
    ENDIF

 ENDDO 
 
 // controlar el ultimo corte que nos quedo en cbuf si no se acabo con chr(13)+chr(10)
 IF SUBSTR(cBuff,1,1) <> '#' // por igual-> comentario, paso a siguiente linea
    loadpar(aPar,cBuff) 
 ENDIF
 // cierre del archivo cutlog.ini
 FCLOSE(nManiConf)






"""







# Variables indicativas del Sudoku (en siguientes versiones se pasaran atraves de un archivo de configuaracion <sdk.ini>)
cSDK = "123456789"
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
    f_in = open("sdk", mode="r", encoding="utf-8")

except:
    alert("No puedo abrir el fichero de carga del sudoku")
    sys.exit(0)

cbuff=f_in.read()
f_in.close()

# Carga del sudoku a resolver leyendo nSDK*nSDK caracteres VALIDOS (definidos en la variable: cSDK)
"""
Es interesante saber como podemos pasarle el sudoku a resolver, ejemplos:

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

La carga solo entiende la cadena de numerica: 123456789 y el caracter " " como casilla a resolver,
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
nvuelta = 0
check = 0
while True:

    # el objetivo es agrupar las casillas resueltas por fila columa y cuadrado.
    ini_comp(aVar,aFil,aCol,aInt)

    # Control
    print("Estado del sudoku al inicio de su resolucion y su evolucion. Vemos casillas resueltas y candidatos de las no resueltas.")
    presenta(aVar)
    
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

    # Variable de control, para pasar a 2º estrategia si no encontramos mas elementos con la estrategia 1º
    lsal = True

    #***********************
    # Estrategia SIMPLE **

    lsal = Bucle1(aVar,aFil,aCol,aInt,nvuelta)

    # Si no hallamos mas elementos en las casillas la variable lsal:=.T.
    # Para ir a la siguiente estrategia

    # FIN estrategia SIMPLE
    #***********************


    #***************************************************
    # Estrategia SOLO PUDE SER ESE, poque es el unico **

    if lsal:

        if Bucle2(aVar,aFil,aCol,aInt):
            check += 1
            #print(check)
            #alert()
            continue

    # FIN estrategia SOLO PUDE SER ESE, poque es el unico **
    #*******************************************************

    #Estado de situación
    if lsal:
        aPend = situacion(aVar)


    # Si entramos en el if siguiente, hemos finalizado, si entramos en else a la siguiente estrategia (FUERZA BRUTA) 
    if lsal and len(aPend) == 0:
        alert('¡¡¡¡ RESUELTO !!!!!')
        presenta(aVar)
        break

    else:
        alert('No conseguido. Siguiente paso fuerza BRUTA')
        presenta(aVar)
        break



"""
    **********************************
    ****** Estado de SITUACION *******
    **********************************

    IF lsal
       aPend:=situacion(aVar)
    ENDIF

    ***** FIN Estado de SITUACION *******


    ******************************************
    ****** Verificacion de CONGRUENCIA *******
    ******************************************

    *********************
    ***** No hace falta verificacacion de congruencia **********
    *********************

    **********************************
    ****** Carga de SOLUCIONES *******
    *******aVar,aFil,aCol,aInt***************************
    IF lsal .AND. LEN(aPend)=0  // no existen elementos pendientes
       // conseguido
       // alert('Conseguido y Congruente')

       // distintas soluciones
       IF lPreSol
          alert('¡¡¡¡ AHI VA !!!!!')
          Scroll()
          presenta(aVar)
       ENDIF

       // carga en fichero de salida
       writeSol(nManiOut,aVar)

       // cuantas soluciones tiene
       ++nSol

       /*
       // presentacion en pantalla de como va consiguiendo soluciones
       @18,05 SAY 'Solución:' + STR(nSol)
       */

       // check
       IF nSol=nNumSol  // nº maximo de soluciones que quiero que me de
          EXIT
       ENDIF


       IF nVuelta = 0
          EXIT  //salida del DO WHILE no hay mas soluciones
       ELSE

          // Punto de Control Particular
          // alert("vuelta:"+ str(nVuelta))


          // seguir siguientes soluciones en Fuerza Bruta
          lsal:= .F.
       ENDIF

    ENDIF





"""




