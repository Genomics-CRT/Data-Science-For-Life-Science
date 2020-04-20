# Week 1: Introduction to R Worksheet.

A quick note on the layout of this document:

* The file type is a **markdown** file, which allows for Headers, block quotes, inline code and language specific code blocks. It can be opened in R Studio and other applications. If you are interested in generating your own markdown documents, I cannot recommend **Typora** highly enough. It compiles the markdown language in real time to produce nicely formatted code blocks (https://typora.io/). Markdown cheat sheets are widely available online (https://www.code2bits.com/assets/cheat-sheets/cheatsheet-markdown.pdf).
* The issues section of Github (and many other bioinformatics websites) and R Studio use markdown notation to produce nicely formatted posts. I would encourage you to test out markdown syntax.

* In some code blocks you will see I have appended output from R Studio code. It is usually denoted by `[1] output`. This is done for your benefit however:
  * You cannot execute code in a markdown document, 
  * We encourage you to copy and paste code into R Studio and play around with it. You will learn  faster by getting your hands dirty.

# Calculations

Let’s start with the basic syntax for mathematical calculations in R. R performs addition, subtraction, multiplication, division, exponentiation and modulo with `*` `-` `+` `/` `^` `%%`.

An example is given below:

```{R}
# Results in "500"
573 - 74 + 1
[1] 500

# Results in "50"
25 * 2
[1] 50

# Results in "2"
10 / 5
[1] 2
```

Mathematical operations in R follow the standard mathematical order of operations.

# Comments
Text written in a program but not run by the computer is called a comment. R interprets anything after a `#` as a comment.
It is good practice to add comments to your code so When you revisit the code months down the road, you will understand exactly what the code was designed for:

Furthermore, comments can be placed in code blocks to 'deactivate' that line of code. The following code block uses a for loop to generate numbers from 1 - 10 stored as the variable `i`. For each number in the sequence, 2 is added `i <- i + 2`, resulting in the output:
```R
# For loop to calculate i + 2

# Comments can be added here 
for(i in seq(1:10)){ 
  i <- i + 2  # Adding a comment here will not deactivate the line of code
  print(i)
}

[1] 3
[1] 4
[1] 5
[1] 6
[1] 7
[1] 8
[1] 9
[1] 10
[1] 11
[1] 12
```

Now when we add a comment before code at start of line 2, the line is deactivated and the loop no longer adds 2 to `i`:
```R
for(i in seq(1:10)){
#  i <- i + 2
  print(i)
}

[1] 1
[1] 2
[1] 3
[1] 4
[1] 5
[1] 6
[1] 7
[1] 8
[1] 9
[1] 10
```

# Code Blocks

In R Studio, if you type into the document it will be rendered as markdown. To activate a code block you will have to type 3 back ticks ` followed by {R}. 

````{R}` 

some code, comments here

To close the code block type three back ticks `. 

When a code block has been created you the code will produce a greyscale background and have a "play" icon to run the code. Alternatively you can run a line of code by placing the cursor on the line and typing `ctrl + enter`. To run the entire block, make sure your cursor is inside the code block and type `ctrl + shift + enter`.

# Data Types

Let’s dive into how R “thinks about” different types of data. In R and in programming, data types are the classifications 
we give different kinds of information pieces. In this lesson, we will explore the following R data types:

* **Numeric**: Any number with or without a decimal point: `23`, `0.03` and the numeric null value `NA`.
* **Character**: Any grouping of characters on your keyboard (letters, numbers, spaces, symbols, etc.) or text. Most strings are surrounded by single quotes: ' ... ' or double quotes " ... ". You will hear this type referred to as a “**string**.”
* **Logical**: This data type only has two possible values— either TRUE or FALSE (without quotes). It’s helpful to think of logical types or **booleans** as on and off switches or as the answers to a “yes” or “no” question. 
* **Vectors**: A list of related data that is all the same type.
* **NA**: This data type represents the absence of a value, and is represented by the keyword NA (without quotes). It has its own significance in the context of the different types. That is there is a numeric NA, a character NA,and a logical NA.

Look at the following examples:
```R
class(2) # numeric
class('hello') # character
class('23') #character
class (FALSE) #logical
class(NA) #logical
```
In the example above, notice that the third line is labeled a character type. This is because the digits 23 are in quotes, so it gets classified as a character. 

# Variables
Now that you know how R classifies some of the basic information types, let’s figure out how to store them. 
In programming, variables allow us to store information and associate that information with a name. 
In R, we assign variables by using the assignment operator, an arrow sign `<-` made with a carat and a dash.

```R
course_name <-"Genomics CRT"
```
In the example above, we store the string value "Genomics_CRT" in a variable called course_name. Variables can't have spaces or symbols in their names other than an underscore (_). They can't begin with numbers but they can have numbers after the first letter (e.g, var_1  is OK).

If we need to update a variable but perform the same logical process on it, we can change its value! For example, take the variable message_string:

```R
# Greeting
message_string <- "Hello there"
print(message_string)
```

```R
# Farewell
message_string <- "Bye for now"
print(message_string)
```
Above, we create the variable message_string, assign a welcome message, and print the greeting. 
After we greet the user, we want to wish them goodbye. We then update message_string to a departure 
message and print that out.

**Note**: You can also use = instead of <- to assign a value. However popular nomenclature dictates the use of `<-`. 

**Note**: In R, you can type `alt` + `-` to produce a `<-`. This is convenient as it also inserts spaces before and after the `<-` automatically. 

# Viewing Variables
You may have noticed that variables created are stored under the `environment` window in R Studio. This is a nice feature that can save time by using the GUI instead of typing `class()` or `typeof()`. However in some circumstances (particularly on a computing cluster) the GUI will not be accessible to you. 

# Vectors
As mentioned in Data Types,  vectors are a list-like structure that contain items of the same data type. 

An example of a character vector:
```R
spring_months <- c("March", "April","May","June")
```

In the example above, we created a new variable with the value of a new vector. We created this vector by separating four character strings with a comma and wrapping them inside c(). It is a character vector. 

A few things you should know how to do with vectors:

* You can check the type of elements in a vector by using `typeof(vector_name)`
* You can check the length of a vector by using `length(vector_name)`
* You can access individual elements in the vector by using `[]` and placing the element position inside the brackets. For example, if we wanted to access the second element we would write: `vector_name[2]`. 

```R
numeric_vector <- c(21, 5.5449, 5^2, 67, 2, 5)

# Check type
typeof(numeric_vector)

# Check length
length(numeric_vector)

# Access 2nd element
numeric_vector[2]

# Assign 2nd element to variable
element_2 <- numeric_vector[2]

# Assign 1st element to variable
first <- numeric_vector[1]

# Assign last element to variable
last <- numeric_vector[6]

# Assign a range of elements to variable
range_numerics <- numeric_vector[2:4]
```

To access the final element of your vector it is useful to assign the length of the vector to a variable `key <- length(vector)` and use this as a key to access the final item `vector[key]`. 

**Note: In R, you start counting elements at position one, not zero!**

We can join two vectors together using the `c()` function in R:
```R
vector <- c(1,2,3,4,5)
vector_2 <- c(6,7,8,9,10)

x <- c(vector, vector_2)

print(x)

[1] 1 2 3 4 5 6 7 8 9 10
```

Be careful not to mix data types in a vector. Observe below what happens when mixing variables, characters and numerics in a vector:
```R
# Lets see what happens mixing data types in a vector. 
i <- 12

tester <- c(i, 55) 
print(tester)
[1] num[1:2] 12, 55
# expected behaviour, i is a variable storing the numeric 12

tester_1 <- c(55, i, "epsilon") 
print(tester_1)
# chr[1:3] "55", "12", "epsilon"
```

You may have noticed that mixing data types in a vector might not produce what you hoped for. The presence of one character renders the entire vector as a character data type.  

# Conditionals
In R, we will often perform a task based on a condition. This is also known as control flow, where the user can introduce conditional statements to activate sections of code.

We can perform a task based on a condition using an `if` statement. The code below will print `'This message will print!'` because the conditional statement `if` is set to `TRUE`.
```R
if (TRUE) {
  print('This message will print!')
} 
```

The `if` statement is composed of:

* The `if` keyword followed by a set of parentheses `()` which is followed by a code block or block statement, indicated by a set of curly braces `{}`.
* Inside the parentheses `()`, a condition is provided that evaluates to `TRUE` or `FALSE`.
* If the condition evaluates to `TRUE`, the code inside the curly braces `{}` runs, or executes.
* If the condition evaluates to `FALSE`, the code inside the block won’t execute.

Knowing how to use if statements will help you introduce logic in your data analysis.

There is also a way to add an `else` statement. An else statement must be paired with an `if` statement, 
and together they are referred to as an `if…else` statement.

```{R}
# pseudocode
if (TRUE) {
   print("Go to sleep!")
} else {
   print("Wake up!")
}
```

In the example above, the `else` statement:
* Uses the `else` keyword following the code block of an if statement.
* Has a code block that is wrapped by a set of curly braces `{}`.
* The code inside the `else` statement code block will execute when the `if` statement’s condition evaluates to `FALSE`. 
  These `if…else` statements allow us to automate solutions to yes-or-no questions, also known as binary decisions.

Here is a trivial example: 
```R
message <- "I change based on a condition."

if(FALSE){
  message <- "I execute this when true!"
} else{
  message <- "I execute this when false!"
}

print(message)

# Change FALSE to TRUE to observe different output. 
```

Let's introduce a conditional statement for a variable:
```R
value <- 1

if(value == 10){
  print("value is equals 10")
} else{
  print("value is not equal to 10")
}
```

Below is another example of a `for loop` (you will learn about these later), an `if` and an `else` statement. Briefly, the for loop iterates over each value in the `num_vec` and runs it through the `if...else` code block. Using vector concatenation from the previous topic on vectors, we can append items that are returned by the `if...else` logic to `above_5` and `below_5` vectors respectively. 

```R
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

# Comparison Operators
When writing conditional statements, sometimes we need to use different types of operators to compare values (like in the code example given above). These operators are called comparison operators.

Here is a list of some handy comparison operators and their syntax:

* Less than: `<`
* Greater than: `>`
* Less than or equal to: `<=`
* Greater than or equal to: `>=`
* Is equal to: `==`
* Is NOT equal to: `!=`

Comparison Operators compare the value on the left with the value on the right. For instance:

```R
10 < 12 
# Evaluates to TRUE
```

It can be helpful to think of comparison statements as questions. When the answer is “yes”, the statement evaluates to true,
and when the answer is “no”, the statement evaluates to false. 

This was demonstrated in the `if...else` section above, where values greater that 5 returned `TRUE` and were appended to a vector, values less than 5 were evaluated as `FALSE` and appended to a seperate vector. 

# Logical Operators
Working with conditionals means that we will be using logical, `TRUE` or `FALSE` values. In R, there are operators that work  with logical values known as logical operators. We can use logical operators to add more sophisticated logic to our conditionals. There are three logical operators:

* the AND operator `&`
* the OR operator `|`
* the NOT operator, otherwise known as the bang operator `!`

When we use the `&` operator, we are checking that two things are true:

```R
stopLight <- "green"
pedestrians <- 1

if (stopLight == 'green' & pedestrians == 0) {
  print('Go!');
} else {
  print('Stop');
}

[1] stop
```
When using the `&` operator, both conditions must evaluate to `TRUE` for the entire condition to evaluate to `TRUE` and execute. Otherwise, if either condition is `FALSE`, the & condition will evaluate to `FALSE` and the `else` block will execute.

If we only care about either condition being true, we can use the `|` operator:
```R
day <- "Saturday"

if (day == 'Saturday' | day == 'Sunday') {
  print('Enjoy the weekend!')
} else {
  print('Do some work.')
}
```

When using the `|` operator, only one of the conditions must evaluate to `TRUE` for the overall statement to evaluate to true. 

In the code example above, if either day == 'Saturday' or day == 'Sunday' evaluates to `TRUE` the `if` condition will evaluate to `TRUE` and its code block will execute. If the first condition in an `|` statement evaluates to `TRUE`, the second condition won’t even be checked.

The `!` NOT operator reverses, or negates, the value of a TRUE value:
```R
excited <- TRUE
print(!excited) # Prints FALSE
```

Essentially, the `!` operator will either take a `TRUE` value and pass back `FALSE`, or it will take a `FALSE` value and pass back `TRUE`.

Logical operators are often used in conditional statements to add another layer of logic to our code.

# Functions
Functions are actions we can perform. R provides a number of functions, and you have been using them 'under the hood'. 

We call, or use, these functions by stating the name of the function and following it with an opening and closing parentheses: ie. `functionName()`. In addition, between the parenthesis, we usually pass in an argument, or a value that the function uses to conduct an action, i.e. `functionName(value)`.

Does that syntax look a little familiar? When we have used `print()` we’re calling the print function. When we made a vector, we actually used the combine `c()` function! Let’s see `print()` and some real functions in action!

```R
sort(c(2,4,10,5,1)); 
[1] 1 2 4 5 10

length(c(2,4,10,5,1)); 
[1] 5

sum(5,15,10) 
[1] 30
```
Let’s look at each of the lines above:
* On the first line, the `sort()` function is called with a parameter of the vector c(2,4,10,5,1). The result is a sorted vector c(1,2,4,5,10) with the values in ascending order.
* On the second line, we called a function we’ve mentioned before: `length()` and it returned the value 5 because there were five items in the vector.
* On the third line, we called a function `sum()` which added up all of the arguments we passed to it.

Understanding how to call a function and what arguments it needs is a fundamental part of leveraging R as a tool to conduct analysis. 

**Note: To view the documentation of a function, type the function and hit F1 to render the documents in the bottom right  window of R Studio.**

Example of the unique function:
```R
values <- c(2,6,2,5,8,7,2,6,7,9,11)

unique(values) #prints output to stdout

# assign it to a variable for further use

unique_val <- unique(values)

print(unique_val)
```



# User Defined Functions

In R we can create our own functions to use anywhere in the document. In the same way assigning a vector to a variable allows us to call the vector by typing the variable name, leading to more concise, clear code, we can do the same for functions we want to reuse. 

```{R}
function.name <- function(arguments) 
{
  computations on the arguments
  some other code
}
```

Here, arguments can take on any name. This argument name will be referred to in the function body, but nowhere else in the document. This means that the variable is local, not global:

```{R}
global_variable <- 55

my_first_function <- function(input){
    # compute the square of input
    input * input
}

my_first_function(5)
[1] 25

#print(input)

print(global_variable)
[1] 55
```



Uncomment the `print(input)` line, and you will receive an error. This is because `input` defined in the function is not a global variable, and is only used within the function definition. We will see the same sort of behaviour in for loops. 

# For Loops

Numerous examples of for loops have been utilised already in this document. A for loop begins by using the `for` statement, followed by open brackets `()`. Inside the brackets, you can assign a local variable name that will be used in the code block, which is wrapped in curly braces `{}`.

Lets use for loops to introduce some other concepts in R, building the code up step by step:
```R
gene_A <- c(2, 0, 4, 40, 50, 66)

for(gene_exp in gene_A){
  print(gene_exp)
  }

# output:
[1] 2
[1] 0
[1] 4
[1] 40
[1] 50
[1] 66
```

Lets add some text before printing the variable. To do this in R, we use the `paste0` function which allows you to print strings along with variable values. The `paste0()` function must be wrapped in the `print()` function, with the quoted text followed by a comma:
```R
for(gene_exp in gene_A){
  print(paste0("Gene A expression values: ", gene_exp))
}

# output:
[1] "Gene A expression values: 2"
[1] "Gene A expression values: 0"
[1] "Gene A expression values: 4"
[1] "Gene A expression values: 40"
[1] "Gene A expression values: 50"
[1] "Gene A expression values: 66"
```

Lets assume the vector of gene expression values for gene A come from 6 samples. We are going to assign sample numbers in an incremental fashion:
```R
i = 0

for(gene_exp in gene_A){
  i <- i + 1
  print(paste0("Gene A expression value in sample ", i, ": ", gene_exp))
}

# output 
[1] "Gene A expression value in sample 1: 2"
[1] "Gene A expression value in sample 2: 0"
[1] "Gene A expression value in sample 3: 4"
[1] "Gene A expression value in sample 4: 40"
[1] "Gene A expression value in sample 5: 50"
[1] "Gene A expression value in sample 6: 66"
```

In the above code we set `i <- 0` and used it as an index. For each iteration of the for loop, we tell it to increase `i` by 1 `i <- i + 1`. Hopefully the above examples have given a clear idea of what for loops are capable of. 

# While Loops
In contrast to for loops which iterate over an existing objects until every item has been visited, while loops will operate over items -- but only whilst a condition is `TRUE`. That is to say, until the condition is no longer satisfied. You will need to make use of the conditional statements covered earlier in a while loop:
```R
i <- 1

while (i <=6) {
  print(i*i)
  i = i+1
}

[1] 1
[1] 4
[1] 9
[1] 16
[1] 25
[1] 36
```

In the code above, we tell R to print `i*i` or `i` multiplied by `i`, and then to add 1 to `i` to increment its value.

**Note: if we do not increment i by 1, then i will never reach 6 and the condition will never be satisfied. This will cause an infinite loop and depending on your laptop, may crash R**. 



# Lists

In contrast to vectors which must have the same data type, lists can store any type of object. To create a vector, we used the combine `c()` function to append items. To create a list we will be using the `list()` function to append items to a list. 

```{R}
my_list <- list("characters", 2.445, FALSE, NA)

print(my_list)

[[1]]
[1] "characters"

[[2]]
[1] 2.445

[[3]]
[1] FALSE

[[4]]
[1] NA
```



```{R}
typeof(my_list)
length(my_list)

[1] "list"
[1] 4
```

You can also store vectors in a list: 

```{R}
my_list <- list(c("character", "vector"), c(1,2,3,4,5))

print(my_list)

[[1]]
[1] "character" "vector"   

[[2]]
[1] 1 2 3 4 5
```

Furthermore, you can name the elements in your list. This is an extremely useful function that is a precursor to calling column names in a dataframe, which will be covered in next weeks workshop. To do this you will have to use the `names()` function, placing the name of your list within the parentheses and supplying a character vector for each item in the list: 

```R
list_data <- list("Red", "Green", c(21,32,11), TRUE, 51.23, 119.1)

names(list_data) <- c("Color1", "Color2", "vector", "logical", "float", "float")

print(list_data)

$Color1
[1] "Red"

$Color2
[1] "Green"

$vector
[1] 21 32 11

$logical
[1] TRUE

$float1
[1] 51.23

$float2
[1] 119.1
```

To access a specific value in a list, we call the list object and use a `$` to indicate we want to access an item:

```R
list_data$Color1

[1] "Red"
```

This is in contrast to vectors where a numeric must be supplied (e.g `my_vector[4]` accesses the 4th item), however if your list contains a vector we can combine the two methods!

```R
list_data$vector[2]

[1] 32
```



#### Looping over lists

Looping over elements in a list is the same as a vector:

```R
dataList=list("Hello", c("USA", "Red", "100"), c("India", "Blue", "76"))

for(i in dataList){
    print(i)
}

[1] "Hello"
[1] "USA" "Red" "100"
[1] "India" "Blue"  "76" 
```

However to loop over every item in the lists elements, we will need to introduce a nested for loop. Think of it as follows, you have been asked to visit every classroom in a school, in each classroom you have to count the number of students in the classrooms:

```R
#pseudocode

for(classrooms in school){
    for(students in classroom){
        counts students
    }
}
```

Previous code example:

```R
for(i in dataList){
    for(j in i){
        print(j)
    }
}

[1] "Hello"
[1] "USA"
[1] "Red"
[1] "100"
[1] "India"
[1] "Blue"
[1] "76"
```

In the above code we assign the list items to the variable `i`. In the second for loop, we iterate over the elements of `i` (assigned to variable `j`). Be careful when constructing loops and nested loops that the notation follows `for(){}`. 

# Importing Packages

R’s popularity is also largely due to the many fantastic packages available in the language!  A package is a bundle of code that makes coding certain tasks easier.  There are all sorts of packages for all sorts of purposes, ranging from visualising and cleaning data, to ordering pizza or posting a tweet. This is why you might hear them differentiate packages from “`Base R`.” `Base R` refers the R language by itself and  all that it can do without importing any packages.

Base R is very powerful, but most of the time, you’ll want to import a package to make your life easier. You only need to run this command the first time you install a package, after that there is no need to run it:

```R
install.packages('package-name')
```
To import a package simply:
```R
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

An example of a package on bioconductor is `fgsea`. The tool itself is not important for these exercises. Practice downloading and installing `fgsea` via bioconductor by googling "fgsea", or visit the package site [here](https://bioconductor.org/packages/release/bioc/html/fgsea.html). Bioconductor packages contain a code snippet you can copy and paste to complete the download: 
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
* Create user defined functions (UDF)
* Iterate over items in vectors and lists using a for loop
* R programmers have published lots of useful packages that specialize in different tasks, which are all available for you to use in your programs after you install and load them

