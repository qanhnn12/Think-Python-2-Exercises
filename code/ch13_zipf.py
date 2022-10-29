import matplotlib.pyplot as plt
from ch13_analyze_book1 import read_file


def rank_freq(d):
    """
    Returns a list of (rank, freq) tuples
    :param d: map from word to frequency
    :return: list of (rank, freq) tuples
    """
    # sort the list of frequencies in decreasing order
    freqs = list(d.values())
    freqs.sort(reverse=True)

    # enumerate the ranks and frequencies
    rf = [(r + 1, f) for r, f in enumerate(freqs)]
    return rf


def print_ranks(d):
    """
    Prints the rank vs. frequency data
    :param d: map from word to frequency
    """
    for r, f in rank_freq(d):
        print(r, f)


def plot_ranks(hist, scale='log'):
    """
    Plot frequency vs. rank
    :param hist: map from word to frequency
    :param scale: string 'linear' or 'log'
    """
    t = rank_freq(hist)
    rs, fs = zip(*t)

    plt.close()
    plt.xscale(scale)
    plt.yscale(scale)
    plt.title('Zipf plot')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    plt.plot(rs, fs, 'r-', linewidth=3)
    plt.show()


def main(filename='emma.txt', flag='plot'):
    hist = read_file(filename, skip_header=True)

    # print the results or plot them
    if flag == 'print':
        print_ranks(hist)
    elif flag == 'plot':
        plot_ranks(hist)
    else:
        print('Usage: zipf.py filename [print|plot]')


if __name__ == '__main__':
    main()
