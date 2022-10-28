def has_no_e(word):
    for i in word:
        if i == 'e':
            return False
    return True


def pct_no_e(filename):
    fin = open(filename)
    total = 0
    no_e_count = 0

    for line in fin:
        word = line.strip()
        total += 1
        if has_no_e(word):      # or use: if 'e' not in word
            print(word)
            no_e_count += 1

    no_e_pct = no_e_count / total * 100
    print(no_e_pct, 'percent of words in the list that have no “e”.')


if __name__ == '__main__':
    pct_no_e('words.txt')