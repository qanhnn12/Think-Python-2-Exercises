from ch13_analyze_book1 import read_file


def subtract(d1, d2):
    """
    Returns a set of all keys that appear in d1 but not in d2
    :param d1, dictionary
    :param d2: dictionary
    """
    return set(d1) - set(d2)


def main():
    hist = read_file('emma.txt', skip_header=True)
    words = read_file('words.txt', skip_header=False)
    diff = subtract(hist, words)
    print("Words in the book that aren't in the wordlist are:")
    for word in diff:
        print(word, end=' ')


if __name__ == '__main__':
    main()
