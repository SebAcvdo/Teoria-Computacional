# Problema - Tablero de Ajedrez

Problema del tablero usando python.

## Descripción del Problema
En un tablero de 4x4, colocar una o dos piezas que tienen el comportamiento de un rey. El primero se colocará en la esquina superior izquierda, teniendo como objetivo llegar a la esquina inferior derecha. El segundo, en la esquina superior derecha para llegar a la esquina inferior izquierda. Cada casilla del tablero representa un estado. 

Genramos una cadena de r's y b's. Esta cadena representa el color rojo y negro respectivamente. Cada vez que en la cadena encontremos una 'r', significa que la ficha se tiene que mover en alguna de las casillas rojas adyacentes a su posición actual. Aunado a esto, las fichas no deben cruzar caminos en ninguna de las casillas del tablero.

Mediante los resultados arrojados podemos comprobar que para el caso donde se utilizan 2 fichas, ninguna choca con la otra en alguno de sus estados.

La siguiente imagen representa el problema, con la diferencia que es un tablero de 3x3. NO de 4x4.
![Capturatablero](https://github.com/SebAcvdo/Teoria-Computacional/assets/101211184/997e5c19-063b-466a-a809-94d1a88e343b)



## Instrucciones de Uso
El programa presentará dos opciones iniciales:
a) 1 pieza
b) 2 piezas
Teclee la letrta correspondiente a la opción deseada.

Al terminar, el programa imprime en consola el camino a seguir.

## Salida
- Salida para 1 ficha: `[(1, 'r'), (5, 'b'), (10, 'b'), (9, 'r'), (13, 'b'), (14, 'r'), (11, 'r'), (14, 'r'), (13, 'b'), (10, 'b'), (13, 'b'), (14, 'r'), (13, 'b'), (14, 'r'), (13, 'b'), (9, 'r'), 
(6, 'r'), (11, 'r'), (8, 'r'), (11, 'r'), (10, 'b'), (11, 'r'), (16, 'r')]`


![tablero](https://github.com/SebAcvdo/Teoria-Computacional/assets/101211184/c7801ab7-a0b9-47c0-81de-8af0b528cd6d)


Utilizando el tablero como verificar si el camino cumple con llegar de la casilla 1 a la 16 mediante el camino proporcionado por el programa.


## Requisitos del Sistema
- Python 3.x

## Instalación
1. Clona este repositorio.
2. Corre el programa
