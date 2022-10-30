def signature(s):
    """
    Returns the signature of this string.
    Signature is a string that contains all letters in order
    :param s: string
    :return: ordered string
    """
    t = sorted(s)
    t = ''. join(t)
    return t


def order_tuples(s):
    """
    Returns a tuples of ordered letters
    :param s: string
    :return: tuples
    """
    p = tuple(sorted(s))
    return p


def all_anagrams(filename):
    """
    Finds all anagrams in a list of words
    :param filename: string filename of the word list
    :return: a dictionary that maps from each tuple of words to its anagrams
    """
    d = dict()
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)     # opt2: use order_tuple

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)

    return d


def print_anagram_sets(d):
    """
    Prints anagram sets in d
    :param d: map from tuples to list of their anagrams
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_sorted_anagrams_sets(d):
    """
    Prints anagram sets in d in descending order of size
    :param d: map from tuples to list of their anagrams
    """
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    t.sort(reverse=True)

    for x in t:
        print(x)


def filter_length(d, n):
    res = dict()
    for tp, word in d.items():
        if len(word) == n:
            res[tp] = word
    return res


if __name__ == '__main__':
    anagram_map = all_anagrams('words.txt')
    print_sorted_anagrams_sets(anagram_map)

    bingo_words = filter_length(anagram_map, 8)
    print_sorted_anagrams_sets(bingo_words)
