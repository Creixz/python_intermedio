# Comprehensions, Lambdas y Manejo de errores

## List Comprehensions

- Creamos una lista vacia luego le pusimos un for para que eleve los valores al cuadrado y una condicional que solo eleve al cuadrado a los valores que no sean divisibles por 3.
- Usando **List Comprehensions** esto resulta más facil y tiene la siguiente estructura:

```
[element for element in iterable if condition]
```
- El primer **element** representa a cada uno de los elementos a poner en la nueva lista.
- El **for element in iterable** es el ciclo a partir del cual se extraerá los elementos de otra lista o de un rango (iterable).
- El **if condition** es la condicion opcional para filtrar los elementos del ciclo.

### Reto #1

Usando **List Comprehensions** crear un lista que muestre todos los múltiplos de 4, 6 y 9, que tengan como máximo 5 dígitos.

- Primero sacamos MCM(4, 6, 9) = 36 y el código específico sería:
```
multiples_of_36 = [i for i in range(1,100000) if i % 36 == 0]
print(multiples_of_36)
```

## Dictionary Comprehensions

- Usar **Dictionary Comprehensions** es casi igual que las **List Comprehensions** y tiene la siguiente estructura:

```
[key: value for key in iterable if condition]
```
- El **key: value** presenta cada una de las llaves y valores que tomará cada elemento del diccionario.
- El **for key in iterable** es el ciclo del cual se extraen los elementos de un rango (iterable) u otro diccionario.
- El **if condition** es la condición para filtrar los elementos del diccionario.

### Reto #2

Usando **Dictionary Comprehensions** crear un diccionario que tenga como llaves los 1000 primeros numeros naturales y como valores las respectivas raíces cuadradas.

- Sería optimo redondear la cantidad de decimales a 2, para que sea más legible el output, el código específico sería:
```
dict_raices_cuadradas = {i: round(i**(1/2),2) for i in range(1,1001)}
print(dict_raices_cuadradas)
```

## Funciones anónimas y Lambdas

Las funciones anónimas sirven para definir una función que no tenga un nombre específico.
- Se define de la siguiente manera:
```
lambda argumentos: expresión
```
- Cuando se define:
```
name_var = lambda string: string == string[::-1] -> esto retorna un objeto del tipo función y se guarda en la variable, no es el nombre de la función.
print(name_var(valor)) -> Esto no llama a la función, más bien, se utiliza la variable con el paréntesis para invocar al objeto de tipo función.
```
## High order functions: filter, map y reduce

### Filter

- Es una de las funciones de orden superior, y se encarga de filtrar una determinada lista bajo ciertas condiciones, y se define de la siguiente manera.
 
```
name_filter_list = list(filter(lambda x: x%2 != 0, list_to_filter))
```
- Filter recibe dos parámetros que son una función anónima y la lista que será filtrada.

### Map

- Es otra de las funciones de orden superior, y se encarga de modificar de forma uniforme o proporcional a todos los elementos de una determina lista, y se define de la siguiente manera.
```
name_map_list = list(map(lambda x: x ** 2, list_to_filter))
```
- Map recibe dos parámetro que son una función anónima y la lista que será modificada.

### Reduce

- Es otra de las funciones de orden superior, y se encara de reducir los elementos de una lista a un determinado valor, y se define de la siguiente manera.
```
from functools import reduce

name_reduce = reduce(lambda a, b: a * b, list_to_reduce)
```
- **Reduce** primero se debe importar de **functools** y recibe dos parámetros que son una función anónima con dos argumentos y la operación que reducirá los elementos de la función.

## Manejo de errores en Python

### Errores en el código

Cuando python nos avisa que tenemos un error en el código nos avienta un mensaje que conocemos como traceback, puesde ser debido a:

- Errores de Sintaxis (SyntaxError) → escribimos mal alguna palabra clave (typo), el programa no se ejecuta.
- Excepciones (Exeption) → Producen un colapso o interrupción de la lógica del programa en alguna línea en específico por ejemplo (todas las líneas anteriores se ejecutan), pueden ser de varios tipos, generalmente aparecen cuando no existe un componente clave en la ejecución o hay alguna imposibilidad lógica (matemática) para efectuar la instrucción, tambipen pueden generarse dentro del código o fuera de el (elevar una excepción)

### Lectura de un traceback

- La manera correcta de leer un traceback es iniciar por el final, en el caso de un error de sintaxis nos indicará en qué línea se encuentra dicho error.
- En el caso de excepciones la última línea nos indicará el tipo de exepcion que se generó (generalmente son autoexplicativas pero si no entienedes que paso puedes buscar este error)
- La penúltima línea nos indicará dende se encuentra el error (archivo y línea)
- La antepenúltima línea nos muestra “most recent call last” lo que significa que la llamada más reciente es la última (el programa se cerró después de esa llamada, se genero un error)

### Elevar una excepción

- Cuando tenemos una excepción en python lo que sucede es que se crea un objeto de tipo exception que se va moviendo a través de los bloques de código hasta llegar al bloque principal si es que no se maneja dicha excepción en algún bloque intermedio el programa se interrumpe y genera el traceback.

### Debugging 

- Para aplicar esta técnica si utilizas Visual Studio Code, presiona **Ctrl-Shift-D** y luego **Run and Debug** para poder examinar tu código paso a paso con las opciones disponibles y encontrar el error de lógica de manera más eficiente.

### Manejo de excepciones

#### Try and except

- El **except** solo funciona para los errores del tipo TypeError.
- Se produce el error debido a que se ingresa un valor que no se esperaba por lo que el **try-except** permite enviar un mensaje en caso de que se coloque un valor no válido.
```
def palindromo(string):
    return string == string[::-1]

try:
    print(palindromo(1))
except TypeError:
    print("Solo se puede ingresar strings")
```

#### Raise

- Usaremos **raise** en caso de que el **try** no detecte el error y no pueda lanzarse el exception.
```
def palindromo(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacía")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    print(palindromo(""))
except TypeError:
    print("Solo se puede ingresar strings")
```

#### Finally

- Se podría utilizar **finally** después de un **try** para cerrar un archivo dentro de Python o cerrar una conexión a la base de datos o liberar recursos externos.
```
try:
    f = open("archivo.txt")
    #Aquí hacer cualquier cosa con el archivo
finally:
    f.close()
```
- Es imperativo usar el finally para cerrar correctamente un archivo o una base de datos ya que si se cortará el programa de forma abrupta por algún error, esto podría dañar el archivo o base de datos que se está utilizando.