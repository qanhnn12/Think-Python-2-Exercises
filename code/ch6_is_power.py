def is_divisible(x, y):
    return x % y == 0


def is_power(a, b):
    # 1st base case: a=b, a is a power of itself
    if a == b:
        return True

    # 2nd base case: b=1, the only positive integer that is a power of '1' is '1' itself
    elif b == 1:
        return False

    # call is_divisible() and call is_power() recursively
    else:
        return is_divisible(a, b) and is_power(a/b, b)


if __name__ == '__main__':
    print("is_power(1, 1) returns:", is_power(1, 1))
    print("is_power(3, 3) returns:", is_power(3, 3))
    print("is_power(10, 1) returns:", is_power(10, 1))
    print("is_power(10, 2) returns:", is_power(10, 2))
    print("is_power(27, 3) returns:", is_power(27, 3))
    print("is_power(17, 2) returns:", is_power(17, 2))

