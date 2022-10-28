def str_fill(i, n):
    """
    Returns i as a string with at least n digits.

    :param i: int
    :param n: int length
    :return: string
    """
    return str(i).zfill(n)


def are_reversed(i, j):
    """
    Checks if i and j are the reverse of each other.

    :param i: int
    :param j: int
    :return: boolean
    """
    return str_fill(i, 2) == str_fill(j, 2)[::-1]


def num_instances(diff, flag=False):
    """
    Counts the number of palindromic ages.

    Returns the number of times the mother and daughter have
    palindromic ages in their lives, given th difference in age.

    :param diff: int difference in ages
    :param flag: boolean, if True, prints the details
    """
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff

        # assuming that mother and daughter don't have the same birthday,
        # they have two chances per year to have palindromic ages.
        if are_reversed(daughter, mother) or are_reversed(daughter, mother + 1):
            count = count + 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count


def check_diffs():
    """
    Finds age difference that satisfy the problem.

    Enumerate the possible differences in age between mother
    and daughter, and for each difference, counts the number
    of times over their lives they will have ages that are
    the reverse of each other.
    """
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1


print('diff  #instances')
check_diffs()

print()
print('daughter  mother')
num_instances(18, True)

# Currently, she is 57, her mom is 75.
