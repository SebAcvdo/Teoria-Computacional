# Autómata de Pila

Problema del automata de pila usando python.

Leer el pdf para más contexto teórico. 
## Descripción del Problema
Programar un autómata de pila que sirva para reconocer el lenguaje libre de contexto {0^n1^n|n >= 1}.

En la implementación, primero planteamos un autómata que nos permita realizar la tarea de un pushdown automata como el planteado en la siguiente imagen.

![pushdown](https://github.com/SebAcvdo/Teoria-Computacional/assets/101211184/e23c734b-2e9b-4f32-b65f-78d9f73c998d)

En el autómata planteado, utilizamos el signo $ para delimitar el fin de la pila.
La letra E se puede ver como la representación de epsilon. Este autómata funciona cuando en el string de entrada, consta de 0’s y 1’s en la misma cantidad.
Dado esto, podemos decir que: Σ = [0, 1] L = [0^n1^n|n >= 1]


## Instrucciones de Uso
1. Ejecuta el programa.
2. Selecciona la opción para modo automático o manual.
   - En el modo automático, el programa genera una cadena aleatoria y la evalúa.
   - En el modo manual, ingresa la cadena que deseas evaluar cuando se solicite.
## Salida
El programa genera un archivo pda.txt con el comportamiento del autómata.
 Ejemplo de salida automática:
```
Cadena ==>  0011 
Char =  
Estado = 0
[]
/----------------------/
Char = 0
Estado = 1
['$']
/----------------------/
Char = 0
Estado = 1
['$', '0']
/----------------------/
Char = 1
Estado = 1
['$', '0', '0']
/----------------------/
Char = 1
Estado = 2
['$', '0']
/----------------------/
Char =  
Estado = 2
['$']
/----------------------/
```



Utilizando el tablero como verificar si el camino cumple con llegar de la casilla 1 a la 16 mediante el camino proporcionado por el programa.


## Requisitos del Sistema
- Python 3.x

## Instalación
1. Clona este repositorio.
2. Ejecuta el programa con python con el comando `python prog6.py`.
