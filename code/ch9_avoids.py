def avoids(word, forbids):
    for c in word:
        if c in forbids:
            return False
    return True


def words_no_avoids(filename):
    forbids = input('Enter a string of forbidden letters: ')
    fin = open(filename)
    count = 0
    for line in fin:
        word = line.strip()
        for c in word:
            if avoids(word, forbids):
                count += 1
    print("The number of words that don't contain any forbidden letters:", count)


if __name__ == '__main__':
    words_no_avoids('words.txt')