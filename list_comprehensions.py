def run():
    # lista_normal = list(range(1,101))
    # lista_cuadrados = []

    # for elemento_cuadrado in lista_normal:
    #     if elemento_cuadrado % 3 != 0:
    #         lista_cuadrados.append(elemento_cuadrado**2)
            
    # print(lista_cuadrados)

    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    print(squares)

    multiples_of_36 = [i for i in range(1,100000) if i % 36 == 0]
    print(multiples_of_36)



if __name__ == '__main__':
    run()