# NumPy

NumPy is a linear algebra library for python. It is an important package to learn as many data science packages use it as a foundation that they build upon.

The reason we are using NumPy to learn about working with dataframes is because of NumPy arrays. 

NumPy arrays are either 1 dimensional (vectors) or two dimensional (matrices).

## Installing NumPy in Anaconda

To install NumPy go to the command line/terminal and type the following:

`conda activate name_of_your_python_environment_in_anaconda`

`conda install numpy`

## NumPy Arrays

We can turn Python objects, such as lists, into arrays.

```python
#first import numpy and rename it np for ease of use
import numpy as np

#create your list as normal and print it
my_list = [1,2,3,18,93,33]
print(my_list)

#turn your list into an array and print it.
#compare your list output with your array output
my_array = np.array(my_list)
print(my_array)
```



So why would we want to use an array instead of a normal list?
With arrays it becomes much easier to subset and work with data.

### Subsetting data with NumPy

```python
#filter an array based on a certain condition
my_array_conditioned = my_array[my_array > 20]
my_array_conditioned

#this shows the boolean values for this  chosen condition
#it will go through the array and only keep the items
#for which the boolean value, at that values index, is true
print(my_array > 20)
my_array

'''
[1,2,3,18,93,33]
[False, False, False, False, True, True]
1 = False, 2 = False, 3 = False, 18 = False, 93 = True, 33 = True

So we get out only the items which = True and in this case that is
[93, 33]
'''

```

If we wanted to do the previous filtering on a list object we would have had to write a for loop and check each item individually with conditional statements and assign the result to a new list.

### Creating Matrices in Python using NumPy

To create a matrix in python we can use a lists of lists. This is a list object which contains a list at each index.

```python
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(my_matrix)
my_matrix = np.array(my_matrix)
print(my_matrix)
```

Notice how the lists of lists is one dimensional and the matrix is now two dimensional. We have created columns and rows using NumPy.



NumPy has its own range function which is `.arange()`

We can use this to create arrays based on a range of values instead of typing out a list or a list of lists

```python
#Arguments to pass for arange() are (start point, end point, step size)
my_array_arange = np.arange(0,101,5)
print(my_array_arange)
```

Slightly different from `.arange()` is `.linspace()` which will return an array of numbers with the third argument determining how many numbers will be in the array unlike in `.arange()` where the last argument is the step size



```python
#number of points you want between the range is denoted by third argument.
#the arguments which are passed are:
#(start point, end point, amount of numbers)

print(np.linspace(0,5,10))
#this prints 10 numbers between 0 and 5. These 10 numbers are equally spaced apart.
```



If you need to create an empty array to fill later there are methods to do this.
these are `.zeros()` and `.ones()`, there is also a method to create an identity matrix `.eye()` which is something that is commonly used in linear algebra.

```python
#to create a 1 dimensional vector pass the .zeros() one number
np.zeros(3)

#to create a 2 dimensional array pass in a tuple 
#which is in the form (rows,columns)
np.zeros((100,5))

#.ones() takes the same arguments are .zeros(), 
#the ouput is just different
np.ones((3,4))

#to create an identity matrix, you pass in one argument as
#identity matrices are always square. 
#This will create a 10x10 identity matrix
np.eye(10)
```

### Random number arrays in NumPy

We can create arrays filled with random numbers using the NumPy `.random`
method. `random` comes with many different methods to allow you to sample random numbers from different distributions.

```python
#to create a one dimensional array from a uniform distribution between 0 and 1, pass in one number
np.random.rand(10)

#a two dimensional array from the uniform distribution takes two arguments
np.random.rand(5, 5)

#if you want the normal distribution distributed around zero,
#use randn() instead.
np.random.randn(5, 5)

#to create an array of random numbers given a range of values,
#use .randint(), the arguments for this are (start, end, amount of random numbers wanted)

random_array = np.random.randint(1,100,20)
print(random_array)

#see the NumPy documentation for all of the different distributions
#that you can sample from

```

### NumPy array details

Finding details about an array is trivial with NumPy. We can find the max or min values which is useful when it comes to plotting the data. Knowing the shape of the data is important when we want to filter it and the data type of the values is needed before we start doing operations with the data.

```python
#for finding the max value in your array
random_array.max()

#for finding the min value in your array
random_array.min()

#what is the shape of our array?
random_array.shape

#are our data values in the array intgers or strings etc?
random_array.dtype

```

### NumPy array indexing and operations

NumPy indexing is based on the indexing we learned for lists. You can review last weeks material if you need to understand what is happening here.

```python
#to grab the value at index 4
random_array[4]
#to grab the items from index 1 up to index 5
random_array[1:5]
```

NumPy combines slicing with updating to easily update an array of values

```python
#if we wanted to update the first 3 values in a list
my_list = [0, 1, 2, 3]
my_list[0:3] = 10
#This will result in an error

#in NumPy this is easy to do
random_array[0:3] = 10

#remember when we had to write a for loop to 
#add a 1 to each number in our list?
#in NumPy:
print(random_array)
random_array = random_array + 1
print(random_array)

#only some values?
random_array[0:3] = random_array[0:3] + 1

#to add two whole arrays together use concatination
my_other_array = np.random.randint(1,50,20)
added_array = random_array + my_other_array

#NumPy arrays support all of the usual Python
#Python operators we have learned
random_array * random_array
random_array ** random_array
random_array / random_array
random_array - random_array

#some extra functions offered by NumPy, a full list
#is available in the NumPy documentation
np.sqrt(random_array)
np.log(random_array)
np.exp(random_array)
```

### Reshaping arrays

NumPy is so useful because of how easy it makes filtering or reshaping data.
`.reshape()` allows us to change the numbers of rows and columns in our data.
We can use this on our one dimensional random array to create a 2d array.

```python
#reshape the array into a (5 row, 4 column) matrix
random_array_2d = random_array.reshape(5,4)
print(random_array_2d)
```

How do we index two dimensional arrays? We use bracket notation.

```python
#The first value contains the row and the second value 
#contains the column
random_array_2d[0,1]

#if we want multiple rows or columns we use slice notation
#within the brackets
random_array_2d[2:4, 0:3]

#to get the transpose of an array use .T
random_array_2d.T
```

