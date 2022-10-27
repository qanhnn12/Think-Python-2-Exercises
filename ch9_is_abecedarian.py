# Approach 1. Use for loop
def is_abecedarian_1(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True


# Approach 2. Use recursion
def is_abecedarian_2(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian_2(word[1:])


# Approach 3. Use while loop
def is_abecedarian_3(word):
    i = 0
    while i < len(word) - 1:
        if word[i + 1] < word[i]:
            return False
        i = i + 1
    return True


# Approach 4. Use for loop with the idea of while loop
def is_abecedarian_4(word):
    i = 0
    previous = word[i]
    for letter in word:
        if letter < previous:
            return False
        i = i + 1
    return True
