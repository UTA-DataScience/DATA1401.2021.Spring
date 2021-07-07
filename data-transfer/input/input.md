---
title: Data input methods
tags: [data, input, IO]
keywords: data, input, IO, python
summary: "This note aims at providing an overview of data-input methods in Python."
#permalink: /notes/data-transfer/input/index.html
last_updated: July 9, 2019
---

So far, we have indirectly discussed several methods of getting input information from the user, and several methods of outputting the result in a Python program. This note attempts to formalize all the previous discussions and introduce more general efficient methods of the code interaction with users. Let's begin with example code, explaining the meaning of input/output (I/O) in Python,
```python
from math import exp
a = 0.1
b = 1
x = 0.6
y = a*exp(b*x)
print(y)
```
    0.1822118800390509

In the above code, $a,b,x$ are examples of input data to code, and $y$ is an example of code output. In such case as in the above, the input data is said to be **hardcoded** in the program.  


    <b>In general, in any programming language, including Python you should always avoid hardcoding input information into your program.</b><br><br>
    If data is hardcoded, then every time it has to change, the user has to change the content of the code, and this is not considered good programming style for software development.

In general, input data can be fed to a program in four different ways:  
1. let the user answer questions in a dialog in the **terminal window**,
2. let the user provide input on the **command line**,
3. let the user provide input data in a **file**,
4. let the user write input data in a **graphical interface**.  

## Input data from the terminal window  

We have already introduced and used this method frequently in previous notes, via the Python's builtin function `input()`. If we were to get the input data for the above example code via the terminal window, an example would be the following,
```python
from math import exp
a,b,x = input('input the values for a,b,x (comma separated): ').split(",")
y = float(a)*exp(float(b)*float(x))
print(y)
```
    input the values for a,b,x (comma separated): 0.1,1,0.6
    0.1822118800390509

## Input data from the command line    

This approach, which we discussed in the previous notes, is most popular in Unix-like environments, where most users are accustomed to using the Bash command line. However, it can be readily used in the Windows environment as well. For this approach, there is a Python module `sys` that can accomplish what we desire,
```python
from math import exp
import sys
a,b,x = sys.argv[1],sys.argv[2],sys.argv[3]
y = float(a)*exp(float(b)*float(x))
print(y)
```

Now if you save this code in a file named [input_via_sys.py](input_via_sys.py), and run it on the Bash command line, the program expects you the enter 3 float numbers following the name of the program,
```bash
$ python input_via_sys.py 0.1 1 0.6
0.1822118800390509
```

**Pay attention to the convention for the input command-line arguments.**  
1. As you see in the above example, the name of the program is considered as the first command line argument (<code>sys.argv[0]</code>). Also the arguments must be separated by a white space, and should appear in the proper order.  
2. If one value has a white space (e.g., a string value with white space character in it), then it has to be contained in quotation marks <code>''</code> or <code>\"\"</code>.<br><br>
3. Also note that all input command-line arguments are taken as string values. Therefore, you will have to convert them to the proper type (e.g., float, int, ...) once they are read from the command line.

<br>

### Variable number of command line arguments  

If the number of input arguments on the command line is not known a priori, then you can get a list of all input arguments using `sys.argv[1:]` and then use a for-loop to loop over individual elements of it, or use `len()` function to find the total number of input arguments.  
<br>

### Option-value pairs as command-line input  

Once the number of input arguments to your code increases, the process of inputting data as command line arguments can get complicated. Ideally, the user should be able to enter data in any arbitrary order. This can be done by indicating the meaning of each input by a flag before the input value. For example, suppose you were to find the location $y(t)$ of an object thrown up in the air vertically, given that the object started at $y=y_0$, at $t=0$ with an initial velocity $v_0$, and thereafter was subject to a constant acceleration $a$,
$$
y(t) = y_0 + v_0t + \frac{1}{2}at^2 ~.
$$
Obviously, this formula requires four input variables: $y_0$, $v_0$, $a$, and $t$, and we don't the program user to memorize their order of entry on the command line. The solution is to identify the type of each input using a flag preceding the input value. This can be done using `argparse` Python module. Details of the usage of this module go beyond the limited time of our class. However, I recommend you to have a look at the [syntax and usage of *argparse* module](https://docs.python.org/3/library/argparse.html), as you will find it very handy in your Python codes, projects, and software development.  


## Input data from a file  

In cases where the input data is large, the command-line arguments and input from a terminal window are not efficient anymore. In such cases, the most common approach is to let the code read input data from a file, the path to which is most often given to the code from the command line or the terminal window.

### Reading a file line by line  

To read a file, say [this file](data.in), one first needs to open it,  

```python
myfile = open('data.in', 'r')
type(myfile)
```
    _io.TextIOWrapper

```python
myfile.<press tab>
     myfile.buffer         myfile.detach         myfile.fileno         myfile.line_buffering myfile.newlines       myfile.readline       myfile.seekable       myfile.writable
     myfile.close          myfile.encoding       myfile.flush          myfile.mode           myfile.read           myfile.readlines      myfile.tell           myfile.write
     myfile.closed         myfile.errors         myfile.isatty         myfile.name           myfile.readable       myfile.seek           myfile.truncate       myfile.writelines
```

The function `open` creates a file object, stored in the variable `myfile`. The second input argument to `open`, `'r'` tells the function that the purpose of this file opening is to read data (as opposed to, for example, writing data, or both reading and writing).  

Now you can use a for loop to read the data in this file line by line:  

```python
for line in myfile:
    print(line)
```
    1
    
    3
    
    4
    
    5
    
    6
    
    7
    
    88
    
    65

What is printed here, is actually the content of `data.in` file, line by line.  

### Alternative method of reading a data file  

Instead of reading one line at a time, as in the above, we can load all lines into a single list of strings,  

```python
myfile = open('data.in', 'r')
lines = myfile.readlines()
type(lines)
```
    list

Note that each element of `line` contains one line of the file.  

```python
lines
```
    ['1\n', '3\n', '4\n', '5\n', '6\n', '7\n', '88\n', '65\n']

The action of the method `readlines()` is equivalent to a for-loop like the following,  

```python
myfile = open('data.in', 'r')
lines = []
for line in myfile:
    lines.append(line)
lines
```
    ['1\n', '3\n', '4\n', '5\n', '6\n', '7\n', '88\n', '65\n']

or this *list comprehension* format,  

```python
myfile = open('data.in', 'r')
lines = [line for line in myfile]
lines
```
    ['1\n', '3\n', '4\n', '5\n', '6\n', '7\n', '88\n', '65\n']

Now suppose you were to calculate the mean of the numbers in [this file](data.in). You could simply use the following list comprehension code to do so,  

```python
mean = sum([float(line) for line in lines])/len(lines)
print(mean)
```
    22.375

Note that once you read the file, you can close it using,  

```python
myfile.close()
```

### The *with* statement  

Frequently in modern Python code, you may see the `with` statement for reading a file, like the following,  

```python
with open('data.in', 'r') as myfile:
    for line in myfile:
        print(line)
```
    1
    
    3
    
    4
    
    5
    
    6
    
    7
    
    88
    
    65


This is technically equivalent to,  

```python
myfile = open('data.in', 'r')
for line in myfile:
    print(line)
myfile.close()
```
    1
    
    3
    
    4
    
    5
    
    6
    
    7
    
    88
    
    65

The difference here is that with the modern `with` statement, there is no need to close the file in the end.  

### The old *while True* construction  

The call `myfile.readline()` returns a string containing the text at the current line. Adding a new `myfile.readline()` will read the next line. If the file reaches the end, then `myfile.readline()` returns an empty string, the end of the file has reached and the code must stop the further reading of the file. The traditional way of telling the code to stop at the end of the file is a `while` loop like the following,  

```python
myfile = open('data.in', 'r')
while True:
    line = myfile.readline()
    if not line:
        break
    print(line)
```
    1
    
    3
    
    4
    
    5
    
    6
    
    7
    
    88
    
    65

### Reading an entire file as a single string  

While the `readlines()` method returns a list of lines in the file, the `read()` method returns a string containing the entire content of the file.  
```python
myfile = open('data.in', 'r')
s = myfile.read()
s
```
    '1\n3\n4\n5\n6\n7\n88\n65\n'

```python
print(s)
```
    1
    3
    4
    5
    6
    7
    88
    65

The major advantage of this method of reading file content is that you can then immediately apply string methods directly on the file content.  

```python
myfile = open('data.in', 'r')
numbers = [float(x) for x in myfile.read().split()]
mean = sum(numbers)/len(numbers)
print(mean)
```
    22.375

### Reading data from special data files  

It will happen quite often in your research that you will need to read data from a spreadsheet data file, most importantly `*.csv` and Microsoft Excel files (e.g., `*.xls` data files), or also frequently, from an `*.xml` data file. There are many ways and Python libraries to read such files. For Excel files, the task can be a bit complex, since Excel files can contain multiple sheets. A good starting point might be [this webpage](http://www.python-excel.org/), also [Pandas module](http://pbpython.com/excel-pandas-comp.html).  

For CSV files, Python standard library has a solution. Suppose you want to read [this CSV file](data_input.csv). A Python solution would be the following,  
```python
import csv
with open('data_input.csv','r') as myfile:
    for counter, row in enumerate(csv.reader(myfile)):
        print(row)
        if counter>10: break
```
    ['pdb', 'pdb_id', 'chain', 'site', 'zr4s_JTT', 'r4s_JTT', 'zr4s_JC', 'r4s_JC']
    ['132L_A', '132L', 'A', '2', '-0.3133', '1.02', '0.04475', '1.188']
    ['132L_A', '132L', 'A', '3', '0.8385', '1.955', '0.2036', '1.311']
    ['132L_A', '132L', 'A', '4', '2.093', '2.973', '1.451', '2.272']
    ['132L_A', '132L', 'A', '5', '-0.8878', '0.5537', '-0.7985', '0.5382']
    ['132L_A', '132L', 'A', '6', '-1.443', '0.1028', '-1.426', '0.05416']
    ['132L_A', '132L', 'A', '7', '-0.1195', '1.177', '-0.07917', '1.093']
    ['132L_A', '132L', 'A', '8', '-0.7236', '0.6869', '-0.8997', '0.4602']
    ['132L_A', '132L', 'A', '9', '-1.107', '0.3755', '-0.8971', '0.4622']
    ['132L_A', '132L', 'A', '10', '0.7076', '1.848', '0.7369', '1.722']
    ['132L_A', '132L', 'A', '11', '0.9573', '2.051', '0.8809', '1.833']
    ['132L_A', '132L', 'A', '12', '-0.8315', '0.5993', '-0.9243', '0.4413']

Note how I have used Python `enumerate()` function to control the number of lines that is read from the file (The file contains more than 70000 lines of data!).  

Similarly, if you wanted to write a CSV file, you can use `csv.writer()` method,
```python
with open('data_input.csv','r') as infile, open('data_output.csv', 'w') as outfile:
    for counter, row in enumerate(csv.reader(infile)):
        csv.writer(outfile).writerow(row)
        if counter>10: break
```

The output of the code is the file [data_output.csv](data_output.csv) (If you run this code on Windows machines, you may get an extra empty line between each row in the CSV file).  

For `*.xml` files, Python standard library has a package [ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html), which you can use for both parsing and writing xml data files.  

### Reading data from the World Wide Web  

Nowadays, a lot of data repositories are available online to the public community, and you may encounter problems that need to parse data from an online repository. Such problems happen almost daily in a scientific research career, even in High-Performance Computing, and Python's capability to easily handle such data-IO problems is indeed one of the main reasons for its popularity.  

For many of the most famous repositories, such as the [Protein databank](http://www.rcsb.org/pdb/home/home.do), excellent python packages have been written that automate the process of fetching data from online pages or repositories (e.g., [Biopython](http://biopython.org/wiki/Biopython)).  

Nevertheless, at some point in your research or career, you may need to read data from a web address by yourself. Frequently, the online data is contained in an `HTML` file, like the contents of this very page that you are reading right now. Suppose you wanted to extract the contents of an HTML page, say, The Astronomy Picture of the Day (APOD), which has the URL: [https://apod.nasa.gov/apod/astropix.html](https://apod.nasa.gov/apod/astropix.html). A simple solution would be the following via Python's standard function [urllib](https://docs.python.org/3/library/urllib.html) module,  

```python
import urllib.request as ur
myurl = 'https://apod.nasa.gov/apod/astropix.html'
with ur.urlopen(myurl) as webfile:
    webcontent = [line.decode("utf-8") for line in webfile.readlines()]
```

Now the variable `webcontent` is a list, whose elements are each row in the HTML file for this page.  

```python
webcontent[0:10]
```
    ['<!doctype html>\n',
     '<html>\n',
     '<head>\n',
     '<title>Astronomy Picture of the Day\n',
     '</title> \n',
     '<!-- gsfc meta tags -->\n',
     '<meta name="orgcode" content="661">\n',
     '<meta name="rno" content="phillip.a.newman">\n',
     '<meta name="content-owner" content="Jerry.T.Bonnell.1">\n',
     '<meta name="webmaster" content="Stephen.F.Fantasia.1">\n']

Note that the content of the file is read in `byte` format. Therefore, to convert it to a string, one has to apply `.decode("utf-8")` on each line, as we did in the above. Similar to opening a file on a hard disk, one can also use `.read()` and `.readline()` methods to read the contents of the web address. Alternatively, one could also save the entire content of the web address, in a single file locally,  

```python
import urllib.request as ur
myurl = 'https://apod.nasa.gov/apod/astropix.html'
ur.urlretrieve(myurl, filename='apod.html')
```

This will output the file named [apod.html](apod.html) in your current working directory of Python's Interpreter that you are using.

The file that we just imported from the web does not contain any scientific *raw research data* (of course, it is highly scientific content, but in the form of astronomical news, not data). Later on, we will see real-world scientific examples that show the value of Python's ability to parse the contents of web pages.  

## Converting user input to live Python objects  

One of the cool features in Python I/O is that you can provide text containing valid Python code as input to a program and then
turn that text into *live Python objects* as if the text were lines of code written directly into the program beforehand. This is a very powerful tool for letting users specify function formulas, for instance, as input to a program. The program code itself has no knowledge about the kind of function the user wants to work with, yet at run time the user's desired formula enters the computations. To achieve the goal, one can use Python's **magic functions**, a.k.a. **special methods**.  

### The magic *eval* function  

The `eval` function takes a **string as argument** and **evaluates** this string as a **Python expression**. The result of an expression is an **object**. For example,  

```python
eval('1+2')
```
    3

This is equivalent to typing,  

```python
1+2
```
    3

or another example,  

```python
a = 1
b = 2
c = eval('a+b')
c
```
    3

or,  

```python
from math import sqrt
eval('sqrt(4)')
```
    2.0

But, note that in all of the above examples, the `eval` function **evaluates** a Python expression, that is, this function **can not execute** a Python statement.  

Now the cool thing about this function is that you can directly apply it to the user input. For example, suppose the user is asked to input a Python expression and then the code is supposed to evaluate the input just like a simple calculator,  

```python
eval(input('Input an arithmetic expression to evaluate: '))
```
    Input an arithmetic expression to evaluate: 2 + 3.0/5 + exp(7)
    1099.2331584284584

### The magic *exec* function  

Similar to the `eval` function, there is also an `exec` magic function that executes a string containing an arbitrary
Python code, not just a Python expression. This is a powerful idea since it now enables the user to write a formula as input to the program, available to the program in the form of a string object. The program can then convert this formula to a callable Python code, or function, using the magic `exec` function.  

```python
exec('import math')
exec('a=1; b=2; c=a+b')
a,b,c
```
    (1, 2, 3)

One could even input a full function definition to the exec function,  

```python
myFuncString = input('Input a Python function definition of interest: ')
f = exec(myFuncString)
```
    Input a Python function definition of interest, named func: def func(x): return 2*x + 1  
    
```python
func(x=1)
```
    3

Now, since this is such a useful functionality in Python, there is already a package written `scitools`, that converts an input expression to a Python function,  

```python
from scitools.StringFunction import StringFunction
myfuncString = input('Input a Python expression to build your requested Python function: ')
myfunc = StringFunction(myfuncString)
```

The only major caveat with this module is that, at the moment, it only works with Python 2.x, and not Python 3. So, the above code will not work on your Python 3 platform.  