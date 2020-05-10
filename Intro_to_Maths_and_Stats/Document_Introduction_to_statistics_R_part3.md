# Introduction to Statistics in R Worksheet. Part 2

​	Linear regression analysis is a machine learning method which is used to predict a continuous outcome variable (y) based on the value of one or multiple predictor variables (x). It assumes a linear relationship between the outcome and the predictor variables. Basically, it builds a mathematical equation like y=bx1 + bx2 + ... + a, which then can be used to predict the outcome variable (y) using new values of the predictor variables x. 

* a - intercept
* b1, b2, ..., bn - regression coefficients or weights 

​	The linear regression coefficients are determined so that the error in predicting the outcome value is minimized. <i>Ordinary Least Squares </i> is used to to compute these coefficients. Predictor variables can be both continuous and categorical. 

​	In some cases, the relationship between the outcome and the predictor variables is <b> not linear </b>. In these situations, you need to build a non-linear regression, such as polynomial and spline regression.

​	Let's start with simple linear regression analysis. We are going to use data about death rate (continuous variable) and how it depends on availability of doctors, hospitals, income and population density (source: Life In America's Small Cities, by G.S. Thomas).

Columns description:

* death_rate = death rate per 1000 residents 

* doctors = doctor availability per 100,000 residents

* hospitals = hospital availability per 100,000 residents

* income = annual per capita income in thousands of dollars

* pop_density = population density people per square mile

  We are going to predict death rate based on other variables in dataset.

  Let's look at the data:

```{r}
df <- read.table('datasets/linreg.txt', sep='\t', header=T)
names(df) <- c('death_rate', 'doctors', 'hospitals', 'income', 'pop_density')

head(df, 3)
[1]   death_rate doctors hospitals income pop_density
[1]  1	 8.0	         78	    284	      9.1	       109
[1]  2	 9.3	         68	    433      	8.7	       144
[1]  3	 7.5	         70   	739	      7.2	       113

# plot the data in a form of scatterplot
# add a smoothed line to show the linear dependency
# it looks like there is some linear dependency
# we will check it by model
df %>% gather(key, value, -death_rate) %>% 
  ggplot(aes(x = value, y = death_rate)) +
  geom_point() +
  stat_smooth(method = lm) +
  facet_wrap(~key, scales = 'free') +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=30))
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/regres1.png" alt="drawing" width="1200"/>

​	Let's start with the simple model with only one predictor (income).

```{r}
# define variables: outcome (y) and predictor(x)
y <- df$death_rate #real y values, outcomes 
x <- df$income # predictor x values

# build a model
# syntax is pretty simple: 
simple_model <- lm(death_rate ~ income, df)
simple_model
# output of the model is the intercept and the beta coefficient
[1] Call:
[1] lm(formula = y ~ x)

[1] Coefficients:
[1] (Intercept)            x  
[1]    11.8145      -0.2659  
```

​	So, we have got the formula for death rate:

<b> 	death_rate = -0.2659 * income + 11.8145 </b>

​	What can this formula tell us about the relationship between outcome and predictor?

* The intercept is equal to 11.8145. It can be interpreted as the predicted death rate unit (number of deaths per 1000 residents) if income is 0. So for income 0 we might expect 11.8145 deaths per 1000 residents. 

* The regression coefficient (it's also called a slope) for the income variable is -0.2659. Income is represented as annual per capita income in thousands of dollars. So for a income equal to 1 thousand of dollars we can expect an decrease of -0.2659 * 1 units in death rate. So in total, death rate would be 11.8145 - 0.2659*1 = 11.5486 units of death rate, which means 11.5486 deaths per 1000 residents. 

Let's plot our data with found regression line. 
As you can see here some of the points are above the black line and some are below it. 
Besides, we will add residual errors - differences between real y and predicted y values as red lines.

```{r}
# yhat = predicted values, yhat = a*x + b
yhat <- simple_model$fitted.values

# difference between real y and predicted y values
diff <- y-yhat 


reg_df <- data.frame(x = x, y = y, outcomes = yhat, diff = diff)

# red lines = residual errors or residuals, difference between real y and predicted y
ggplot(reg_df, (aes(x=x, y=outcomes)))+
        geom_line()+ 
       geom_segment(aes(x=x, xend=x, y=y, yend=outcomes), col="red")+
        geom_point(aes(x=x, y=y), color='black') +
       labs(title="regression errors (residuals)", color="series", ylab='y') +
  theme(panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        axis.line = element_line(colour = "black")) +
  theme(text = element_text(size=30)) + theme(legend.position = "none")
```

<img src="https://github.com/triasteran/Data-Science-For-Life-Science/blob/master/Statistics_and_Math_in_R/pictures/regres.png" alt="drawing" width="600"/>

​	Importantly, we need to estimate the usability of the model: how significant is the model and what are impacts of the coefficients.

​	You can use function summary:

```{r}
summary(simple_model)
[1] Call:
[1] lm(formula = y ~ x)

[1] Residuals:
[1]     Min      1Q  Median      3Q     Max 
[1] -5.9811 -0.8620  0.2975  1.1987  2.9530 

[1] Coefficients:
[1]             Estimate Std. Error t value Pr(>|t|)    
[1] (Intercept)  11.8145     2.0249   5.835 3.72e-07 ***
[1] x            -0.2659     0.2132  -1.247    0.218    
[1] ---
[1] Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

[1] Residual standard error: 1.654 on 51 degrees of freedom
[1] Multiple R-squared:  0.02958,	Adjusted R-squared:  0.01055 
[1] F-statistic: 1.555 on 1 and 51 DF,  p-value: 0.2181
```

The summary outputs consists of following parts:

* <b> Call </b> shows the formula of the regression 

* <b> Residuals </b> shows the basic points of distribution of residual errors. Residuals are essentially the difference between the actual observed response values and predicted ones. When assessing how well the model fit the data, you should look for a
  symmetrical distribution across these points on the mean value zero. Here the distribution does not seem to be strongly symmetrical (minimum and maximum should be roughly equal in absolute value as well as quantiles, and we have min=-5.9 and max=2.9). That means that the model predicts certain points that fall far away from the actual observed points. 

* <b> Coefficients </b> shows the regression beta coefficients (slopes), intercept  and their statistical significance. 

  * Column 'Estimate' shows values of the intercept and coefficients
  * Column 'Std. Error' shows standard error of the coefficients. In the example, the intercept can vary by 2.0249 and the slope can vary by 0.2132, in case we ran the model again and again. Ideally we want them to be lower relative to their coefficients. 

  * Column 't value' shows the t-statistic of the test: 

    * H0: coefficient = 0  (there is no link between predictor and outcome)
    * H1: coefficient != 0 (there is a link between predictor and outcome)

  T-statistics here represents how many standard errors our coefficient estimate is far away from 0 (as you remember t-statistic from 2-samples t.test, it measures  the mean difference relative to the variation of the data, so it's basically has the same meaning):  

  ![equation](http://latex.codecogs.com/gif.latex?T_Statistic%3D%5Cfrac%7B(coeff.estimate)-0%7D%7BSE%7D)  

  We want it to be far away from zero as this would indicate we could reject the null hypothesis. In this
  example T-statistic for intercept is far away from zero and is large relative to the standard error, but for the slope it does not appear that a strong relationship between predictor and outcome exists.

  * Column 'Pr(>|t|)' shows p-value of the test. The higher the t-statistic and the lower the p-value, the more significant the predictor. 

* <b> Signif. codes </b> are for the orders of p-value.

* <b> Residual standard error </b> is the average variation of points around the fitted regression line. The lower the RSE, the better it is. You can use it to compare models. 

* <b> Multiple R-squared. </b> R-squared represents the proportion of variation in the data, explained by model. The higher the R-squared, the better the model. Adjusted R-squared increases when extra explanatory variables are added to the model. In this model R-squared is 0.02958 and adjusted R-squared is 0.01055, they are considarably low, which means that this model does not have the ability to explain a lot of variability in the outcome data.  

* <b> F-statistic. </b> This statistic came from F-test. F-test here tests whether any of the independent variables in a multiple linear regression model are significant. In general, it can be also used to test equality of variances in two normal populations. 

  *  H0: all coefficients = 0 
  *  H1: at least one coefficient is not equal 0

  For this model, we have got  p-value: 0.2181, which means that we can't reject H0 and all coefficients here are non-significant. 

  In total, our model is not suitable and predictor that we used is not good to represent the outcome. 

  We can try to use multiple predictors. In this case only 'pop_density' predictor seems to be promising (Pr(>|t|) = 0.0587), however  distribution of residuals does not seem to be normal (no symmetry) as well as adjusted R-squared (0.07235) is still pretty low. P-value of F-test is 0.1075, which tells us that we can't reject H0 and all predictors are not significant (all coefficients are equal 0).  

```{r}
model2 <- lm(death_rate ~ ., df)

summary(model2)

[1] Call:
[1] lm(formula = death_rate ~ ., data = df)

[1] Residuals:
[1]     Min      1Q  Median      3Q     Max 
[1] -5.6404 -0.7904  0.3053  0.9164  2.7906 

[1] Coefficients:
[1]               Estimate Std. Error t value Pr(>|t|)    
[1] (Intercept) 12.2662552  2.0201467   6.072 1.95e-07 ***
[1] doctors      0.0073916  0.0069336   1.066   0.2917    
[1] hospitals    0.0005837  0.0007219   0.809   0.4228    
[1] income      -0.3302302  0.2345518  -1.408   0.1656    
[1] pop_density -0.0094629  0.0048868  -1.936   0.0587 .  
[1] ---
[1] Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

[1] Residual standard error: 1.601 on 48 degrees of freedom
[1] Multiple R-squared:  0.1437,	Adjusted R-squared:  0.07235 
[1] F-statistic: 2.014 on 4 and 48 DF,  p-value: 0.1075
```

How to compare 2 models?  We can use ANOVA for that.  It tests whether one model is significantly better at capturing the data than the other model. If the resulting p-value is sufficiently low (usually less than 0.05), we conclude that the first model is significantly better than the second one, and thus favor the first model. 

As we can see here, Pr(>F) = 0.1084, so two models are not different significantly.

```{r}
anova(model2, simple_model)

[1] Analysis of Variance Table

[1] Model 1: death_rate ~ doctors + hospitals + income + pop_density
[1] Model 2: death_rate ~ income
[1]   Res.Df    RSS Df Sum of Sq      F Pr(>F)
[1] 1     48 123.07                           
[1] 2     51 139.48 -3   -16.403 2.1324 0.1084
```
