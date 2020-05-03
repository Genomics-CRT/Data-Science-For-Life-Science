#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:39:20 2020

@author: stephen
"""

# =============================================================================
# [1] Reading in a CSV file
# =============================================================================

# [i] Download and save the .csv file located in this weeks github folder
import pandas as pd
import numpy as np
# [ii] Open the csv file using pandas and save it to a variable
my_df = pd.read_csv("example_csv.csv", index_col=0)


# =============================================================================
# [2] Data exploration
# =============================================================================

# [i] Explore the top and bottom of the data
my_df.head(2)
my_df.tail(2)

# [ii] How many rows and columns does the data have?
my_df.shape

# [iii] Get the transpose of thise dataframe. Would it be better to use this?
df_T = my_df.transpose()


# [iv] Get the summary statistics of the data and save it to a variable
stats = my_df.describe()

# [v] Using what you know about indexing Dataframes
#      pull out the value of the standard deviation for Wed
#      from the variable you created in [2][iii]
std_wed = stats.loc['std', 'Wed']
std_wed
# =============================================================================
# [3] Indexing dataframes
# =============================================================================

# [i] Select the information for the 'Tue' column only and assign it to a variable
tues = my_df['Tue']
tues
# [ii] Select rows 20 to rows 50
my_df.iloc[20:51]

# [iii] Select only the weekday columns
my_df.loc[:,'Mon':'Fri']

# =============================================================================
# [4] Dropping and adding information
# =============================================================================

# [i] Drop the weekend columns and drop any row of your choice
my_df.drop(['Sat','Sun'], axis=1, inplace=True)
my_df.drop([99], inplace=True)


# [ii] Change all NAs in the dataframe to 0
my_df = my_df.fillna(0)
my_df
# [iii] Filter the dataframe so that it only contains the rows
#      where the 'Mon' column is greater than 50 (it will still contain all columns)
my_df = my_df[my_df['Mon']>50]
my_df

# [iv] Create a new column that is Mon column multiplied by 10
my_df['Mon*10'] = my_df.Mon * 10
my_df

# [v] Create a new row with any 6 values and add it to your dataframe
new_row = pd.DataFrame(np.random.randint(100, size=(1,6)), columns=my_df.columns)
new_row

my_df.append(new_row, ignore_index=True)

# =============================================================================
# [5] Outputting a file
# =============================================================================

# [i] Output your modified cvs file to your working directory
my_df.to_csv('Modified_exampe_csv.csv')
