# Problema - Tablero de Ajedrez

## Descripción del Problema
En un tablero de 4x4, colocar dos piezas que tienen el comportamiento de un rey. El primero se colocará en la esquina superior izquierda, teniendo como objetivo llegar a la esquina inferior derecha. El segundo, en la esquina superior derecha para llegar a la esquina inferior izquierda. Cada casilla del tablero representa un estado. Para determinar la ruta que debe seguir cada pieza, el usuario o el programa en su defecto, debe ingresar una cadena de r’s y b’s.

Esta cadena representa el color rojo y negro respectivamente. Cada vez que en la cadena encontremos una 'r', significa que la ficha se tiene que mover en alguna de las casillas rojas adyacentes a su posición actual. Aunado a esto, las fichas no deben cruzar caminos en ninguna de las casillas del tablero.

Al terminar la ejecución, el programa genera un archivo txt con el camino a considerar tomando en cuenta la cadena generada. Mediante los resultados arrojados podemos comprobar que para el caso donde se utilizan 2 fichas, ninguna choca con la otra en alguno de sus estados.

## Instrucciones de Uso
1. Ingresa la cadena de 'r's y 'b's para cada ficha.
2. Ejecuta el programa.
3. Encuentra el archivo de salida con el camino generado.

## Ejemplo de Entrada y Salida
- Entrada: `rrbb`
- Salida: Archivo `camino_generado.txt`

## Requisitos del Sistema
- Python 3.x
- Librerías adicionales (si es necesario)

## Licencia
Este programa está bajo la licencia [nombre de la licencia].

## Instalación
1. Clona este repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.

## Ejemplo de Código
```python
# Código de ejemplo aquí
