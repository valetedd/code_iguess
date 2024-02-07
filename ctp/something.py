### Exercise x functions
# test function for the algorithm

def test_is_in_entry(first_word, second_word, bib_entry, expected):
    result = is_in_entry(first_word, second_word, bib_entry)
    if result == expected:
        return True
    else:
        return False

# function

def is_in_entry(first_word, second_word, bib_entry):
    result = 0
    if first_word in bib_entry:
        result += 1
    if second_word in bib_entry:
        result += 1
    return result 

## tests

# print(test_is_in_entry("murder", "horror", "Tagliaferri, L. (2018). How To Code in Python. ISBN: 978-0999773017", 0))
# print(test_is_in_entry("Code", "ananas", "Tagliaferri, L. (2018). How To Code in Python. ISBN: 978-0999773017", 1))
# print(test_is_in_entry("Python", "ISBN", "Tagliaferri, L. (2018). How To Code in Python. ISBN: 978-0999773017", 2))    

###########################################################################

### Exercises from book

from collections import deque


# Test function
def test_do_it(str, num, expected):
    result = do_it(str, num)
    if result == expected:
        return True
    else:
        return False
    
    
# Requested function
def do_it(str, num):
    vow_list = ["a","e", "i", "o", "u"]
    vow_num = 0
    vow_queue = deque()
    
    for i in str:
        if i in vow_list:
            vow_num += 1
            vow_queue.append(i)
        
    if vow_num < num:
        return "Oh no!"
    else:
        return vow_queue

## tests
# print(test_do_it("gaelician", 7, "Oh no!"))
# print(test_do_it("gaelician", 4, deque(["a", "e", "i", "i", "a"])))

#######################################################

### Ex. 2 loops

from collections import deque
    
def test_stack_from_list(input_list, expected):
    if stack_from_list(input_list) == expected:
        return True
    else:
        return False



def stack_from_list(input_list):
    output_stack = deque() 
    for item in input_list:
        output_stack.append(item)
    return output_stack
## tests
# print(test_stack_from_list(list(["a", "b", "c"]), deque(["c", "b", "a"])))
# print(test_stack_from_list(list(["a", "b", "c"]), deque(["a", "b", "c"])))   

##########################################################

### Ex. 3 loops

def test_my_enumerate(input_list, expected):
    if my_enumerate(input_list) == expected:
        return True
    else:
        return False

def my_enumerate(input_list):
    index_list = range(len(input_list))
    result = list()
    for item in index_list:
        result.append((item, input_list[item]))
    
    return result
## tests
# print(test_my_enumerate(list(["a", "b", "c",]), list([(0, "a"), (1, "b"), (2, "c")])))
# print(test_my_enumerate(list(["a", "b", "c",]), list([(0, "a"), (1, "b"), (2, "d")])))

############################################################

### Exercise 4 loops 

def test_my_range(stop_number, expected):
    if my_range(stop_number) == expected:
        return True
    else:
        return False

def my_range(stop_number):
    result = list()
    n = 0
    while n < stop_number:
        result.append(n)
        n += 1
    return result
## tests
# print(test_my_range(4, list([0, 1, 2, 3])))   
#  
##########################################

### Exercise 5 loops 

def test_my_reversed(input_list, expected):
    if my_reversed(input_list) == expected:
        return True
    else: 
        return False

def my_reversed(input_list):
    reversed_list = input_list[::-1]
    return reversed_list
## tests
# print(test_my_reversed(list([0, 1, 2, 3]), list([3, 2, 1, 0])))

###variant

def test_my_reversed(input_list, expected):
    if my_reversed(input_list) == expected:
        return True
    else: 
        return False

def my_reversed(input_list):
    rev_list = list()
    index_list = range(1, len(input_list) + 1)
    for i in index_list:
        rev_list.append(input_list[-i])


    
    return rev_list
##tests  
# print(test_my_reversed(list([]), list([])))

#############################################

###Leetcode ex (https://leetcode.com/problems/longest-substring-without-repeating-characters/)

def test_no_repetition_substring(string, expected):
    if no_repetition_substring(string) == expected:
        return True
    else:
        return False


def no_repetition_substring(string):
    pass
    


"""
#tests
print(test_no_repetition_substring(" ", 1))
print(test_no_repetition_substring("a", 1))
print(test_no_repetition_substring("abcdcp", 4))
print(test_no_repetition_substring("abcdefg", 7))
print(test_no_repetition_substring("frzfhjgpor", 8))
print(test_no_repetition_substring(" sptzu mp lw", 7))
print(test_no_repetition_substring("abcafgh", 6))
"""
#####################################
#Ex 1 Recursion

def test_exponentiation(base_number, exponent, expected):
    if exponentiation(base_number, exponent) == expected:
        return True
    else:
        return False

def exponentiation(base_number, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base_number
    else: 
        return base_number * exponentiation(base_number, exponent - 1)
    
"""
print(test_exponentiation(3, 4, 81))
print(test_exponentiation(17, 1, 17))
print(test_exponentiation(2, 0, 1))
"""
##########################################
# Ex 2 Recursion

def test_fib(n, expected):
    if fib(n) == expected:
        return True
    else: 
        return False

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
"""    
# tests
print(test_fib(1, 1))
print(test_fib(0, 0))
print(test_fib(2, 1))
print(test_fib(3, 2))
print(test_fib(4, 3))
print(test_fib(419, 1645645409178311156114050175340179094658577397657624573049761120640548215334513341070281))
"""
### Ex. 30A CTP Book ###

def test_odd11(y, expected):
    result = odd11(y)
    return result == expected

def odd11(y):
    if y % 2 != 0:
        y += 11
    y = y / 2
    if y % 2 != 0:
        y += 11
    T = 7 - (T % 7)
    return T

### Ex. 29A CTP Book ###

from random import randint
from itertools import permutations

def test_fy(s, exptected):
    result = fy(s)
    if result in exptected:
        return True
    else:
        return False


def fy(s):
    char_list = list(s)
    for i in range(len(char_list)-1):
        c = char_list[i]
        j = randint(i, len(char_list)-1)
        c, char_list[j] = char_list[j], c
    perm = "".join(char_list)
    return perm

    
### Ex. 28A CTP Book ###

def test_nearest(list_i, expected):
    result = nearest(list_i)
    return result == expected


def nearest(list_i):
    l_o = list()
    l_o.append(None)
    indexes = range(1, len(list_i))
    
    for idx in indexes:
        num = list_i[idx]
        smaller_exists = False
        rev_indexes = reversed(range(idx))
        for p_idx in rev_indexes:
            prev_num = list_i[p_idx]
            if prev_num < num:
                l_o.append(prev_num)
                smaller_exists = True
                break
        if smaller_exists == False:
            l_o.append(None)
    print(l_o)
    return l_o
"""                     
print(test_nearest([0, 8, 4, 12, 2, 10, 6, 14, 1], [None, 0, 0, 4, 0, 2, 2, 6, 0]))
print(test_nearest([], []))
print(test_nearest([7], [None]))
print(test_nearest([7, 3], [None, None]))
print(test_nearest([3, 7], [None, 3]))
print(test_nearest([0, 8, 4, 12, 2, 10, 6, 14, 1], [None, 0, 0, 4, 0, 2, 2, 6, 0]))
"""
### Ex. 28A CTP Book ###
from string import ascii_lowercase
from random import choice

def test_qgpm(s, t, expected):
    result = qgpm(s, t)
    return result == expected

def qgpm(s, t):
    s_set = set(s)
    t_set = set(t)
    Km = len(s_set.intersection(t_set))
    return (2 * Km) / (len(s) + len(t))

print(test_qgpm("ciao", "ciao", 1))
print(test_qgpm("mummy", "my", 4 / 7))
print(test_qgpm("m", "mummy", 2 / 6))