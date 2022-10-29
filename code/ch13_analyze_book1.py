import string


def read_file(filename, skip_header=False):
    """
    Creates a histogram that maps from each word to its frequency
    :param filename: string
    :param skip_header: boolean, whether to skip the Gutenberg header
    :return: dictionary
    """
    d = dict()
    data = open(filename, encoding='utf8')

    # skip the header
    if skip_header:
        for line in data:
            if line.startswith('*** START OF THE PROJECT'):
                break

    # read the file until it reaches this
    for line in data:
        if line.startswith('*** END OF THE PROJECT'):
            break

        # for each line in fin, replace hyphens with spaces
        line = line.replace('-', ' ')

        # for each word in the list, remove punctuation and whitespaces
        # and convert it to lowercase
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()

            # map from word to frequency:
            d[word] = d.get(word, 0) + 1

    return d


def total_words(d):
    """Returns the total of the frequencies in a histogram"""
    return sum(d.values())


def different_words(d):
    """Returns the number of different words in a histogram"""
    return len(d)


def common_words(d):
    """Approach 1
    Makes a list of word-freq pairs in descending order of frequency
    :param d: map from word to frequency
    :return: list of (frequency, word) pairs
    """
    common = []
    for word, freq in d.items():
        common.append((freq, word))
    common.sort(reverse=True)
    return common


def common_words_1(d):
    """Approach 2
    Makes a list of word-freq pairs in descending order of frequency
    :param d: map from word to frequency
    :return: list of (frequency, word) pairs
    """
    common = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return common


def subtract(d1, d2):
    """
    Returns a dictionary with all keys that appear in d1 but not in d2
    :param d1: dictionary
    :param d2: dictionary
    """
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res


def main():
    d = read_file('emma.txt', skip_header=True)
    print('Total number of words:', total_words(d))
    print('Number of different words:', different_words(d))

    t = common_words(d)
    print('10 most common words are:')
    for freq, word in t[:10]:
        print(word, freq, sep='\t')

    words = read_file('words.txt', skip_header=False)
    diff = subtract(d, words)
    print("Words in the book that aren't in the wordlist are:")
    for word in diff.keys():
        print(word, end=' ')


if __name__ == '__main__':
    main()
