def right_justify(s):
    print((70-len(s))*' ' + s)


def main():
    s = input('Enter a string: ')
    right_justify(s)


if __name__ == '__main__':
    main()