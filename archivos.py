def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding = "utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Facund0", "Miguel", "Pepe", "Christian"]
    # Se puede usar "a" en vez de w para que el archivo ya no se sobreescriba sino que agregue el contenido al final del archivo
    with open("./archivos/names.txt", "w", encoding = "utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n") 


def run():
    write()


if __name__ == '__main__':
    run()