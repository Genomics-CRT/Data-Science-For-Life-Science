# Basic Command Line Tutorial

## Introduction

A lot of bioinformatics software uses a command line interface, and if you're planning on doing more bioinformatics work in the future, you will most likely be using a cluster or server, which are accessed through the command line. This tutorial is meant as a very basic introduction to useful tools for navigating the command line. 

We won't be giving tutorials on widely used bioinformatics software, but if you have any questions about these tools, about how you might process your own data, give us a shout and we can try to help, or at least point you in the right direction.

Both Linux and Mac operating systems are in the family of unix-like operating systems, and their command prompts are very similar. I'm not going to go into any detail on the nitty-gritty of these OSs, but the command prompt is essentially a text-based interface that you can use to communicate with the computer and get it to perform the operations you want it to. 

This tutorial is going to run through some basic commands, so if you open up the terminal  on your computer, you'll be able to try them out too. On a mac, this is in the Utilities folder in Applications; on a windows computer, launch your ubuntu subsystem (or cygwin for those who don't have windows 10) that you installed at the start of this course. If you didn't get around to installing this on your computer, instructions are in the "Getting Started" section of the github. To navigate to your Desktop, in cygwin type: `cd /cygdrive/c/Users/username/Desktop` ; in the Ubuntu subsystem type `cd /mnt/c/Users/username/Desktop`  (where username is your username); on a mac, type `cd Desktop`. It's probably a good idea to make a folder for this tutorial: to do this type `mkdir cmd_tut` (or whatever you want to call the tutorial) and then `cd cmd_tut` to go into that directory. We'll talk through these commands in a minute, but now you're good to go to start the tutorial. 

## 1.  File Structures

Your computer is organised into a hierarchal structure, with files being contained in directories, which are contained in other directories, which are (probably) contained in *other* directories. The directory which contains all the other directories is the root directory, denoted `/` . This is *not* your home directory. This is denoted `~` as shorthand, but on a mac or  linux computer, this can also be written as `/home/username/`. Your Desktop is a subdirectory of this, as are things like your Downloads folder etc. `.` denotes the directory you're currently in, and `..` denotes the directory above that. We're going to talk about how to see what's in your computer, how to navigate your file structures and how to make new directories and move and copy files.

 To list all the contents of a particular directory, you use the command `ls`.

`ls` on its own lists the contents of the directory you're currently in. Typing `ls` right now (if you're in your new `cmd_tut` directory) will probably return nothing, because you haven't made any new files yet. You can also type `ls /path/to/directory` where path/to/directory is some directory you want to see the contents of. For example, `ls ..` lists the content of the directory above the one you are currently in (in this case, your Desktop).

You can also use what are called "wildcards" to list the contents of a directory that contain a certain string you're interested in. For example, if you want to list all fastq files in a directory, type `ls *.fastq.gz` and they will be listed. There are also various flags you can use to change how the files are listed. You can investigate all these options using `ls --help`, but the most useful are `-l`,`-h`,`-r` and `-t`. `l` means long-form (so you can see the owner of the file, the permissions, the last time it was edited and the size); `h` converts the size of the files to human-readable form; `r` means sort in reverse order and `t` means sort by time. `ls -rt` would list files in reverse order of time modified, with the most recent being at the bottom of the list.

You're going to want to be able to move around your file structures. `cd` allows you to change directory. `cd ..` will move you up to the directory above the one you're in, and you can use this shortcut to go back multiple directories- e.g. `cd ../../../` will bring you into one which is three above the one you're currently working in. You can also just stick the path to whatever directory you want to go to. 

If you're ever unsure about what directory you're in, `pwd` will print the current working directory. 

If you want to make a new directory, `mkdir directory_name` will make a new directory called "directory_name/". If you then want to move some files to this directory, `mv file directory_name/` will move it. Alternatively, you may want to make a copy of a file here. `cp file directory_name/` will do this. `mv`can also be used to rename files: `mv temp file_name` will rename the file "temp" to "file_name". 

If you want to find something on your machine, you can use the command `locate`:  `locate pattern` will search for `pattern`. Be careful you're specific enough: if you share a server with lots of other people you can get a huge number of results which are not useful. 

## 2. Create New Files

Your tutorial directory is currently empty: you're going to want to change this. 

We're going to make one using a text editor and one using redirection.

### a. Text Editor

You've probably noticed by now that the command line works through plain-text commands and plain-text files. There are a few different plain-text editors which are useful; vim is my favourite (it's very flexible), but nano is probably the quickest to pick up, so we're going to be using it for the purposes of this tutorial. You can find a guide to vim [here](http://vimdoc.sourceforge.net/htmldoc/quickref.html) and nano [here](https://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/). 

To open a text file to write, type `nano test_file_nano.txt` . This will open the text editor, which you can type whatever you want. Use ctrl-O to save and ctrl-X to quit.

If you list the contents of your directory, you'll see there's a file called `test_file_nano.txt`. 

*Note: I would recommend playing around with vim as well if you're planning on doing more bioinformatics work.*

### b. Redirection

Another way to make new files is to redirect the output of commands using this symbol `>` .  For example, you might need a file with a list of sample names, which could be achieved by typing `ls > sample_list.txt` in the directory where sample files are stored. 

You might also want to combine previously existing files to make a new one. If you want to print the contents one after the other, this can be achieved with `cat file1 file2 > combined_files` ; using the `cat` command without redirection prints this to the screen (standard output).

You can also use `paste` to put two files together side-by-side: `paste file1 file2 > pasted_files` will make a file with the contents of file1 to the left and file2 to the right. 

`echo` can be used to print things to standard output, which can be redirected into a file: for example `echo "this is a test" > test.txt` makes a file called test.txt containing one line: `this is a test`. `echo -e` ignores special characters so you can echo multiple lines: for example `echo -e "this\nis\na\nmulti-\nline\ntest!">multi_line_test.txt` makes a file called multi_line_test.txt containing 

`this
is
a
multi-
line
test!`

## 3. Removing Files

You've made a few throwaway files by now, and you probably want to clean up your directory a bit. 

`rm file` will delete your file called file, and `rm file*` will remove all files with the prefix "file". Be careful though- this command removes your file forever.

If you try to remove a directory, you will see this message: 

`rm: cannot remove 'my_directory/': Is a directory`

`rmdir` will remove a directory, but only if it's empty. (If there are empty directories in it, use `-p`, which deletes empty directories and their (otherwise empty) parents )

However, if you're sure you want to remove all the contents of a directory, you can use `rm -r my_directory/`, which will remove it and all its contents. (`-r` means perform an operation recursively)

## 4. Viewing Files

We've already seen some of the commands used to print files to your screen, for example `cat`. However, because this prints the entire contents of a file onto the screen, it makes it virtually impossible to inspect a very large file (which is fairly standard when you're working with something like genomic data).

`more` and `less` are both more manageable ways to view a file:

 `more`prints out enough of the file to view it on the screen and then you use the space bar to move down and read it. The enter key can be used to look at this line-by-line. 

`less file`  prints some of the file to the screen; use `e` to go forward one line, `y` to go back one line; `f` to go forward one window and `b` to go back. Type `q` or `Q` to exit.

`head` and `tail`  are also very useful allow you to look at the first and last 10 lines of a file, which is useful to quickly check the contents. the `-n` flag allows you to change the number of lines you're looking at. 

You might also want to just look at certain lines of a file, for example lines containing a certain pattern (like a sample ID). You can search for these lines using the command `grep pattern file` . For example, `grep leprae read_class.txt` would return all lines containing the pattern `leprae` from the file `read_class.txt` 

This could return

`C	MG00HS14:628:C98GRACXX:2:2116:18277:59120	Mycobacterium leprae (taxid 1769)	101	0:25 1769:1 0:41
C	MG00HS14:628:C98GRACXX:2:2116:6840:81177	Mycobacterium lepraemurium (taxid 64667)	37	64667:2 0:1
C	MG00HS14:628:C98GRACXX:2:2202:4734:98284	Mycobacterium leprae (taxid 1769)	78	0:24 1769:5 0:15
C	MG00HS14:628:C98GRACXX:2:2203:6264:73005	Mycobacterium leprae (taxid 1769)	47	0:4 1760:4 1769:3 0:2
C	MG00HS14:628:C98GRACXX:2:2204:8977:26073	Mycobacterium leprae (taxid 1769)	43	0:3 1769:1 0:5
C	MG00HS14:628:C98GRACXX:2:2204:17441:26412	Mycobacterium lepraemurium (taxid 64667)	90	0:3 379:5 64667:7 1760:2 0:39`

`grep -v`  does the *opposite* of grep: it returns all lines which do not contain the pattern passed in with the command. This is useful if you quickly want to filter out a particular sample ID before doing some analysis (for example, if you aren't interested reads classified as Mycobacterium lepraemurium).

`grep -E` (extended regexp) allows you to search for **multiple** words. e.g. `grep -E -w "leprae|tuberculosis"` searches for both `leprae` and `tuberculosis`, keeping with our mycobacterial example. 

`C	MG00HS14:628:C98GRACXX:2:1313:4899:65386	Mycobacterium leprae (taxid 1769)	63	0:8 1783272:3 0:7 1769:2 0:7 1239:1 2:1
C	MG00HS14:628:C98GRACXX:2:1313:17827:76721	Mycobacterium lepraemurium (taxid 64667)	58	0:3 1763:3 0:13 64667:3 0:2
C	MG00HS14:628:C98GRACXX:2:1313:20774:89155	Mycobacterium tuberculosis complex (taxid 77643)	49	0:12 77643:1 0:2`

`-e` allows multiple search terms `-e word1 -e [kK]B` ; this example also shows the use of regular expressions in grep: here the command will search for word1 and kB or KB. 

`-i`: if you can't remember what case something is, this flag allows you to ignore case. 

## 5. Other Useful Commands

`wc`; `wc -l` : counts the number of words in a file; `wc -l` counts the number of lines

`uniq`: returns unique occurences of a line from a file; this file must be sorted. `uniq -c` counts the number of unique occurences of each of these.

`sort` ; `-n` `-k` `-g` `-t`: Sorts a file alphabetically; `-n` sorts numerically; `-g` sorts by numbers in scientific notation. `-k` allows you to specify which field you want to sort by, and `-t` specifies the delimiter. So, if you wanted to sort a csv file by the 4th column, you would type `sort -t, -k4 filename.csv`

`cut` `-f` `-d`: Cuts a string or file and returns the fields specified by `-f`; the delimiter is specified by `-d`; If you wanted to get the third to 6th field of a file delimited by a hyphen, you could type `cut -f3- -d- file-name`.  If you want to cut a string, you echo the string first and pipe the output into a cut command: an example of this is given below.

## 6. Combining commands: piping and for loops

In many cases, you're going to want to use lots of commands together, but you aren't going to want to make lots of intermediate files, as it uses unnecessary resources. A really handy thing to use here is a pipe (`|`). Pipes allow you to put multiple commands together, and the output from preceding commands is piped into other commands. For example, if you wanted to extract the 5th field of a file, but only from those lines that contained the string "ANC", you could use the command `cat results.csv | grep ANC | cut -d, -f5` . If you also wanted to sort it: `cat results.csv | grep ANC | cut -d, -f5 | sort` . 

For basic commands, this doesn't add much efficiency, but as you begin to expand the repertoire of commands you use, this becomes much more useful. It not only increases your speed, it keeps things neat and reproducible. 

You will have come across for loops in the python and R sections of this course;  you can also use them in the command line.

For example, if you want to rename files so their names are formatted slightly differently, it is easy enough to do this in a for loop. This also involves assigning bash variables, which you do using the `$` character.

So, in our example, we have some bam files who have names formatted `KNO41-A-BEX1-LIB1-37-PCR1.trimmed34.sorted.grouped.mq20.rmdup.indel.softclip.bam`: we've realised that we've made a mistake when naming these, and actually these files have all been filtered for sequencing reads more than 30 base pairs, *not* 34. We want to change the filenames to reflect this, but want to keep all the other unique information that's contained in those IDs. There's one thing in common with all these files: the information about trimmed read length is the first bit of information after the file ID. 

`for bam in $(ls *trimmed34*bam); do prefix=$(echo ${bam} | cut -d. -f1); suffix=$(echo ${bam} | cut -d. -f3-); mv ${bam} ${prefix}.trimmed30.${suffix}; done`

The above is a command to allow you to do this- each semicolon signifies a new line; each $ signifies a variable, and you're piping "echo" commands into "cut".

This is a fairly trivial example, but gives an overview of how you might go about this. If you're ever carrying out operations on the command line and thing it might be easier to do in a for loop, give it a go- I would recommend echoing new filenames/ variables before you actually change any files though, to make sure you're doing it right (I frequently make typos, so this is useful for me anyway!).

## 7. The End

This was meant to be a brief overview of useful command line tools: we ended up realising that it is quite difficult to do a "brief" overview of this, especially when most of you will probably not be using command line tools for your work, but we hope this tutorial has provided a quick overview of how to get started.

We haven't gone into much detail here, but if you do end up wanting more help with the command line, feel free to email us, or use google: nearly every problem you could possibly encounter has been encountered by someone else, and they will probably have posted it to stackoverflow. Documentation for all these tools is available online, and there are also more detailed tutorials floating around.

