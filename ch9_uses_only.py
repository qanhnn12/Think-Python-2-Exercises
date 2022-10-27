def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True


if __name__ == '__main__':
    available = input('Enter letters you want to create words: ')
    print('Words using only those letters are:')

    for line in open('words.txt'):
        word = line.strip()
        if uses_only(word, available):
            print(word)
