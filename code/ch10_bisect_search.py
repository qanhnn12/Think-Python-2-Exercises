import bisect


def make_word_list():
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    t.sort()
    return t


def in_bisect(word_list, word):
    if len(word_list) == 0:
        return False

    # divide the list into 2 parts
    i = len(word_list) // 2

    # if it coincidentally matches the word we want to find:
    if word_list[i] == word:
        return True

    # search the first half
    elif word_list[i] > word:
        return in_bisect(word_list[:i], word)

    # search the second half
    else:
        return in_bisect(word_list[i+1:], word)


def in_bisect_cheat(word_list, word):
    i = bisect.bisect_left(word_list, word)

    # base case: the list is empty or the word we want to find isn't in it
    if i == len(word_list):
        return False
    return word_list[i] == word


if __name__ == '__main__':
    word_list = make_word_list()

    print('Check the list using in_bisect():')
    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect(word_list, word))

    print()

    print('Check the list using bisect module:')
    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect_cheat(word_list, word))
