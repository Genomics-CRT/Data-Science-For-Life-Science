# Introduction to R - Part Two

## 1. Data Structures 

You should now have a basic understanding of basic data structures such as vectors. However it is impractical to store all data in singular vectors.  Other data structures have been designed to store higher dimensional data.

### 1.1 Matrices

Matrices are 2-dimensional data structures which contain data of the same type. Data structures >2-d are known as arrays but matrices will remain our primary focus due to their more widespread use.

The standard function in R used to create matrices is matrix() which takes as input the data required, the number of columns and the number of rows.

- The example below creates a 3x3 matrix using the numbers 1-9.
- The same matrix can be created by supplying vectors.

```{R}
#make a matrix 
matrix(1:9, ncol=3, nrow=3)

      [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9

#make a matrix using vectors

#create vectors
x<- c(1,2,3)
y<- c(4,5,6)
z<- c(7,8,9) 

#supply vectors to matrix
matrix(data=c(x,y,z), ncol=3, nrow=3)

    [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9
```


Similarly matrices can be constructed from character vectors.

```{R}
matrix(data=c("A","T", "C", "G"), 2, 2)

     [,1] [,2]
[1,] "A"  "C" 
[2,] "T"  "G" 
```

However, matrices cannot contain character and numeric entries.

This matrix appears normal but in fact the numeric entries have been converted to characters as denoted by the quotation marks.
```{r}
my_matrix=matrix(data=c("A","T", 1, 2), 2, 2)
my_matrix

     [,1] [,2]
[1,] "A"  "1" 
[2,] "T"  "2" 
```


Real-world data often contains a mixture of data types which suggests that matrices are not optimal for many datasets. For this reason the most commonly used data structure is a ```Dataframe```.


### 1.2 Dataframes

Dataframes are the primary way in which large datasets are stored in R. They can contain a variety of data types such as character, numeric and factor vectors.

The standard way to create a dataframe is using the function data.frame() where predetermined vectors can be supplied (as above) or vectors can be supplied within the function. The names of each vector can also be supplied.

Dataframes can also be created by "binding " vectors together either as rows or columns using the functions rbind() or cbind respectively.

**Note: **cbind() and rbind() can also be used to create matrices.

The following example creates a  dataframe that contains information on the number of bases in a DNA sequence per sample in addition to an imagined phenotype per sample.

***Using data.frame***

```{r}
##create using data.frame()
data.frame(A=c(3,4,6,3,8), T=c(2,4,5,3,2), C=c(3,6,7,4,9), G=c(4,6,2,1,3), pheno=c("y","n", "y", "n", "y"))

 A T C G pheno
1 3 2 3 4     y
2 4 4 6 6     n
3 6 5 7 2     y
4 3 3 4 1     n
5 8 2 9 3     y


```



***Using cbind()***

```{r}
#create using cbind()

#create vectors
A=c(3,4,6,3,8)
T=c(2,4,5,3,2)
C=c(3,6,7,4,9)
G=c(4,6,2,1,3)
pheno=c("y","n", "y", "n", "y")

#####Note: using cbind() for this example will convert the numeric vectors to characters
#####cbind.data.frame() is used to preserve the numeric nature of the vectors
#####If cbind() is used the vectors can be converted back to numeric using as.numeric()
#####You can observe the differences in output below

#create dataframe

##cbind()
my_df_char<-cbind(A,T,C,G,pheno)
my_df_char
 	
my_df_char
     A   T   C   G   pheno
[1,] "3" "2" "3" "4" "y"  
[2,] "4" "4" "6" "6" "n"  
[3,] "6" "5" "7" "2" "y"  
[4,] "3" "3" "4" "1" "n"  
[5,] "8" "2" "9" "3" "y"  

#cbind.data.frame()
my_df<-cbind.data.frame(A,T,C,G,pheno)
my_df

  A T C G pheno
1 3 2 3 4     y
2 4 4 6 6     n
3 6 5 7 2     y
4 3 3 4 1     n
5 8 2 9 3     y
```



## 2. Exploring Data

Now that we have constructed a dataframe, we need to know how to explore it. While the toy example we have created is easily explored by calling the variable name most real-world examples will not be. This section will describe the most commonly used functions and can be used for both dataframe and matrices except where explicitly specified.

### 2.1 Viewing and Accessing Data

Dataframes can be viewed using the following functions:

- head() - This is used to view the first entries of a dataframe which by default is 6 rows.  This can be altered by supplying the n=x argument to the function 
- tail() - Operates similarly to head() but displays the last rows of a dataframe.

```{r}
#head data
head(my_df, n=3)

  A T C G pheno
1 3 2 3 4     y
2 4 4 6 6     n
3 6 5 7 2     y

#tail data
tail(my_df, n=2)

  A T C G pheno
4 3 3 4 1     n
5 8 2 9 3     y
```

Often viewing the first (or last) number of rows will not be sufficient. Instead  you may want to access specific rows or columns. 

There are two ways to do this:

- $ - This can be used to access a particular column.
- [x,y] - Indexes can be used to access particular columns, rows or a specific entry. The x entry corresponds to the row number while the y value corresponds to the column number. Using x or y will give the column or row only while using both gives the entry at that location (column and row names can also be used).

```{r}
#Isolate the phenotype column
my_df$pheno
[1] y n y n y

my_df[,5]
[1] y n y n y

#Pull out the second row
my_df[2,]
  A T C G pheno
2 4 4 6 6     n

#Find the second entry of the third column
my_df[2,3]
[1] 6

#Head the first two entries of the A column
head(my_df[,1], n=2)
[1] 3 4

##OR##
#Get first two entries of column A

my_df[1:2,1]
[1] 3 4

my_df[1:2, "A"]
[1] 3 4
```



### 2.2 Summarising Data

When we need to look at the data overall there are a few things we may want to know such as the number of columns, rows, average values etc... The following functions are commonly used in these situations.

- dim() - Gives the overall dimensions of a data structure 

- ncol() - Gives the number of columns

- nrow() - Gives the number of rows

  

```{r}
#Get number of rows and columns
dim(my_df)
[1] 5 5

#Get number of rows
nrow(my_df)
[1] 5 

#Get number of columns
ncol(my_df)
[1] 5 
```



- dimnames() - Gives/sets the names of rows and columns
- rownames() - Give/sets the names of rows
- colnames() - Gives/sets the names of columns
- names() - Gives/sets the names of columns



```{r}
#Get column and row names
dimnames(my_df)
[[1]]
[1] "1" "2" "3" "4" "5"

[[2]]
[1] "A"     "T"     "C"     "G"     "pheno"

#Get row names
rownames(my_df)
[1] "1" "2" "3" "4" "5"

#Get column names
colnames(my_df)
[1] "A"     "T"     "C"     "G"     "pheno"

names(my_df)
[1] "A"     "T"     "C"     "G"     "pheno"

#Set new row names
rownames(my_df)=c("Sample_1","Sample_2", "Sample_3","Sample_4", "Sample_5")
rownames(my_df)
[1] "Sample_1" "Sample_2" "Sample_3" "Sample_4" "Sample_5"

#Change the name of the "pheno" column to "Phenotypes"
#Use indexing to specify which column
colnames(my_df)[5]="Phenotypes"
colnames(my_df)
[1] "A"          "T"          "C"          "G"          "Phenotypes"

##Get indexes of columns and rows using data.frame(), rownames() and colnames()
data.frame(colnames(my_df))
colnames.my_df.
1               A
2               T
3               C
4               G
5      Phenotypes
data.frame(rownames(my_df))
  rownames.my_df.
1        Sample_1
2        Sample_2
3        Sample_3
4        Sample_4
5        Sample_5
```



- summary() - Gives a summary of the data frame per column including mean, median, min, max etc..

  **Note:** As a factor vector, the summary contains the number of samples for each level.

```{R}
#Get summary stats
summary(my_df)
     A             T             C             G       Phenotypes
 Min.   :3.0   Min.   :2.0   Min.   :3.0   Min.   :1.0   n:2       
 1st Qu.:3.0   1st Qu.:2.0   1st Qu.:4.0   1st Qu.:2.0   y:3       
 Median :4.0   Median :3.0   Median :6.0   Median :3.0             
 Mean   :4.8   Mean   :3.2   Mean   :5.8   Mean   :3.2             
 3rd Qu.:6.0   3rd Qu.:4.0   3rd Qu.:7.0   3rd Qu.:4.0             
 Max.   :8.0   Max.   :5.0   Max.   :9.0   Max.   :6.0       

```



The toy example we have used thus far had been useful in demonstrating some of the basic functions concerning dataframes. However going forward a larger and more realistic dataset will be helpful as we learn how to manipulate dataframes. In order to do this we must first **read in **a dataset.

## 3. Reading In and Writing Out Data

Creating large dataframes from scratch by combining vectors is not a common occurrence. Often data is created as the output of a program (or study) and is then read in for further analysis.

### 3.1 Reading In Data  

Data can be read into R in a number of ways dependent on file type.  The following functions read in data and convert  data to dataframes.

- read.table() -  Most generalised function for reading in data
- read.csv() - Used for comma separated files
- read.delim() - Used for delimited file (default is tab)

The main difference between these functions are the arguments that are passed to them and the default values these arguments contain. 

The following arguments are common to all three above functions:

- file - This is the file to be read in contained within quotation marks e.g. "my_file.txt"

- header - Set to header=TRUE if the first row contains column names

- sep - This is the separation used to separate entries.

  - read.table uses whitespace separation as default which is denoted as sep=" "

  - read.csv uses comma separation as default which is denoted as sep=","

  - read.delim uses tab separation as default which is denoted as sep="\t"

  - read.table can read in take whitespace and tab separated files by altering the sep argument

    

    

The read.table function also contains the row.names argument which if set as row.names=1 will take the first column as rownames.

The GTEx<sup>1</sup> portal contains expression and genotypic data in order to enable the study of tissue specific gene expression.  For this tutorial we will read in a file called "gtex_altered.txt" which was adapted from the phenotypic annotation data freely available on the portal. It contains information on each sample such as tissue of origin, sequencing type and other pathological and experimental information.  As we are not concerned with the exact nature of the data for this tutorial, particular columns will only be described as needed. For full information regarding the data you can visit https://gtexportal.org/home/datasets and download the following file listed under the ANnotations section: GTEx_Analysis_v8_Annotations_SubjectPhenotypesDD.xlsx.

```{R}
##read in data
gtex<-read.table("gtex_altered.txt", header=TRUE, sep ="\t")

#explore
#head data
#result omitted as it is quite large
head(gtex)

#get row/col numbers
dim(gtex)
[1] 6149   62

##get col names
colnames(gtex)
[1] "SAMPID"    "SMATSSCR"  "SMCENTER"  "SMRIN"     "SMTS"      "SMTSD"     "SMUBRID"   "SMTSISCH" 
 [9] "SMTSPAX"   "SMNABTCH"  "SMNABTCHT" "SMNABTCHD" "SMGEBTCH"  "SMGEBTCHD" "SMGEBTCHT" "SMAFRZE"  
[17] "SMGTC"     "SME2MPRT"  "SMCHMPRS"  "SMNTRART"  "SMNUMGPS"  "SMMAPRT"   "SMEXNCRT"  "SM550NRM" 
[25] "SMGNSDTC"  "SMUNMPRT"  "SM350NRM"  "SMRDLGTH"  "SMMNCPB"   "SME1MMRT"  "SMSFLGTH"  "SMESTLBS" 
[33] "SMMPPD"    "SMNTERRT"  "SMRRNANM"  "SMRDTTL"   "SMVQCFL"   "SMMNCV"    "SMTRSCPT"  "SMMPPDPR" 
[41] "SMCGLGTH"  "SMGAPPCT"  "SMUNPDRD"  "SMNTRNRT"  "SMMPUNRT"  "SMEXPEFF"  "SMMPPDUN"  "SME2MMRT" 
[49] "SME2ANTI"  "SMALTALG"  "SME2SNSE"  "SMMFLGTH"  "SME1ANTI"  "SMSPLTRD"  "SMBSMMRT"  "SME1SNSE" 
[57] "SME1PCTS"  "SMRRNART"  "SME1MPRT"  "SMNUM5CD"  "SMDPMPRT"  "SME2PCTS" 
```



### 3.2 Writing Out Data

Saving our analysed data is known as writing out. This is completed using the below functions which are similar to those used to read in data.

- write.table() -  Most generalised function forwriting out data
- write.csv() - Used for comma separated files

The main difference between these functions are the arguments that are passed to them and the default values these arguments contain. 

The following arguments are common to all three above functions:

- file - This is the file name to be wrote out contained within quotation marks e.g. "my_file.txt"
- x - This is the variable name of the data to be saved
- col.names - Set to TRUE if the first row contains column names
- row.names - Set to TRUE if the first column contains row names
- quote - Wraps character and factor vector entries in strings
- sep - This is the separation used to separate entries.

  - write.table uses whitespace separation as default which is denoted as sep=" "

  - write.csv uses comma separation as default which is denoted as sep=","




To write out the gtex dataframe we have just created we would do the following:

```{R}
###write out
write.table(gtex, "my_new_table.txt", sep="\t", row.names=T, col.names=T)
```



Now that we can read in our new data we can move on to perhaps the most important step **manipulating data**.



## 4. Manipulating Data

Having the ability to manipulate data is a very important skill. Datasets rarely contain all the information we may need and often must be processed in order to achieve our end goals.

### 4.1 Removing Rows and Columns

Rows can be removed as follows.

```{r}
#Remove the first row
 gtex <- gtex[-c(1),] 

#Remove rows 5:8
gtex <- gtex[-c(5:8),]
```



This dataframe has 63 columns. We will now remove some columns which are not needed.

```{r}
#Remove from column 18 onwards
gtex <- gtex[,-c(19:63)]

#Remove column 18
gtex <- gtex[,-18]

#Or if we know the name, remove column 17
gtex$SMGTC<- NULL

```



### 4.2 Missing Values

Many datasets contain missing values, if these values need to be removed/altered there are two common ways to deal with these issues.

**Removing NA's**

Samples with missing values may  have to be removed from a dataset in this case we remove all rows which contain NA's using na.omit(). For this tutorial we will remove all rows containing missing values but another common method is described below for completeness.

```{r}
## NOTE: This dataset contains blank entries i.e. whitespace ##
#For this exercise we will treat them as NA
#Set these to NA as follows
gtex[gtex==""] <- NA
gtex[gtex==" "] <- NA
##Remove NA's
gtex_complete <- na.omit(gtex)
```



**Setting NA's to 0**

Often, setting missing values to zero will be required to proceed with analysis. This can be achieved using the is.na() function to check for NA's and set them to 0 as follows:

```{r}
##set NA to 0
#don't bother running this, we have already removed na's
gtex[is.na(gtex)] <- 0
```



### 4.3 Removing Duplicates

If our dataset contains duplicated data, it must be removed in order to generate reliable results. This can be achieved using the duplicated() function.

```{r}
##Check for duplicates
#Returns a vector of logical values (only first results shown)
duplicated(gtex_complete)
 [1] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
[18] FALSE FALSE FALSE 

#Check which rows are duplicated
which(duplicated(gtex_complete))
[1] 2443 2444 2445 2446 2447 2448 2449 2450 2451 2452 2453
[12] 2454 2455 2456 2457 2458 2459 2460 2461 2462 2463 2464
[23] 2465 2466 2467 2468 2469 2470

##Remove duplicates
#! allows values not duplicated to remain in the dataset.
gtex_dedup <- gtex_complete[!duplicated(gtex_complete), ]

#Check if any duplicates are left
which(duplicated(gtex_dedup))
integer(0)
```



### 4.4 Adding Rows and Columns

Now that our dataset has undergone rudimentary cleaning we can now think about adding more data.

For example, suppose you want to add a new column or row, we could do this by binding the new column/row to our dataframe using cbind() or rbind, the order in which the arguments are supplied will affect where the column/row is bound to.

```{r}
##add new column
#example only
gtex_new<-cbind(gtex,my_new_column)

##add new row
#example
gtex_new_r<-rbind(gtex, my_new_row)
```

Columns can also be added by naming a new column of the dataframe and assigning the new values using either a vector or column of a pre-existing dataframe etc. Columns can also be created using the data contained within the dataframe. 

For example, the  SMRIN columnof our dataframe contains information regarding the RIN number for each sample.  RIN numbers give an idea as to the quality of the RNA used in the experiment. For this next example we will imagine that we have been advised by our colleagues that the RIN values in our dataset are incorrect. The RIN values we have are greater by 0.5. To correct this we will construct a new column which contains RIN values that corrects for this error.

```{R}
##create new column
##RIN/2
gtex_dedup$RIN_corrected<- gtex_dedup$SMRIN - 0.5
#head new column and old column
head(gtex_dedup[,c(4,17)])
SMRIN RIN_corrected
4    8.0           7.5
5    6.9           6.4
13   7.8           7.3
14   7.3           6.8
15   7.0           6.5
20   6.4           5.9

#Remove old column
gtex_dedup$SMRIN=NULL
```



### 4.5 Subsetting

Subsetting involves accessing/filtering data based on certain conditions. If you look closely we have already used certain functions such as na.omit() to subset our data.  We have also accessed certain columns using indexing which also subsets our data.

The two most common ways used to subset data are:

- Square Brackets []
- subset()

Square Brackets can be used to subset data and both indexes and column names can be supplied to them to do this.

As stated RIN numbers indicate RNA quality with 10 indicating highest quality and 1 suggesting highly degraded RNA. Suppose we want to only keep samples with RIN >= 5. The , after the five indicates that we want to select rows that meet this condition and all columns must also be retained. If we decide that we only want specific columns this can also be specified.

```{r}
#remove entries with RIN <=5
gtex_quality<-gtex_dedup[gtex_dedup$RIN_corrected >= 5,]
#remove  entries with RIN <=5, including columns 1:5 and 10:16
gtex_qual_cols=gtex_dedup[gtex_dedup$RIN_corrected >= 5,c(1:5, 10:16)]

```



 More than one condition can also be added to the square brackets. Suppose we want the above conditions and samples that were taken forward for RNAseq (SMAFRZE column).

```{r}
#remove entries with RIN <=5 AND excluded going forward
gtex_qual_samples=gtex_dedup[gtex_dedup$RIN_corrected >= 5 & gtex_dedup$SMAFRZE=="RNASEQ",c(1:5, 10:16)]

```



Moving forward with ```gtex_qual_samples```, we can use subset() to further slice up our data. Subset() takes the dataframe to be subsetted, the condition on which to subset and select can also be supplied as an argument to indicate columns. The SMTS column contains information on the tissue sample. Let's observe which tissues we have and pick one for further analysis.

```{r}
##identify tissues
unique(gtex_qual_samples$SMTS)
[1] Blood Vessel Heart       
Levels: Blood Blood Vessel Heart

#Lets concentrate on Blood Vessels for further analysis
gtex_bloodv<-subset(gtex_qual_samples, gtex_qual_samples$SMTS=="Blood Vessel")

#Check
unique(gtex_bloodv$SMTS)
[1] Blood Vessel
Levels: Blood Blood Vessel Heart
```



Ordering is specific type of subsetting known as integer subsetting. Below we will use order() to order the data by RIN number and also by date of batch.

```{R}
##order samples by RIN
gtex_bloodv_order<-gtex_bloodv[order(gtex_bloodv$RIN_corrected), ]

#order by date
#watch format, US date format used for this dataset
date_order<-gtex_bloodv_order[order(as.Date(gtex_bloodv_order$SMNABTCHD, format="%m/%d/%Y")),]


```



### 4.6 Merging

Sometimes we will need to add new data to our data frame, the annot.txt file contains anonymized individual level data. This may be helpful future analysis. We will first read this data in and then attempt to merge with our existing data.



```{r}
##read in data
annot<-read.table("annot.txt", sep="\t", header=T)
#head data
head(annot)
  SUBJID 	   SEX   AGE    DTHHRDY
1 GTEX-1117F   2 	60-69       4
2 GTEX-111CU   1 	50-59       0
3 GTEX-111FC   1 	60-69       1
4 GTEX-111VG   1 	60-69       3
5 GTEX-111YS   1 	60-69       0
6 GTEX-1122O   2 	60-69       0
```



The first thing you will notice is that the sample Id's only partially match between the dataframes. This is because the phenotype file we have worked with contained information on a tissue sample level and individuals may have donated more than one tissue. In order to merge to individual level, we have first decided to focus on only one type of blood vessel ```Artery - Aorta```. The tissue Id's can then be altered to match individual Id before using this to merge datasets.

The following function are used in the next code block:

- merge() - Takes the dataframes to be merged and the columns to merge by
- gsub() - Used to find and replace items

```{R}
#Filter dataframe to only incldue Artery-Aorta
gtex_aorta<-subset(date_order, date_order$SMTSD=="Artery - Aorta")

#Strip SAMPID after first -
gtex_aorta$SAMPID=gsub("^([^-]*.[^-]*).*", "\\1", gtex_aorta$SAMPID)

#Merge
merged_gtex<-merge(gtex_aorta,annot, by.x="SAMPID", by.y="SUBJID")
```



### 4.7 Control Flow and Loops

Control flow such as if,else statements and loops have already been described in part 1 of this introduction and can be useful in manipulating data.  This section will give trivial examples of control flow applied to data frames. More detailed explanations of for loops can be found in ```Introduction to R: Part One```.



We have sex data in our dataset. This example prints a statement based on the sex of the participant in the study. For each entry, the sex of the participant is printed using if else. We will limit this loop to the first 10 entries

```{R}
#for sample in df
for (sam in merged_gtex$SEX[1:10]) {
	#if sample =1
	if (sam == 1){
        #print male
    	print("Male")
        #otherwise
	}   else {
        #print female
   			 print("Female")
	}
}    
  

```

This loop applies the unique() function to the dataframe and stores the information in a new vector  to identify the number of unique entries per column.

```{R}
#initalise vector
unique_vec<-c()
##for each column
for (i in 1:length(colnames(merged_gtex))) {
    x<-length(unique(merged_gtex[,i]))
    unique_vec<-append(unique_vec,x)
}
#set rownames
names(unique_vec)<-colnames(merged_gtex)

#head vector
head(unique_vec)
[1] 429   3     1   1   2
```



## 5 Summary

- Matrices, arrays and dataframes handle higher dimensional data in R
- Dataframes are the most commonly used data structure for higher dimensional data
- Dataframes can be accessed similar to lists and vectors
- Reading in and writing out data is trivial but delimiters must not be ignored
- Subsetting is useful for filtering data and is used in combination with many functions
- Control flow can be applied to dataframes in a similar manner to other data structures to avoid repetitive code
- Further information on the functions used can be accessed through the Rstudio help page



1. The Genotype-Tissue Expression (GTEx) Project was supported by the [Common Fund](https://commonfund.nih.gov/GTEx)  of the Office of the Director of the National Institutes of Health,  and by NCI, NHGRI, NHLBI, NIDA, NIMH, and NINDS. The data used for the  analyses described in this tutorial were obtained from: the GTEx Portal on 20/04/2020.

