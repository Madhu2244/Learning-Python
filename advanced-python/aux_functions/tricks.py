import main

def do_a_trick():
    print('here\'s magic trick')

def list_compreshension():
    #naive way to create 0 to 9 array
    ar = []
    for i in range(10):
        ar.append(i)
    print(ar)

    # brackes mean its an array
    # theres a for loop inside.
    # the i on the outside is what you are putting into the array in every iteration
    ar = [i for i in range(10)]

def slicing_arrays():
    ar = [z for z in range(5)] #0,1,2,3,4

    #naive way to get indexes 0-2
    output = []
    for i in range(0,3,1): #[0,3), increment 1
        output.append(i)
    print(output)

    #python way to get indexes 0 to 2. start at 0, "stop at the index before 3"
    print(ar[0:3])
    print(ar[:3])

    #get the last 2 elements naive
    output = []
    for i in range(3,5,1):
        output.append(i)
    print(output)

    #python way to get last 2 elements. -1 means last element, -2 is second last element, etc.
    print(ar[-2:])
    print(ar[-1])

def join_ar():
    ar = [hello for hello in range(5)] #0,1,2,3,4

    #printing array without autoformatting in a naive way
    for i in range(len(ar)):
        if i < len(ar) - 1:
            print(ar[i], end=' ')
        else:
            print(ar[i], end='\n')

    #non naive way to print array wo autoformatting
    print('-'.join([str(element) for element in ar])) #.join is expecting a string, not an int array
    print(type(ar)) #you cant cast a list to a string
    print(type(ar[0]))  # you cant cast a list to a string
    print(type(str(ar)))

def string_format():
    name = 'Madhu'
    school = 'UCI'
    print (name + ' goes to ' + school + ' for college') #its very redundant to keep doing + and ' ' stuff
    #string formatting
    print('{} goes to {} for college'.format(name, school))

def try_enum():
    ar = ['Madhu', 'Kevin', 'Shrey']
    #index
    for i in range(len(ar)):
        print(ar[i])

    #enhanced for loop
    for element in ar:
        print(element)
        #you cant do el = 'asefasdf', you dont have the index to change it.

    for i, el in enumerate(ar):
        print(i)
        print(el)
        if el == 'Madhu':
            ar[i] = 'Madhu is cool'
    print(ar)

def test_map():
    ar = ['234','296', '923'] # cant do math with these numbers bc they are strings
    output = []
    for el in ar:
        output.append(int(el))
    print(output)
    output = [int(el) for el in ar]

    output_map = map(int, ar)
    print (output_map) #prints memeory address of output

    output = list(map(int,ar))
    print(output)

    ar = ['234', '296', '923']
    ar = list(map(int,ar))
    #lets say you had to square every number and add 10
    #naive way:
    output = []
    for num in ar:
        output.append(num * num + 10)
    print(output)

    #using lambdas
    output = list(map(lambda x: x * x + 10, ar)) #you use lambdas when you wanna apply a function onto everything
    #for every element in x, we are going to reaplce it with x * x + 10, and we want to apply this to array ar
    print(output)

def test_zip():
    names = ['Madhu', 'Kevin', 'Shrey']
    midterm_grade = [66, 99, 100]
    age = [17, 15, 19]
    #student = [('Madhu', 66), ('Kevin', 99), etc etc]

    #list = [a,a,a,a]
    #tuple = () it holds pairs
    #apple = (red,shiny,round)

    students = []
    assert len(names) == len(midterm_grade)
    for i in range (len(names)):
        students.append((names[i],midterm_grade[i]))
    print(students)

    students = list(zip(names,midterm_grade,age))
    print(students)

def test_assert():
    names = ['Madhu', 'Kevin', 'Shrey']
    midterm_grade = [66, 99, 100]
    age = [17, 15]
    #length of age is diff
    assert len(names) == len(midterm_grade) == len(age), 'length of names, midterm_grade, and age must be the same.'
    students = list(zip(names, midterm_grade, age))
    print(students) # prints [('Madhu', 66, 17), ('Kevin', 99, 15)]
                    # (ignores the last person because age length is 1 less.


if __name__ == '__main__':
    main.main()
