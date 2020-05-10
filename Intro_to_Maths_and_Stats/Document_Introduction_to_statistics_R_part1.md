# Introduction to Statistics in R Worksheet. Part 1.

** DISCLAIMER **

​	I will try to explain the basics of statistics using very simple words which might not be fully mathematically correct, but in this way it's far short and more easy to understand. 

​	Apparently it's not possible to explain all statistics concepts in one tutorial, so I hope that most of you are already familiar with it to some extent and everything will be pretty obvious for you :) 

​	If not, don't be shy, post your question on git-hub issues or try to Google it. 

---------------------------------------------------------------------------------------------------------------------------

Here will be 3 documents for 1 week. 

* part 1: descriptive statistics for one variable (measures of central tendency, variability, quantiles), descriptive statistics for dataframe, Central Limit Theorem, confidence interval for mean. 

* part 2: hypothesis testing, 2-samples comparison (T-test, non-parametric test), correlation tests (parametric and non-parametric) 

* part 3: linear regression analysis 


## Libraries

First, you need to install and include libraries. 

```{r}
#to install library:
#install.packages('ggplot2')

#to include library:
library(ggplot2) # visualisation 
library(dplyr) # data frame manupulation 
library(tidyr) # data frame manupulation 
library(psych) # descriptive statistics for data frame 
library(Rmisc) # confidence interval
library(car) # LeveneTest

# if you want to suppress package sturtup messages:
suppressPackageStartupMessages(library(ggplot2))
```

## Descriptive statistics for one variable

​	Before starting any statistical analysis, it's important to perform an exploratory analysis first. There are simple functions in R which can help you with that. Let's start with some basic part of descriptive statistics in R. 

​	First of all, we are going to discuss descriptive statistics for a single random variable, which can be simply presented as a vector. As a reminder, a <i> random variable </i> is a variable whose value is the outcome of a random event, e.g. a random variable could be the outcome of the roll of a dice or the flip of a coin, or height of a male person in a population. 

```{r}
# let's open data frame with pre-generated data
# it contains variable 'var' we are going to work with
set.seed(123)
var <- read.table('datasets/data_for_distribution_plot.txt', sep='\t')

head(var)

[1]    var
  1	-0.2384994			
  2	0.1083136			
  3	1.9866437			
  4	0.4240338			
  5	0.4857521			
  6	2.1508182	
```

​	We can plot the distribution of this variable.

<i> 	A distribution </i>  in statistics is a function that shows the possible values for a variable and how often they occur. E.g. you can plot it as histogram using <i>ggplot</i>. As you can see here variable takes negative and positive values, and for each value (or interval of values) the height of the bar in the histogram represents the number of occurrences (counts) of such value in the data: 

```{r}
# basic syntax for histogram: ggplot(data = your_data_frame, aes(x = variable)) + geom_histogram()
# other options are needed to adjust plot characheristics 
ggplot(data=var, aes(var)) + 
    geom_histogram(binwidth = 0.8,
                   col = 'darkgreen',
                   fill="darkgreen", 
                   alpha=.5) +
          labs(title="Histogram for Var", x="Variable", y="Count") + 
    theme(panel.grid.major = element_blank(), 
          panel.grid.minor = element_blank(),
          panel.background = element_blank(), 
          axis.line = element_line(colour = "black")) +
   theme(text = element_text(size=25))
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/dist_hist.png" alt="drawing" width="500"/>

Also you can use density plot to demonstrate data distribution.  This chart is a variation of a histogram that uses kernel smoothing to plot values, allowing for smoother distributions by smoothing out the noise. On y-axis there are normalized counts. Sum of all probabilities in a distribution (area under density curve) is equal to 1. 

```{r}
# basic synax for density plot: ggplot(data=your_data_frame, aes(x = variable)) + geom_density()
ggplot(data=var, aes(var)) + 
  geom_density(col = 'darkgreen',
                 fill="darkgreen", 
                 alpha=.5) +
        labs(title="Density plot for Var", x="Variable", y="Density") + 
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) + 
  theme(text = element_text(size=25))
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/dist_density.png" alt="drawing" width="500"/>

​	Another form of distribution is CDF - Cumulative Distribution Function.  CDF is function F(x), which is equal to the probability that random variable X will take a value less than or equal to x: F(x) = P(X <= x). 

```{r}
# you can just add stat_ecdf() to plot cdf from your data
# other elements here are optional, just to show what does the value of this function mean 
ggplot (data=var, aes(x=var)) + 
  stat_ecdf(color = 'darkgreen') +
  labs(title="CDF", x="Var", y="cdf") + 
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) + 
  theme(text = element_text(size=25)) +
  geom_vline(xintercept=0.5, col='blue') +
  geom_hline(yintercept=0.5, col='red') +
  geom_point(aes(x=0.5, y=0.5), colour="orange") +
  geom_segment(aes(x = 0.86, y = 0.86, xend = 0.55, yend = 0.55),
                  arrow = arrow(length = unit(0.3, "cm"))) +
  geom_text(x = 0.80, y = 0.91, label='Prob(Var <= 0.5) = 0.5', size=8) +
  scale_x_continuous(breaks = c(-4, -3, -2, -1, 0, 0.5, 1, 2, 3, 4)) +
  theme(axis.text.x = element_text(angle = 90))
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/ecdf.png" alt="drawing" heigth = "200" width="500"/>

## Central tendency 

​	How would you describe a vector? What first comes to your mind? Most likely, you want to calculate some measure that reflects the 'middle' or the 'average' value of your data. Generally speaking, it's called measures of central tendency. 

​	The most popular measures are:

 * mean, the average value

```{r}
mean(var$var)
[1] 0.6470099

# if vector has NA:
tmp <- cbind(var$var, NA)

# mean of vector with NA will give NA!
mean(tmp)
[1] NA

# to avoid such behavior:
mean(tmp, na.rm = TRUE)
[1] 0.6470099
```

 * median, the middle value

```{r}
median(var$var)
[1] 0.5166295

# if vector has NA:
median(cbind(var$var, NA))
[1] NA

# to avoid this:
median(cbind(var$var, NA), na.rm = TRUE)
[1] 0.5166295
```

 * mode, the most frequent value.

```{r}
#strangely, but base R does not have a function for mode, so it can be obtained by custom functions, or in additional packages
mode <- function(v) {
   uniqv <- unique(v)
   uniqv[which.max(tabulate(match(v, uniqv)))]
}

apply(var, 2, mode)
[1]        var 
    -0.2384994
```


All this measures are shown on the plot below, red - mean, blue - median and black is mode. 

```{r}
# using geom_vline you can add vertical lines to the plot:
ggplot(data=var, aes(var)) + 
  geom_histogram(fill="darkgreen", 
                 alpha=.5) +
        labs(title="Histogram for Var", x="Variable", y="Count") + 
        theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) +
        geom_vline(xintercept=mean(var$var), color='firebrick1', size=2) +
        geom_vline(xintercept=median(var$var), color='dodgerblue3', size=2) +
        geom_vline(xintercept=apply(var, 2, mode), size=2) +
theme(text = element_text(size=20))
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/central_tendency.png" alt="drawing" width="500"/>

## Variability 

​	Besides, you might also want to know how your data is spread out, what are the highest and lowest values. However, taking just minimum and maximum value (which is called range) is not the only way to describe variability of your data. 

* range (min and max of the data)

```{r}
range(var$var)
[1] -3.818338  5.174666
```


* variance

```{r}
var(var$var)
[1] 2.925926
```

* standard deviation (square root of variance)

```{r}
sd(var$var)
[1] 1.710534
```

Higher variance means that distribution will look more flat (spread):

```{r}
# open data with 2 identical distributions, different by variance. For one variable variance is 1, for another is 4
df  <- read.table('datasets/diffvar.txt', sep='\t')
head(df, 3)
 [1]           var     group
 [1] 1	-0.07355602	variance1		
 [1] 2	-1.16865142	variance1		
 [1] 3	-0.63474826	variance1
  
# Using facet_wrap(~ group), you can plot multiple subplots on one figure splitted by group variable
ggplot(data=df, aes(var)) + 
  geom_density(col = 'darkgreen',fill="darkgreen", alpha=.5) +
  labs(title="Difference between distributions with variance=1 and variance=4", x="Variable", y="Density") + 
  facet_wrap(~group)  +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=20)) +
  theme(strip.text.x = element_text(size = 30))
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/variability.png" alt="drawing" width="700"/>

You definitely need to remember some basic distributions.

## Distributions 

​	Distributions can be discrete and continuous. They are represented as a function with parameters. 

​	Discrete distributions are those for which list of outcomes is countable (e.g. only 2 sides of coin, only 6 sides of dice, number of clients visiting a website, etc.) They can be described by <b>Probability Mass Function (PMF)</b>. PMF is a function that gives the probability that a discrete random variable is exactly equal to some value (you can imagine it like a dictionary: {value : probability of observing such value}). 

​	Continuous distributions are those for which list of outcomes is uncountable, e.g. height of women in a population of South Africa, size of tumor in immunodeficient mice, expected project time completion, etc. <b>  Probability Density Function (PDF) </b> is used to describe them. PDF is used to specify the probability of the random variable falling <i>within a particular range of values</i>, as opposed to taking on any one value. The integral of a PDF gives the probability that a random variable falls within some interval. 

​	Sum of all probabilities in PMF as well as area under PDF curve (or intergral) are equal to 1 (this is a part of density function definition). 

Every distribution in R has four types of functions: 

* <b>p</b> for "probability", the cumulative distribution function, CDF (CDF is not widely used unlike density functions, but sometimes I see them in papers, so it's good to know about its existence)  
* <b>q</b> for "quantile" (values that partition a distribution into q intervals of equal probability)
* <b>d</b> for "density", the density function (probability density function, PDF or probability mass function, PMF)
* <b>r</b> for "random", a random variable having the specified distribution (basically, it is used for sampling from distribution)

## Discrete distributions 

<b> Bernoulli </b> 

​	Think of Bernoulli as a single coin flip, with probability of success <i>p</i> the coin will land heads (or tails, whatever you like) and probability of failure <i>q = 1-p</i>.  <i>X</i> - the random variable defining the outcome of the coin flip, and it will follow a Bernoulli distribution: 

<img src="https://render.githubusercontent.com/render/math?math=X \sim Bern(p, p(1-p))">

where <i>p</i> - mean, <i>p(1-p) = pq</i> - variance. There are only 2 outcomes: success and failure, so this distribution is characterized by a probability mass function as any other discrete distribution (e.g. Binomial and Poisson). 
Examples of events which follow Bernoulli distribution:

* whether student will pass (success, if student is well-prepared, p = 0.8) or fail an exam (failure, q = 1-p = 0.2)
* rolled dice will either show a 6 (success, if dice is fair, p=1/6) or any other number (failure, q = 1-1/6 = 5/6)
* flipping a coin and you will win if the output is tail (if coin is fair, p = q = 0.5)

```{r}
# create data frame with outcomes - 0, 1 and probabilities of these outcomes - 0.8 and 0.1 
bernoulli_df <- data.frame(value = c(0, 1),
                            prob = c(0.8, 0.1))
bernoulli_df$value <- factor(bernoulli_df$value)

#png("plots/bernoulli.png", width = 600, height = 500)

# lollipop plot consists of circle (geom_point()) and a segment (geom_segment()): 
ggplot(bernoulli_df, aes(x=value, y=prob)) +
  geom_segment( aes(x=value, xend=value, y=0, yend=prob)) +
  geom_point( size=8, color="red",  alpha=0.7, shape=21, stroke=2)  +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=20)) +
  theme(strip.text.x = element_text(size = 30)) +
  ylim(0, 1) +
  labs(title='PMF for Bernoulli')
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/bernoulli.png" alt="drawing" width="500"/>


<b> Binomial distribution </b>

​	Binomial distribution can be presented as multiple independent Bernoulli trials, each with probability of success <i>p</i>. So basically it reflects the probability of observing <i>X</i> successes in <i>n</i> independent Bernoulli trials with the probability of success <i>p</i> (independence means that none of the trials have an effect on the probability of the next trial). 

​	Examples of events (variables) which follow Binomial distribution:

* There are n clinical trials of a new drug. What the probability of observing X events of curing the disease (successes) if the probability of success in one trial is equal to p?
* Typical example about coin: if we flip that coin 5 times and coin is unfair this time (p = 0.8 for getting tails), what the probability of having the situation with 3 heads and 2 tails? 

The random variable <i>X</i>  defining the number of successes in <i>n</i>  trials, will follow a Binomial distribution:

<img src="https://render.githubusercontent.com/render/math?math=X \sim B(n, p)">

<i>n</i> - number of trials, <i>p</i> - probability of success (mean is <i>np</i>, variance is <i>np(1-p)</i>). This distribution is also discrete and it is characterized by a PMF: 

```{r}
# function dbinom helps us generate probabilities of observing a particular number of successes 
# x is number of successes in trial, 6
# size is number of trials, 20
# p is probability of success, 0.7
dbinom(x=6, size=20, p=0.7)
[1] 0.000218107


# we can also create a vector of probabilities for all possible values of variable: 
dbinom(x=1:20, size=20, p=0.7)
[1] 1.627166e-09 3.606885e-08 5.049639e-07 5.007558e-06 3.738977e-05
[6] 2.181070e-04 1.017833e-03 3.859282e-03 1.200665e-02 3.081708e-02
[11] 6.536957e-02 1.143967e-01 1.642620e-01 1.916390e-01 1.788631e-01
[16] 1.304210e-01 7.160367e-02 2.784587e-02 6.839337e-03 7.979227e-04

# sum of all probabilities should be equal to 1 
sum(density=dbinom(x=1:20, size=20, p=0.7)) 
[1] 1

# to generate sample from binomial distribution:
# n - size of the sample, 5
# size - number of trials, 10
# prob - probability of success, 0.4
rbinom(n=5, size=10, prob=0.4)
[1] 3 5 4 6 6

# it gives you probability that random variable X (number of successes) will take a value less than or equal to q = 9, when number of trials is equal to size = 10 and probability of success is equal to prob = 0.4
pbinom(q = 9, size = 10, prob = 0.4)
[1] 0.9998951

# to calculate quantile: the 40% percentile or 0.4 quantile indicates the point where 40% percent of the data have values less than this number when number of trials is size = 20 and probability of success is prob = 0.4
# more intuitive quantile definition will be discussed in the next chapter 
qbinom(p = 0.4, size = 20, prob = 0.4)
[1] 7
```

```{r}
# now we create data frame with binomial data and plot it to compare disributions with different parameters 
set.seed(123)
binomial_df <- data.frame(values=c(rbinom(n = 1000, size = 100, prob = 0.8), 
                                    rbinom(n = 1000, size = 100, prob = 0.5),
                                    rbinom(n = 1000, size = 100, prob = 0.2)),
                          parameter=c(rep('p=0.8', 1000), rep('p=0.5', 1000), rep('p=0.2', 1000)))


ggplot(binomial_df, aes(x = values,  fill=parameter, col=parameter)) + 
  geom_density(position="dodge", alpha=0.4) +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=20)) +
  theme(strip.text.x = element_text(size = 30), 
        legend.text=element_text(size=24))+
  labs(title='PMF for binomial dist')
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/binomial.png" alt="drawing" width="500"/>

<b> Poisson </b>

​	A Poisson Process is a model for a series of discrete events where the average time between events is known (it denotes as <img src="https://render.githubusercontent.com/render/math?math=\lambda">), but the exact timing of events is random. The arrival of an event is independent of the event before and two events cannot occur at the same time. Poisson processes are generally associated with time, but they do not have to be.

Important to mention that Poisson distribution is used to describe the distribution of rare events in a large population. 

<img src="https://render.githubusercontent.com/render/math?math=X \sim Poiss(\lambda)">

with <img src="https://render.githubusercontent.com/render/math?math=\lambda">  being both the mean and the variance.
<img src="https://render.githubusercontent.com/render/math?math=\lambda"> can be thought of as the expected number of events in the interval.

Examples of Poisson distributions:

* What the probability of waiting for a bus for 1 year if the average waiting time is 20 minutes? This example is frequently used to describe Poisson process, however, in real life, buses have schedule and the arrivals are not independent of one another. 
* Poisson process can model not only time: the average number of visitors to a website is equal to 1000 per day, what the probability that on the next day there will be 1102 visitors? 1 visitor?


```{r}
# probability of observing 21 units if lambda = 20 units
dpois(x = 21, lambda = 20)
[1] 0.08460506

# generate 10 values from Poisson distribution with lambda 1
set.seed(10)
rpois(n = 10, lambda = 1)
[1] 1 0 1 1 0 0 0 0 1 1

# Probaility that random variable X distributed by Poisson with lambda 5 is equal to and less than q=3
ppois(q = 3, lambda = 5)
[1] 0.2650259

# quantile: lower quartile for Poisson distribution with lambda 18
# the lower quartile indicates the point where 25% percent of the data have values less than this number
qpois(p = 0.25, lambda = 18)
[1] 15
```

```{r}
# let's plot PMF for different lambdas of Poisson distribution
poisson_df <- data.frame(values=c(rpois(n = 1000, lambda = 5), 
                                  rpois(n = 1000, lambda = 10), 
                                  rpois(n = 1000, lambda = 20)),
                          parameter=c(rep('lambda=5', 1000), 
                                      rep('lambda=10', 1000), 
                                      rep('lambda=20', 1000)))
ggplot(poisson_df, aes(x = values,  fill=parameter, col=parameter)) + 
  geom_density(position="dodge") +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=20)) +
  theme(strip.text.x = element_text(size = 30), 
        legend.text=element_text(size=24))+
  labs(title='PMF for Poisson dist')
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/poisson.png" alt="drawing" width="500"/>


## Continuous distributions 

<b> Uniform </b>

​	The Uniform distribution describes an experiment where there is an arbitrary outcome that lies between certain bounds: parameters, a and b, which are the minimum and maximum values. It models the situation when events that are equally likely to occur.

<img src="https://render.githubusercontent.com/render/math?math=X \sim U(a, b)">

where <i> (a+b)/2 </i> is mean and variance is <i> 1/12*(b-a)^2 </i>. 

​	Examples of Uniform distributions:

* If you choose a card in a deck of unique cards (e.g. 36 cards in total and they all are equally likely to choose, 1/36)
* Perfect random number generators (outcomes are equally likely)
* Probability of guessing exact time at any moment (outcomes should be equally likely, so you probably have to sit in a dark room for a while to make sure that you have no idea whether it's morning or evening)

```{r}
# it gives the value of density function for X=4, uniform distribution with parameters a=min=1 and b=max=10
dunif(x = 4, min = 1, max = 10)
[1] 0.1111111

# it generates values from uniform distributions with parameters a=min=1 and b=max=10
set.seed(24)
runif(n = 5, min = 1, max = 10)
[1] 9.012088 7.343454 1.197819 2.317245 7.183389

# it gives you probability that random variable X distributed uniformly with parameters a=min=1 and b=max=10 will take a value less than or equal to q = 7
punif(q = 7, min = 1, max = 10)
[1] 0.6666667

# it gives the value of quantile function
# quantile 0.5 (50% or median) indicates the point where 50% percent of the data have values less than this number
qunif(p = 0.5, min = 1, max = 10)
[1] 5.5
```

```{r}
# let's plot PDF for different parameters of Uniform distribution
set.seed(123)
uniform_df <- data.frame(values=c(runif(n = 10000, min = 1, max = 20), 
                                  runif(n = 10000, min = 4, max = 25), 
                                  runif(n = 10000, min = 8, max = 12)),
                          parameter=c(rep('a,b=1,20', 10000), 
                                      rep('a,b=4,25', 10000), 
                                      rep('a,b=8,12', 10000)))

ggplot(uniform_df, aes(x = values,  fill=parameter, col=parameter)) + 
  geom_density(position="dodge") +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=20)) +
  theme(strip.text.x = element_text(size = 30), 
        legend.text=element_text(size=24))+
  labs(title='PDF for Uniform dist')
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/uniform.png" alt="drawing" heigth = "200" width="500"/>

```{r}
# you can get a more recognisable form of 'rectangular distribution' using dunif and base R graphics:
plot(dunif(x =1:60, min = 10, max = 50), type = "o", ylab='density of uniform distribution', xlab='values')
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/uniform2.png" alt="drawing" heigth = "200" width="500"/>

<b> Normal </b> 

​	The normal distribution is probably the most common distribution in all of probability and statistics. It is symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the mean. Only mean and the standard deviation is required to explain the entire distribution. Mean, median and mode are all equal.

<img src="https://render.githubusercontent.com/render/math?math=X \sim N(\mu, \sigma^2)">

where <img src="https://render.githubusercontent.com/render/math?math=\mu"> - mean,  <img src="https://render.githubusercontent.com/render/math?math=\sigma"> - standard deviation 

Examples: 

* height or weight of animals
* blood pressure 
* travel time for employees

```{r}
# it gives the value of density function for X=10, normal distribution with parameters mean = 0 and sd = 1
dnorm(x = 10, mean = 0, sd = 1)
[1] 7.694599e-23

# it generates values from normal distributions with parameters mean = 0 and sd = 1
set.seed(24)
rnorm(n = 6, mean = 0, sd = 1)
[1] -1.3538489 -0.5793773 -0.8610442  0.9726783
[5]  0.6191458  1.3854457

# it gives you probability that random variable X distributed normally with parameters mean = 0 and sd = 1 will take a value less than or equal to q = 3
pnorm(q = 3, mean = 0, sd = 1)
[1] 0.9986501

# it gives the value of quantile function:
# 0.2 quantile indicates the point where 20% percent of the data have values less than this number
qnorm(p = 0.2, mean = 0, sd = 1)
[1] -0.8416212

```

```{r}
# let's plot PDF for different parameters of normal distribution
set.seed(123)
norm_df <- data.frame(values=c(rnorm(n = 10000, mean=3, sd=1), 
                               rnorm(n = 10000, mean=0, sd=3), 
                               rnorm(n = 10000, mean=6, sd=4)),
                          parameter=c(rep('mean,s = 3, 1', 10000), 
                                      rep('mean,s = 0, 2', 10000),
                                      rep('mean,s = 6, 4', 10000)))

ggplot(norm_df, aes(x = values,  fill=parameter, col=parameter)) + 
  geom_density(position="dodge") +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=20)) +
  theme(strip.text.x = element_text(size = 30), 
        legend.text=element_text(size=24))+
  labs(title='PDF for Normal dist')
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/norm.png" alt="drawing" heigth = "200" width="500"/>

​	There is an important empirical rule about normal distribution: 

* Approximately 68% percent of the data fall within 1 standard deviation of the mean
* Approximately 95% of the data fall within 2 standard deviations of the mean
* Approximately 99.7% of the data fall within 3 standard deviations of the mean

```{r}
# generate sample data from normal distribution
set.seed(100)
v <- data.frame(v = rnorm(50000, 0, 1))

# calculate sigma and mu from sample:
sigma <- sd(v$v)
mu <- mean(v$v)

# create basic density plot
p <- ggplot(v, aes(v)) +
          geom_density(fill="white")

# add to the previous plot colored areas using geom_area()
# add text to the plot using geom_text()
# don't you find ggplot syntax intuitive? :) 
d <- ggplot_build(p)$data[[1]]


# this is going to be complex plot
# there is no need to uderstand everything what's going on here, but for those who might want to create something 
# like this, it might be interesting 
labels <- c(expression(-3*sigma), expression(-2*sigma), expression(-1*sigma), expression(mu), expression(1*sigma), expression(2*sigma), expression(3*sigma))

p + geom_area(data = subset(d, x < -3*sigma), aes(x=x, y=y), fill="royalblue4", alpha=1) +
  geom_area(data = subset(d, (x < -2*sigma) & (x > -3*sigma)), aes(x=x, y=y),  fill="darkgreen", alpha=1) + 
  geom_area(data = subset(d, x > 3*sigma), aes(x=x, y=y),  fill="royalblue4", alpha=1) +
  geom_area(data = subset(d, (x < 3*sigma) & (x > 2*sigma)), aes(x=x, y=y),  fill="darkgreen", alpha=1) +
  geom_area(data = subset(d, (x < -1*sigma) & (x > -2*sigma) ), aes(x=x, y=y), fill="mediumvioletred", alpha=1) + 
  geom_area(data = subset(d, (x < 2*sigma) & (x > 1*sigma) ), aes(x=x, y=y), fill="mediumvioletred", alpha=1) + 
  geom_area(data = subset(d, (x < 1*sigma) & (x > mu) ), aes(x=x, y=y), fill="slateblue4", alpha=1) + 
   geom_area(data = subset(d, (x > -1*sigma) & (x < mu) ), aes(x=x, y=y), fill="slateblue4", alpha=1) +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=20)) +
 scale_x_continuous(name="variable", limits=c(-4.5, 4.5), breaks = c(-3*sigma, -2*sigma, -1*sigma, 0, sigma, 2*sigma, 3*sigma), labels = labels) + 
  geom_text(x=-0.5, y=0.2, label="34.1%", size=5, col='white') + 
  geom_text(x=0.5, y=0.2, label="34.1%", size=5, col='white') + 
  
  geom_text(x=-1.45, y=0.06, label="13.6%", size=5, col='white') + 
  geom_text(x=1.45, y=0.06, label="13.6%", size=5, col='white') + 
  
  geom_text(x=-2.6, y=0.05, label="2.1%", size=5, col='black') +
geom_text(x=2.6, y=0.05, label="2.1%", size=5, col='black') +
  
  geom_text(x=-3.8, y=0.02, label="0.1%", size=5, col='black') +
geom_text(x=3.8, y=0.02, label="0.1%", size=5, col='black') 
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/empirical.png" alt="drawing" heigth = "200" width="500"/>


<b> Student T distribution </b>

​	T distribution is another distribution which is widely utilized in statistics tests (e.g. Student's t-test, confidence intervals, linear regression analysis). It looks almost identical to the normal distribution curve, but it has heavier tails, which means that it contains more values that fall far from its mean. 

​	The t distribution is used instead of the normal distribution when you have small samples (e.g. in confidence intervals of the mean). The larger the sample size, the more the t distribution looks like the normal distribution. 

<img src="https://render.githubusercontent.com/render/math?math=X \sim T(df)">

where df - degrees of freedom, df = n - 1, n - number of independent observations in sample.   

```{r}
# it gives the value of density function for X=1, T-distribution with n=20, df=n-1=19
dt(x = 1, df = 19)
[1] 0.2357406

# it generates values from T-distribution with parameters df=n-1=19
set.seed(24)
rt(n=5, df=19)
[1]  0.5979578 -1.7849844  1.8205241  1.4047534 -0.3133408

# it gives you probability that random variable X t-distributed df=19 will take a value less than or equal to q = 2
pt(q = 2, df=19)
[1] 0.969999

# it gives the value of quantile function:
# 0.2 quantile indicates the point where 20% percent of the data have values less than this number
qt(p = 0.2, df=19)
[1] -0.8609506
```

```{r}
# let's plot PDF for different parameters of normal distribution
set.seed(123)
t_df <- data.frame(values=c(rt(1000, df = 3), 
                               rt(1000, df = 12), 
                               rt(1000, df = 99)),
                          parameter=c(rep('df=3', 1000), 
                                      rep('df=12', 1000),
                                      rep('df=99', 1000)))

ggplot(t_df, aes(x = values,  fill=parameter, col=parameter)) + 
  geom_density(position="dodge",  alpha=0.5) +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=20)) +
  theme(strip.text.x = element_text(size = 30), 
        legend.text=element_text(size=24))+
  labs(title='PDF for T dist')
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/t.png" alt="drawing" heigth = "200" width="500"/>

## Quartiles, quantiles, percentiles 

​	As you might remember, quartiles are 3 points dividing a dataset into four equal groups, each consisting of 25% of the data. There are lower quartile (Q1), middle quartile (median, Q2) and upper quartile (Q3). Surely, you can choose any number of groups to split your data.  E.g. percentile, which divides a dataset into 100 equal groups. 

​	Examples:

* The 5th percentile is the boundary between the smallest 5% of the data and the largest 95% of the data. 

* The median of a dataset is the 50th percentile of the dataset. 

* The 25th percentile is the first quartile, and the 75th percentile the third quartile.

  Let's look at the example:

```{r}
# let's generate observations with replacement 
set.seed(789)
y <- sample(1:10, 22, replace = TRUE)
y
[1]  4 10 10  3  5  4  3  6  4  1  9  6  2  2  2  5  2  6  7  8  8 10

x <- data.frame(y = y)
```

​	In R you can simply use in-built function:

```{r}
# it gives you 0th, 25th, 50th, 75th and 100th percentiles
quantile(y)
[1] 0%   25%   50%   75%  100% 
 	1.00  3.00  5.00  7.75 10.00 

# you can also choose which quantile you want
quantile(y, probs = c(0.05, 0.3, 0.7, 0.96))
[1] 5%  30%  70%  96% 
 	2.0  3.3  6.7 10.0 
```

```{r}
# this is another type of plot - dotplot
# it's histogram, but instead of bars - points representing counts of value
# red - lower quartile, blue - middle quartile, purple - upper one
ggplot(x, aes(y)) + 
  geom_dotplot(binwidth=1, method='histodot') + 
  scale_y_continuous(name = "", breaks = NULL) +
  scale_x_continuous(breaks = seq(1, 10, 1)) +
  labs(title = 'Dotplot') +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) +
        geom_vline(xintercept=quantile(y, probs=0.25), color='red') +
        geom_vline(xintercept=quantile(y, probs=0.5), color='blue') +
        geom_vline(xintercept=quantile(y, probs=0.75), color='purple') 
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/quartiles1.png" alt="drawing" heigth = "200" width="500"/>

Let's look at the another example with continuous distribution.
On a plot you can see that Q1,  Q2 and Q3 divide data into 4 intervals with equal probabilities (25% each):

```{r}
# generate data from normal distribution
set.seed(100)
v <- data.frame(v = rnorm(50000, 0, 1))

#calculate quartiles
Q1 <- quantile(v$v, probs = 0.25)
Q3 <- quantile(v$v, probs = 0.75)
Q2 <- quantile(v$v, probs = 0.5)


# create basic density plot
p <- ggplot(v, aes(v)) +
          geom_density(fill="white")

# add to the previous plot colored areas using geom_area()
# add text to the plot using geom_text()
# don't you find ggplot syntax intuitive? :) 
d <- ggplot_build(p)$data[[1]]

p + geom_area(data = subset(d, (x > Q2) & (x < Q3)), aes(x=x, y=y), fill="chartreuse4", alpha=0.5) +
  geom_area(data = subset(d, (x < Q2) & (x > Q1)), aes(x=x, y=y), fill="chartreuse4", alpha=0.5) +
  geom_area(data = subset(d, x > Q3), aes(x=x, y=y), fill="darkgoldenrod1", alpha=0.5) +
  geom_area(data = subset(d, x < Q1), aes(x=x, y=y), fill="darkgoldenrod1", alpha=0.5) +
geom_text(x=-1.1, y=0.1, label="25%", size=5.8) +
  geom_text(x=-0.3, y=0.1, label="25%", size=5.8) +
  geom_text(x=0.4, y=0.1, label="25%", size=5.8) +
  geom_text(x=1.1, y=0.1, label="25%",  size=5.8) +
  geom_text(x=Q1, y=0.015, label="Q1",  size=6.5) +
  geom_text(x=Q2, y=0.015, label="Q2",  size=6.5) +
  geom_text(x=Q3, y=0.015, label="Q3",  size=6.5) +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=20)) +
  scale_x_continuous(breaks = seq(-4, 4, 1))
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/quantiles2.png" alt="drawing" width="600"/>

​	Quartiles are used in another very popular and informative representation of data distribution - boxplot. Lower boundary of the box is Q1 (lower quartile), middle (red) is median or Q2, upper boundary is Q3 (upper quartile). 

​	Q3 - Q1 is an <b>interquartile range</b> which is another popular measure of data variability as well as variance and standard deviation. The greater height of the box (IQR = Q3 - Q1), the higher variability of the data. 

​	Upper dashed line ends up at Q3 + 1.5 * IQR and lower dashed line ends up at Q1 - 1.5 * IQR. All values above and below these boundaries are considered to be outliers - extremely high and low values. 

```{r}
# let's create boxplot using base R 
# using text(x=x, y=y, labels='labels') you can add text on plot 
# you can find IQR using in-built R function:
IQR <- IQR(v$v)

boxplot(v, medcol="red") 
text(x=1.25, y=Q1, labels='Q1', cex=1.5)
text(x=1.3, y=Q2, labels='median', cex=1.5)
text(x=1.25, y=Q3, labels='Q3', cex=1.5)
text(x=1.25, y=Q1-1.5*IQR, labels='Q1-1.5*IQR', cex=1.5)
text(x=1.25, y=Q3+1.5*IQR, labels='Q3+1.5*IQR', cex=1.5)
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/boxplot.png" alt="drawing" width="500"/>

```{r}
#show boxplot points in density plot
IQR <- IQR(v$v)
low_boundary <- Q1 - 1.5*IQR 
high_boundary <- Q3 + 1.5*IQR 

p <- ggplot(v, aes(v)) +
          geom_density(fill="white") + 
          geom_vline(xintercept = low_boundary, 
                color = "darkgreen", size=0.5) + 
          geom_vline(xintercept = high_boundary,
                color = "darkgreen", size=0.5)

# subset region and plot
# LP = Q1 - 1.5*IQR
# HP = Q3 + 1.5*IQR
d <- ggplot_build(p)$data[[1]]
p + geom_area(data = subset(d, (x < Q2) & (x > Q1)), aes(x=x, y=y), fill="chartreuse4", alpha=0.4) +
  geom_area(data = subset(d, x < Q1), aes(x=x, y=y), fill="darkgoldenrod1", alpha=0.4) +
  geom_area(data = subset(d, x > Q3), aes(x=x, y=y), fill="darkgoldenrod1", alpha=0.4) +
  geom_area(data = subset(d, (x < Q3) & (x > Q2)), aes(x=x, y=y), fill="chartreuse4", alpha=0.4) +
  geom_text(x=Q1, y=0.015, label="Q1", size=5.5) +
  geom_text(x=Q2, y=0.015, label="Q2", size=5.5) +
  geom_text(x=Q3, y=0.015, label="Q3", size=5.5) +
  geom_text(x=low_boundary, y=0.015, label="LP", size=5.5) +
  geom_text(x=high_boundary, y=0.015, label="HP", size=5.5) +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) +
  scale_x_continuous(breaks = seq(-4, 4, 1)) +
  theme(text = element_text(size=20)) 
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/boxplot_expl.png" alt="drawing" width="500"/>

## Descriptive statistics for data frame

​	In previous paragraphs we have known how to describe the distribution of one variable: measures of central tendency (mean, median, mode), measures of variability (range, interquartile range, variance, standard deviation) and quantiles (quartiles, percentiles).  We also are aware of some basic visualization methods such as histogram, density plot and boxplot. Let's move to the description of multiple variables combined into data frame.

​	You can calculate basic different statistics for data frame, using function <i>describe</i> from package <i>psych</i>. 
Pay attention to categorical variables (they are denoted as * in output data frame), they can't have mean or median (it's for numeric variables only). So the best practice is to delete them from data frame before applying function describe: 

```{r}
# generate some random data
df <- data.frame(var1 = rbeta(100, 3, 5), 
                 var2 = rpois(100, 4), 
                 var3 = rbinom(100, 20, 0.5),
                 group_var1 = as.factor(sample(c(0,1), replace=TRUE, size=100)),
                 group_var2 = as.factor(sample(seq(1, 5, 1), replace=TRUE, size=100)))

# here we apply function describe, removing categorical variables such as group_var1 and group_var2 
# as you can see, this function allows you to obtain different statistical measures for multiple variables 
describe(df[,-c(4, 5)])

[1] 
		vars  n mean      sd  median trimmed     mad     min     max
var1	1	100	0.39	0.15	0.39	0.39	0.17	0.07	0.83	
var2	2	100	3.90	1.69	4.00	3.80	1.48	1.00	9.00	
var3	3	100	9.82	2.44	10.00	9.90	1.48	4.00	16.00	
3 rows | 1-5 of 13 columns
```

Besides, descriptive statistics can be obtained for groups:

```{r}
# here we group data by group_var1 (it has values 1 and 0 which is reflected in columns group1)
describeBy(x = df[,-c(4, 5)], group = df$group_var1, mat=T, digits = 2)[0:5]

# output is too big, only part is shown
[1]
	 item group1  vars   n  mean      sd  median trimmed     mad
var11	1	   0	 1	49	0.38	0.15	0.35	0.37	0.14	
var12	2	   1	 1	51	0.41	0.16	0.41	0.40	0.15	
var21	3	   0	 2	49	3.65	1.59	3.00	3.51	1.48	

#group by 2 variables
describeBy(x = df[,-c(4, 5)], group = list(df$group_var1, df$group_var2), mat=T, digits = 2)

# output is too big, only part is shown
[1]
     item group1 group2 vars    n   mean      sd  median trimmed
var11	1	   0	  1	   1	9	0.39	0.16	0.37	0.39	
var12	2	   1	  1	   1	15	0.40	0.17	0.36	0.38	
var13	3	   0	  2	   1	9	0.32	0.16	0.33	0.32
```

-----------------------------------------------------------------------------------------------------------------------

## Central Limit Theorem

​	<b>The central limit theorem</b> states that if you have a population with mean μ and standard deviation σ and take sufficiently large random samples from the population with replacement, then the distribution of the sample means will be approximately normally distributed with mean <img src="https://render.githubusercontent.com/render/math?math=\mu">  and standard mean error <img src="https://render.githubusercontent.com/render/math?math=se = \sigma / sqrt(n)"> (standard mean error is just a standard deviation for sample means distribution). 

​	The higher n, the lower variability of the sample means (distribution of sample means is narrower). 

​	Random sample should be sufficiently large if population is not normally distributed (n>=30).

​	Visualization of this theorem you can find here: https://istats.shinyapps.io/sampdist_cont/, https://istats.shinyapps.io/SampDist_discrete/

## Confidence interval for mean 

​	Let's dive into statistics applications. 

​	If we want to estimate a parameter, ideally we would compute its value from the whole population. However, in real world we have to deal only with samples from population. What's even worse, we usually have only one sample.  Confidence intervals can help us. They are mainly used to estimate a population parameter from sample data. Let's calculate the 95% confidence interval for a population mean. 

<b> Confidence interval based on Z-score </b>

​	You can use a z-interval when:

* sample size >= 30, population standard deviation is known (<img src="https://render.githubusercontent.com/render/math?math=\sigma">)
* original population is normal,  population standard deviation is known (<img src="https://render.githubusercontent.com/render/math?math=\sigma">)

​	As we know from CLT, sample means are distributed <i> normally </i> with mean value equal to the population mean (<img src="https://render.githubusercontent.com/render/math?math=\mu">) and standard error (<img src="https://render.githubusercontent.com/render/math?math=se=\sigma / sqrt(n)">). 

​	For normal distribution the following is true: from empirical rule we know that approximately 95% of the data fall within 2 standard deviations of the mean, but more precisely it's 1.96 standard deviations. This 1.96 is actually <img src="https://render.githubusercontent.com/render/math?math=Z_{0.95}"> score. 

​	And finally, if we want to find this 95% interval for population mean, having only 1 sample, we can just use the next formula: 

<img src="https://render.githubusercontent.com/render/math?math=(M - Z_{0.95} * se, M %2B Z_{0.95} * se)">

where M - sample mean, se - standard mean error (or simply standard deviation of the sample mean distribution, which is equal to <img src="https://render.githubusercontent.com/render/math?math=\sigma / sqrt(n)">) and <img src="https://render.githubusercontent.com/render/math?math=Z_{0.95}"> is Z-score, which is equal here to 1.96. In order to use it we need somehow to know population sd - <img src="https://render.githubusercontent.com/render/math?math=\sigma">.

```{r}
# R does not contain in-built functions for Z-interval, because in practice it is rarely used
# so do it using base functions
set.seed(123)
sample <- rnorm(n=50, mean=0, sd=1)

sd <- 1 # sd of the real population we somehow managed to know 
n <- 50 # number of observations in sample

# Z_0.95 = qnorm(0.975)
c(mean(sample) - qnorm(0.975)*sd/sqrt(n), mean(sample) + qnorm(0.975)*sd/sqrt(n))
[1] -0.2427772  0.3115843
```


​	E.g. if we want to estimate 70% confidence interval, we just need to substitute the formula with appropriate Z-score (<img src="https://render.githubusercontent.com/render/math?math=Z_{0.70}">). But this method is not widely used in real life. If we don’t know the population mean (that’s what we are trying to estimate), then how would we know the population standard deviation <img src="https://render.githubusercontent.com/render/math?math=\sigma">? 

<b> Confidence interval based on T-score </b>

​	This interval is used for more relatistic scenario: you don't need to know (<img src="https://render.githubusercontent.com/render/math?math=se=\sigma / sqrt(n)">). 

​	You can use a t-interval when:

* <img src="https://render.githubusercontent.com/render/math?math=\sigma"> is not known

  For 95% confidence interval formula is similar to Z-interval: 

<img src="https://render.githubusercontent.com/render/math?math=(M - T_{0.95} * se/sqrt(n), M %2B T_{0.95} * se/sqrt(n))">

​	Let's calculate T-based confidence interval using functions in R.

```{r}
# let's generate random sample from normal population
set.seed(123)
sample <- rnorm(n=50, mean=0, sd=1)

# do it using base functions
se <- sd(sample) # se 
n <- 50 # number of observations in sample
# T_0.95 score = qt(0.975, df = n-1), df - parameter of T-distribution, degrees of freedom
c(mean(sample) - qt(0.975, df = n-1)*se/sqrt(n), mean(sample) + qt(0.975, df = n-1)*se/sqrt(n))
[1] -0.2287258  0.2975329


# find 95% confidence interval
CI(sample, ci = 0.95)
[1]      upper        mean       lower 
 0.29753289  0.03440355 -0.22872579 

# find 99% confidence interval. Important to note, this interval is wider and gives us less narrow estimate. 
[1] CI(sample, ci = 0.99)
      upper        mean       lower 
 0.38531053  0.03440355 -0.31650344 
```

​	Let's talk a bit about an interpretation of confidence interval. The name of the interval sounds always misleading.  Basically, it means that 95% of all confidence intervals for sample means (infinite number of samples should be drawn!) would include the mean of population. In other words, the confidence level represents the frequency (the proportion) of possible confidence intervals that contain the true value of the unknown population parameter. For 95% CI this proportion is 0.95. To better understand it visually, you can use this link: https://istats.shinyapps.io/ExploreCoverage/

​	Remember to use the correct units. E.g. if you data were in inches, you should say that 95% confidence interval for the population mean is (-0.22872579 inches, 0.29753289 inches). 

---------------------------------------------------------------------------------------------------------------------

​	If you are not bored and tired yet, let's talk how to calculate <img src="https://render.githubusercontent.com/render/math?math=Z_{0.95}"> and understand why we used qnorm(0.975). 

<b> Z-score </b>

​	Z-score (standard score) allows us to standardize two or more normal distributions: to put them on the same scale. Besides, it is used in confidence intervals.  

​	A z-score measures exactly how many standard deviations above or below the mean a data point is.
It is calculated by subtracting the population mean from an individual raw score and then dividing the difference by the population standard deviation: 

<img src="https://render.githubusercontent.com/render/math?math=Z%3D%5Cfrac%7Bx-m%7D%7Bsd%7D">

​	A positive z-score says the data point is above average, a negative z-score says the data point is below average.

​	Let's work with standard normal distribution: mean = 0, sd = 1. If we standardize any point, we will get the same value:

​			                                                                        <img src="https://render.githubusercontent.com/render/math?math=Z%3D%5Cfrac%7Bx-0%7D%7B1%7D=x">.

​	So Z-scores for standard normal distribution are just data points. 

```{r}
set.seed(100)
# it's standard normal distribution, mean=0, sd=1
# so each z-score = (X - 0) / 1 = X, so it's just a value of variable 
v <- data.frame(v = rnorm(50000, 0, 1))

p <- ggplot(v, aes(v)) + geom_density(fill="white")

d <- ggplot_build(p)$data[[1]]

Z <- 1.96

p + geom_area(data = subset(d, (x < Z) & (x > 0)), aes(x=x, y=y), fill="lightpink3", alpha=0.5) +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=30)) +
  scale_x_continuous(breaks = c(-4, -2, 0, 1.96, 4), labels = c(-4, -2, 0, 'Z', 4)) +
  labs(title = 'Standard normal dist') + xlab('variable or Z-scores')
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/zscore1.png" alt="drawing" heigth = "200" width="500"/>

​	Suppose we want to know which two z-scores separate out the middle 95% of the data. As you already know, from empirical rule approximately 95% of the data fall within 2 standard deviations of the mean (Z-scores = -2 and 2). In reality, it’s not exactly ±2, but close enough for rough calculations. Let's calculate these Z-scores accurately. 

​	We can use quantiles for that: 

```{r}
# we want to get central 95% of the normally distributed data
# quantile of level X is a cut point in a distribution for which X% of the data are located on the left side of this point 
# so it's 0.95 + ((1 - 0.95)/2) = 0.975
q1 <- qnorm(0.975)
q2 <- qnorm(0.025)
q1 
# [1] 1.959964
q2 
# [1] -1.959964

set.seed(100)
# we use standard normal distribution 
v <- data.frame(v = rnorm(50000, 0, 1))

p <- ggplot(v, aes(v)) + geom_density(fill="white")

d <- ggplot_build(p)$data[[1]]

p + geom_area(data = subset(d, (x > q1)), aes(x=x, y=y), fill="white", alpha=0.5) +
  geom_area(data = subset(d, (x < q2)), aes(x=x, y=y), fill="white", alpha=0.5) +
  geom_area(data = subset(d, (x > q2) & (x < q1)), aes(x=x, y=y), fill="lightpink3", alpha=0.5) +
geom_text(x=2, y=0.05, label="Z \n qnorm(0.975)", size=8, color='purple4') +
  geom_text(x=-2, y=0.05, label="Z \n qnorm(0.025)", size=8, color='purple4') +
  geom_text(x=0, y=0.15, label="95% of \n the data", size=8) +
   geom_text(x=-3.5, y=0.03, label="2.5%", size=8) +
   geom_text(x=+3.5, y=0.03, label="2.5%", size=8) +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=20)) +
  scale_x_continuous(breaks = c(-4, -3, -1.96, -1, 0, 1, 1.96, 3, 4), labels = c(-4, -3, -1.96, -1, 0, 1, 1.96, 3, 4)) 
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/zscore.png" alt="drawing" heigth = "200" width="500"/>
