from functools import reduce


def run():
    original_list = [1, 2, 3, 4, 5]

    all_multiplied = reduce(lambda a, b: a * b, original_list)

    print(all_multiplied)


if __name__ == '__main__':
    run()