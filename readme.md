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

usando **List Comprehensions** crear un lista que muestre todos los múltiplos de 4, 6 y 9, que tengan como máximo 5 dígitos.

- Primero sacamos MCM(4, 6, 9) = 36 y el código específico sería:
```
multiples_of_36 = [i for i in range(1,100000) if i % 36 == 0]
print(multiples_of_36)
```

