import random
from ch10_list_exercises import has_duplicates


def random_bday(n):
    """
    Returns a list of integers from 1 to 365 with length n
    :param n: int
    :return: list of int
    """
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


def count_matches(num_students, num_simulations):
    """
    Generates a sample of birthdays and count duplicates
    :param num_students: how many students in the group
    :param num_simulations: how many groups to simulate
    :return: int
    """
    count = 0
    for i in range(num_simulations):
        t = random_bday(num_students)
        if has_duplicates(t):
            count += 1
    return count


def main():
    num_students = 23
    num_simulations = 1000
    count = count_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)


if __name__ == '__main__':
    main()