import random
from bisect import bisect
from ch13_analyze_book1 import read_file
from ch12_most_frequent import histogram


def choose_from_hist(h):
    """
    Returns a random letter and its probability in a histogram
    :param h: map from letter to frequency
    """
    random_word = random.choice(list(h.keys()))
    probability = h[random_word] / sum(h.values())
    print(f"Random value is {random_word} and its probability "
          f"is {h[random_word]}/{sum(h.values())}, i.e.{probability}")


def random_word(d):
    words = []
    freqs = []
    total_freq = 0

    # make a list of words and a list of cumulative frequencies
    for word, freq in d.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)

    x = random.randint(0, total_freq-1)
    index = bisect(freqs, x)

    return words[index]


def main():
    d = read_file('emma.txt', skip_header=True)
    h = histogram(d)
    choose_from_hist(h)

    print("Here are some random words from the book:")
    for i in range(100):
        print(random_word(d), end=' ')


if __name__ == '__main__':
    main()
