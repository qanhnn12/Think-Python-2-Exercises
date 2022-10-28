from ch10_bisect_search import make_word_list, in_bisect_cheat


def reverse_pair(word_list, word):
    rv_word = word[::-1]
    return in_bisect_cheat(word_list, rv_word)


if __name__ == '__main__':
    word_list = make_word_list()
    for word in word_list:
        if reverse_pair(word_list, word):
            print(word, word[::-1])


