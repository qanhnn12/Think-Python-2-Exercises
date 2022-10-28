from ch12_anagram_sets import all_anagrams


def word_diff(word1, word2):
    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1
    return count


def metathesis_pairs(d):
    for anagrams in d.values():

        """word1 & word2 go through every string in each anagram list
        and return a pair of strings. It's a Cartesian product.
        Read more: https://www.w3schools.com/python/gloss_python_for_nested.asp"""

        for word1 in anagrams:
            for word2 in anagrams:

                """word1 < word2 avoids the case when word1 & word2 are the same string.
                If there are 2 differences between word1 & word2, they are metathesis_pairs"""

                if word1 < word2 and word_diff(word1, word2) == 2:
                    print(word1, word2)


if __name__ == '__main__':
    sets = all_anagrams('words.txt')
    metathesis_pairs(sets)
