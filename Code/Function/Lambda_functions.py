# Lambda arguments : expression

# We need lambda functions
# Example: If you want to change the behavior of all the elements of a list using a function, but you feel like the
# function will not have any further use once it has changed the behavior of the elements
# Lambda just reduces the lines of code you have, if you are using a function once, use lambda
# Takes up less memory because less lines of code to execute
import math

def add_10(c):
    c = c + 10
    return c

add10 = lambda x: x + 10
print(add10(5))

mult = lambda x,y: x * y
print(mult(7,2))

points = [(1,2), (4,1), (3,5), (10,4)]
points_Sort = sorted(points, key = lambda x : math.pow(abs(x[0]-x[1]),2))
print(points_Sort)

#map(function,sequence)
a = [1,2,3,4,5]
b = map(lambda x : x*2,a)
print (a)
print (list(b))

c = [x*2 for x in a]
print (list(c))

#filter(function, sequence)
b = filter(lambda x : x % 2 != 0, a)
b = [x for x in a if x % 2 != 0]

#reduce(function,sequence)
from functools import reduce
a = [1,2,3,4,5]
b = reduce(lambda x, y: x/y, a)
print(b)
