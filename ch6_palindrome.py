def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


# return nothing when a string has equal or less than 2 letters
if __name__ == '__main__':
    print(middle('hi'))
    print(middle('i'))
    print(middle(''))