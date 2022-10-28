def rotated_word(word, num):
    new_word = ''
    for letter in word:
        new_word = new_word + chr(ord(letter) + num)
    print(new_word)


if __name__ == '__main__':
    word = str(input("Enter a string: "))
    num = int(input("Enter a number: "))
    rotated_word(word, num)