from ch11_pronounce import read_dictionary
from ch11_worddict import make_word_dict


def homophones(a, b, phonetic):
    """
    Checks if two words can be pronounced the same way.
    If either word is not in the pronouncing dictionary, return False.

    :param a: string
    :param b: string
    :param phonetic: map from words to pronunciation codes
    :return: boolean
    """
    if a not in phonetic or b not in phonetic:
        return False
    return phonetic[a] == phonetic[b]


def check_word(word, word_dict, phonetic):
    """
    Checks to see if the word has the following property:
    removing the first letter yields a word with the same
    pronunciation, and removing the second letter yields
    a word with the same pronunciation.

    :param word: string
    :param word_dict: dictionary with words as keys
    :param phonetic: map from words to pronunciation codes
    :return: boolean
    """
    word1 = word[1:]
    if word1 not in word_dict:
        return False
    if not homophones(word, word1, phonetic):
        return False

    word2 = word[0] + word[2:]
    if word2 not in word_dict:
        return False
    if not homophones(word, word2, phonetic):
        return False

    return True


if __name__ == '__main__':
    phonetic = read_dictionary()
    word_dict = make_word_dict()

    for word in word_dict:
        if check_word(word, word_dict, phonetic):
            print(word, word[1:], word[0] + word[2:])
