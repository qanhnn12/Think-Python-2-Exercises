from ch6_palindrome import first, middle, last


def is_palindrome(word):
    if len(word) < 2:
        return True
    elif first(word) != last(word):
        return False
    else:
        return is_palindrome(middle(word))


if __name__ == '__main__':
    print(is_palindrome('mom'))
    print(is_palindrome('bobby'))
    print(is_palindrome('noon'))
    print(is_palindrome('danger'))
