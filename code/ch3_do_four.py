def do_twice(f, a):
    f(a)
    f(a)


def print_spam(a):
    print(a)


def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)


if __name__ == '__main__':
    do_twice(print_twice, 'spam')
    do_four(print_spam, 'abc')
