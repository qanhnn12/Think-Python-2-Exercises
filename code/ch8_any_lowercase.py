def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


"""
print(any_lowercase1('Noon'))

This function only check whether the fist letter in the string is lowercase.        
In the case of 'Noon', there are 3 lowercase letters but the function returns False.
"""


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


"""
print(any_lowercase2('NOON'))

This function ALWAYS returns True.
It doesn't test each character c in the string s, but the lower string 'c' in 'c'.islower().
Wrapping ' ' outside True or False doesn't change anything.
In the case of 'NOON', all letters are uppercase but the function returns True.
"""


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


"""
print(any_lowercase3('nooN'))

This function only displays whether the last letter is lowercase.
In the case of 'nooN', the first 3 letters are lowercase but the function returns False.
"""


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


"""
print(any_lowercase4('noon'))
print(any_lowercase4('Noon'))
print(any_lowercase4('nooN'))
print(any_lowercase4('nOOn'))
print(any_lowercase4('NOON'))

This function is correct. flag is set to False by default.
When c.islower() is False, flag remains False (False OR False is False);
But when c.islower() is True, flag becomes True (False OR True is True),
and it remains True from then.
"""


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


"""
print(any_lowercase5('nooN'))

This function tests whether all letters are lowercase.
In the case of 'nooN', the first 3 letters pass the check and stay True.
The last letter meets the condition that 'not c.islower()',
therefore, the function returns False and terminates there.
"""


# Modify any_lowercase5(s) to return what we want:
def modify_any_lowercase5(s):
    for c in s:
        if c.islower():
            return True
    return False
