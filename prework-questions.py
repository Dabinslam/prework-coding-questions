#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    print("hello_" + user_name + "!")
#hello_name(input())

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    x = 1
    r = range(49)
    for n in r:
        x = x + 2
        print(x)
#first_odds()

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    x = max(a_list)
    return x
#print(max_num_in_list([50,51,42,34,4351]))

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
#The return should be boolean Type (true/false)
def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    elif a_year % 100 == 0 and a_year % 4 == 0: 
        return False
    elif a_year % 4 == 0:
        return True
    else: 
        return False
#print(is_leap_year(506))

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    test_list = []
    x = min(a_list)
    for i in a_list:
        test_list.append(x)
        x = x + 1
    if test_list == a_list:
        return True
    else:
        return False
#print(is_consecutive([3,2,5,4]))