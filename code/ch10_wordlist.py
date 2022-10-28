# Approach 1: Use append method
import time
def word_list_1():
    fin = open('words.txt')
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


# Approach 2: Use the idiom t = t + [x]
def word_list_2():
    fin = open('words.txt')
    t = []
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t


start_time1 = time.time()
t1 = word_list_1()
elapsed_time1 = time.time() - start_time1

print(len(t1))
print(t1[:20])
print(elapsed_time1, 'seconds')
# runtime = 0.0628809928894043 seconds


start_time2 = time.time()
t2 = word_list_2()
elapsed_time2 = time.time() - start_time2

print(len(t2))
print(t2[:20])
print(elapsed_time2, 'seconds')
# runtime = 155.08912873268127 seconds

"""
The + operator creates a new list by concatenating the original list t with a new list [word],
then copy all the elements from the original lists to the freshly allocated list. => Longer
.append() only modifies the existing list by adding a new element to it. => Less time
