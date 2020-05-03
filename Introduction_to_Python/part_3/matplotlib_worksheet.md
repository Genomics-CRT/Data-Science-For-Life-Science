
### Worksheet 

The following questions will be centred around creating different plots - the answers will be entirely subjective for the most part, with how you approach the problem entirely up to personal preference. 

### Question 1

Create a simple lineplot of cumulative coronavirus deaths in Ireland vs. United Kingdom using the following [data](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_time.csv). Be sure to label the x axis with dates (Last_update object). 


If this looks a little hard to read, try to adjust the scale (maybe plot on a log scale?). 


**Hint - use np.log() for transformations if using matplotlib - ie use np.log(data) inside the plot object**

Try adding another country to this comparison - I would suggest France

### Question 2 


Create a gridded set of plots to visualise the relationship between sepal length and sepal width across 3 species and in all species using the iris [dataset](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv). 

**Note - if using matplotlib with plt.subplots, you'll have to refer to declared axes like this - 
`fig,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2)` where the first set of axes (ax1 and ax2) refer to the first row and the second (ax3 and ax4) refer to the second row, and so get their own set of brackets**

### Question 3

Create a plot to visualise the differences between petal length across species.

Do the same on a different scale (log)
