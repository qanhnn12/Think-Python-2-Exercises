cache = {}


def ack(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)

    if (m, n) in cache:
        return cache[(m, n)]
    else:
        cache[(m, n)] = ack(m-1, ack(m, n-1))
        return cache[(m, n)]


def main():
    m = int(input('Enter a number for m: '))
    n = int(input('Enter a number for n: '))
    print(ack(m, n))


if __name__ == '__main__':
    main()
