def check_format(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")


def input_num():
    a = int(input("Choose a number for a: "))
    b = int(input("Choose a number for b: "))
    c = int(input("Choose a number for c: "))
    n = int(input("Choose a number for n: "))
    check_format(a, b, c, n)


if __name__ == '__main__':
    input_num()