from ch11_worddict import make_word_dict
from ch8_rotated_word import rotated_word


def rorate_pairs(word, word_dict):
    for num in range(1, 14):
        rotated = rotated_word(word, num)
        if rotated in word_dict:
            print(word, num, rotated)


if __name__ == '__main__':
    word_dict = make_word_dict()

    for word in word_dict:
        rorate_pairs(word, word_dict)
