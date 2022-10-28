def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def most_frequent(s):
    h = histogram(s)
    t = []
    for letter, freq in h.items():
        t.append((freq, letter))

    t.sort(reverse=True)

    res = []
    for freq, letter in t:
        res.append(letter)

    return res


def read_file(filename):
    return open(filename).read()


if __name__ == '__main__':
    string = read_file('words.txt')
    letter_seq = most_frequent(string)
    for letter in letter_seq:
        print(letter)