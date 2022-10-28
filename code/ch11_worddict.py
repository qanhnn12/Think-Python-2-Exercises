import time
from ch10_bisect_search import make_word_list, in_bisect_cheat


def make_word_dict():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = 1
    return d


def check_list(word_list, word):
    return word in word_list


def check_dict(word_dict, word):
    return word in word_dict


def main():
    # runtime for list with in operator:
    start_time_list = time.time()
    check_list(make_word_list(), 'hallo')
    elapsed_time_list = time.time() - start_time_list
    print('For list with in operator:', elapsed_time_list, 'seconds')

    # runtime for list with binary search
    start_time_bi = time.time()
    in_bisect_cheat(make_word_list(), 'hallo')
    elapsed_time_bi = time.time() - start_time_bi
    print('For list with binary search:', elapsed_time_bi, 'seconds')

    # runtime for dictionary with in operator
    start_time_dict = time.time()
    check_dict(make_word_dict(), 'hallo')
    elapsed_time_dict = time.time() - start_time_dict
    print('For dictionary with in operator:', elapsed_time_dict, 'seconds')


if __name__ == '__main__':
    main()