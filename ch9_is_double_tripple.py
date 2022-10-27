def is_double_triple(word):
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            i += 1
            count = 0
    return False


def find_triple_double(filename):
    fin = open(filename)
    for line in fin:
        word = line.strip()
        if is_double_triple(word):
            print(word)


if __name__ == '__main__':
    print('Words in the list that have three consecutive double letters:')
    find_triple_double('words.txt')