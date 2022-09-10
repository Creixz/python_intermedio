def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dic = {"firstname": "Freddy", "lastname": "Santana"}

    super_list = [
        {"firstname": "Freddy", "lastname": "Santana"},
        {"firstname": "Eduardo", "lastname": "Salas"},
        {"firstname": "Vanessa", "lastname": "Lazaro"},
        {"firstname": "Zoe", "lastname": "Santana"},
        {"firstname": "Eva", "lastname": "Lozano"}
    ]

    super_dic = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dic.items():
        print(key, "-", value)

    for item_list in super_list:
        print(f'La lista número {super_list.index(item_list)+1} es {item_list}')


if __name__ == '__main__':
    run()