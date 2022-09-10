def run():
    # Lista original que se va a filtrar
    list_to_filter = [1, 4, 5, 6, 9, 13, 18, 19, 21, 26, 30, 31]

    # Se está filtrando la lista de arriba quitándole los elementos pares.
    filtered_list = list(filter(lambda x: x % 2 != 0, list_to_filter))

    print(filtered_list)


if __name__ == '__main__':
    run()