def gcd(a, b):
    # base case: gcd(a, 0) = a
    if b == 0:
        return a

    # if r is the remainder when a is divided by b, gcd(a, b) = gcd(b, r)
    else:
        r = a % b
        return gcd(b, r)


if __name__ == '__main__':
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    print(f"The greatest common divisor of {a} and {b} is", gcd(a, b))