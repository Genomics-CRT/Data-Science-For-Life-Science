## Data Visualisation in R - Learning Materials

### Contents:

- [Introduction](https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/Data_Visualisation_in_R-Learning_Materials.md#introduction)
- [Plotting in base R](https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/Data_Visualisation_in_R-Learning_Materials.md#plotting-in-base-r)
- [Plotting with `ggplot2`](https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/Data_Visualisation_in_R-Learning_Materials.md#plotting-with-ggplot2)
  - [*Tidy data*](https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/Data_Visualisation_in_R-Learning_Materials.md#tidy-data)
  - [*A Grammar of Graphics*](https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/Data_Visualisation_in_R-Learning_Materials.md#a-grammar-of-graphics)
  - [*Building a ggplot*](https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/Data_Visualisation_in_R-Learning_Materials.md#building-a-ggplot)
  - [*Saving your work*](https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/Data_Visualisation_in_R-Learning_Materials.md#saving-your-work)

- [Other packages and resources](https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/Data_Visualisation_in_R-Learning_Materials.md#other-packages-and-resources)
  - [*Packages*](https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/Data_Visualisation_in_R-Learning_Materials.md#packages)
  - [*Resources*](https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/Data_Visualisation_in_R-Learning_Materials.md#resources)
- [Summary](https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/Data_Visualisation_in_R-Learning_Materials.md#summary) 

<br/>

---

### Introduction

One of the most important facets of data science is data visualisation and R is pretty powerful and easy to use when it comes to creating visualisations. This tutorial will cover how to create visualisations in R mainly using the `ggplot2` package. This tutorial will not cover the principles of what makes a good data visualisation but there are plenty of resources out there (the gospel being [the works of Edward Tufte](https://www.edwardtufte.com/tufte/)) and also plenty of examples of what to avoid when creating a visualisation (see [this graph of coronavirus case numbers recently featured on Fox News](https://twitter.com/Carnage4Life/status/1246579721585868800?s=20)).

<br/>

----

### Plotting in base R

There are plenty of R packages out there specifically for data visualisation but even base R has some basic plotting capabilities. 

<p align='center'>
<img src='https://media0.giphy.com/media/l1KdbHUPe27GQsJH2/200.gif' width=60%>
</p>



Functions such as `plot`, `hist`, `boxplot` and `barplot` won't necessarily produce publication-ready graphs but can be quite useful for getting a quick idea of what your data looks like.

- `plot()` accepts an `x` and `y` argument, which correspond to the values to be plotted on the x and y axes respectively. These `x` and `y` arguments should be vectors of equal length. If only one argument is passed to `plot()` it will assume these values correspond to the y axis and the index (position in list) of each point is plotted on the x axis.

  

  <details>
    <summary><b>See An Example</b></summary>
  
  
  ```R
  # simulate data
  x_vals <- rnorm(n = 100, mean = 20, sd = 5) # generates a vector of 100 random numbers from a normal distribution with mean=20 and sd=5
  y_vals <- rnorm(n = 100, mean = 10, sd = 10)
  
  # plot data
  plot(x = x_vals, y = y_vals)
  ```
  
  
  <p align='center'>
  <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/basic_plot.png' width=60%>
  </p>
  
  ```R
  plot(x_vals)
  ```
  
  <p align='center'>
      <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/basic_plot2.png' width=60%>
  </p>
  
  
  
  </details>
  
  By default, `plot()` will output a scatterplot but this can be changed with the `type` argument. Some useful `plot` arguments are listed below:
  
  - `type` - specify which type of graph to plot ('l' for line, 'p' for points, 'b' for both or 'o' for overplot).
  
  - `col` - specify colour. Will accept a string such as 'red' or an integer which corresponds to base R's default colour palette.
  
  - `lty` - if plotting a line, will specify which type of line to plot (1 for solid line, 2 for dashed line).
  
  - `pch` - if plotting points, will specify the shape of points to be plotted (1 for empty circle, 16 for filled circle, see more [here](https://www.datanovia.com/en/wp-content/uploads/dn-tutorials/ggplot2/figures/106-pch-in-r-r-pch-list-showing-different-point-shapes-in-rstudio-1.png)).
  
  - `xlim`, `ylim` - specify limits for the x and y axis respectively. Will accept a vector with a minimum and maximum value.
  
  - `xlab`, `ylab` - specify labels for the x and y axis respectively.
  
  - `main` - specify title for the plot.
  
    
  
  There are also some commands that can be run after `plot` to add to the graph that has just been plotted.
  
  - `points` - add another dataset to the graph.
  
  - `abline` - add a line to the graph.
  
  - `text` - add text to the graph.
  
  - `legend` - add a legend to the graph.
  
  - `title` - change the graph titles (main for main plot title, sub for subtitle and xlab and ylab for x and y axis labels respectively).
  
    
  
  
  
  <details>
    <summary><b>See A More Complicated Example</b></summary>
  
  
  ```R
  # set up a dataframe
  df <- data.frame(date = seq(as.Date('2020-04-01'), as.Date('2020-04-14'), by = 1),
                   n_total_cases = c(3235, 3447, 3849, 4273, 4604, 5111, 5364, 
                                     5709, 6224, 7393, 8089, 8928, 9655, 10647),
                   n_new_cases = c(325, 212, 402, 424, 331, 507, 253, 
                                   345, 515, 1169, 696, 839, 727, 992))
  
  # plot # of total cases per day
  plot(x = df$date, y = df$n_total_cases, type = 'o', col = 'aquamarine', pch = 16,
       xlab = '', ylab = '', ylim = c(min(df$n_new_cases), max(df$n_total_cases)))
  # add # of new cases per day
  points(df$date, df$n_new_cases, type = 'p', col = 'indianred', pch = 15)
  # add line and text 
  abline(v = as.Date('2020-04-10'), lty = 2, col = 'grey65')
  text(x = as.Date('2020-04-10'), y = 3000, labels = 'Lockdown extended \nby 3 weeks')
  # add a legend
  legend('topleft', lty = 1, lwd = c(1, 0), pch = c(16, 15), col = c('aquamarine', 'indianred'), 
         legend = c('# of total cases', '# of new cases'))
  # add titles
  title(main = 'Coronavirus Case Number in Ireland (April 1st-14th)',
        sub = 'Data source: World Health Organisation')
  ```
  
  <p align='center'>
      <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/cov_plot.png' width=80%>
  </p>
  
  </details>

<br/>

- `hist()` - accepts one variable and will plot a histogram of its distribution.

- `boxplot()` - accepts any number of numerical variables and plots a boxplot of each of them.

- `barplot()` - accepts any number of numerical variables, each of which specifies the height of a bar.

  <details>
    <summary><b>See An Example</b></summary>

  ```R
  # simulate data
  df <- data.frame(Case = rnorm(1000, 80, 40),
                   Control = rnorm(1000, 200, 80))
  
  # plot data
  par(mfrow = c(2, 2)) # this sets up a grid with 2 rows and 2 columns so we can plot multiple graphs beside each other
  hist(df$Case, col = 'deeppink', main = 'Distribution of case values', xlab = 'Value', xlim = c(min(df), max(df))) # plot a histogram of case values
  hist(df$Control, col = 'darkorange', main = 'Distribution of control values', xlab = 'Value', xlim = c(min(df), max(df))) # plot a histogram of control values
  boxplot(df, col = c('deeppink', 'darkorange'), frame = FALSE, horizontal = TRUE) # plot a boxplot of case and control values
  barplot(c(mean(df$Case), mean(df$Control)), col = c('deeppink', 'darkorange'), names = c('Case Mean', 'Control Mean')) # plot a barplot of the average value for case and control
  ```

  <p align='center'>
      <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/other_base_plots.png' width=80%>
  </p>

  </details>
  
  <br/>

------

### Plotting with `ggplot2`

<p align=center>
    <img src='https://github.com/tidyverse/ggplot2/raw/master/man/figures/logo.png' width=15%>
    <img src='https://tidyverse.tidyverse.org/articles/tidyverse-logo.png' width=15%>
</p>

#### Tidy data

`ggplot2` is an R package for data visualisation that was created by Hadley Wickham in 2005 and is also a part of the [tidyverse](https://www.tidyverse.org/) - a collection of R packages for data science. These packages all share an underlying design philosophy based on the concept of 'tidy data'. You don't need to know how to use other tidyverse packages to use `ggplot2` but you should make sure your data is in 'tidy' format. This means that your data is stored in a dataframe where each row represents an observation and each column represents a variable. For example, `ggplot2` comes with a pre-loaded dataset called `mpg` - a dataframe that describes the fuel economy of different car models and can be viewed by running `data(mpg)`, followed by `View(mpg)`. Here, the observations are cars, so each row represents a single car and the variables (columns) are manufacturer, model, year etc. (to learn more about `mpg`, open its help page by running `?mpg`).

<p align=center>
    <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/mpg.png' width=68%>
</p>

<br/><br/>

#### A Grammar of Graphics

`ggplot2` is inpired by Leland Wilkinson's concept of a *Grammar of Graphics*  - which is a general scheme for building up data visualisations from semantic layers of components and is also the basis of many other data visualisation tools such as Vega-Lite and Tableau. Graphs are made up of a set of fundamental layers (shown below) - by defining each of these layers it is possible to plot virtually anything. Although this may seem more clunky and convoluted than plotting in base R, it is ultimately way more powerful.

<p align=center>
    <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/gg.png' width=35%>
</p>

<br/><br/>

#### Building a ggplot

ggplots are built in steps by first initialising the plot with the `ggplot()` function and then sequentially adding layers to the plot using other `ggplot2` functions. 

<p align=center>
    <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/ggplot_example.gif'>
</p>

<details>
  <summary><b>Show code</b></summary>

```R
ggplot(data = mpg, # initialise plot by specifying data and aesthetic mappings
       aes(x = hwy, y = displ, color = class)) +  
   geom_point() + # draw a scatter plot
   scale_color_manual(values = rainbow(7)) + # change the colors
   labs(title = 'Engine size vs. fuel efficiency', # add title & axis labels
        x = 'Highway miles per gallon',
        y = 'Engine displacement (litres)') + 
   theme_linedraw() # change the theme
```

</details>

<br/><br/>

<h5>Initialising the plot</h5>

As mentioned above, the `ggplot()` function will initialise a ggplot. You should pass two arguments to this function: 

1. The data to be plotted - this is very simply just the dataframe that you would like to visualise.
2. How that data should be mapped to different aesthetics - for example, which variables (i.e. columns) in the dataframe should be represented on the x and y axis.

A basic `ggplot()` call will look something like this: `ggplot(data = mpg, aes(x = hwy, y = displ))`. This tells ggplot that we want to build a plot with the `mpg` dataframe, we want the `hwy` column to be represented by the x axis and the `displ` column to be represented on the y axis. We could also specify other aesthetics, for example, if we wanted cars with different fuel types to be represented by different shapes on the graph, we could use shape as an aesthetic i.e. `ggplot(mpg, aes(x = hwy, y = displ, shape = fl))`. Other aesthetics that you can use to represent variables are colour, fill, alpha (transparency of data points) and size.

<br/><br/>

<h5>Geometries</h5>

If you tried running any of the snippets above to initialise a plot, you'll notice that nothing actually gets plotted by this call, it just draws a blank canvas. This is because we need to define the geometry layer and tell ggplot which type of plot we would like to draw. `ggplot2` defines the geometry layer by different geoms which are geometrical objects that a plot uses to represent data. Different geoms can be used to plot the same data. For example `geom_point()` will plot a scatterplot and `geom_smooth()` will plot a smooth line through the points. It is also possible to add multiple geoms to the same plot.

<p align=center>
    <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/geoms.gif'>
</p>

<details>
  <summary><b>Show code</b></summary>

```R
ggplot(data = mpg, aes(x = hwy, y = displ)) + # initialise plot
   geom_point() # draw scatterplot

ggplot(data = mpg, aes(x = hwy, y = displ)) + 
   geom_smooth() # draw a smooth line through the datapoints

ggplot(data = mpg, aes(x = hwy, y = displ)) +
   geom_point() +
   geom_smooth() 
```

</details>

Some other commonly used geoms include: 

- `geom_col()`- bar chart 
- `geom_vilolin()`-  violin plot
- `geom_histogram()`-  histogram 
- `geom_boxplot()`-  boxplot 
- `geom_density()`-  density plot 
- `geom_tile()` - heatmaps
- `geom_hline()`/`geom_vline()`-  horizontal/vertical line 

For a full list of available geoms see [here](https://ggplot2.tidyverse.org/reference/#section-layer-geoms). 

Different geoms have different aesthetic mapping requirements - for example, to draw a scatterplot `geom_point()` requires an x *and* y aesthetic, whereas to draw a histogram `geom_histogram()` will only accept *either* an x or y aesthetic. To see what arguments and aesthetics each geom will accept, you can run `?geom_X` (where X is whichever geom you're interested in). You will notice that it's also possible to define your aesthetic mappings in your `geom_X()` call as well as in your initialising `ggplot()` call, it shouldn't make a difference either way. You can also set fixed aesthetics in your `geom_X()` call  - for example if we wanted to uniformly change the colour or size of all points on a scatterplot, you can specify this in your `geom_point()` call as shown below. *Note:* this is different to defining an aesthetic mapping using `aes()` because here, the colour/size of points doesn't actually tell us anything about any of the variables in the data.

<p align=center>
    <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/geom_point.png'>
</p>

<details>
  <summary><b>Show code</b></summary>

```R
# draw a generic scatterplot (left)
ggplot(data = mpg, aes(x = hwy, y = displ)) + 
   geom_point()

# draw a scatterplot with fixed colour, size, shape points (right)
ggplot(data = mpg, aes(x = hwy, y = displ)) + 
   geom_point(colour = 'skyblue2', size = 5, shape = 17) 
```

</details>

<br/><br/>

<h5>Scales</h5>

The next layer of the plot that we can customise is the scales layer. For each aesthetic that you include in your `aes()` call, there is a corresponding scale that can be modified. For example, if you've defined x and y aesthetics, you can alter the x and y axis to have fixed limits or a fixed number of breaks. The function you use to update the x or y axis in this case will depend on whether the axes represent continuous or categorical variables. If the x axis represents a categorical variable you would use `scale_x_discrete()`, whereas if a continuous variable is being mapped to the x axis you would use `scale_x_continuous()` (for y axis, just replace x with y).

<p align=center>
    <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/scales.gif'>
</p>

<details>
  <summary><b>Show code</b></summary>

```R
ggplot(data = mpg, aes(x = class, y = displ)) + # initialise plot
   geom_col() + # draw barchart
   scale_x_discrete(limits = c('2seater', 'compact')) + # set the limits on the x axis
   scale_y_continuous(breaks = seq(0, 150, 10)) # set the breaks on the y axis
```

</details>

In the same way that there are scale functions to adjust the x and y aesthetics, there are also scale functions for other aesthetics including colour, size, shape and alpha. See shape example below.

<p align=center>
    <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/scale_shapes.png'>
</p>

<details>
  <summary><b>Show code</b></summary>



```R
# draw scatterplot with default shapes (top)
ggplot(mpg, aes(x = hwy, y = displ, shape = as.factor(year))) +
	geom_point()

# use scales to change shapes (bottom)
ggplot(mpg, aes(x = hwy, y = displ, shape = as.factor(year))) +
	geom_point() +
	scale_shape_manual(values = c(1, 2))
```

</details>

<br/>

*A note on colour*  :heart::yellow_heart::green_heart::blue_heart::purple_heart::black_heart::

If you're including colour as an aesthetic in your graph there are many ways to adjust the scales. If the colour is being mapped to a categorical variable, the easiest way is to use `scale_colour_manual()` - similar to `scale_shape_manual()` above - and specifying the colors you want to use. You can use strings e.g. 'red' to specify a colour or you can use hex colours (a six-digit combination of numbers and letters defined by its mix of red, green and blue, see [here](https://htmlcolorcodes.com/)). You can also use a predefined colour palette, such as the ones in the [RColorBrewer](https://rdrr.io/cran/RColorBrewer/man/ColorBrewer.html) package, using `scale_colour_brewer()`. If your variable is continuous you have similar options i.e. `scale_colour_continuous()` and `scale_colour_distiller()`. Some examples below.

<p align=center>
    <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/cat_cols.gif'>
    <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/con_cols.gif'>
</p> 

<details>
  <summary><b>Show code</b></summary>

```R
# create a basic plot with default colours for a categorical variable
p1 <- ggplot(data = mpg, aes(x = hwy, y = displ, colour = class)) +
		geom_point()

# change colours with scale_colour_manual()
p1 + scale_colour_manual(values = c('#2B1F4B', '#007C50', '#95EA58', '#FCC72E', '#F95C1F', '#FB003E', '#7C0063'))

# change colours with scale_colour_brewer()
p1 + scale_colour_brewer(palette = 'Dark2')

# ---

# create a basic plot with default colours for a continuous variable
p2 <- ggplot(data = mpg, aes(x = hwy, y = displ, colour = cty)) +
		geom_point()

# change colours with scale_colour_continuous()
p2 + scale_continuous(low = '#fce674', high = '#f5372a')

# change colours with scale_colour_distiller()
p2 + scale_colour_distiller(palette = 'YlGnBu')

# change colours with scale_colour_gradientn()
p2 + scale_colour_gradientn(colours = c('#00D281', '#F95C1F', '#FB003E'))

```

</details>

<br/><br/>

<h5>Facets</h5>

Faceting is a feature of `ggplot2` that allows you to split your plot into facets (subplots that each display one subset of the data), which is particularly useful when dealing with categorical variables. For example, suppose we wanted to look at the distribution of engine size (displ) values for different classes of cars - we could use a density plot to visualise these values and use colour as an aesthetic to represent class, as shown in the left figure below. However, this plot is very messy and it's difficult to tell the distributions apart - this is where faceting comes in handy. We can use `facet_wrap()` to split the plot into separate subplots based on class, that each display one density plot, as shown in the right figure below.

<br/>

<p align=center>
    <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/dens.png' width=45%>
    <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/facets.png' width=45%>
</p>

<details>
  <summary><b>Show code</b></summary>

```R
# to build the plot on the left
ggplot(mpg, aes(x = displ, fill = class)) + 
 	geom_density(alpha = 0.5) + # alpha changes the transparency of the density plots
	labs(title = 'Distribution of car engine sizes by class', x = 'Engine displacement (litres)') # adjust title and x axis label

# ---

# to build the plot on the right
 ggplot(mpg, aes(x = displ, fill = class)) + 
  	geom_density(alpha = 0.5, show.legend = F) + # we don't need the legend if we're using facets
 	labs(title = 'Distribution of car engine sizes by class', x = 'Engine displacement (litres)') + 
	facet_wrap(~class, nrow = 3) # this tells ggplot plot that we want our plot split into subplots based on class and we want the subplots in 3 rows
```

</details>

<br/><br/>

<h5>Coordinates</h5>

The default coordinate system in `ggplot2` is the Cartesian coordinate system where the x and y positions act independently to determine the location of each point. Occasionally (but not often), it is useful to be able to modify the coordinate system. For example, if you wanted to zoom in on a section of a plot, you can define x or y limits with `coord_cartesian()` - this is subtly different from setting x and y limits using `scale_x_X()` or `scale_y_X()` as those functions will remove points outside the limits from the plot whereas using `coord_cartesian()` just zooms in on a specific region of the plot so that points outside the limits are still there but we just can't see them anymore. Other coordinate functions that are sometimes useful are `coord_flip()` which will flip the x and y axis, and `coord_polar()` which converts coordinates to polar coordinates (useful for radar charts or pie charts). Examples of use cases for these functions are shown below.

 <p align=center>    
     <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/coords.gif'>   
</p>

<details>
  <summary><b>Show code</b></summary>

```R
# create a basic barchart
p <- ggplot(mpg, aes(x = class, fill = class)) +
         geom_bar(show.legend = F) +
         labs(title = '# of cars in each class')

# zoom in on a region of the barchart using coord_cartesian()
p + coord_cartesian(xlim = c(1, 4))

# turn regular barchart into a horizontal barchart using coord_flip()
p + coord_flip() 

# turn regular barchart into a radar chart using coord_polar()
p + coord_polar()
```

</details>

<br/><br/>

<h5>Themes</h5>

The final customisable layer of the graph is the theme, which relates to almost every part of the graph except the data points themselves. `ggplot2` comes with several pre-defined themes baked in (see 'Complete themes' [here](https://ggplot2.tidyverse.org/reference/#section-themes)), the default of which is `theme_grey()`, which is what is responsible for the grey background in all the ggplots we've created so far. To update the theme of your plot, just add a `+ theme_X()` call to your plot, where X is one of grey, bw, classic, linedraw, etc. See examples of the exact same plot but with different themes below.

 <p align=center>    
     <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/themes.gif'>   
</p>

<details>
  <summary><b>Show code</b></summary>

```R
# draw boxplot with default theme
p <- ggplot(mpg, aes(x = manufacturer, y = displ, fill = manufacturer)) +
         geom_boxplot(show.legend = F)  +
         labs(title = 'Car engine sizes (L)', x = NULL) 

# change the theme to linedraw, classic, dark
p + theme_linedraw() 
p + theme_classic()
p + theme_dark()
```

</details>

It is also possible to tweak the display of different components of an existing theme. For example, in the plot above you'll notice that text on the x axis is overlapping and impossible to read. We can fix this by using `theme()` to rotate the x axis text by 90&deg;.

 <p align=center>    
     <img src='https://github.com/Genomics-CRT/Data-Science-For-Life-Science/blob/master/Introduction_to_R/part_3/imgs/theme.gif'>   
</p>

<details>
  <summary><b>Show code</b></summary>

```R
p + # plot from previous image
  theme_linedraw() + # change theme to linedraw
  theme(axis.text.x = element_text(angle = 90)) # rotate x axis text
```

</details>

<br/><br/>

#### Saving your work

When you've decided that your plot is sufficiently beautiful and you want to save it as a png, you have a few options. 

- Using `png()` - this function will work for plots created using base R or `ggplot2`. The syntax follows the pattern below.

  ```R
  png('my_plot.png') # open connection to a new png file
  ggplot(mpg, aes(x = cyl, y = hwy)) + # draw the plot
    geom_point()
  dev.off() # close the connection
  ```

- Using `ggsave()` - this will only work for plots built using `ggplot2`. The syntax follows the pattern below.

  ```R
  ggplot(mpg, aes(x = cyl, y = hwy)) + # draw the plot
    geom_point()
  ggsave('my_plot.png') # save the plot to file called my_plot.png
  ```

- For both of these functions you can also specify a width or height argument e.g. `ggsave('my_plot.png', width = 20)`.

<br/>

----

### Other packages and resources

#### Packages

Although `ggplot2` is pretty powerful, there are many other R packages out there for enhancing your plots, some of which are extensions to `ggplot2`. Below is a list of some of the data visualisation packages I find particularly useful - to see examples of what each of them can be used for just click the links.

:package: [`ggforce`](https://ggforce.data-imaginist.com/) - Package with extra geoms such as `geom_ellipse()` and `geom_sina()` which is a nice alternative to `geom_violin()`.

:package: [`gganimate`](https://github.com/thomasp85/gganimate) - Package for creating animated graphs.

:package: [`patchwork`](https://github.com/thomasp85/patchwork) - Package that makes it ridiculously easy to create multiple subplots within a ggplot.

:package: [`cowplot`](https://cran.r-project.org/web/packages/cowplot/vignettes/introduction.html) - Another package for creating plot grids, also comes with some nice extra themes. 

:package: [`ggrepel`](https://cran.r-project.org/web/packages/ggrepel/vignettes/ggrepel.html) - Package with a useful `geom_label_repel()` function which is an alternative to the regular `geom_label()` function in `ggplot2`, which will find the best positions for labelling data points on a plot so that they don't overlap. 

:package: [`ggtext`](https://github.com/wilkelab/ggtext) - Package that allows you to turn text elements on a plot into markdown so they can be styled using markdown and html syntax, useful for making text bold, italic, coloured etc.

:package: [`paletteer`](https://github.com/EmilHvitfeldt/paletteer) - Package that combines colour palettes from many other packages. By far the most comprehensive collection of color palettes that I have found.

:package: [`viridis`](https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html) - Package with popular viridis colour palettes - comes with handy `scale_colour_viridis()` function.

:package: [`plotly`](https://plotly.com/r/getting-started/) - Package that uses JavaScript to make interactive plots. Can turn a ggplot into an interactive plot using handy `ggplotly()` function.

:package: [`gghighlight`](https://cran.r-project.org/web/packages/gghighlight/vignettes/gghighlight.html) - Package that makes it easy to highlight certain data points or series on your plots.

:package: [`ggannotate`](https://github.com/MattCowgill/ggannotate) - Package that launches an app to help you annotate your plots with text, arrows etc.

:package: [`gghalves`](https://github.com/erocoar/gghalves) - Package that allows you to make plots with half-half geoms e.g. half boxplot and half dotplot.

:package: [`corrplot`](https://cran.r-project.org/web/packages/corrplot/vignettes/corrplot-intro.html) - Package for plotting correlograms to show correlation between variables.

:package: [`ggbeeswarm`](https://github.com/eclarke/ggbeeswarm)  - Package for creating beeswarm plots - nice alternative to `geom_violin()`.

<br/><br/>

#### Resources

There is a tonne of information on the internet related to visualising data in R. Here are some resources you might find useful.

- [:page_facing_up: `ggplot2` Cheat Sheet](https://rstudio.com/wp-content/uploads/2015/03/ggplot2-cheatsheet.pdf) - A handy cheatsheet that somehow manages to condense this entire tutorial onto two concise pages.
- [:books: The Data Visualisation chapter of R for Data Science](https://r4ds.had.co.nz/data-visualisation.html) - This book is available for free online and is also the source of a lot of the material in this tutorial.
- [:bar_chart: The R Graph Gallery](www.r-graph-gallery.com) - This gallery contains every type of graph you can imagine and the code to build them in R.
- :cinema: YouTube tutorials - There are plenty of YouTube tutorials out there for data visualisation in R. I recommend [this playlist](https://www.youtube.com/watch?v=t6IIJEoqPyk&list=PLRPB0ZzEYegPa4uvvAVJnr6loSKbN4wLb) from Danielle Navarro which is suitable for R newbies, or [this playlist](https://www.youtube.com/watch?v=h29g21z0a68&t=23s) from Thomas Lin Pederson, one of the maintainers of the `ggplot2` package, which goes into detail about the *Grammar of Graphics* and how it is represented in `ggplot2`. 

<br/>

-----

### Summary

Here’s a summary of some of the concepts covered in this tutorial:

-  R is a great platform for data visualisation.
- You can create graphs in base R without having to load any packages, using functions such as `plot()`, `boxplot()` and `hist()`. 
- `ggplot2` is the most effective way of building data visualisations in R. 
- ggplots are made up of a combination of layers, each of which is customisable.

Hopefully by now I've convinced you that `ggplot2` is really cool and you can plot nearly anything with it if you have enough free time. Here's some proof:

- Someone has created a ggplot version of the distracted boyfriend meme ([source](https://twitter.com/Sicarul/status/1253325058161836036?s=20)).

  <p align=center>
      <img src='https://pbs.twimg.com/media/EWS0WN6UwAQ08e0?format=png&name=small' width=35%>
  </p>

- Somebody else has built a recreation of Pacman using `ggplot2` and `gganimate` and made all of the code available ([source](https://github.com/mcanouil/ggpacman)).

<p align=center>
    <img src='https://github.com/mcanouil/ggpacman/raw/master/man/figures/README-pacman-1.gif' width=40%>
</p>

- There is a whole community of "generative artists" who make beautiful pieces of art from data, using `ggplot2` and other R packages. See works below from [Danielle Navarro](https://djnavarro.net/art/) and [Thomas Lin Pederson](https://www.data-imaginist.com/art).  

<p align=center>
    <img src='https://live.staticflickr.com/65535/49762680033_0f6b0df13e_z.jpg' width=20%>
    <img src='https://live.staticflickr.com/65535/49696234021_d8eab35766_z.jpg' width=20%>
</p>

<p align=center>
    <img src='https://d33wubrfki0l68.cloudfront.net/bbcf693667de5a002d25d85e6232455921bdb4d3/855ba/art/007_storms/storms351_hub2582e41a7771db26553a293a4ffab8a_1704789_500x500_fill_box_center_2.png' width=20%>
    <img src='https://d33wubrfki0l68.cloudfront.net/0a511cb6df95ea9c03169d5b9cbbb5ec22e22f36/0be6e/art/005_genesis/genesis6400_hu31f8b6d6a3b3121f892b0a35dcb2bfca_139765_500x500_fill_box_center_2.png' width=20%>
</p>



<br/>

-----

<p align="center">
:sparkles: Happy Plotting :sparkles:
</p>

