from ch12_anagram_sets import all_anagrams, signature
import shelve


def store_anagrams(filename, anagram_map):
    """
    Stores the anagrams from a dictionary in a shelf
    :param filename: string filename of shelf
    :param anagram_map: dictionary that maps from strings to list of anagrams
    """
    shelf = shelve.open(filename, 'c')

    for word, word_list in anagram_map.items():
        shelf[word] = word_list

    shelf.close()


def read_anagrams(filename, word):
    """
    Looks up a word in a shelf and returns a list of its anagrams
    :param filename: string filename
    :param word: word to look up
    :return: list of anagrams
    """
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []


def main(command='make_db'):
    if command == 'make_db':
        anagram_map = all_anagrams('words.txt')
        store_anagrams('anagram.db', anagram_map)
    else:
        print(read_anagrams('anagrams.db', command))


if __name__ == '__main__':
    main(command='make_db')