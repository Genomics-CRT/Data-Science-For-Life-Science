# Pandas

Pandas is built on top of NumPy and it is used when working with dataframes, especially outside files which you load in.

The first thing to do is test to see if you have pandas installed in your anaconda environment.

Do do this you can type the following into Spyder:

```python
import pandas as pd
```

If you get an error saying pandas isn't found, do the following in the command line/terminal of your computer system.

```
conda activate your_anaconda_environment_name

conda install pandas
```

## Pandas Series 

A pandas series is similar to a NumPy array but with some slight differences which make them more user friendly.

```python
import numpy as np
import pandas as pd

#lets make a list of our pcr runs
pcr = ['one', 'two', 'three']

#and a list of the quality of the DNA from each run
quality = [1.9, 2.0, 1.7]

#lets make an NumPy array out of this just so we can compare
#between an array and a series
our_array = np.array(quality)

#and finally a dictionary containing all of the data in one
#variable
our_dict = {'one':1.9, 'two':2.0, 'three':1.7}
```

To create a pandas series we use the `Series()` function (note that capitalisation is important in python).

```python
#lets create a series using our data from before
pd.Series(data=quality)

#and we can compare this with our NumPy array
print(our_array)

#and this command shows why Pandas is so useful, we can specify
#what we want the index labels to be.
pd.Series(data=quality, index=pcr)

#Pandas can turn the NumPy array we made into a series
pd.Series(our_array, pcr)

#Using a dictionary is useful because the keys will turn
#into the index for our series
pd.Series(our_dict)
```

The importance of being able to specify our own labels makes looking up the data we want in a series very fast and easy. It also allows simple concatenation of series using python operators. 

```python
our_gene_counts = pd.Series([8,14,6], ['Gene_1','Gene_2','Gene_3'])
print(our_gene_counts)
print(our_gene_counts['Gene_3'])

our_gene_counts_2 = pd.Series([7,12,9], ['Gene_1','Gene_2','Gene_3'])

total_counts = our_gene_counts + our_gene_counts_2
print(total_counts)
```



## Pandas Dataframes

While Pandas series can be useful, the real reason that Pandas is used for data science is the Pandas DataFrames. A Pandas DataFrame can be thought of as multiple Pandas Series together which share the same index. I.e. each column in your DataFrame is a series and their rows are lined up based on their shared index. You can create a dataframe using many different types of data. 

```python
#this command means we can use randn() as shorthand for np.random.randn()
from numpy.random import randn

#we are using random numbers but if we want to get the same
#random numbers every time, we can set the seed that they are
#generated from
np.random.seed(8)

#in this command we use randn(5,4) to create a 5x4 matrix
#we pass this to pd.DataFrame() as the input data.
#We then pass in a list for the row names and then a list
#for the column names
our_df = pd.DataFrame(randn(5,4),['Gene_1', 'Gene_2', 'Gene_3', 'Gene_4', 'Gene_5'],['Experiment_1', 'Experiment_2','Experiment_3',
'Experiment_4'])

#print out the original 5x4 matrix and compare it to the new
#DataFrame that we created.
print(randn(5,4))
print(our_df)
```

### Data exploration

When you first load in a dataframe you will want to see what it looks like. This will help you write further commands to manipulate and analyse it as you will now know the index, the column names etc.

```python
#This command will print out the first two rows of the dataframe.
#This will tell us the names of the columns and the type of data we have
print(our_df.head(2))

#.tail() works much the same as .head but will give us information
#from the bottom of the dataframe
print(our_df.tail(3))

#This command will give us the shape of the dataframe as (#rows, #columns)
#This is an easy way to get the number of rows and columns in a dataframe
print(our_df.shape())

#To get a view of the summary statistics in a dataframe use .describe()
our_df.describe()

#You can get the transpose of a dataframe very easily, this can come in handy if
#you decide that it would be easy to work with the transpose version of the dataframe
our_df.describe().T
```

### Indexing Pandas DataFrames

Indexing DataFrames by column uses the same bracket notation that we have learned from lists, arrays, and series. If we want to index by row, we use the `.loc[]` or  `.iloc[]` methods.

```python
#get the data for the Experiment 3 column
our_df['Experiment_3']

#get the data for Experiments 1 and 4 only, note the double bracket
#notation.
our_df[['Experiment_1', 'Experiment_4']]


#How to index rows?

#If we want to use the index labels we use .loc[]
our_df.loc['Gene_1']

#if we want to use the index integer location itself we use .iloc[]
our_df.iloc[0]

#grabbing a specific value again in the form of (row, column)
our_df.loc['Gene_1', 'Experiment_3']

#grabbing multiple rows and columns
our_df.loc[['Gene_1', 'Gene_4'], ['Experiment_1'. 'Experiment_4']]

```

### Add new row and columns to a Pandas DataFrame

```python
#get another 5 random numbers.
new_column = randn(5)

#add a new column and call it 'New_Experiment'.
#be sure to specify that you want to give our new_column datathe same index as in our_df. 
#If we dont do this we end up with missing values
our_df['New_Experiment'] = pd.Series(new_column,index=our_df.index)

#check the result
print(our_df)

#To add a new row or rows we need to make a new dataframe which contains our
#column names so that we can append it correctly.
#You can append as many rows as you like so long as you have the correct column names

new_row= pd.DataFrame(randn(1,5), columns=our_df.columns, index=['Gene_6'])
our_df = our_df.append(new_row)
our_df
```

### Create a new column based on the values in another column

If you need to total up the values in every row of a dataframe how could you do this in a fast an efficient way? Without Pandas you would have to loop over every line of the dataframe one at a time, with Pandas you can use the vectorised arithmetic which comes builtin thanks to NumPy. This means it will compute the result for all rows at the same time.

```python
our_df['Total'] = our_df['Experiment_1'] + our_df['Experiment_2'] + our_df['Experiment_3'] + our_df['Experiment_4'] + our_df['New_Experiment']
print(our_df)
```

You can also use the `.apply()` method to apply a function across all rows or columns in your dataframe

```python
#This command will apply the mean method from numpy to all rows in the dataframe
#for columns use axis=0
our_df.apply(np.mean, axis=1)
```



### Drop columns or rows from a DataFrame

We can delete rows or columns by using the `.drop()` method.

By default the `.drop()` will try to delete rows. To delete columns we have to use `axis=1`. To explain axis we have to recall what we know about tuples.
The shape of our dataframe is now 6x6 or 6 rows and 6 columns or in tuple form:
(6,6) where tuple[0] is the rows and tuple[1] is the columns. So `axis=0` will refer to the first value in the tuple which defines the rows and `axis=1` will refer to the columns.

```python
#try it with the default option which is axis=0
our_df.drop('Total')

#add axis=1 to access the columns index
our_df.drop('Total', axis=1)

#you'll notice your dataframe has not actually changed
print(our_df)

#to make this change permanent you need to use inplace=True
our_df.drop('New_Experiment', axis=1, inplace=True)
print(our_df)
```

To Drop rows 

```python
our_df.drop('Gene_4', axis=0)

#or as we have seen that axis=0 is the default:
our_df.drop('Gene_4')

#and to make it permanent
our_df.drop('Gene_4', inplace=True)
```

Many times in data science we will come across messy dataframes which contain missing values. These missing values will disrupt our analysis and may stop commands from working properly causing misleading output. To drop rows or columns that contain NAs we use `.dropna()`

```python
missing_dict = {'First' : [12,22,np.nan],'Second':[10,np.nan,np.nan],'Third':[11,24,13]}
missing_df = pd.DataFrame(missing_dict)
print(missing_df)
missing_df_dropped_na = missing_df.dropna()
print(missing_df_dropped_na)

#to drop NAs based on columns
missing_df.dropna(axis=1)
#to add a threshold for how many NAs you will accept before dropping the row
missing_df.dropna(thresh=2)
#to change NAs to a value instead of dropping them
missing_df.fillna(value=0)

#to replace NAs in a specific column with a value based on the mean of that column
missing_df['First'].fillna(value=missing_df['First'].mean())
```



## Filtering DataFrames

Filtering of values in a Pandas DataFrame is very similar to how we did it in NumPy arrays. We use boolean values to extract only the values which equal True after we have placed conditions on the data.

If it helps, you can think of these as very very condensed for loops with an if else flow control, we loop over each row in the dataframe and if it equals True: we keep it, else if it equals False: we get rid of it.

```python
#have a look at the boolean output of this
our_df['Experiment_1'] > 0

#now we pass this to our dataframe by encapsulating it in our_df[]
our_df[our_df['Experiment_1'] > 0]

#lets store this in a variable so we can work on it some more
exp_1_less_than_zero = our_df[our_df['Experiment_1']<0]

#What if we only want to see the data for Experiment_1 and
#Experiment_4 when Experiment_1 is less than 0?
#note the double brackets.
exp_1_less_than_zero[['Experiment_1', 'Experiment_4']]

#all of this can be done in one line once you get used to Pandas
our_df[our_df['Experiment_1']<0][['Experiment_1','Experiment_4']]

#as we saw with filtering lists and arrays, you can filter by
#multiple conditions to really control your data. note the
#brackets here to keep the conditions separate.
#`&` here works similar to `and` that you learned from conditioning variables last week.

our_df[(our_df['Experiment_1']>0) & (our_df['Experiment_4']>1)]

```

### Giving DataFrames a new index

Sometimes we get new information on our data and we need to update our dataframes to reflect this. In our example dataframe we only have Gene_1, Gene_2 etc. but what would we do if we got the actual names of the genes?
We would need to update the index. We can do this by using `.set_index() `and passing it a list of values

```python
#create a new list of gene names. Recall .split() will 
#convert strings into lists based on the character you
#give it as an argument, here we just use a space
new_index= 'BRCA1 BRCA2 P53 RB APC CDK1'.split(' ')

#create a new column called 'Gene Names' with these gene names
#as the values, the same way we added a new column previously
our_df['Gene Names']= new_index

#finally, turn this column into the index with .set_index()
our_df= our_df.set_index('Gene Names')
print(our_df)

#https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
```

### Creating and working with a multi-indexed DataFrame

A lot of times a single index will not be sufficient to deal with the complexity of a dataframe. This can be especially true in the life sciences where an experiment can have multiple treatments, controls, and experiment runs. 

```python
#first lets create two lists which contain the index values we will want to use
#in this case we have three experiments with a test/control for each.
exp_groups = ['Test', 'Test', 'Test', 'Control', 'Control', 'Control']
exp_number = [1,2,3,1,2,3]

#the zip() function here will stick together both of our lists by their index values
#notice how each tuple in the list contains the values at each index of both lists
print(list(zip(exp_groups,exp_number)))
#save this in a variable to use later
exp_levels = list(zip(exp_groups,exp_number))

#now we can use these tuples to create a multiindex variable.
#https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html
exp_index = pd.MultiIndex.from_tuples(exp_levels)
exp_index
#now lets create a random dataframe that has 6 rows and two columns using the following
#command. the data: randn(6,2), the index: exp_index, 
#the column names: ['Treatment_1', 'Treatment_2']
exp_df = pd.DataFrame(randn(6,2), exp_index, ['Treatment_1', 'Treatment_2'])

#have a look at the dataframe and notice that the two index columns have no name
exp_df
#now use .index.names to give the multiindex their names
exp_df.index.names = ['Groups', 'Exp_Number']
#now look at the dataframe and notice the index names
exp_df

#lets use these names to start filtering the dataframe
#we can filter using one .lo[] method
exp_df.loc['Test']

#or chain .loc[] methods to dive deep into the data
exp_df.loc['Test'].loc[1]
exp_df.loc['Test'].loc[1].loc['Treatment_2']

#if we want to skip index levels we can use .xs()
exp_df.xs('Test')

#here we skip the test or control index and go straight to the Exp_Number sub index
#and pull out row 1. This is useful when you have many index levels and would have to 
#chain lots of .loc[] together. It is much more readable this way.
exp_df.xs(1,level = 'Exp_Number')
```

## Merging two dataframes based on a common column

Many times we will generate similar dataframes at different time points and will want to join these into one single large dataframe. This is trivial in Pandas by using the `.merge()` function



```python
#merging two data frames based on a matching column

first = pd.DataFrame({'Experiment': ['1', '2', '3', '4'],
                     'Control_1': ['30', '45', '40', '40'],
                     'Treatment_1': ['3', '4', '3', '2']})
   
second = pd.DataFrame({'Experiment': ['1', '2', '3', '4'],
                          'Control_2': ['32', '36', '42', '45'],
                          'Treatment_2': ['30', '28', '37', '42']})  

#both dataframes have matching values in the 'Experiment' columns, this will be used
#to as the key (on) for merge.
merged_df= pd.merge(first, second,how='inner',on='Experiment')
merged_df
```



## Importing DataFrames from outside sources

Up until now we have looked at how we can create DataFrames from scratch, this is important to know in order to master pandas. Now we will look at importing already created dataframes into pandas to analyse. 

We can import csv files for pandas using the `pd.read_csv()`function. 
Download the cases_time.csv file from this weeks python page on the  Genomics CRT GitHub and make sure you move it to your working directory which can be found running the function `pwd()`.

```python
#First we read in the data using pd.read_csv()
corona_data_local = pd.read_csv('cases_time.csv')

#Take a look at what the data looks like. This is always the
#first step in any data analysis. use .head(3) to look at the first
#three rows of the dataframe.
corona_data_local.head(3)

#We can see that pandas has given the dataframe an integer index after it was read in
#if we want to specify what index to give the dataframe
#we use index_col= , and give it a column number.
#in this case the first column in the dataframe is the country name
#this would be perfect to use as an index, so
#redo the command but this time pass in index_col=0
corona_data_local = pd.read_csv('cases_time.csv', index_col=0)

#Now look at the dataframe and see that it is indexed correctly
corona_data_local.head(3)

#Now that is indexed correctly we can use .loc[] to filter the
#dataframe so that it only has the rows related to Ireland
ireland_corona_data_local = corona_data_local.loc['Ireland']

#Lets output this dataframe to a new csv file using .to_csv()
#so that it is easier to work with in the future.
ireland_corona_data_local.to_csv('irish_corona_data.csv')
```

This works well but we can skip downloading and saving the entire dataframe by passing a URL to pandas.

```python
#first save the URL
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_time.csv'

#next, pass the url link to pd.read_csv()
corona_data = pd.read_csv(url, index_col=0)

#look at the data and filter as we did locally
print(corona_data.head(2))
ireland_corona_data = corona_data.loc['Ireland']
ireland_corona_data.to_csv('irish_corona_data_current.csv')

```

## Visualisation of DataFrames using Pandas

You will be learning more about visualisation in python next week but if you want to see what can be done with a few extra commands passed to pandas then keep reading here.

Pandas has some built in matplotlib capabilities which can be used as a good starting point in checking to see what the data you are working with actually looks like. Matplotlib is a package which can be installed the same way we installed NumPy and Pandas.



```python
#%%
#Lets look at the deaths in Ireland as a result of Covid19
#First we can subset out ireland_corona_data into the two columnswe want which are Deaths 
#and Last_Update (date). We would like to work with the data as the index so use
#.set_index('Last_Update'). You can use this .set_index() method at any time to change your
#dataframes index.  .plot tells pandas to create a plot of the data and .line() will specify
#a line graph. row=45 will just rotate our x axis ticks so that they are more readable
death_plot=ireland_corona_data[['Deaths','Last_Update']].set_index('Last_Update').plot.line(rot=45)

#to set the labels for the graph use .set() method and pass in your labels. This line
#and the previous line have to be run together in order for the labels to show up on the
#graph so either create a cell block or highlight both lines and press f9
death_plot.set(xlabel='Date', ylabel='Deaths', title='Coronavirus deaths in Ireland')
#%%

#to save our figure to our working directory import pylot from matplotlib and use .savefig()
#, bbox_inches='tight' will limit the amount of whitespace around your image, this is not
#necessary but is useful
from matplotlib import pyplot as plt
plt.savefig('death_plot_17042020.png', bbox_inches='tight')


#the figure we created before had a lot of non-useful information, lots of early days
#without any deaths. We can subset the dataframe using the conditional filtering
#we learned earlier ireland_corona_data[ireland_corona_data['Deaths'] > 0]
#will create a dataframe containing only the rows that have a value greatert than 0 in the
#death column so it will start on the date of the first death. The rest of the command is
#the same as before.

#%%
corona_plot_first_death = ireland_corona_data[ireland_corona_data['Deaths'] > 0][['Deaths', 'Last_Update']].set_index('Last_Update').plot.line(rot=45, x_compat=False)
corona_plot_first_death.set(xlabel='Date', ylabel='Deaths', title='Coronavirus deaths in Ireland')
#%%
plt.savefig('corona_plot_first_death_17042020.png', bbox_inches='tight')
```



# Some links to check out

Pandas documentation  
https://pandas.pydata.org/docs/



Pandas documentation tutorials  
https://pandas.pydata.org/docs/user_guide/index.html#user-guide



Geeksforgeeks have a nice intro and a table with commonly used pandas methods  
https://www.geeksforgeeks.org/python-pandas-dataframe/



The dataquest pandas cheat sheet is always useful to check if you are stuck  
https://www.dataquest.io/blog/pandas-cheat-sheet/