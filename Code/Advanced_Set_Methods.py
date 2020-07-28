'''
#Test
name = "Madhu"
num = 17
ans = True

if num == 17 and name == "Madhu":
    print("Hello")

#Loops
for i in range(1,11,2):
    print(i) #Prints 1,3,5,7,9

print()

for c in name:
    print(c) #Prints each character in the string

print()

for i in range (1,5):
    for c in name:
        print(c) #Prints each character in the string (5-1=4) times

lst = ["Green", "Blue", "Red"]
print(lst)

lst = ["Red",32,True,0.02]
#indexing in list
print(lst[1])
print(lst[-1])

lst.append("Pink") #Adds to the end of the list
lst.insert(2,"yellow") #Index where you want to insert the element and pushes the rest of the list forward one
lst.pop() #Deletes the last element
lst.remove("Red") #Removes a specific part of the element that matches the parameter

#in-place sorting
#lst.sort() #only works if the datatype is consistent in the list.
#Sorting - Arranging the elemenets in ascending or decending mannr
print(lst)

lst = [0]*10 # [0,0,0,0,0,0,0,0,0,0]
lst2 = [1]*10 # [1,1,1,1,1,1,1,1,1,1]
lst = lst + lst2 #merges the lists together
print(lst)

#slicing
print(lst[0:4]) #1,2,3,4,5,6 --> 1,2,3,4
print(lst[::2]) #retrieves every second element from the list

lst2 = lst #Shallow copy. That means that the lst object present in the memory is only one but has 2 references to it
#Any change made to lst2 is made to lst also
print (lst2)
lst2.pop()
print(lst2)
print(lst) #Same as lst2

lst2 = lst.copy()#Copy will create a duplicate instance of the list object
lst2 = list(lst) #List function and in the parthenthesis put in the list object which you want to be copied
lst2 = lst[:] #slicing --> Get all the elements of the lst and store it in a new list.

a = [1,2,3,4,5,6]
b = [i + 3 for i in a]
print(b)

tup = ()
tuple_ex = "Hello",32,"Dog"
print(tuple_ex)

a = (2,3,4,5,6,7,7,8,1,9,9)
#count
print(a.count(9))

#reverse tup[le
print(a[::-1])

#example of unpacking
tuple_unpack = "Madhu", "Pycharm", "Python"
name,editor,language = tuple_unpack
print(name)
print(editor)
print(language)

#Difference between list and tuples
import sys
lst = [2,3,4,"Hello"]
tup = (2,3,4,"Hello")
print(sys.getsizeof(lst),bytes) #Figure out why tuple smaller than list
print(sys.getsizeof(tup),bytes)

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number = 100000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number = 100000))


def findNumbers(nums):
    count = 0
    for num in nums:
        if (len(str(num)) % 2 ==0):
            count +=1
    return count


lst = [2234,234,231,32,1235125,23123,4512]
print(findNumbers(lst))


def containsDuplicate(nums):
    for i in range(len(nums)):
        for k in range(i+1,len(nums)):
            print(nums[i], ",", nums[k])
            if (nums[i] == nums[k]):
                return True
    return False

print(containsDuplicate([1,2,3,4,5,6,7]))
'''
'''
dict = {"Green": 2, "Blue": 3, "Yellow": 4}
#Accessing the value
print(dict["Green"])
print(dict.pop("Blue"))
#print(dict.popItem())
print()
#Iterate in a dictionary
for key in dict.keys(): #keys will have the list of keys
    print(key)
    print(dict[key])
print()
for val in dict.values(): #values --> List of values
    print(val)
print()
for item in dict.items(): #items --> list of key value paris
    print(item)

print()
dict_1 = {"color":"Blue","Age":24}
dict_2 = {"Name":"John"}
dict_1.update(dict_2) #Adds onto the implicit parameter
print(dict_1)
'''
'''
def moveZeros(lst):
    zeroCount = 0
    for i in range(len(lst)-1,0,-1):
        print(lst[i])
        if lst[i] == 0:
            zeroCount+=1
            lst.pop(i)

    lst = lst + [0] * zeroCount
    return lst

print(moveZeros([3,0,4,0,0,9,2]))
'''

'''
def firstUniqChar(s):
    str = list(s)
    for i in range(0,len(str)):
        check = False
        for k in range(i+1,len(str)):
            if (str[i]==str[k]):
                check = True
        if (not check):
            return i
    return -1

print(firstUniqChar("abcabd"))
'''
'''
def firstUniqCharDictionary(s):
    dictc = {}
    for c in s:
        if c in dictc:
            x = dictc[c]+1
            dictc[c]=x
        else:
            dictc[c]=1
    count = 0
    for i in s:
        if dictc[i] == 1:
            return count
        count +=1
    return -1

print(firstUniqCharDictionary("abccabd"))


#Dictionaries and sets they work on the concept of hashing. for hashing to work you need to have a static object or an
#object which is not going to mutate
#Sets - Unordered,Mutable, No duplicates
set_ex = set()
empty_set = {}
print(type(set_ex)) #dictionary --> class R
lst = [1,2,3,1,4,4,2]
#set_ex = {[1,2,4,4,3,1,2]} #set_ex = 1,2,3,4 #not going to work
set_ex = set(lst)
set_ex = set("Hello") # --> H,e,l,o

#Add elements in set:
set_ex.add(9)

#Iterate in a set
for i in set_ex:
    print(i)

#Check if element is existing in the set
if 2 in set_ex:
    print("Yes")
else:
    print("No")

#Union, Intersection,Difference
even = {2,4,6,5,8}
odd = {1,3,5,9}
union_sums = odd.union(even) #Give me a set containing all the unique elements from set odd and set even
intersect = odd.intersection(even) #5

#Difference
setA = {1,2,3,4,5,6,7,8,9}
setB = {3,4,5,6,7,8,13,14}
diff = setA.difference(setB) #Set diff is going to contain all the elements which present in setA but not in setB

#get unique elements from both of the sets:
elms = setA.symmetric_difference(setB)
setA.update(setB)#Add elements from setB not present in setA
setA.intersection_update(setB)#elements only present in both sets
setA.difference_update(setB)#removes elements from setA present in setB
print(setA.issubset(setB))#Checks if setA is subset of setB
print(setA.issuperset(setB))#Checks if setA is superset of setB
print(setA.isdisjoint(setB))#If no common elements in them
'''
def gcdOfStrings(str1, str2):
    s = ""
    gcd = ""
    for c in str1:
        s = s+c
        if len(s)>len(str2):
            break
        print(s*int(round(len(str1)/len(s))))
        print(s*int(round(len(str2)/len(s))))
        if s*int(round(len(str1)/len(s)))==str1 and s*int(round(len(str2)/len(s)))==str2:
            gcd = s
    return gcd

print(gcdOfStrings("ababab","ab"))