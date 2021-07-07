---
title: First Python program
tags: [first, Python, program]
keywords: first, Python, program
summary: "This note aims at introducing simple programs and how to run the programs in different ways."
#permalink: /notes/values-variables-types/first-program/index.html
last_updated: July 9, 2019
---


> Here is a [Python cheatsheet for beginners](beginners_python_cheat_sheet_all.pdf).

## The first Python program  

The traditional first program in Python language has the following form.
```python
print ('Hello World!')  
```
    Hello World!


## Methods of running a Python program  

### Running Python code on the Python interpreter's command prompt  

Now, as you may have noticed, in the above example, I used IPython command line to code my first simple Python program. This is one of the simplest and quickest methods of Python coding and is actually very useful for testing small simple Python-ideas and code snippets on-the-fly.  

### Running Python code inside a Python file Python from the Bash command line  

As the program size grows, it wiser to put all of your Python scripts into a single file, and then let the Python interpreter run (i.e., interpret) your entire file all at once. To save the above simple "Hello World" Python code in a file and run it, open a Bash command prompt, then use the Bash `cat` command to create and add the Python command to your Python file as in the following (On Windows devices, you can use the Git command prompt).  

```bash
$ cat >> firstPythonCode.py << EOF
print ('Hello World!')
EOF
```

Then you can use call python interpreter from the Bash command line to execute your Python code.  

```bash
$ python firstPythonCode.py
python firstPythonCode.py
```
    Hello World!

### Running Python code inside a Python file from the Bash command line as a standalone executable  

You can also avoid typing the name of the interpreter (`python`) in order to run your code by adding the following [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) at the top of your Python script, like the following.  

```bash
$ cat >> firstPythonCodeWithShebang.py << EOF
#!/usr/bin/env python
print ('Hello World!')
print ('This is a Python script with Shebang!')
EOF
```

The result is that now you can run your Python script without the interpreter's name, as an executable file,  

```bash
$ ./firstPythonCodeWithShebang.py
```
    Hello World!
    This is a Python script with Shebang!

Note that *shebang* directive only works under Unix/Linux operating systems and command prompts (not windows). When a Python script with a shebang is run as a program, the program loader parses the rest of the script's initial line as an interpreter directive. The specified interpreter program is run instead, passing to it as an argument the path that was initially used when attempting to run the script.  

On the other hand, if you try to run your original code (without Shebang) as an executable without Python interpreter name, you will get an error message like the following,  

```bash
Amir@CCBB-Amir MINGW64 ~
$ ./firstPythonCode.py
```
    ./firstPythonCode.py: line 1: syntax error near unexpected token `'Hello World!''
    ./firstPythonCode.py: line 1: `print ('Hello World!')'


### Running Python code inside a Python file by first compiling it to bytecode from the command line  

You can also compile your Python script into a bytecode. This is, however, a topic of a future lecture.  

## Python's print function  

We have already used print function to create the first Python program. But note also the difference in `print` between the two Python versions. In **Python 3**, `print` is a **Python function**, whereas in **Python 2**, it is a **Python statement**.  

```python
print('My name is Amir')
```
    My name is Amir
    
**Note:** You can use wildcards in Python strings. You can also use double quotes for strings.  

```python
print("My name is Amir",'\n') # You can use wildcards in Python strings. You can also use double quotes for strings.
```
    My name is Amir 

```python
print('My name is Amir','\n'*2,"I am a faculty member of the  \"University of Texas\".") 
print('''
You can multiply strings by integer! \n
Note how I used wildcards for quotation marks around "University of Texas" in my previous print function, in order to be consistent with Python syntax.

Did you also notice how I am creating a multi-line Python string right now?!
''')
```
    My name is Amir 
    
     I am a faculty member of the  "University of Texas".
    
    You can multiply strings by integer! 
    
    Note how I used wildcards for quotation marks around "University of Texas" in my previous print function, in order to be consistent with Python syntax.
    
    Did you also notice how I am creating a multi-line Python string right now?!

```python
"""
This is also a multi-line
comment in
Python
"""
```
    '\nThis is also a multi-line\ncomment in\nPython\n'

```python
'''
You can use single quotes
for multi-line commenting as well.
Always be as expressive as possible with your comments in your code.
It does not harm!
'''
```
    '\nYou can use single quotes\nfor multi-line commenting as well.\nAlways be as expressive as possible with your comments in your code.\nIt does not harm!\n'

In the following sections, you will learn much more about the `print` function, especially when dealing with variables.  

<a name="python-as-simple-calculator"></a>
## Python interpreter as a simple calculator
One of the greatest advantages of Python is that it can be used as a simple calculator and program interpreter on-the-fly, just like MATLAB, Mathematica, R, and other scripting languages. You will see why and how this is the case.  

