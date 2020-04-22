

# Python basics

## Anaconda and the Spyder IDE

Open Anaconda and launch Spyder, this is the IDE for Python which comes with Anaconda.


It will look something like this :

![Spyder IDE overview](https://github.com/Genomics-CRT/images/blob/master/SpyderIDE2.png)

I have labelled a few of the important areas in the IDE.

1. Is what is called your working directory, this is where any files you are working with should be stored and it is also where the code you write will be saved on your computer.

2. Is our editor, this is where we write our scripts

3. Is called the console, you can write code here line by line and see the output straight away. 
   This is also where the output from our long scripts will show when we run them. If you ever get stuck in some code and want to exit it. Go to the console and press ctrl+c.

If you want to run the whole script you have written in the editor, press F5.
If you want to run a single code line or a highlighted portion of lines, press F9
When writing code which spans multiple lines, such as for loops,  it can be useful to create code cells.
In Spyder you do this by prefacing the code cell with `#%%` and ending it with the same.
To run a code cell that you are currently in, press ctrl+enter.

When following these tutorials please have Spyder open and type the code in as you are reading it, it will help you learn and get used to using Spyder.

## Resources to help with coding

A large part of your time spent coding will be reading through package documentation and on websites which specialise in solving coding problems. The main websites which you should search when you encounter a problem are www.stackoverflow.com and www.biostars.com .

So a google search would be something like "stackoverflow how to sort a list in python".

## Operators

Python uses the same calculation operators as R. 

`+  - * / **` which is addition, subtraction, multiplication, division, and exponent.

You can try these out by typing code into the editor and pressing F9 to run the line, you will see the answer show up in the console.

## Variables

Variables are a way to store values for use later in your code. 

This can be done using the `=` key, for example:

`x = 10`

Will assign 10 to the variable x

Now if you want to see what is saved inside a variable you can print it to the console
`print(x)`

You should always choose a variable name which is related to the value inside the variable. e.g. if you are storing a persons name inside a variable do not call the variable “age”.
Never create a variable which has the same name as a function. For example, never do this:

`list = [1, 2, 3, 4, 5]`

We can combine variable with operators to do things such as:

`x + 5`

This will give the answer 15

We can also update our variable as needed such as:

`x = x + 5`

x will now equal 15, this type of updating variables is very useful as you will see later on.

Python variable naming convention states that the words in variables are lowercase and separated by an underscore e.g. :
`gene_name = 'BRCA1'`

There are two types of variables in python, global and local.
A global variable is one that is defined outside of functions. Global variables can be recalled from anywhere, in the local or the global space. Local variables can only be recalled within the local space where it was created, such as a function. This will be explained in more detail later when we come to using local space.

## Comments

Comments can be added to your python code by placing `#` before what you type.  
It is good practice to comment your code so that others, and yourself, can understand what your thought process was when you were writing the code. This allows easy understanding, and editing, of the code in the future. 
When you run your script python will ignore anything you type after the `#`.


## Data types

The type of data you are dealing with will influence which functions or methods you can use on it
You can use the `type()` function to check what data type you are dealing with e.g.

```
x = 5
type(x)
```

### Numeric

This includes integers and floats.  
Integers are numbers without a decimal point whereas floats have a decimal point.

### String

This is any character or group of characters which are surrounded by quotes.

### Boolean

Also known as logical, this includes the `True` and `False` boolean values. You can use `==`
to test for equivalence in python. Please note the capital T and F, python is a case sensitive language.

Try this code out to see how True and False works.

```python
x = 5 
x == 5

y = 10
y == 11
```

This is what the boolean truth table looks like, it wil be useful to refer back to this when you deal with conditional statements later.

```python
True and True == True				True or True == True
True and False == False				True or False == True
False and True == False				False or True == True
False and False == False			False or False == False
```



### Sequence

Any data type which can store collections of data, this includes Strings, Lists, Tuples, and Dictionaries

## Parenthesis, brackets, curly brackets

All code which contains an opening `(`  `[` or `{` must be accompanied by a closing `)` `]` `}`
It is very common for errors in code to be the result of not enclosing code correctly. 

## Indentation in Python

Other programming languages(such as R) rely on using `{` to break up code blocks, Python uses indentation. This causes uniformity between all python coders which makes reading and understanding other peoples work much easier.

Indentation can be a tab character or four spaces. The image below gives an example of this. Everything which is indented will be run as part of the for loop command, even if those commands have nothing to do with the list which is being looped over (more on for loops later), because they are in the same code block caused by the indentation.

The final print command at the bottom of the code will only be printed once because it is not indented into the same group (code block) as the others. 

![Indentation](https://github.com/Genomics-CRT/images/blob/master/Indentation.png)



# Strings, Lists, Tuples, Dictionaries, Functions, For Loops, While loops.


## Strings
Strings are simply characters surrounded by `'` or `"` quotes
For example, `my_string = 'This is a string'`.
The `print()` function can be used to show the output of strings.

Strings can be joined together using the `+` operator, this is known as concatenation. 

```python
print(my_string + " which I made longer")
```

You can change the string to upper or lower case using the `.upper()` or `.lower()` methods
`my_string.upper()` will output `THIS IS A STRING`You can check what data type a variable is by using the type function 

The .replace() method will change a subset of your string to another string which you specify

```python
your_string = my_string.replace('This', 'That')
```



`type(my_string)` will return `str`

Any character can be a string, this include digits.

`type('8')` will return `str`

What would happen if you typed this?:
`print(‘8’ + ‘8’)`

This can be overcome by using the `int()` function which converts string digits into integers.

`print(int(‘8’) + int(‘8’))`

When working with strings in python it is best practice to use what are called formatted string literals, more simply known as f strings.

f strings allow easy and readable formatting of strings. 

```python
date = "02/04/20"
experiment_number = 17
result17 = "Success"

print(f'Experiment {experiment_number} which was carried out on {date} was a {result17}')
```
f strings also allows you to do calculations, function calls, methods etc. within a string

`print(f'The answer to 50 * 275 is {50*275}')`
`print(f'There is no need to shout {my_string.upper()}')`

We can use the same variable as many times as needed when printing f strings.

```python
new_line = '\n'
print(f"A {new_line} new line {new_line} any {new_line} time we want{new_line} one")
```



# Tuples and Lists

You can store more than just one value in a variable in python by using sequence data types such as tuples or lists. Unlike strings which can only hold one type of data, lists and tuples can contain any type of data. You can have integers, floats, strings, other lists or tuples all in the same variable.

Tuples are created by using `( )` e.g. `my_tuple = (1,3,7,8,16)`  
Lists are created using ` [ ]` e.g. `my_list = [2,4,5,12,60]`

You can select the first value in these by doing the following: (Python starts counting from 0 unlike R which is 1)

`my_tuple[0]` 
 `my_list[0]` 

The first value in our tuples/lists is index 0.

You can grab multiple values from a list at once by using indexing.
The notation for this is using `[:]` which is interpreted by python as

`[start from here:end here]`

`my_list[ : 3]`  will grab all of the values in my_list up to the 3rd index. 
`my_list [2:4]` will grab values 5 and 12 from my_list,  you can visualise this by breaking it down into:  
`my_list[2]`
`my_list[3]`

Note how the 4th value is not grabbed, this is a common rule in python when dealing with ranges of numbers, it will include the starting number but will stop one number below the given ending number. `my_list[2:4]` directly translates as grab everything from index 2 up to but not including index 4.

Negative indexing works much the same way but it starts at the other end of the string, `[-1]`will be the last item in the list.

A further `:` will add a step to the search.

`my_list[::2]`

This will start at the beginning of the list/tuple/string and stop at the end while only selecting every second index. This is useful for when we need to subset or reverse something.

The following code will select the entire string then start stepping backwards by 1 index until it reaches the start.

```python
my_dna = 'ATGCGTGCTGATGTACAGTAGACAGTG'
my_dna_reversed = my_dna[::-1]
```

The main difference between tuples and lists is that tuples cannot be modified once they are made.

Let's try to update the first value in each of these. What happens to the contents of your variables when you run this code? What error message are you getting?


```python
my_tuple[0] = 100
my_list[0] = 100

print(my_tuple)
print(my_list)
```

The `.append()` method allows you to add an item to a list.

```python
print(my_list)
my_list.append(22)
print(my_list)
```

Lists can be sorted into ascending values using the `.sort()` method

```python
print(my_list)
my_list.sort()
print(my_list)
```
You can remove a value from lists by passing the .remove() method

```python
print(my_list)
my_list.remove(22)
print(my_list)
```
This will remove the first occurrence of the value 22 in the list.

What if you want to delete the third entry of your list, regardless of its value? Use `del`

```python
print(my_list)
del my_list[2]
print(my_list)
```

Strings can be turned into lists using the `split()` method. This method will split the string into a list containing items based on the separator you pass into it. The separator can be anything at all, in the two examples below a space character is used in the first and a hyphen in the second.

```python
the_string = ('BRCA1 BRCA2 P53 RB APC')
string_to_list = the_string.split(' ')
print(string_to_list)
type(string_to_list)

list_of_names_from_a_string = ('Barry-Stephen-Ghandi').split('-')
```


# Dictionaries
Dictionaries are a way of storing information (values) and returning those values using an identifier (key).
`{'key':'value'}

```python
my_dict = {'BRCA1':[45,34,44,47,66], 
           'BRCA2':[88, 82, 75, 78, 90], 
           'P53':[12, 15, 10, 19, 16]}

#get the values relating to the key 'BRCA2'
my_dict['BRCA2']

#get the value of the item at index 4 of 'BRCA2'
my_dict['BRCA2'][4]
```





# For loops

For loops are used to automate tasks so that the user does not have to type multiple lines of code.
Some examples of for loops:

```python
a_list = [1,2,3,6,7,8]
for i in a_list:
    print(i)
```

And a slightly more complicated one:

```python
#create your various lists
list_of_dates=["02/04/2020", "03/04/2020", "04/04/2020"]
experiment_numbers = [17,18,19]
results = ["Success", "Failure", "Success"]

#initialise the for loop, for the first value in the list_of_dates, 
#assign it to the temporary variable date

for date in list_of_dates:
    #next, print this temporary variable

    print(f'The experiment took place on {date}')

    #Once this has been done, return to the list_of_dates list and assign the 
    #next value to the temporary variable date
    #repeat until every value in dates has been used up, the for loop will then end.
    
```
For loops can be challenging to understand without a visualisation of the steps that are occurring.
This website http://www.pythontutor.com/visualize.html#mode=edit shows you what line of code is executing and the output that it generates. It can be useful to put your code here and run the visualisation to understand things a bit better.


This for loop is useful but how can we use a single for loop to loop over multiple lists?  
Instead of initiating the loop using the list, we can use the indexing we learned earlier and some new functions which can create sequences of numbers.

```python
dates=["02/04/2020", "03/04/2020", "04/04/2020"]
experiment_numbers = [17,18,19]
results = ["Success", "Failure", "Success"]

#initialise the for loop
for i in range(0, len(dates)):
    print(f'Experiment {experiment_numbers[i]} which was carried out on {dates[i]} was a {results[i]}')
```

To explain what happened here we need to understand the range and len functions.
`len()` finds the length of an object. `len(dates)` will return 3 as there are 3 items in the dates list

`range()` creates a sequence starting from the first argument and ending before the next argument.  
`range(0, len(dates)` is the same as `range(0, 3)` which will give the sequence `0, 1, 2`

So the first iteration of the loop would be  
`print(f'Experiment {experiment_numbers[0]} which was carried out on {dates[0]} was a {results[0]}')`

The second iteration of the loop would use the second number in the sequence which is 1
`print(f'Experiment {experiment_numbers[1]} which was carried out on {dates[1]} was a {results[1]}')`

And so on, you can imagine how useful this type of automation would be when dealing with data which has 1000s of entries.

# Conditional statements
Conditional statements are used to control what your code does and when it does it

The conditional statements in Python are `if` `elif` `else`   
We can go back to our previous for loop and add some flow control to it.

```python
x = 10
y = 9

if x == 10:
    print("correct")
    
if y == 8:
    print("correct")
```

When writing conditional statements it is important that you evaluate all variables separately.
To see if x or y equals 6, it can be tempting to write something like the following which makes sense when spoken in English but in python it means you are asking if x exists or if y equals 6. 
This will print correct even though neither x or y equals 6.

```python
if x or y == 6:
    print("correct")
```

This prints correct because of the boolean values which are returned
The boolean values are True and False so the question we are asking python is
print correct if x is True or if y is True, x is True so it prints correct.



The proper way to do this is the following which will produce the boolean values
False and False so it will not print.

```python
if x ==6 or y ==6:
    print("correct")
```

We could also do this another way using `in`

```python
if 6 in [x,y]:
    print("correct")
```

We can check to see if a sequence data type contains our variable of interest:

```python
if x in [1, 10, 43]:
    print("x is in this list")
```

We have seen how using `or` will initialise code even when only one of the conditions is True. We can use `and` to initialise code only when allconditions are True

```python
if x == 10 and y == 7:
    print("correct")
```

`else` statements can be used with if to execute code when the boolean value is False.
For example in this code we use `and` which will only print correct if all conditions are True. The boolean values are True and False which evaluates to False and so the `else` statement will be executed instead.

```python
if x == 10 and y == 7:
    print("correct")
else:
    print("incorrect")
```

`elif` which is short for else if is another level of control that we can have over our loops.
Instead of evaluating both variables together and running the same operations on them we can break it up using `elif` which allows us to have one operation for the x condition and a different operation for the y condition

```python
if x == 8:
    print('x is eight')
    x = x ** 2
elif y == 9:
    print('y is equal to nine')
    y = y / 2
else:
    print('x is not equal to eight and y is not equal to nine')
    x = x + 1
    y = y + 1
```

Let's put this type of flow control into practice by modifying our previous for loop.

```python
dates=["02/04/2020", "03/04/2020", "04/04/2020"]
experiment_numbers = [17,18,19]
results = ["Success", "Failure", "Success"]

#initialise the for loop
for i in range(0, len(dates)):

  #check if it is the date we are looking for
	if dates[i] == “04/04/2020”:
   		 print(f'Experiment {experiment_numbers[i]} which was carried out on {dates[i]} was a {results[i]}')
  
  #if its not the date we are looking for, check if it was a Success
    elif results[i] == "Success":
      print(f'Experiment number {experiment_numbers[i]} was a Success!)  
  
  #if its not the date or a success then run the else statement 
	else
      print(f'We are not looking for this experiment')

```

For the first if statement this code will only print the result if the date is equal to “04/04/2020”. elif (else if) will print out if the first `if` condition is not met and the `elif` condition is met. Conditionals are very useful when dealing with large datasets, they allow you to pull out exactly what you are looking for. Try to modify this code so that it will only print for experiment number 18, do not use the dates list to do this.

There are many ways to control your code using if statements and conditionals such as `== != > < <= >=` (equal to, not equal to, greater than, less than, less than or equal to, greater than or equal to)


## While loops
While loops are another type of loop which rely on Boolean values to control when to run and when to finish. They differ from for loops in that for loops tend to iterate over a sequential data type until that data type runs out of values whereas while loops will run constantly until a condition is met.

```python
i = 10

while i > 5:
    print(f"When will this while loop end?. i is now {i}")
    i = i -1

```

Here we initialise i to equal 10 before we enter the loop and we tell our while loop to run if i is greater than 5.
The first loop of this will check to see if i is greater than 5 and it will be 10 so it evaluates to the boolean value True and it runs the first iteration of the loop. We update i  inside the loop using

`i = i -1` which when we break it down is the same as   `i = 10 - 1`
So now the next iteration of the while loop will check to see if i , now 9, is greater than 5. This continues until i == 5 and the boolean value changes to False, thus ending the loop. 

A common mistake when working with while loops is to forget to update the value being used. If we did not have `i = i -1` inside the loop then it would always be greater than 5 and we would get stuck in an infinite loop. 

Try to rewrite that while loop using a for loop and an if statement.

The `break` statement is commonly used in loops as it offers a way to exit the loop when a condition is met. The `continue` statement will restart the loop. In the example below, the loop will break when the password is guess and it will return to the start if the `else` clause is triggered which in this case is when the guess doesn't equal the password.

```python
#initiate the loop with While True, this create an infinite loop which can
#be broken out of with the break statement once an if condition is met.
while True:
    password = 'VerySecurePassword'
    guess = input('Please enter your password: ')
    if guess == password:
        break
    else:
        continue
```



# Creating your own functions

We have so far used the functions which are built in to python such as `print()`, `int()`, `type()` etc.

But what if python does not have a built in function which does the task that you need?

To make your own function you need to use `def` which is short for define. After `def` you put the name of the function you are defining and add any arguments that will be passed to the function in parenthesis.

In the example below the argument `numbers` is simply a placeholder for any argument you want to give to the function, the arguments you give to the function when you are actually using it will replace `numbers` throughout the function.

We use the `return` statement to decide what data we want to get out of the function, in this case we want to `return` the updated argument `numbers`. 

```python
def add_one(numbers):
    #loop over the data you are giving to the function
    for i in range(0, len(numbers)):
        #update the data you gave to the function by adding 1 to each element
        numbers[i]= numbers[i] + 1
    #finally, return the updated data
    return numbers
```

You can also create functions which do not have any initial arguments.

```python
def gc_analysis():
    dna = input('Please enter your DNA sequence to be analysed: ')
    gc_percent = ((dna.count('G') + dna.count('C')) / len(dna)) * 100
    print(f'The GC percentage of this DNA is {gc_percent}')
    return gc_percent


gc_percent_for_primer_one = gc_analysis()
print(gc_percent_for_primer_one)

```

 #### A note on global and local variables

The local variables in the previous function are `dna` and `gc_percent`. These variables only exist within this function. Even though we have assigned data to `dna`, if we were to call it in the global space, it would throw an error and say that dna is not defined. 

# Some links to check out

The python for biologists book is aimed at biologists wanting to start programming.
http://userpages.fu-berlin.de/digga/p4b.pdf

Don't like f strings and would like to use something else?
https://www.geeksforgeeks.org/python-format-function/

Python visualisation website.
http://www.pythontutor.com/visualize.html

SoloLearn is a free app for your phone which teaches many different languages.
https://www.sololearn.com/

Automate the boring stuff is a free book which is great for beginners.
https://automatetheboringstuff.com/



