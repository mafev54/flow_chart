# Condicionales y bucles en python

Hola, en este repositorio encontraras diferentes ejercicios solucionados desde mi punto de vista, tambien algunas herramientas basicas acerca del mundo de la programación, tales como los son los condicionales, bucles, funciones, etc.

### Bucles en python:

En Python, los bucles for y while son estructuras de control que permiten repetir un bloque de código varias veces.

El bucle for se utiliza cuando se conoce la cantidad exacta de veces que se desea repetir un bloque de código. Se puede utilizar para iterar sobre una secuencia de elementos, como una lista, una tupla, un rango numérico o cualquier objeto iterable en Python. La sintaxis básica de un bucle for en Python es la siguiente:

<for elemento in secuencia:
    # código a ejecutar>

Donde elemento es una variable que toma el valor de cada elemento de la secuencia en cada iteración, y secuencia es el objeto iterable sobre el cual se itera. El bloque de código indentado que sigue al encabezado del bucle for se ejecuta en cada iteración.

Por otro lado, el bucle while se utiliza cuando se desea repetir un bloque de código mientras se cumpla una determinada condición. La sintaxis básica de un bucle while en Python es la siguiente:

<while condición:
    # código a ejecutar>

Donde condición es una expresión booleana que se evalúa en cada iteración. Mientras la condición sea verdadera, el bloque de código indentado se seguirá ejecutando. Es importante asegurarse de que la condición se vuelva falsa en algún momento para evitar un bucle infinito.

En resumen, los bucles for se utilizan cuando se conoce la cantidad exacta de iteraciones, mientras que los bucles while se utilizan cuando la cantidad de iteraciones depende de una condición.

### Condicionales en python:

En Python, los condicionales se utilizan para ejecutar diferentes bloques de código según una o varias condiciones se cumplan o no. Los condicionales más comunes son las estructuras if, elif y else. La sintaxis básica de un condicional en Python es la siguiente:

<if condición1:
    # código a ejecutar si la condición1 es verdadera
elif condición2:
    # código a ejecutar si la condición2 es verdadera
else:
    # código a ejecutar si ninguna de las condiciones anteriores es verdadera>


Aquí hay algunos puntos clave para entender los condicionales en Python:

La condición1 se evalúa como una expresión booleana, es decir, una expresión que devuelve True o False. Si la condición1 es verdadera, se ejecuta el bloque de código indentado debajo del if.
La palabra clave elif (que significa "sino, si") se utiliza para agregar condiciones adicionales. Si la condición1 es falsa pero la condición2 es verdadera, se ejecuta el bloque de código indentado debajo del elif.
La palabra clave else (que significa "sino") se utiliza al final del condicional y no tiene una condición asociada. Si ninguna de las condiciones anteriores es verdadera, se ejecuta el bloque de código indentado debajo del else.
Puedes tener tantos bloques elif como necesites en un condicional.
Es importante tener en cuenta la indentación en Python, ya que define la estructura del código. Todos los bloques de código dentro de un condicional deben estar indentados de la misma manera (generalmente con cuatro espacios o una tabulación).
Aquí hay un ejemplo de un condicional en Python:

edad = 25

if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres adulto")
else:
    print("Eres mayor de edad")

En este ejemplo, el código evalúa la variable edad y muestra un mensaje dependiendo de su valor. Si la edad es menor que 18, se imprime "Eres menor de edad". Si la edad está entre 18 (inclusive) y 65 (no inclusive), se imprime "Eres adulto". Si ninguna de las condiciones anteriores es verdadera, se imprime "Eres mayor de edad".