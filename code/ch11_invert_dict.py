def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]

        # create an empty list as the the value of the inverse dict
        # append (keys of d as) values into the inverse dict
        inverse.setdefault(val, []).append(key)
    return inverse


if __name__ == '__main__':
    d = {'a': 0, 'b': 1, 'c': 1, 'd': 2}
    print(invert_dict(d))
