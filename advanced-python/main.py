# Importing required packages
from aux_functions import tricks
#otherwise if it was same directory, you just put 'import tricks'


#function without arguments
def print_greeting():
    print('Hello there')

#function with arguments
def print_greeting(name, var, is_person=True):
    print('Hello there, ' + name)
    print(var)
    print(is_person)

def main():
    var = 100
    # there are 3 parameters in print_greeting, but we are calling 2. still works bc is_person predef
    print_greeting('Madhu', var)
    print()
    # can edit the value of is_person and other variables
    print_greeting('Madhu', var=20, is_person=False)
    tricks.do_a_trick()
    tricks.list_compreshension()
    tricks.slicing_arrays()
    tricks.join_ar()
    tricks.string_format()
    tricks.try_enum()
    tricks.test_map()
    tricks.test_zip()
    tricks.test_assert()
if __name__ == '__main__':
    # do something
    # anything definied here is a global variable.
    # if we were to do this same thing in another function,
    # we would get an error because that variable isn't global
    main() #just having main() is useful bc prevents any global var issues, no other code
