#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 09:52:46 2020

@author: stephen
"""

# =============================================================================
# [1] Carry out basic mathematic operations using python
# =============================================================================
#%%
# [i]    addition
(2 + 2) * 2

# [ii]  subtraction
5 - 1

# [iii] multiplication
2 * 2

# [iv]  division
10 / 5

# [v]   exponent
2 ** 2

#%%

# =============================================================================
# [2] Assign and update a variable
# =============================================================================

# [i]    Assign a value to a variable
x = 2

# [ii]   Print that variable 
print(x)

# [iii]  Update that variable to make it a new value
x = x + 1

# [iv]   Print the variable to see if it updated
print(x)


x += 1
print(x)
#%%

# =============================================================================
# [3] Working with strings
# =============================================================================

# [i]   Assign your name, in string format, to an aptly named variable
name = 'Stephen'

# [ii]  Check to see that the value in your variable is a string
type(name)


# [iii] Change all of the characters in the variable to lower case
name.lower()

# [iv]  Use f strings to create a message which includes your name variable
print(f'Hello, {name}, welcome to python')

# [v]   Create a string of ten numbers separated by commas
my_numbers = '1,2,4,5,6,3,8,10,3,2'

#%%
# =============================================================================
#  [4] Working with lists
# =============================================================================

# [i]   Take the string you created in [3][v] and turn it into a list
my_list = my_numbers.split(',')
my_list
# [ii]  Get the value of the third item in the list
my_list[2]

# [iii] Get the same value but use negative indexing
my_list[-8]

# [iv]  Get the first two items in the list using slice notation
my_list
my_list[0:2]

# [v]   Get every second item from the list
my_list[1::2]

# [vi]  Update item at index 5 to a new value
my_list[5] = '7'
my_list
# [vii] Update item at index 6 to a new value which is the sum of
#       the value of item index 2 and item index 3 together

my_list[6] = str((int(my_list[2]) + int(my_list[3])))
my_list
# [viii] Add a new value to the end of the list
my_list.append('6')
my_list
# [ix]  Delete the value at item index 5
del my_list[5]

#%%

# =============================================================================
# [5] Working with dictionaries
# =============================================================================

# [i]   Create a dictionary with two keys, have the first key contain
#       a list of integers and the second key contain a list of strings
my_dict = {'ints':[1,2,3,4,5], 'strings':['2','2','3','4','1']}
# [ii]  Print out only the second keys values
my_dict['strings']

# [iii] Get the value of the first item in the first keys values
my_dict['ints'][0]

#%%
# =============================================================================
#  [6] Conditional statements
# =============================================================================
#Recall the boolean True False table
'''
True and True == True				True or True == True
True and False == False				True or False == True
False and True == False				False or True == True
False and False == False			False or False == False
'''




x = 100
y = 200

# [i]   Does x equal y
x == y

# [ii]  Does either x or y equal 200
(x == 200) or (y == 200)

# [iii] Does x and y equal 50
(x == 100) and (y == 50)

# [iv]  Does half of y equal x?
(y /  2 == x)

#[v]    Does half of y equal x and does double x equal y
(y / 2 == x) and (x * 2 == y)

#%%
# =============================================================================
#  [7]  For loops
# =============================================================================

# [i]   Create a for loop which loops over the list you created in [3][v]
#       and prints each item into a f string.
my_list

for number in my_list:
    print(f"This number is {number}")


#%%


# [ii]  Create a for loop which will only print the value of the item
#       in the list if it is greater than or equal to the last item in the list

for i in my_list:
    if int(i) >= int(my_list[-2]): #only runs if True
        print(f'{i} is greater than or equal to {my_list[-1]}')  
    else:
        print(f'{i} is not greater than or equal to {my_list[-1]}')

#%%
# [iii] Create a for loop which will loop over your list and append each item to
#       a new list
new_list= []

for i in my_list:
    new_list.append(i)

print(new_list)
print(my_list)
#%%

# =============================================================================
#  [8] Create a function
# =============================================================================

# [i] Create a function which asks for the users details and returns a dictionary
#     with the keys 'Name', 'Date of birth', and 'Nationality'.
#     Assign the output to a variable.

def personal_details():
    name = input("Please enter your name: ")
    dob = input("Please enter your date of birth: ")
    nationality = input("Please enter your nationality: ")
    return {'Name':name, 'Date of birth':dob, 'Nationality':nationality}

stephen_details = personal_details()


#%%