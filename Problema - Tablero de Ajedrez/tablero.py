import random
import math

def main():
    #Crea la matriz del tablero con arreglos
    matriz = crearMatriz()
    while(1):
        print("=====EJERCICIO DEL TABLERO=====")
        print("Elija una opción:")
        print("a) 1 pieza")
        print("b) 2 piezas")
        piezas = input() 
        if piezas == "a":
            unaATM(matriz)
        elif(piezas == "b"):
            #2 piezas automatico
            dosATM(matriz)
            
        else: print("Opción de pieza no disponible" )
            
def crearMatriz():
    colores=['r','b','r','b']

    #Crea matriz de 4x4
    # 4 filas de 4 elementos
    matriz = [[(x+1+y*4) for x in range(4)] for y in range(4)] 

    for i in range(len(matriz)):
        '''
        Asigna el color de la casilla. Usa el método zip para combinar las filas con la lista coloroes.
        El método list hace que retorne una lista, para que la matriz no se vea alterada.
        '''
        matriz[i] = list(zip(matriz[i],colores))

        #Cada vez que hay un salto de fila, el orden de los colores se invierte.
        colores.reverse()
    return(matriz)

def unaATM(matriz):
    path = [matriz[0][0]]
    ficha = 1
    while(ficha != 16 ):

        i = int(math.ceil(ficha/4)) - 1
        j = ficha - (i*4) - 1
        moves = crearMoves(i,j,matriz,ficha)                 

        peso = [(d+1)*(2*d+3) for d in range(len(moves))]
        siguiente = random.choices(moves, weights=peso, k=1)[0]      
        ficha = siguiente[0]
        moves.clear()     
        path.append(siguiente)
              
    print(path)

def dosATM(matriz):
    path1 = [matriz[0][0]]
    path2 = [matriz[0][3]]
    lim1 = 16
    lim2 = 13
    ficha1 = 1
    ficha2 = 4

    if(random.randint(1, 2) == 2):
        path1,path2 = path2,path1
        ficha1,ficha2 = ficha2, ficha1
        lim1,lim2 = lim2,lim1 

    while(ficha1 != lim1 or ficha2 != lim2):

        i = int(math.ceil(ficha1/4)) - 1
        j = ficha1 - (i*4) - 1
        moves1 = crearMoves(i,j,matriz,ficha1)
        #print(moves1)

        i = int(math.ceil(ficha2/4))-1
        j = ficha2 - (i*4) - 1
        moves2 = crearMoves(i,j,matriz,ficha2)
        #print(moves2)

        peso = [(d+1)*(2*d) for d in range(len(moves1))]
        #peso = [(d+1)*40 for d in range(len(moves1))]
        #print(peso)

        siguiente = random.choices(moves1, weights=peso, k=1)[0]      
        ficha1 = siguiente[0]
        path1.append(siguiente)
        #print(siguiente)
        moves1.clear()        

        peso = [(d+1)*(2*d) for d in range(len(moves2))]
        #peso = [(d+1)*40 for d in range(len(moves2))]

        while(siguiente[0] == ficha1):
            siguiente = random.choices(moves2, weights=peso, k=1)[0]      
            ficha2 = siguiente[0] 
            #print(ficha2)

        path2.append(siguiente)
        
        moves2.clear()               
    print(path1,"\n")
    print(path2)

def crearMoves(i,j,matriz,ficha):
    moves = []
    for k in range(i-1,i+2):
        if(-1 < k < 4):
            for m in range(j-1,j+2):
                if(-1 < m < 4):
                    if (matriz[k][m][0] != ficha):
                        moves.append(matriz[k][m])   
    return moves


main()
