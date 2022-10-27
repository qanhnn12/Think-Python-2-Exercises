from ch9_uses_only import uses_only


# Approach 1:
def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True


# Approach 2:
def uses_all_1(word, required):
    return uses_only(required, word)


if __name__ == '__main__':
    required = input('Enter required letters: ')
    count = 0
    for line in open('words.txt'):
        word = line.strip()
        if uses_all(word, required):
            count += 1
    print('Words containing required letters:', count)
