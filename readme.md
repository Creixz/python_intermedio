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
