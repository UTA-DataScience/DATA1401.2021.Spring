---
title: Branching and If-constructs
tags: [branching, control_constructs, if_block, python]
keywords: branching, control_constructs, if_block, python
summary: "This note aims at explaining the concepts of branching statements and if-blocks."
#permalink: /notes/control-constructs/branching/index.html
last_updated: July 9, 2019
---

## Branching in Python  

Consider we are in a class with the following students defined in a dictionary together with their roles in the class.  

```python
class_dict  = { 
            , 'Christian Chrysler'  : 'student'
            , 'Matthew Bagby'       : 'student'
            , 'Niyousha Dredger'    : 'student'
            , 'Pauline Davachi'     : 'student'
            , 'Marcos Kuffel'       : 'student'
            , 'Lauren Kumbhare'     : 'student'
            , 'Shashank Guillen'    : 'student'
            , 'Hany Moorman'        : 'student'
            , 'Sarah Mahdy'         : 'student'
            , 'Andrew Osborne'      : 'student'
            , 'Joshua Myers'        : 'student'
            , 'Rebecca Vedovato'    : 'student'
            , 'Carolina Proni'      : 'student'
            , 'Amir Shahmoradi'     : 'instructor'
            }
```

Now suppose we would like to write a Python script that, when executed, asks the user to input the full name of a person in our class and then outputs on screen, the role of the person in class. To do this, first we should get familiar with Python's built-in function `input()`.

In Python 2, the corresponding function is <code>raw_input()</code>. In Python 3, it is now renamed to <code>input()</code>.

```python
input("\n Please enter the full name of the person: ")
```
    Please enter the full name of the person: Amir Shahmoradi
    'Amir Shahmoradi'

The function `input()` is a Python built-in function that outputs the input string inside parentheses to the output screen, and then waits for the user to enter an input. This function reads a line from input, and converts it to a **string** (stripping a trailing newline), and returns that. One can also put the user's input directly into a variable, which is the normal way of using this function.
```python
input_variable = input("\n Please enter the full name of the person: ")
```
    Please enter the full name of the person: Amir Shahmoradi

```python
print(input<press tab>
    input          input_key      input_variable
```

```python
print(input_variable)
```
    Amir Shahmoradi

```python
type(input_variable)
```
    str

```python
input_variable = input("\n Please enter the full name of the person: ")
```
    Please enter the full name of the person: 1234

```python
type(input_variable)   # whatever type the input is, it will be converted to a string by Python interpreter
```
    str

Now, back to our originally stated problem in the above, we want to write a program that takes in the name of a person from the command line and then tells the user some information about them, depending on their name. To achieve this, we need to become familiar with the concept of **branching** in Python.  Specifically, we can achieve our goal by writing an `if-elif` statement in Python as in the following python script.  

The general syntax for `if` blocks in python is the following.  

```python
if expression1:     # if expression1 is True
   statement(s)         # execute the required Python statements
elif expression2:   # else if expression2 is True
   statement(s)         # execute the required Python statements
elif expression3:   # else if expression3 is True
   statement(s)         # execute the required Python statements
else:               # else if neither of the above was True
   statement(s)
```

Note that the indentations at the beginning of each of the statements are necessary, otherwise the Python interpreter will give you a syntax error. However, it is important to note also that the number of indentations is arbitrary.  

> I highly recommend you to be consistent in indentations of your Python code. The whole point of Python is to write a highly-human-readable code. This requires you to write your code in the most consistent way possible. For example, I recommend you to always use either 2,3, or 4 white-space characters for indentations in your code (4-spaces is ideal in my opinion for Python and most other programming languages). Also, <b>AVOID USING <a href="https://en.wikipedia.org/wiki/Tab_key" target="_blank">TAB CHARACTER</a> AS INDENTATION IN YOUR CODES</b> unless your editor automatically converts it to a pre-specified number of white-space characters. The <code>tab</code> character can create a huge mess in your Python codes, and some extra work to clean them up. <a href="http://www.secnetix.de/olli/Python/block_indentation.hawk" target="_blank">Here</a> is a good resource to learn more about indentations in Python.

```python
#!/usr/bin/env python
class_dict = { 'nicholas dhana'     : 'student'
             , 'bradley driver'     : 'student'
             , 'sagar boeker'       : 'student' 
             , 'travis bridges'     : 'student'
             , 'eric garcia'        : 'student'
             , 'christian gagliano' : 'student'
             , 'matthew janssen'    : 'student'
             , 'lucero goree'       : 'student'
             , 'jake herrera'       : 'student'
             , 'michael lewis'      : 'student'
             , 'colin langford'     : 'student'
             , 'mark mendiola'      : 'student'
             , 'emilio loveland'    : 'student'
             , 'kreshel philley'    : 'student'
             , 'russell nguyen'     : 'student'
             , 'caleb robbins'      : 'student'
             , 'joseph phillips'    : 'student'
             , 'bradley varier'     : 'student'
             , 'vivek smith'        : 'assistant'
             , 'amir shahmoradi'    : 'instructor'
             }
name = input("\n Please enter the full name of the person: ")
if name in class_dict:    # First make sure the name is in our dictionary
    if class_dict[name] == 'instructor':
        print( '\nThe name you enetered: {} belongs to the instructor of this course. His office hours are Mondays 3-4 p.m.\n'.format(name) )
    elif class_dict[name] == 'assistant':
        print( '\nThe name you enetered: {} belongs to the Teaching Assistant of this course.\n'.format(name) )
    elif class_dict[name] == 'student':
        print( '\nThe name you enetered: {} belongs to one of the students of our class.\n'.format(name) )
else:
    print('\nThe name you entered: {} does not correspond to any real person in this class. Make sure you are not looking for a ghost, as our class is ghost-free.\n'.format(name) )
```

Now, if we run the [file](class_roster.py) containing this script, we will get something like the following,  

```bash
$ ./class_roster.py
```
    Please enter the full name of the person: amir shahmoradi
    The name you entered: amir shahmoradi belongs to the instructor of this course. His office hours are on Mondays at 5-6 p.m.

```bash
$ ./class_roster.py
```
    Please enter the full name of the person: Harry Potter
    The name you entered: Harry Potter does not correspond to any real person in our class. Make sure you are not looking for a ghost, as our class is ghost-free.

Conditional `if` statement is the only built-in branching method in Python. However, it can be written in several different sytaxes, each of which can be useful in some circumstances:  

**1.** One-line conditional **statement**:  

```python
if condition: statement
```

For example:  

```python
if sqrt(2) < 2: print('sqrt(2) < 2\nOf course that was obvious!')
```
    sqrt(2) < 2
    Of course, that was obvious!

**2.** multiple line (as stated above) conditional **statement**:
```python
if condition:
    block statements
elif:
    block statements
else:
    block statements
```

**3.** Inline conditional **expression**: This is a particularly useful syntax for conditional value assignments in Python.  

```python
expression1 if condition_is_met else expression2
```

For example, instead of writing,  

```python
if condition:
    a = value1
else
    a = value2
```

one can summarize it all in one line,  

```python
a = (value1 if condition else value2)
```

Note that the paratheses are not necessary, however, they are recommended for clarity. Here is an example code,  

```python
name = input('Input the name: ')
print( 'This person is the course instructor' if name == 'amir' else 'This person is not the course instructor')
```
    Input the name: amir
    This person is the course instructor

### Non-boolean conditions in if-statements  

There is a rather interesting feature of conditions in Python if-statements, that allows the programmer to use a non-boolean variable or value type directly in place of the condition in if-statement. What really happens here is that Python interpreter converts the non-boolean type to a boolean value, when it occurs in place of an if-statement condition.  

```python
if 5.6:
    print('The condition in this if-statement is automatically converted from float to boolean')
```
    The condition in this if-statement is automatically converted from float to boolean

```python
if 0.0:
    print('A float value of zero is converted to False')
```
    

```python
if not 0.0:
    print('A float value of zero is converted to False')
```
    A float value of zero is converted to False

```python
if 0.000000000000000000000000000000000000000000000000000000000000000000001:
    print('Any non-zero float value of any precision is converted to True')
```
    A float value of zero is converted to False

```python
if 1.e-323:
    print('Any non-zero float value of any precision is converted to True')
```
    Any non-zero float value of any precision is converted to True

```python
if 1.e-324: # make sure you don't go beyond computer precision
    print('Any non-zero float value smaller than the computer precision will be set to 0')
```
    
```python
if not 1.e-324: # make sure you don't go beyond computer precision
    print('Any non-zero float value smaller than the computer precision will be set to 0')
```
    Any non-zero float value smaller than the computer precision will be set to 0

```python
if 12:
    print('The same rules also hold for integers.')
```
    The same rules also hold for integers.

```python
if "":
    print('An empty string is converted to boolean False')
```

```python
if not "":
    print('An empty string is converted to boolean False')
```
    An empty string is converted to boolean False

```python
if " ":
    print('A non-empty string is converted to boolean True')
```
    A non-empty string is converted to boolean True

```python
if []:
    print('An empty list is converted to boolean False')
```

```python
if not []:
    print('An empty list is converted to boolean False')
```
    An empty list is converted to boolean False

```python
if [1]:
    print('A non-empty list is converted to boolean True')
```
    A non-empty list is converted to boolean True

```python
if not {}:
    print('The same rules also hold for sets and dictionaries.')
```
    The same rules also hold for sets and dictionaries.

```python
if {1:2}:
    print('The same rules also hold for sets and dictionaries.')
```
    The same rules also hold for sets and dictionaries.

```python
if not None:
    print('The keyword None is also equivalent to False.')
```
    The keyword None is also equivalent to False.

```python
bool("amir") # You can always get the boolean-conversion of a given value or type using Python's built-in function bool().
```
    True


## Exercise

1. Single-line Python input and string manipulation: [web-link](https://www.cdslab.org/recipes/programming/python-single-line-input-string-manipulation/python-single-line-input-string-manipulation)  


