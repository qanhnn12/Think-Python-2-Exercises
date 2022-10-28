import math


# Newton's method to compute square root of a number
def mysqrt(a, x):
    while True:
        est_sqrt = (x + a/x) / 2.0
        if est_sqrt == x:
            break
        x = est_sqrt
    return x


def test_square_root():
    a = 1
    x = 4
    print('a  ', 'mysqrt(a)', ' ' * 3, 'math.sqrt(a)', ' diff')
    print('-  ', '-' * 9, ' ' * 3, '-' * 12, '', '-' * 4)

    while a < 10:  # another approach: for a in range (1, 10)
        m = format(mysqrt(a, x), ".11f")
        n = format(math.sqrt(a), ".11f")
        diff = math.sqrt(a) - mysqrt(a, x)
        print(float(a), m, n, diff)
        a = a + 1


if __name__ == '__main__':
    test_square_root()