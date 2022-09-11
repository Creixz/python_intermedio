def divisors(num):
    # divisors = []
    # for i in range(1,num+1):
    #     if num % i == 0:
    #         divisors.append(i)
    try:
        if num <= 0:
            raise ValueError("Ingrese un número positivo")
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        return ve


def run():
    try:
        num = int(input("Ingrese un número: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un número")


if __name__ == '__main__':
    run()