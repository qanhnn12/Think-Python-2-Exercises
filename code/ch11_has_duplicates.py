def has_duplicates(t):
    d = dict()
    for x in t:
        if x in d:
            return True
        d[x] = None
    return False


def has_duplicates_1(t):
    d = dict()
    for x in t:
        d[x] = None
    return len(t) > len(d)


def has_duplicates_2(t):
    d = dict()
    for x in t:
        d[x] = d.get(x, 0) + 1
        if d[x] > 1:
            return True
    return False


def has_duplicates_3(t):
    return len(t) > len(set(t))


if __name__ == '__main__':
    t = [1, 2, 3, 4]
    print(has_duplicates(t))
    t.append(1)
    print(has_duplicates(t))

    t = [1, 2, 3, 4]
    print(has_duplicates_1(t))
    t.append(1)
    print(has_duplicates_1(t))

    t = [1, 2, 3, 4]
    print(has_duplicates_2(t))
    t.append(1)
    print(has_duplicates_2(t))

    t = [1, 2, 3, 4]
    print(has_duplicates_3(t))
    t.append(1)
    print(has_duplicates_3(t))
