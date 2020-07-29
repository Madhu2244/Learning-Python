'''from itertools import product
a = [2,3]
b = [4,8]
prod = product(a,b) #gives the caresign product
print(list(prod))
# 2 is 4, 2 is 8 and 3 is 4, 3 is 8

from itertools import permutations
lst = [1,2,3]
perm = permutations(lst) #Gives all the possible permutations
print(list(perm))
perm = permutations(lst,2) #permutations of length 2
print(list(perm))

from itertools import combinations
lst = [1,2,3]
com = combinations(lst,2)
print(list(com))
''''''
from itertools import accumulate
lst = [1,2,5,3,4]
acc = accumulate(lst)
print(list(acc))
import operator
acc = accumulate(lst, func=operator.mul) #multiply by previous
print(list(acc))
acc = accumulate(lst, func=max) #max
print(list(acc))

from itertools import groupby
def greater_than(x):
    if x > 5:
        return True
    else:
        return False

lst = [4,3,9,12,5,13]
grp = groupby(lst,key=greater_than)
grp = groupby(lst, key = lambda x: x > 5) #same as previous line
print(grp)
for key, value in grp:
    print(key, list(value))

#infinite iterators
from itertools import count, repeat, cycle

for i in count(10):
    print(i)
    if i ==25:
        break
a = [1,2,3]
count = 0

for i in cycle(a):
   count +=1
   print(i)
   if count == 12:
       break

for i in repeat(a,4):
    print(i)
'''
from itertools import count, repeat, cycle
def sortString(s):
    maxVal = 0
    output = ""
    count = 0
    new_str = s
    for char in cycle(s):
        if ord(char) > maxVal:
            output += char
            maxVal = ord(char)
            new_str = new_str[:count] + new_str[(count+1):]
        count+=1
        if (count > len(s)):
            break
    print(new_str)
    newer_str = ''.join(sorted(new_str, reverse = True))
    print(newer_str)
    maxVal = maxVal + 1
    last_str = newer_str
    print(new_str)
    count = 0
    for char in cycle(newer_str):
        print(ord(char))
        if ord(char) < maxVal:

            output += char
            maxVal = ord(char)
            last_str = last_str[:count] + last_str[(count + 1):]
            print(maxVal)
        count += 1
        if (count > len(newer_str)):
            break
    print(last_str)
    print(output)
    if (len(output) > len(s)):
        sortString(s)
    return output

def sortStrings(s):
    s = list(s)
    result = ''
    while s:
        for letter in sorted(set(s)):
            s.remove(letter)
            result += letter
        for letter in sorted(set(s), reverse=True):
            s.remove(letter)
            result += letter
    return result
print(sortStrings("aaaabbbbcccc"))