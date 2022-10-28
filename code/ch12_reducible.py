def make_word_dict():
    """
    Creates a dictionary and add "i", "a" and empty string to it.
    :return: dictionary
    """
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None
    for c in ["", "i", "a"]:
        d[c] = c
    return d


def children(word, word_dict):
    """
    Returns a list of words in the dictionary that can be formed
    by removing one letter from the specified word.

    :param word: string
    :param word_dict: dictionary
    :return: list of strings
    """
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i + 1:]
        if child in word_dict:
            res.append(child)
    return res


"""memo is a dictionary that maps from each word that is known
to be reducible to a list of its reducible children. It starts
with the empty string."""

memo = {}
memo[''] = ['']


def is_reducible(word, word_dict):
    """
    If a word is reducible, returns a list of its reducible children.
    Also, adds an entry to the memo dictionary.

    A string is reducible only when it has at least one child that is
    reducible. The empty string is also reducible.

    :param word: string
    :param word_dict: dictionary with words as keys
    :return: list of reducible words
    """
    # if it has already checked this word, return the answer
    if word in memo:
        return memo[word]

    # check each of the children and make a list of the reducible ones
    res = []
    for child in children(word, word_dict):
        if is_reducible(child, word_dict):
            res.append(child)

    # memoize and return the result
    memo[word] = res
    return res


def all_reducible(word_dict):
    """
    Checks all words in the word_dict.
    Returns a list of their reducible ones.
    :param word_dict: dictionary with words as keys
    """
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res


def print_trail(word):
    """
    Prints the sequence of words that reduces a word to the empty string.
    If there is more than one choice, it chooses the first.
    :param word: string
    :return: string
    """
    if len(word) == 0:
        return
    print(word, end=' ')
    t = is_reducible(word, word_dict)

    # in is_reducible(), each time a child is appended to res, it is at last
    # we only want to take the "mother", therefore t[0]
    print_trail(t[0])


def print_longest_words(word_dict):
    """
    Finds the longest reducible words and prints them.
    :param word_dict: dictionary of valid words
    :returns: strings
    """
    words = all_reducible(word_dict)

    # use DSU to sort by word length
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    # print the longest 5 words
    for length, word in t[0:5]:
        print_trail(word)
        print('\n')


if __name__ == '__main__':
    word_dict = make_word_dict()
    print_longest_words(word_dict)
