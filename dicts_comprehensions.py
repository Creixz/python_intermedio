def run():
    nros_cubicos = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(nros_cubicos)

    dict_raices_cuadradas = {i: round(i**(1/2),2) for i in range(1,1001)}
    print(dict_raices_cuadradas)


if __name__ == '__main__':
    run()