def read_word():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)


if __name__ == '__main__':
    read_word()

