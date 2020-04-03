# Calculations
Let’s start with the basic syntax for mathematical calculations in R. R performs addition, subtraction, multiplication
and division with `*` `-` `+` `/`.

An example is given below:

```{R}
# Results in "500"
573 - 74 + 1

# Results in "50"
25 * 2

# Results in "2"
10 / 5
```
Mathematical operations in R follow the standard mathematical order of operations.

Calculate the result of this equation: `25 * 4 + 9 / 3` in the R code block in your R-markdown file. 
A code block has been initialised for you below to insert the equation. 

```{R}

```

Check your answer:

```{R}
25 * 4 + 9 / 3
```

# Comments
Text written in a program but not run by the computer is called a comment. R interprets anything after a `#` as a comment.
It is good practice to add comments explaining briefly what the code does, what input it requires, or your thought 
process behind the code. When you revisit the code months down the road, you will thank yourself. 

Furthermore, comments can be placed in code blocks to 'deactivate' that line of code. The following illustrates this:

```{R}
for(i in seq(1:10)){
  i <- i + 2
  print(i)
}
```

Now add a comment to the line `i <- i +2` to disable the line of code and check the output. 

# Data Types
Let’s dive into how R “thinks about” different types of data. In R and in programming, data types are the classifications 
we give different kinds of information pieces. In this lesson, we will explore the following R data types:

* **Numeric**: Any number with or without a decimal point: 23, 0.03and the numeric null value NA.
* **Character**: Any grouping of characters on your keyboard (letters, numbers, spaces, symbols, etc.) or text.
             Most strings are surrounded by single quotes: ' ... ' or double quotes " ... ". 
             Sometimes you will hear this type referred to as “string.”
* **Logical**: This data type only has two possible values— either TRUE or FALSE (without quotes). It’s helpful to think
           of logical types or booleans as on and off switches or as the answers to a “yes” or “no” question. 
* **Vectors**: A list of related data that is all the same type.
* **NA**: This data type represents the absence of a value, and is represented by the keyword NA (without quotes) 
      but it has its own significance in the context of the different types. That is there is a numeric NA,
      a character NA,and a logical NA.

Look at the following examples:
```{R}
class(2) # numeric
class('hello') # character
class('23') #character
class (FALSE) #logical
class(NA) #logical
```
In the example above, notice that the third line is labeled a character type. This is because the characters 23 are in quotes, so it gets classified as a character. 

# Variables
Now that you know how R classifies some of the basic information types, let’s figure out how to store them. 
In programming, variables allow us to store information and associate that information with a name. 
In R, we assign variables by using the assignment operator, an arrow sign (<-) made with a carat and a dash.

```{R}
course_name <-"Genomics CRT"
```

In the example above, we store the string value "Genomics_CRT" in a variable called course_name. 
Variables can't have spaces or symbols in their names other than an underscore (_). 
They can't begin with numbers but they can have numbers after the first letter (e.g, var_1  is OK).

If we need to update a variable but perform the same logical process on it, we can change its value! 
For example, take the variable message_string:

```{R}
# Greeting
message_string <- "Hello there"
print(message_string)
```

```{R}
# Farewell
message_string <- "Slan go foil"
print(message_string)
```

Above, we create the variable message_string, assign a welcome message, and print the greeting. 
After we greet the user, we want to wish them goodbye. We then update message_string to a departure 
message and print that out.

Note: You can also use = instead of <- to assign a value. However popular nomenclature dictates the use of `<-`. 

# Viewing Variables
You may have noticed that variables created are stored under the `environment` window in R Studio. This is a nice feature
that can save time by using the GUI instead of typing `class()` or `typeof()`. However in some circumstances (particularly
on a computing cluster) the GUI will not be accessible to you. 

# Vectors
We mentioned Vectors when we introduced data types earlier. In R, vectors are a list-like structure that contain items
of the same data type.

Take a look here:

```{R}
spring_months <- c("March", "April","May","June")
```

In the example above, we created a new variable with the value of a new vector. 
We created this vector by separating four character strings with a comma and wrapping them inside c().

A few things you should know how to do with vectors:

* You can check the type of elements in a vector by using typeof(vector_name)
* You can check the length of a vector by using length(vector_name)
* You can access individual elements in the vector by using [] and placing the element position inside the brackets. 
  For example, if we wanted to access the second element we would write: vector_name[2]. 
  
**Note: In R, you start counting elements at position one, not zero.**

To illustrate the above points, lets look at the for loop used earlier. 
```{R}
# create for loop to print i
for(i in seq(1:10)){
  i <- i + 2
  print(i)
}
```

Run the above code block. You will see `i` stored as a variable in the environment window with a value of 12. 
(the value of i is the last iteration of the loop, i.e 10 + 2) 

Now observe what happens when creating a vector:
```{R}
# Character vector
char <- c("delta", "alpha", "gamma")

# Numeric vector
numer <- c(1, 5, 2, 9, 2)

# Look in the environment window. The prefix chr & num are character and numeric, respectively. 

# Lets see what happens mixing data types in a vector. 
# For this we will use a character "", numeric and the variable i (with value 12).

tester <- c(i, 55) # num[1:2] 12, 55
tester_1 <- c(55, i, "epsilon") # chr[1:3] "55", "12", "epsilon"
```

Hopefully you noticed that mixing data types in a vector might not produce what you hoped for. The presence of one character 
converted every other data type in the vector to a character. 

# Conditionals
In R, we will often perform a task based on a condition. For example, if we are analyzing data for the summer, 
then we will only want to look at data that falls in June, July, and September.

We can perform a task based on a condition using an if statement:

```{R}
if (TRUE) {
  print('This message will print!')
} 
```
Notice in the example above, we have an if statement. The if statement is composed of:

* The if keyword followed by a set of parentheses () which is followed by a code block, or block statement, 
   indicated by a set of curly braces {}.
* Inside the parentheses (), a condition is provided that evaluates to TRUE or FALSE.
* If the condition evaluates to true, the code inside the curly braces {} runs, or executes.
* If the condition evaluates to false, the code inside the block won’t execute.

Knowing how to use if statements will help you introduce logic in your data analysis. 
There is also a way to add an else statement. An else statement must be paired with an if statement, 
and together they are referred to as an `if…else` statement.

```{R}
# pseudocode
if (TRUE) {
   print("Go to sleep!")
} else {
   print("Wake up!")
}
```

In the example above, the else statement:
* Uses the else keyword following the code block of an if statement.
* Has a code block that is wrapped by a set of curly braces {}.
* The code inside the else statement code block will execute when the if statement’s condition evaluates to false. 
  These `if…else` statements allow us to automate solutions to yes-or-no questions, also known as binary decisions.

Here is a trivial example: 
```{R}
message <- "I change based on a condition."

if(FALSE){
  message <- "I execute this when true!"
} else{
  message <- "I execute this when false!"
}

print(message)

# Change FALSE to TRUE to observe different output. 
```

Lets notch it up one level:

```{R}
value <- 1

if(value == 10){
  print("value is correct")
} else{
  print("incorrect value")
}
```

Finally... Below is another example of a `for loop` (you will learn about these later), an `if` and an `else` statement. Briefly, the for loop iterates over each value in the `num_vec` and runs it through the `if...else` code block. 
This code also shows you how to append items to an empty vector (`above_5` and `below_5`, respectively)

```{R}
num_vec <- c(1,4,2,6,8,9,9,4,3,2)

above_5 <- c()
below_5 <- c()

for(i in num_vec){
    if(i > 5){
      above_5 <- c(above_5, i) 
    } else{
      below_5 <- c(below_5, i)
    }
}
```

#Comparison Operators

When writing conditional statements, sometimes we need to use different types of operators to compare values. 
These operators are called comparison operators.

Here is a list of some handy comparison operators and their syntax:

* Less than: `<`
* Greater than: `>`
* Less than or equal to: `<=`
* Greater than or equal to: `>=`
* Is equal to: `==`
* Is NOT equal to: `!=`

Comparison Operators compare the value on the left with the value on the right. For instance:

```
10 < 12 # Evaluates to TRUE
```

It can be helpful to think of comparison statements as questions. When the answer is “yes”, the statement evaluates to true,
and when the answer is “no”, the statement evaluates to false. 

Ths was demonstrated in the `if...else` section above, where values greater that 5 were appended to a vector, and values
less than 5 were appended to a seperate vector. 

# Logical Operators
Working with conditionals means that we will be using logical, true or false values. In R, there are operators that work 
with logical values known as logical operators. We can use logical operators to add more sophisticated logic to our
conditionals. There are three logical operators:

* the AND operator (&)
* the OR operator (|)
* the NOT operator, otherwise known as the bang operator (!)

When we use the `&` operator, we are checking that two things are true:

```{R}
if (stopLight == 'green' & pedestrians == 0) {
  print('Go!');
} else {
  print('Stop');
}
```

When using the `&` operator, both conditions must evaluate to true for the entire condition to evaluate to true and execute. Otherwise, if either condition is false, the & condition will evaluate to false and the else block will execute.

If we only care about either condition being true, we can use the | operator:

```{R}
if (day == 'Saturday' | day == 'Sunday') {
  print('Enjoy the weekend!')
} else {
  print('Do some work.')
}
```

When using the | operator, only one of the conditions must evaluate to true for the overall statement to evaluate to true. 
In the code example above, if either day == 'Saturday' or day == 'Sunday' evaluates to true the if’s condition will evaluate
to true and its code block will execute. If the first condition in an | statement evaluates to true, the second condition
won’t even be checked.

The ! NOT operator reverses, or negates, the value of a TRUE value:

excited <- TRUE
print(!excited) # Prints FALSE

Essentially, the ! operator will either take a true value and pass back false, or it will take a false value and pass back true.

Logical operators are often used in conditional statements to add another layer of logic to our code.

# Functions
Functions are actions we can perform. R provides a number of functions, and you have been using them 'under the hood'. 

We call, or use, these functions by stating the name of the function and following it with an opening and closing
parentheses: ie. functionName(). In addition, between the parenthesis, we usually pass in an argument, or a value that 
the function uses to conduct an action, i.e. functionName(value).

Does that syntax look a little familiar? When we have used print() we’re calling the print function. When we made a vector,
we actually used the combine c() function! Let’s see print() and some real functions in action!

```R
sort(c(2,4,10,5,1)); # Outputs c(1,2,4,5,10)
length(c(2,4,10,5,1)); # Outputs 5
sum(5,15,10) #Outputs 30
```
Let’s look at each of the lines above:

* On the first line, the sort() function is called with a parameter of the vector c(2,4,10,5,1). The result is a sorted vector c(1,2,4,5,10) with the values in ascending order.
* On the second line, we called a function we’ve seen before: length() and it returned the value 5 because there were five items in the vector.
* On the third line, we called a function sum() which added up all of the arguments we passed to it.

Understanding how to call a function and what arguments it needs is a fundamental part of leveraging R as a tool to conduct
analysis. **To view the documentation of a function, type the function and hit F1 to render the docs in the bottom right 
window of R Studio**. 

Example of the unique function:
```R
values <- c(2,6,2,5,8,7,2,6,7,9,11)

unique(values) #prints output to stdout

# assign it to a variable for further use

unique_val <- unique(values)

print(unique_val)
```

# Importing Packages

R’s popularity is also largely due to the many fantastic packages available in the language! 
A package is a bundle of code that makes coding certain tasks easier. 
There are all sorts of packages for all sorts of purposes, ranging from visualizing and cleaning data, 
to ordering pizza or posting a tweet. In fact, most R-grammers (R programmers) use packages when they code. 
This is why you might hear them differentiate packages from “Base R.” Base R refers the R language by itself and 
all that it can do without importing any packages.

Base R is very powerful, but most of the time, you’ll want to import a package to make your life easier. 
You only need to run this command the first time you install a package, after that there is no need to run it:

```
install.packages('package-name')
```

To import a package you simply:
```
library(package-name)
```

You can look up documentation for different packages available in R at the CRAN (Comprehensive R Archive Network).

In this lesson, we coded in Base R but let’s practice importing one of the most popular R packages: dplyr. 

```R
install.packages("dplyr")
library(dplyr)
```

**Note: A common error you will come across when installing packages is "package does not exist". The package you
are trying to install will most likely be in Bioconductor**.

An example of a package on bioconductor is `fgsea`. The tool itself is not important for these excercises. Practice
downloading and installing `fgsea` via biocinductor by googling "fgsea", or visit the package site [here](https://bioconductor.org/packages/release/bioc/html/fgsea.html).
Bioconductor packages contain a code snippet you can copy and paste to complete the download: 

```R
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("fgsea")
```

# Summary 

Here’s a summary of some of the concepts you’ve learned:

* R is a powerful statistical programming language with a large community of data enthusiasts.
* You can calculate arithmetic with R and it will follow the normal order of operations
* Data types allow us to classify different pieces of information.
* You can store that information inside of variables
* You can use conditional statements and operators to introduce logic to your code
* You can call a function in R by using the () and passing in the correct arguments
* R programmers have published lots of useful packages that specialize in different tasks, which are all available for you to use in your programs after you install them.

