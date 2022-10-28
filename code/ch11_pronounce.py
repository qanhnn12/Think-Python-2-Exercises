def read_dictionary(filename='c06d.txt'):
    """
    Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the key
    for the second pronunciation of "abdominal" is "abdominal(2)".

    :param filename: string
    :return: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == "#":
            continue

        # split each line to a list of separate strings
        t = line.split()

        # turn the first string in the list to lowercase
        word = t[0].lower()

        # merge t[1:] items in the list and separate them by a space
        pron = ' '.join(t[1:])

        d[word] = pron

    return d


if __name__ == '__main__':
    d = read_dictionary('c06d.txt')
    for word, pron in d.items():
        print(word, pron)