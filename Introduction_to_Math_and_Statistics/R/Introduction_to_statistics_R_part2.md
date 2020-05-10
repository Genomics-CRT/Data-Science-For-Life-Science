# Introduction to Statistics in R Worksheet. Part 2

```{r}
library(ggplot2) # plotting
library(dplyr) # data frame manipulation
library(tidyr) # data frame manipulation
library(ggpubr) # plotting
library(gridExtra) # plotting
library(car) #leven test for variance comparison
library(cowplot) # arranging plots
library(PairedData) # plot paired data
library(corrplot) # plot correlation 
```

## 2-sample comparison: T-test 

​	What if we conducted experiment with the particular treatment, measured some characteristics and we want to understand whether our treatment works?  We need to validate somehow our hypothesis. In a better world we could use the whole population (all people, all cells, etc.) to determine whether a hypothesis is true, but in practice it is often impossible and we only can deal with random samples - subsets of population. 

​	Let's say that in our imaginary experiment we have cell cultures, which have been treated with antibiotic. We also have untreated control group. You observed some parameter of these cultures, e.g. number of cells.  Your question is: 'Has this treatment caused cell death?' (In other words, we want to know whether the number of dead cells in treated cell cultures is higher than in control group).

​	So now, we had the question (a hypothesis), we performed the experiment and now we can apply statistical analysis. The best way to understand is to show it on the data. 

​	Let's upload the data consisting of 2 groups: treated and control cell cultures. Each group is representing the number of dead cells in culture.  In total, we have 50 observations. It's just imaginary data, so it has nothing to do with real experiments. 

```{r}
df <- read.table('datasets/two_sample_ttest.txt')

head(df, 3)
[1] treated  control
[1]   1	11	     2		
[1]   2	 7	     2		
[1]   3	 8	     3		
```

​	It's always a good idea to plot your data first. You can get the idea of distribution shape and the difference between 2 groups visually. As you can see here, groups can be clearly separated, treated group is shifted to the right and has greater values. 

```{r}
p1 <- df %>% tidyr::gather(group, dead_cells) %>% 
  ggplot(aes(x=dead_cells))+
  geom_histogram(fill='grey', col='black', binwidth = 1) +
  facet_grid(group ~ .) +
  labs(title="Dist. of cell count", x="cell count") +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=20))

p2 <- df %>% tidyr::gather(group, dead_cells) %>% 
  ggplot(aes(x=dead_cells, fill=group))+
  geom_density(alpha=0.6) +
  labs(title="Dist. of cell count", x="cell count") +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=20))

p3 <- df %>% tidyr::gather(group, dead_cells) %>% 
  ggplot(aes(x = group, y=dead_cells, fill=group))+
  geom_boxplot() +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=20))

plot_grid(p1, p2, p3, nrow = 1)
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/ttest1.png" alt="drawing" width="1200"/>

​	So, it seems like treated cell cultures have more dead cells than control cell cultures. But how significant this difference is?  As you might recall from your past courses of statistics, in such case <b>T-test</b> can be used. <b>T-test</b> means that we are going to compare means of groups.  

Let's formulate hypotheses (it's one-sided type):

* H0: mean1 == mean2 - there is no difference between means 
* H1: mean1 > mean2 - difference in one direction 

where <i>mean1</i> is the mean of control and <i>mean2</i> is the mean of treated group. So, the average number of dead cells in treated is higher than in control cultures, which means that treatment may cause cell death. 

Another One-sided type would be:

* H0: mean1 == mean2
* H1: mean1 < mean2

Two-sided hypothesis would be:

* H0: mean1 = mean2
* H1: mean1 != mean2

​	Usually, one-sided type should be used if you discover a statistically significant difference in a particular direction, but not in the other direction. 

​	As a reminder:

* <i>Null hypothesis</i> (H0) claims that sample observations (our data) result <i>purely from chance</i>. In the example, it implies that there is likely to be no difference between groups, they are homogeneous, and treatment do nothing.  

* <i>Alternative hypothesis</i> (H1) states that sample observations are <i>influenced by some non-random cause</i>. It means that there is a difference between groups (due to treatment). 

  

  Besides, T-test could be paired on unpaired.

* Paired t-test compares study subjects at 2 different times (paired observations of the same subject)

* Unpaired t-test compares two different independent subjects


```{r}
ttest <- t.test(x = df$treated, # first group
       y = df$control, # second group
       alternative = 'greater', # type of the hypotheses. Could be greater, less, two.sided 
       paired = F, # unpaired test, becuase it's independent cell cultures 
       var.equal =  T # assumption which should be checked before applying test 
      )


ttest
[1]Two Sample t-test

[1] data:  df$treated and df$control
[1] t = 4.7647, df = 98, p-value = 3.281e-06
[1] alternative hypothesis: true difference in means is greater than 0
[1] 95 percent confidence interval:
[1]  1.550538      Inf
[1] sample estimates:
[1] mean of x mean of y 
[1]      8.22      5.84 

# we can access different data from t test output, e.g. pvalue: 
ttest$p.value
[1] 3.280808e-06

# T statistic
ttest$statistic
[1]  t 
4.76467 

# confidence interval for mean difference:
ttest$conf.int
[1] 1.550538      Inf
attr(,"conf.level")
[1] 0.95
```

​	Let's interpret the output. Generally, you look at only p-value, and draw conclusions like this: "p-value < 0.05, so we have evidence to reject H0 at this level, and it means there is a difference between groups caused not only by chance". But what about t = 4.7647, df = 98 and 95 percent confidence interval? What can these metrics tell us and why are they important too? 

​	When you perform a t-test, you calculate a specific measure called T-statistic. It basically measures the size of the difference between sample mean of group 1 and sample mean of group 2 relative to the variation in the sample data. In other words, T-statistic is simply the calculated difference represented in units of standard error. Just look at the formula (for simplification, denominator is just SE, without details, but it represents standard error of 2 samples):

![equation](http://latex.codecogs.com/gif.latex?T_Statistic%3D%5Cfrac%7B(M1-M2)-0%7D%7BSE%7D)   

where M1 - mean of group 1 and M2 - mean of group 2 (in our example, M1 for treated and M2 for control)

​	As you can see, the greater T, the greater the difference between group means, and the greater evidence against the null hypothesis. The closer T is to 0, the more likely there isn't a significant difference (M1 - M2 = 0 => T = 0, no difference).

​	When you perform a t-test for a single study, you obtain a single t-value. However, if we drew multiple random samples of the same size from the same population and performed the same t-test, we would obtain many t-values and we could plot a distribution of all of them. T-statistics follows (surprise!) Student's T-distribution with parameter df = degrees of freedom (it depends on the sample size).

​	The T-distribution is symmetric and bell-shaped, like the normal distribution, but has heavier tails, meaning that it is more prone to producing values that fall far from its mean: 

```{r}
# png("tdist.png", width = 600, height = 500)

# this is another way to plot distribution in ggplot
# you can define range in dataframe in the main body of ggplot
# and then add stat_function(fun=dt)
# in args you can define parameters of distribution
# e.g. if you want to plot normal distribution, you can use stat_function(fun=dnorm)
ggplot(data.frame(x = c(-5, 5)), aes(x = x)) +
    stat_function(fun = dt, args = list(df = 1)) +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=20)) +
  labs(title='T distribution')

#while (!is.null(dev.list()))  dev.off()
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/tdist.png" alt="drawing" width="600"/>

​	Let's talk about <i>p-value</i>. T-statistic and p-value are tightly linked. T-distributions assume that you draw repeated random samples from a population where <b>the null hypothesis is true</b>. The peak of the graph is right at zero, which indicates that obtaining a sample value close to the null hypothesis is the most likely.

​	You place the t-value from your study in the t-distribution to determine how consistent your results are with the null hypothesis. If its far from zero, closer to any tail, it means that it is unlikely to get such samples that are so different from null hypothesis. 

​	Let's look at the plot with our example. T-statistic has df=98, and it takes value 4.7647 (as you may have noticed that it's definitely far from 0).  P-value = 6.562e-06 (super small).  If we put value of T-statistic on plot (purple line), we can see, how far it is from 0.  And we can finally find a <i>p-value</i>, which is the probability to observe such value of T-statistic or even more extreme (greater in this case) under the assumption that null hypothesis is True (it's is simply area under the density curve, limited by value of T-statistic - purple vertical line). 

```{r}
set.seed(100)
v <- data.frame(v = rt(90000, df=98))

#calculate quantiles
upper_quantile <- quantile(v$v, probs = 0.95) 

p <- ggplot(v, aes(v)) + geom_density(fill="white")

d <- ggplot_build(p)$data[[1]]

p + geom_area(data = subset(d, x > upper_quantile), 
                   aes(x=x, y=y), 
                   fill="purple", 
                   alpha=0.2) +
  geom_text(x=3, y=0.04, label="5%", size=9) +
  geom_text(x=6.3, y=0.1, label=round(ttest$p.value,6), size=7) + 
  geom_text(x=6, y=0.4, label="T=4.76", size=9) + 
  geom_vline(xintercept = 4.7647, color = "purple", size=1.5)  + 
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) + xlim(-7, 7) + 
  theme(text = element_text(size=20)) +
  geom_segment(data=data.frame(x = 6, y = 0.08, xend = 5.5, yend = 0.005), mapping=aes(x=x, y=y, xend=xend, yend=yend), arrow=arrow(), size=2, color="darkblue") +
  labs(title='T dist with df=98') 
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/ttest2.png" alt="drawing" width="600"/> 

​	But what about <i>confidence interval</i> for mean difference? If it includes 0, if means that the sample data are compatible with the null hypothesis.  In our case 95% confidence interval is (1.550538, Inf), and it does not contain 0, which tell us again that we have to reject the H0. You can also think of the confidence interval as arms that "embrace" values that are consistent with the data. If the null value is "embraced", then H0 is certainly not rejected. 

## T test assumptions 

Before applying T-test, we must check underlying assumptions of this test:

* the data are normally distributed. To test this we can use Shapiro-Wilk’s significance test: 

```{r}
shapiro.test(df$treated)
[1] Shapiro-Wilk normality test

[1] data:  df$treated
[1] W = 0.96324, p-value = 0.1215


shapiro.test(df$control)
[1] Shapiro-Wilk normality test

[1] data:  df$control
[1] W = 0.93943, p-value = 0.01279
```

​	For both groups p-value > 0.05 meaning that the distribution of the data are not significantly different from normal distribution. In other words, we can assume normality.

​	Even if the data are not normal, with large enough sample sizes (n >= 30) the violation of the normality assumption should not cause major problems according to Central Limit Theorem.

​	Also, important to note, that normality test is sensitive to sample size. Small samples most often pass normality tests. So, it's better to add visual inspection to significance test. 

​	For this purpose we can use qqPlot (quantile-quantile plot). It represents the correlation between a given sample and the normal distribution. If all points fall approximately across reference line (a 45-degree line), it means normality. In our case we can say that data are normal.

```{r}
p1 <- ggqqplot(df$treated) + labs(title='treated') + theme(text = element_text(size=30))
p2 <- ggqqplot(df$control) + labs(title='control') + theme(text = element_text(size=30))

plot_grid(p1, p2, nrow = 1)
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/qqplot1.png" alt="drawing" width="1200"/>


```{r}
#example with non-normal data
#notice how the points do not fall across the line at the upper end 
set.seed(44)
x <- rgamma(40, shape = 4, rate = 4)
den <- density(x)
dat <- data.frame(x = den$x, y = den$y)
p3 <- ggplot(data = dat, aes(x = x, y = y)) + 
  geom_point(size = 3) +
  theme_classic() + labs(title='density') + theme(text = element_text(size=20))

p4 <- ggqqplot(rgamma(40, 4, 4)) + labs(title='qqplot') +theme(text = element_text(size=20))

plot_grid(p3, p4, nrow = 1 )
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/qqplot2.png" alt="drawing" width="1200"/>


* and the variances of the groups to be compared are homogeneous (equal).

  If the samples, being compared, follow normal distribution, to asses the equality of variances you can use Bartlett’s Test or Levene’s Test. 

  For Bartlett’s test the data must be normally distributed. The Levene's test is an alternative to the Bartlett test that is less sensitive to departures from normality.


```{r}
#p-value is 0.2098, it is not less than 0.05 level of significance, 
#so we can't reject the null hypothesis that the variance is different between groups
bartlett.test(list(df$treated, df$control))

[1] Bartlett test of homogeneity of variances

[1] data:  list(df$treated, df$control)
[1] Bartlett's K-squared = 3.3475, df = 1, p-value = 0.06731
```

​	Bartlett’s test has the null hypothesis that variances across samples are equal. As p-value (0.06731) > 0.05, we cannot reject the null hypothesis that the variance is the same for both groups.  We can also test it using Leven's test (it’s considered more robust since it is less sensitive to data deviations from normal distribution): 

```{r}
df %>% gather(group, count) %>% mutate(group = factor(group)) -> tmp
leveneTest(tmp$count, tmp$group)

[1] Levene's Test for Homogeneity of Variance (center = median)
[1]      Df F value  Pr(>F)  
[1]group  1  3.0742 0.08267 .
[1]      98                  
[1]---
[1]Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
```

​	P-value (0.08267) > 0.05, there is no evidence to reject null hypothesis about equal variances in populations. 

## Non-parametric test for 2-sample comparison

​	What if the assumption about normality is not True? For this situation we can use <b>the Wilcoxon test </b> (also known as <b> Wilcoxon rank sum test </b> or <b> Mann-Whitney test </b>). It is rank-based test. 

​	Let's say we have the same question about treated and control cells whether drug cause cell death or not. 

```{r}
data <- read.table('non_parametric_test.txt')

# plot it first 
p1 <- ggplot(data %>% gather(group, value), aes(x = group, y = value)) +
  geom_boxplot() + theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) + 
  theme(text = element_text(size=20)) 

p2 <- ggplot(data %>% gather(group, value), aes(x = value, fill=group)) +
  geom_density() + theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black")) + 
  theme(text = element_text(size=20)) 

# as you can see here, samples are not normally distributed according to the shape. As you may remember, if the number of observations is more than 30, we can use t-test even without normality assumption. Here it's exactly 30, and it's better to use non-parametric form
# surely you can also check normality with normality test and plot qq plot
plot_grid(p1, p2,  nrow = 1)
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/nonparam1.png" alt="drawing" width="1200"/>

​	As you can see here, p-value is extremely low (p-value < 0.05), so we can reject H0, which means that there is a difference between groups and treated group has more dead cells than control. 

```{r}
wilcox.test(data$treated, 
            data$control, 
            alternative = "greater", 
            paired = F)

[1] cannot compute exact p-value with ties # it means that there are repated values
[1]	Wilcoxon rank sum test with continuity correction

[1] data:  data$treated and data$control
[1] W = 898, p-value = 9.41e-12
[1] alternative hypothesis: true location shift is greater than 0
```

## Paired tests 

​	The paired samples t-test or non-parametric Wilcoxon test are used to compare the means between two related groups of samples. Paired t-test can be used only when the difference between data points is <i> normally </i> distributed. This can be checked using Shapiro-Wilk test. Otherwise, you should use non-parametric paired Wilcoxon test. Besides, if sample size is more than 30, t.test can be used without normality check. 

​	As an example of data, 20 cats received a treatment during half a year. We want to know whether the treatment has an impact on the weight of the cats. So, we have sample with untreated cats and another sample with <i> the same </i> cats, but treated. 

```{r}
data <- read.table('datasets/paired.txt', sep='\t')

# subsetting data
before <- subset(data,  group == "before", weight, drop = TRUE)
after <- subset(data,  group == "after", weight, drop = TRUE)

# plot the data
# package PairedData provides a paired plot to show the increase between the same cats
pd <- paired(before, after)
p1 <- plot(pd, type = "profile", col=group) + theme_bw() + theme(text = element_text(size=20)) 

p2 <- ggplot(data, aes(x = weight, fill=group, color = group)) +
  geom_density() + theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(), 
        axis.line = element_line(colour = "black"))  + 
  theme(text = element_text(size=20)) 

plot_grid(p1, p2, nrow = 1)
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/paired.png" alt="drawing" width="1200"/>


```{r}
# check normality of difference 
# p-value > 0.05, there is no evidence to reject H0 => we can assume normal distribution and use t.test here
shapiro.test(before - after)
[1] Shapiro-Wilk normality test

[1] data:  before - after
[1] W = 0.92344, p-value = 0.1154

# check for variances, P-value > 0.05, there is no evidence to reject H0 => we can assume equal variances
bartlett.test(list(before, after))
[1] Bartlett test of homogeneity of variances

[1] data:  list(before, after)
[1] Bartlett's K-squared = 0.095683, df = 1, p-value = 0.7571

# perform t.test. We are interested in overall difference in both directions, whether the cats gained weight or lost it, so it's two.sided option 
t.test(after, before, 
       paired = T,
       alternative = 'two.sided', 
       var.equal = T)


# p-value is low, < 0.05, so we can reject H0 at this level of significance => treatment has an impact on weight. 95% confidence interval for mean difference is (0.9558432, 1.9041568), which does not contain 0. And it is also strictly above zero, which suggests that the treatment caused weight gain. 

[1] Paired t-test

[1] data:  after and before
[1] t = 6.3123, df = 19, p-value = 4.656e-06
[1] alternative hypothesis: true difference in means is not equal to 0
[1] 95 percent confidence interval:
[1]  0.9558432 1.9041568
[1] sample estimates:
[1] mean of the differences 
[1]                    1.43 

# if the points difference is not normally distributed, you can use wilcox.test with paired=T:
wilcox.test(data$treated, 
            data$control, 
            alternative = "greater", 
            paired = T)
```


## Multiple testing corrections 

​	Remember this 0.05 value you always use to compare p-value with?  This is the significance level (alpha) for a statistical test. In hypothesis testing, if H0 was a True and you rejected it mistakenly, it is Type 1 error, it's a False Positive (when you discover something which is not real difference or effect).

​	Alpha is also type I error rate. So when a single test reaches p-value 0.05, we can intuitively understand that with 5% of chance we make a mistake or 5% of cases we thought significant are actually not. But what if we have multiple test to perform?  E.g. we have N samples and we want to apply t.test for each pair in the set (m tests).  If your chance of making an error in single test is alpha, then your chance to make one or more errors (false positives, mistakenly rejected H0) in m tests will be: 

<img src="https://render.githubusercontent.com/render/math?math=P(AtLeastOneError) = 1 - (1 - alpha)^m">



​	Let's plot it depending on m:

```{r}
prob_at_least_one <- function(m) {
  return (1 - (1 - 0.05)^m)
}

number_of_tests <- seq(1, 100)
prob_of_at_least_one_error <- sapply(number_of_tests, prob_at_least_one)


# if m is large, the chances to get at least one error will be nearly 100%!
plot(number_of_tests, prob_of_at_least_one_error, cex=1.5, cex.main=2.5, cex.lab=2.5, cex.axis=2.5)
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/pval_adj.png" alt="drawing" width="600"/>

​	If m is large, the chances to get at least one error will be nearly 100%! That’s why we need to adjust the p-values for the number of hypothesis tests performed, or to control type I error rate.

```{r}
# generate 100 t.tests p-values 
set.seed(123)
p_values <- replicate(100, t.test(rnorm(20, runif(1, 0, 1), 1), rnorm(20,runif(1, 0, 1), 1))$p.value)

sum(p_values <= 0.05) / 100 # 20 of p-values are significant
[1] 0.2
```

​	There are multiple way to adjust p-values. 

* Bonferroni correction 

```{r}
pvalues_adj <- p.adjust(p_values, method = "bonferroni")
sum(pvalues_adj <= 0.05) / 100 # only 3 significant p_values are left after adjustment. It's really strict type of adjustment 
[1] 0.02
```

* Benjamini and Hochberg

```{r}
pvalues_adj <- p.adjust(p_values, method="BH")
sum(pvalues_adj <= 0.05) / 100 # it left more significant p-values 
[1] 0.05 
```


## Correlation 

​	Correlation analysis is used to study the association between two or more variables.

​	There are 2 methods to perform  <i> linear </i> correlation analysis (by linear I mean that two variables Y and X satisfy the equation Y = aX + b): 

* Parametric test: Pearson correlation. It measures a linear dependence between 2 variables. You can apply it only if both variables follow normal distribution. 

* Non-parametric test: Kendall and Spearman correlation, these tests do not require normality of the data, they are rank-based. 

  These tests give you the correlation coefficient, which ranges from -1 (perfect negative correlation) to 1 (perfect positive correlation).  A correlation of 0 shows no linear relationship between the movement of the two variables.

  Let's calculate correlation coefficient:

```{r}
var1 <- c(21.0, 21.0, 22.8, 21.4,18.7, 18.1, 14.3, 24.4,22.8,  19.2,  17.8, 16.4, 17.3, 15.2, 10.4, 10.4, 14.7)
var2 <- c(160.0, 160.0, 108.0, 258.0, 360.0, 225.0, 360.0, 146.7, 140.8, 167.6, 167.6, 275.8, 275.8, 275.8, 472.0, 460.0, 440.0)

# plot them first to convince that there is linear dependence 
plot(var1, var2)

# check normality assumption first
shapiro.test(var1) # p-value = 0.5916, we can assume normality
shapiro.test(var2) # p-value = 0.06996, we can assume normality, but it close to significance level 0.05 :) 

# this calculates correlation coefficient
# it close to -1 which means that 2 variables are negatively correlated
cor(var1, var2, method='pearson')
[1] -0.874775
```


​	The correlation coefficient measures only the strength of a relationship in samples only. Because we want to draw conclusion about populations not just samples, we have to conduct a statistical significance test and obtain p-value. 

* H0: correlation coefficient = 0
* H0: correlation coefficient != 0

```{r}
# as we can see, p-value <0.05, we have to reject H0, so there is a non-zero significant correlation between variables
# confidence interval, (-0.9542145 -0.6800696), is strictly negative and does not contain 0
cor.test(var1, var2, method = 'pearson')

[1] Pearson's product-moment correlation
[1] data:  var1 and var2
[1] t = -6.9923, df = 15, p-value = 4.335e-06  
[1] alternative hypothesis: true correlation is not equal to 0
[1] 95 percent confidence interval:
[1]  -0.9542145 -0.6800696
[1] sample estimates:
[1]       cor 
[1] -0.874775 


# if you data are not normal, you can use non-parametric test:
cor(var1, var2, method = 'spearman')
cor.test(var1, var2, method = 'spearman')
```

<b> Spurious correlations </b>

​	Correlation coefficient can be high, but dependence between variables is not linear. 

```{r}
x <- seq(1, 50, 0.5)
y1 <- x^2 + 3*x^3
y2 <- cos(0.5*x) + log(14*x)

par(mfrow=c(1, 2))
plot(x, y1, cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)
text(x = 10, y = 100000, labels = paste('corr:', round(cor(x, y1), 3)), col='red',  cex=1.5)
text(x = 10, y = 150000, labels = 'x^2 + 3*x^3', col='blue',  cex=1.5)
plot(x, y2, cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)
text(x = 10, y = 6.7, labels = paste('corr:', round(cor(x, y2), 3)),  col='red',  cex=1.5)
text(x = 19, y = 7.5, labels = 'cos(0.5*x) + log(14*x)',  col='blue',  cex=1.5)
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/spcorr.png" alt="drawing" width="1200"/>

Remember, correlation does not mean causation. 



<b> Correlation matrix plot </b>

​	If you have multiple variables, you can create a fancy plot like this to show pairwise correlation coefficients:

```{r}
data <- read.table('datasets/corrplot.txt', sep='\t')

head(data, 3)
[1]       var1  var2 var3 var4 var5
[1] 1	   21.0	16.46	   4	  4	 160
[1] 2	   21.0	17.02	   4	  4	 160
[1] 3	   22.8	18.61	   4	  1	 108


# this calculates the correlation matrix 
M <- cor(data)

head(M, 3)
[1]           var1       var2       var3       var4       var5
[1] var1 1.0000000  0.4186840  0.4802848 -0.5509251 -0.8475514
[1] var2 0.4186840  1.0000000 -0.2126822 -0.6562492 -0.4336979
[1] var3 0.4802848 -0.2126822  1.0000000  0.2740728 -0.5555692

# corrplot package allows you to plot fancy corraltion plot like this
# blue shades represent positive correlation, the darkest is the highest (1)
# red shades represent negative correlations, the darkest is the lowest (-1)
# argument type "upper" means that you plot only upper triangle
# argument order "hclust" means that variables are clustered by similarity 
corrplot(M, type="upper", order="hclust")
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/corrplot.png" alt="drawing" width="500"/>
