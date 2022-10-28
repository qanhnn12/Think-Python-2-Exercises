def palindrome_odometer():
    for i in range(100000, 1000000):
        if str(i)[2:6] == str(i)[5:1:-1]:                  # last 4 digits
            i += 1
            if str(i)[1:6] == str(i)[5:0:-1]:              # last 5 digits
                i += 1
                if str(i)[1:5] == str(i)[4:0:-1]:          # 4 middle digits
                    i += 1
                    if str(i) == str(i)[::-1]:             # all 6 digits
                        print(i-3)                         # i-3 because we have incremented i by 1 after each set of if statement


print('The following are the possible odometer readings:')
palindrome_odometer()