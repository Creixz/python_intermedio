def run():
    original_list = [1, 2, 3, 4, 5, 6, 7]

    maped_list = list(map(lambda x: x ** 2, original_list))

    print(maped_list)


if __name__ == '__main__':
    run()