
# Python basics

## Anaconda and the Spyder IDE

Open Anaconda and launch Spyder, this is the IDE for Python which comes with Anaconda.


It will look something like this :

![Spyder IDE overview](https://github.com/Genomics-CRT/images/blob/master/SpyderIDE2.png)

I have labelled a few of the important areas in the IDE.

1. Is what is called your working directory, this is where any files you are working with should be stored and it is also where the code you write will be saved on your computer.

2. Is our editor, this is where we write our scripts

3. Is called the console, you can write code here line by line and see the output straight away. 
   This is also where the output from our long scripts will show when we run them.
   
If you want to run the whole script you have written in the editor, press F5.
If you want to run a single code line or a highlighted portion of lines, press F9

## Resources to help with coding
A large part of your time spent coding will be reading through package documentation and on websites which specialise in solving coding problems. The main websites which you should search when you encounter a problem are www.stackoverflow.com and www.biostars.com 

## Operators
Python uses the same operators as R. 

`+  - * /` which is addition, subtraction, multipication, and division.

You can try these out by typing the code into the editor and pressing F9 to run the line, you will see the answer show up in the console.

## Variables
Variables are a way to store values for use later in your code. 

This can be done using the `=` key, for example:

`x = 10`

will assign 10 to the variable x

You should always choose a variable name which is related to the value inside the variable. e.g. if you are storing a persons name inside a variable do not call the variable “age”.

We can combine this with operators to do things such as:

`x + 5`

This will give the answer 15

We can also update our variable as needed such as:

`x = x + 5`

x will now equal 15, this type of updating variables is very useful.


## Print function
The `print()` function in python will print the output of your code onto the console. 

## Comments
Comments can be added to your python code by placing `#` before what you type.  
It is good practice to comment your code so that others, and yourself, can understand what your  
thought process was when you were writing the code. This allows easy understanding, and editing, of the code in the future.

## Data types

The type of data you are dealing with will influence which functions or methods you can use on it
You can use the `type()` function to check what data type you are dealing with e.g.

```
x = 5
type(x)
```

### Numeric
This includes integers and floats.  
Integers are numbers without a decimal point whereas floats have a decimal point

### String
This is any character or group of characters which are surrounded by quotes

### Boolean
Also known as logical, this includes the `True` and `False` boolean values. 
Test this code out to see how True and False works.

```
x = 5 
x == 5

y = 10
y == 11
```

### Sequence
Any data type which can store collections of data, this includes Strings, Lists, Tuples, and Dictionaries

## Parenthesis, brackets, curly brackets
All code which contains an opening `(`  `[` or `{` must be accompanied by a closing `)` `]` `}`
It is very common for errors in code to be the result of not enclosing a code block correctly.

## Indentation in Python
Other programming languages(such as R) rely on using `{` to break up code blocks, Python uses indentation.
Indentation can be a tab character or four spaces. The image below gives an example of this. Everything which is indented will be run as part of the for loop command, even if those commands have nothing to do with the list which is being looped over (more on for loops later).

The final print command at the bottom of the code will only be printed once because it is not indented into the same group (code block) as the others. 

[Indentation](https://github.com/Genomics-CRT/images/blob/master/Indentation.png)

