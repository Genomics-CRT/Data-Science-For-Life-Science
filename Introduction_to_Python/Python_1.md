# Strings, Lists, Tuples, For Loops, While loops.


## Strings
Strings are simply characters surrounded by `'` or `"` quotes
For example, `myString = 'This is a string'`.
The `print()` function can be used to show the output of strings

Strings can be joined together using the `+` operator

`print(myString + " which I made longer")`

You can change the string to upper or lower case using the `.upper()` or `.lower()` methods
`myString.upper()` will output `THIS IS A STRING`

These two methods are useful when you want to work with input from a user.

You can check what data type a variable is by using the type function 

`type(myString)` will return `str`

Any character can be a string, this include digits.

`type('8')` will return `str`

What would happen if you type this?:
`print(‘8’ + ‘8’)`

This can be overcome by using the `in()` function which converts string digits into integers.

`print(int(‘8’) + int(‘8’))`

When working with strings in python it is best practice to use what are called formatted string literals, more simply known as f strings.

f strings allow easy and readable formatting of strings. 

```
date = "02/04/20"
experimentNumber = 17
result17 = "Success"

print(f'Experiment {experimentNumber} which was carried out on {date} was a {result17}')
```
f strings also allows you to do calculations, function calls, methods etc. within a string

`print(f'The answer to 50 * 275 is {50*275}')`
`print(f'There is no need to shout {myString.upper()}')`

We can use the same variable as many times as needed when printing f strings.

```
newLine = '\n'
print(f"A {newLine} new line {newLine} any {newLine} time we want{newLine} one")
```

# Tuples and Lists

You can store more than just one value in a variable in python by using sequence data types such as tuples or lists

Tuples are created by using `( )` e.g. `myTuple = (1,3,7,8,16)`  
Lists are created using ` [ ]` e.g. myList = [2,4,5,12,60]

You can select the first value in these by doing the following: (Python starts counting from 0 unlike R which is 1)

`myTuple[0]` or `myList[0]` This is known as indexing, the first value in our tuples/lists is index 0.

You can grab multiple values from a list at once by using indexing.
`myList[ : 3]`  will grab all of the values in myList up to the 3rd index. 
`mList [2:4]` will grab values 5 and 12 from myList,  you can visualise this by breaking it down into:  
`myList[2]`
`myList[3]`

Note how the 4th value is not grabbed, this is a common rule in python when dealing with ranges of numbers, it will include the starting number but will stop one number below the given ending number. `MyList[2:4]` directly translates as grab everything from index 2 up to but not including index 4.

The main difference between tuples and lists is that tuples cannot be modified once they are made.

Let's try to update the first value in each of these. What happens to the contents of your variables when you run this code? What error message are you getting?


```
myTuple[0] = 100
myList[0] = 100

print(myTuple)
print(myList)
```

The `.append()` method allows you to add an item to a list.

```
print(myList)
myList.append(22)
print(myList)
```

Lists can be sorted into ascending values using the `.sort()` method

```
print(myList)
myList.sort()
print(myList)
```
You can remove a value from lists by passing the .remove() method

```
print(myList)
myList.remove(22)
print(myList)
```
This will remove the first occurrence of the value 22 in the list.

What if you want to delete the third entry of your list, regardless of its value? Use `del`

```
print(myList)
del myList[2]
print(myList)
```

# For loops
For loops are used to automate tasks so that the user does not have to type multiple lines of code.
An example of a for loop is:

```
#create your various lists
listOfDates=["02/04/2020", "03/04/2020", "04/04/2020"]
experimentNumbers = [17,18,19]
results = ["Success", "Failure", "Success"]

#initialise the for loop, for the first value in the listOfDates, 
#assign it to the temporary variable date

for date in listOfDates:
    #next, print this temporary variable

    print(f'The experiment took place on {date})

    #Once this has been done, return to the listOfDates list and assign the 
    #next value to the temporary variable date
    #repeat until every value in dates has been used up, the for loop will then end.
    
```
For loops can be challenging to understand without a visualisation of the steps that are occuring.
This website http://www.pythontutor.com/visualize.html#mode=edit shows you what line of code is executing and the output that it generates. It can be useful to put your code here and run the visualisation to understand things a bit better.


This for loop is useful but how can we use a single for loop to loop over multiple lists?  
Instead of initiating the loop using the list, we can use the indexing we learned earlier and some new functions which can create sequences of numbers.

```
dates=["02/04/2020", "03/04/2020", "04/04/2020"]
experimentNumbers = [17,18,19]
results = ["Success", "Failure", "Success"]

#initialise the for loop
for i in range(0, len(dates)):
    print(f'Experiment {experimentNumbers[i]} which was carried out on {dates[i]} was a {results[i]}')
```

To explain what happened here we need to understand the range and len functions.
`len()` finds the length of an object. `len(dates)` will return 3 as there are 3 items in the dates list

`range()` creates a sequence starting from the first argument and ending before the next argument.  
`range(0, len(dates)` is the same as `range(0, 3)` which will give the sequence `0, 1, 2`

So the first iteration of the loop would be  
`print(f'Experiment {experimentNumbers[0]} which was carried out on {dates[0]} was a {results[0]}')`

The second iteration of the loop would use the second number in the sequence which is 1
`print(f'Experiment {experimentNumbers[1]} which was carried out on {dates[1]} was a {results[1]}')`

And so on, you can imagine how useful this type of automation would be when dealing with data which has 1000s of entries.

# Conditional statements
Conditional statements are used to control what your code does and when it does it

The conditional statements in Python are `if` `elif` `else`   
We can go back to our previous for loop and add some flow control to it.

```
dates=["02/04/2020", "03/04/2020", "04/04/2020"]
experimentNumbers = [17,18,19]
results = ["Success", "Failure", "Success"]

#initialise the for loop
for i in range(0, len(dates)):

  #check if it is the date we are looking for
	if dates[i] == “04/04/2020”:
   		 print(f'Experiment {experimentNumbers[i]} which was carried out on {dates[i]} was a {results[i]}')
  
  #if its not the date we are looking for, check if it was a Success
  elif results[i] == "Success":
      print(f'Experiment number {experimentNumbers[i]} was a Success!)  
  
  #if its not the date or a success then run the else statement
  else
      print(f'We are not looking for this experiment')

```

For the first if statement this code will only print the result if the date is equal to “04/04/2020”. elif (else if) will print out if the first if condition is not met and the elif condition is met. Conditionals are very useful when dealing with large datasets. They allow you to pull out exactly what you are looking for. Try to modify this code so that it will only print for experiment number 18, do not use the dates list to do this.

There are many ways to control your code using if statements and conditionals such as `== != > < <= >=` (equal to, not equal to, greater than, less than, less than or equal to, greater than or equal to)

## While loops
While loops are another type of loop which rely on Boolean values to control when when to run and when to finish. They differ from for loops in that for loops tend to iterate over a sequential data type whereas while loops will run constantly until a condition is met.

```
i = 10

while i > 5:
    print(f"When will this while loop end?. i is now {i}")
    i = i -1

``` 

Here we initialise i to equal 10 and we tell our while loop to run if i is greater than 5.
The first loop of this will check to see if i is greater than 5 and it will be 10 so it evaluates to the boolean value True and it runs the first iteration of the loop. We update i  inside the loop using

`i = i -1` which when we break it down is the same as   `i = 10 - 1`
So now the next iteration of the while loop will check to see if i , now 9, is greater than 5. This continues until i == 5 and the boolean value changes to False, thus ending the loop. 

A common mistake when working with while loops is to forget to update the value being used. If we did not have `i = i -1` inside the loop then it would always be greater than 5 and we would get stuck in an infinite loop.

Try to rewrite this while loop using a for loop and an if statement.
