def is_palindrome(word):
    return word == word[::-1]


if __name__ == '__main__':
    print(is_palindrome('mom'))
    print(is_palindrome('bobby'))
    print(is_palindrome('noon'))
    print(is_palindrome('danger'))