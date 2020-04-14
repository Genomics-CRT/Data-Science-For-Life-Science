
# Installing Anaconda

Anaconda is a package manager, this simply means that it allows users to create environments on their computer 
which contains the software required to do data science. 

It can be downloaded for Windows/Mac/Linux here https://www.anaconda.com/distribution/  
Be sure to select the correct operating system. Please note: Anaconda will require approx. 2.5GB of hard drive space. 

*Note: Please select Python 3.7* 

The installation is pretty straight forward on both Mac and Windows.
Select the default option for everything except the installing microsoft VS code prompt during the Mac install, 
do not install it, just click continue.

We will be using Anaconda as it is cross platform and we are aware that many people do not use Linux on their computers. 
We will be doing a short course on installing and using Linux and the command line if there are people interested in learning
it. Linux is the operating system most used in data science.

Python comes pre-installed with Anaconda but the other commonly used programming language in bioinformatics, R, does not. 
We will walk you through installing R and R-studio in the next section.


## Installing R and R-Studio

R is a very useful programming language for dealing with statistics and visualisations of datasets and has many packages which are commonly used by bioinformaticians. We first need to install the R language onto our computers and then install R-Studio which is an integrated development environment (IDE) for R. You will see the term IDE used quite a lot in data science, it is simply a computer program which makes it easier to work with programming languages.

Installing R is different depending on whether you are using Mac or Windows.

### To install using Mac:

Open the terminal, this can be found using the spotlight search and typing in terminal.
Once in the terminal type the following command:

`conda install r-essentials --yes`

Anaconda will then install all of the libraries, this may take some time.
Next, install R-Studio using the following command in the terminal:

`conda install -c r rstudio --yes`

R-Studio will now be installed.



### To install using Windows:

Search for Anaconda Prompt on your system, this is a built in terminal for Windows users.

Type the following command into the command line:

`conda install r-essentials`

You will be asked to proceed Y/N
Type Y and hit enter, installation of R and various packages will begin, this may take some time to complete. Next step is to install R-Studio

In the command line, type in:

`conda install -c r rstudio`

You will be asked to proceed, type Y and hit enter.
R-studio will now be installed.


# Point and click method to install R/R-Studio on all system types

You should ideally get familiar with using the command line to install software and packages but we are aware that there can be issues when using windows.

This is a point and click method of installing R/R-studio that you can use if the previous methods did not work for you.

First, open Anaconda Navigator and click on environments

![environment tab](https://github.com/Genomics-CRT/images/blob/master/environmenttab.png)

Next, click on create at the bottom. Name your environment something R related so you know what it is for. Select Python then in the dropdown menu select Python 3.7, and select the R checkbox.

![renvironmentname](https://github.com/Genomics-CRT/images/blob/master/renviron.png)

Once this is done click create and wait for it to finish setting up the environment.  
Go to the Home tab, find R-Studio and install it. 

![hometabrstudio](https://github.com/Genomics-CRT/images/blob/master/rstudioinstall.png)

If you get the error message "R-studio cannot be installed on this environment, would you like to set up a new one?" click yes and allow anaconda to set up a new R-studio environment for you. 

Congratulations! You now have everything you need to begin learning Bioinformatics!
