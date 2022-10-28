# EXERCISE 10.1

def nested_sum(t):
    """Approach 1:
    Computes the sum of all numbers in a list of lists
    :param t: list of lists of numbers
    :return: numbers
    """
    total = 0
    for nest in t:
        total += sum(nest)
    return total


def nested_sum_1(t):
    """Approach 2:
    Computes the sum of all numbers in a list of lists
    :param t: list of lists of numbers
    :return: numbers
    """
    k = []
    for l in t:
        for num in l:
            k.append(num)
    return sum(k)


# EXERCISE 10.2

def cumsum(t):
    """
    Computes the cumulative sum of the numbers in a list
    :param t: list of number
    :return: list of number
    """
    t1 = []
    total = 0
    for x in t:
        total += x
        t1.append(total)
    return t1


# EXERCISE 10.3

def middle(t):
    """
    Returns all but the first and last elements of t
    :param t: list
    :return: new list
    """
    return t[1:-1]


# EXERCISE 10.4

def chop(t):
    """Approach 1:
    Removes the first and last elements of t
    :param t: list
    :return: None
    """
    del t[0]
    del t[-1]


def chop_1(t):
    """ Approach 2:
    Removes the first and last elements of t
    :param t: list
    :return: None
    """
    t.pop(0)
    t.pop(-1)


# EXERCISE 10.5

def is_sorted(t):
    """Approach 1:
    Check if a list is sorted
    :param t: list
    :return: boolean
    """
    return t == sorted(t)


def is_sorted_1(t):
    """Approach 2:
    Check if a list is sorted
    :param t: list
    :return: boolean
    """
    return t == t.sort()


# EXERCISE 10.6

def is_anagram(a, b):
    """
    Check if two words are anagrams
    :param a: word or list
    :param b: word or list
    :return: boolean
    """
    return sorted(a) == sorted(b)


# EXERCISE 10.7

def has_duplicates(t):
    """Approach 1:
    Check if a list has duplicates
    :param t: list
    :return: boolean
    """
    t.sort()
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False


def has_duplicates_1(t):
    """Approach 2:
    Check if a list has duplicates
    :param t: list
    :return: boolean
    """
    for i in t:
        if t.count(i) > 1:
            return True
    return False


def main():
    print('**Exercise 10.1')
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))
    print(nested_sum_1(t))
    print()

    print('**Exercise 10.2')
    t = [1, 2, 3]
    print(cumsum(t))
    print()

    print('**Exercise 10.3')
    t = [1, 2, 3, 4]
    print(middle(t))
    print()

    print('**Exercise 10.4')
    chop(t)
    print(t)

    chop_1(t)
    print(t)
    print()

    print('**Exercise 10.5')
    print(is_sorted([2, 2, 3]))
    print(is_sorted(['h', 'a']))
    print()

    print('**Exercise 10.6')
    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))
    print()

    print('**Exercise 10.7')
    t = ['a', 'a', 'v', 'b']
    print(has_duplicates(t))
    print(has_duplicates_1(t))


if __name__ == '__main__':
    main()
