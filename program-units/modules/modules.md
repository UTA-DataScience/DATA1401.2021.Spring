---
title: Python modules
tags: [python, modules, import, dir, command_line, time, timeit, test_block]
keywords: python, modules, import, dir, command_line, time, timeit, test_block
summary: "This note aims at explaining the concept of modules in Python."
#permalink: /notes/program-units/modules/index.html
last_updated: July 9, 2019
---

## Python modules  

We have already used Python modules extensively in previous topics, homework, and quizzes. although we never discussed them. To put it simply, Python modules are a collection of Python definitions, variables, functions, ... that can be reused as a library in future.  

Sometimes you want to reuse a function from an old program in a new program. The simplest way to do this is to copy and paste the old source code into the new program. However, this is not good programming practice, because you then over
time end up with multiple identical versions of the same function. When you want to improve the function or correct a bug, you need to remember to do the same update in all files with a copy of the function, and in real life, most programmers fail to do so. You easily end up with a mess of different versions with different quality of basically the same code. Therefore, a golden rule of programming is to have one and only one version of a piece of code. All programs that want to use this piece of code must access one and only one place where the source code is kept. This principle is easy to implement if we create a module containing the code we want to reuse later in different programs.  

## The import statement  

We have already used the `math` module on multiple occasions, using the `import` statement. Here is an example:  
```python
import math
value = math.factorial(5)
print(value)
```
    120

```python
math.pi
```
    3.141592653589793

```python
math.e
```
    2.718281828459045

In its simplest form, the import has the following syntax:  
```python
import module1[, module2[,... moduleN]
```

like,
```python
import math, cmath, numpy
```

The standard approach for calling names and definitions (variables, functions, ...) inside the module is using the module-name prefix, like the above examples. To call the module names without the prefix, use the following module import statement,
```python
from math import *
factorial(5)
```
    120

To import only specific names, use the format like the following,
```python
from math import pi,e,factorial,erf
```


This will import the four math modules names `pi, e, factorial, erf`. You could also change the name of the input module, or specific names from it, upon importing the module into your code, using `import as` statement,
```python
import numpy as np
np.double(5)
```
    5.0

```python
from numpy import double as dble
dble(13)
```
    13.0

A module can contain executable statements as well as function definitions. These statements are intended to initialize the module. They are executed <b>only the first time the module name is encountered in an import statement</b>.

Also, note that in general the practice of <code>from mod_name import *</code> from a module is discouraged since it often causes poorly readable code. It is however very useful for time-saving and writing compact concise code in interactive sessions like IPython, or Jupyter.

## Listing all names in an imported module  

To get a list of all available names in an imported module, use `dir()` function.  
```python
import math
dir(math)
```
    ['__doc__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'acos',
     'acosh',
     'asin',
     'asinh',
     'atan',
     'atan2',
     'atanh',
     'ceil',
     'copysign',
     'cos',
     'cosh',
     'degrees',
     'e',
     'erf',
     'erfc',
     'exp',
     'expm1',
     'fabs',
     'factorial',
     'floor',
     'fmod',
     'frexp',
     'fsum',
     'gamma',
     'gcd',
     'hypot',
     'inf',
     'isclose',
     'isfinite',
     'isinf',
     'isnan',
     'ldexp',
     'lgamma',
     'log',
     'log10',
     'log1p',
     'log2',
     'modf',
     'nan',
     'pi',
     'pow',
     'radians',
     'sin',
     'sinh',
     'sqrt',
     'tan',
     'tanh',
     'trunc']


## Python standard Modules  
Python comes with a set of standard modules as its library, the so-called [**Python Standard Library**](https://docs.python.org/3/library/). Some of these modules are built into the Python interpreter; these provide access to operations that are not part of the core of the language but are nevertheless built-in, for efficiency and other reasons.  

## Reimporting modules  

Consider the following code snippet which imports the numpy module and uses the numpy `pi` variable,  

```python
import numpy
numpy.pi
```
    3.141592653589793

However, note that the value of numpy `pi` is not a immutable constant. That means one could change the value of `pi` to anything else, for example,  

```python
numpy.pi = 123
numpy.pi
```
    123

From now on, any usage of `numpy.pi` will give the value `123` instead of the actual original value of `numpy.pi` which was `3.141592653589793`. This is true for the entire duration of the session of Python that you are using. Note that reimporting the numpy module will not help fix this problem. For example,  

```python
import numpy
numpy.pi
```
    123

Why doesn't `import numpy` have any effects? Why doesn't it reimport the numpy module in its original state? That is because every Python session, imports a Python package only once and no more over the life of the Python session. It does not matter how many times in your code you may have `import numpy`, it will be imported only once. So, if you change the state or value of any object in the module and you want to revive the original state or value, you will have only two options,  

1. close the current Python session and open a new one, so that a fresh instance of the module can be imported to your Python environment.  
2. use a function named `reload()` inside a Python standard package named `importlib` to reload (reimport) a fresh instance of the module into your Python session. This way, you won't need to close your Python session,  
```python
import importlib
importlib.reload(numpy)
numpy.pi
```  
```
    3.141592653589793
```

> 
While it often possible to change the state or value of entities in an imported Python package (like changing the value of `pi` in `numpy` package as in the examples above, you should never do so **unless you need to, for some specific justifiable reasons**.



## Creating modules  

To make a Python module, simply collect all the functions that constitute the module in one single file with a given filename, for example, `mymodule.py`. This file will be automatically a module, with name `mymodule`, from which you can import functions and definitions in the standard way described above.  

> **Why and when do you need to create a module?**  
> Sometimes you want to reuse a function from an old program in a new program. The simplest way to do this is to copy and paste the old source code into the new program. However, this is not good programming practice, because you then over time end up with multiple identical versions of the same function. When you want to improve the function or correct a bug, you need to remember to do the same update in all files with a copy of the function, and in real life, most programmers fail to do so. You easily end up with a mess of different versions with different quality of basically the same code. Therefore, a golden rule of programming is to have one and only one version of a piece of code. All programs that want to use this piece of code must access one and only one place where the source code is kept. This principle is easy to implement if we create a module containing the code we want to reuse later in different programs.


Note that modules can import other modules. It is customary but not required to place all import statements at the beginning of a module (or script, for that matter). The imported module names are placed in the importing module’s global <a href="https://en.wikipedia.org/wiki/Symbol_table" target="_blank">symbol table</a>.  

### Executing modules as scripts  

When a Python module is called from the Bash command prompt like,

```bash
python mycode.py
```

the code in the module will be executed, just as if you imported it inside another code. This is good, but can sometimes become problematic. Let's explain this with an example, a [script](find_primes.py) that finds and reports all prime numbers smaller than a given input number $n$.  

When you execute this code as a standalone Python script, it will ask you for an integer, to give you all integers that are smaller than the input number. Now suppose you wanted to import this script as a Python module into your code. If you do so, the Python interpreter would run all statements in this script and asks you to input an integer, before importing the rest of the functions in this script.

```python
import find_primes
```
    Enter an integer number:
    n = 13

    Here is a list of all prime numbers smaller than 13:
    13
    11
    7
    5
    3
    2

This may not be necessarily what we want to do. For example, we may only want to use the functions `get_primes` and `is_prime` in this script, without asking the user to input an integer and finding all smaller primes. The solution is to put the part of the code in the script that we don't want to be executed as a module, that is,

```python
print('Enter an integer number: ')
n = int(input('n = '))
print('\n Here is a list of all prime numbers smaller than {}:'.format(n))
get_primes(n)
```

inside the following if-block,  

```python
if __name__ == "__main__":
    print('Enter an integer number: ')
    n = int(input('n = '))
    print('Here is a list of all prime numbers smaller than {}:'.format(n))
    get_primes(n)
```

When the code is run as a standalone script, the `__name__` property of the code is set to `__main__`. However, when the script is imported as a module inside another code, the `__name__` property is automatically set to the name of the module `find_primes`. Thus as a module, the above if-block will not be executed, but the rest of the code (the two functions) will be properly imported. The corrected script is named `mod_find_primes.py` and can be downloaded from [here](mod_find_primes.py).  

```Python
import mod_find_primes
mod_find_primes.__name__
```
    'mod_find_primes'

You could also import specific names or functions from your module, for example,  

```Python
from mod_find_primes import is_prime
```

In summary, **Add test blocks to your modules**.  

> It is recommended to only have functions and not any statements outside functions in a module. The reason is that the module file is executed from top to bottom during the import. With function definitions only in the module file and no main program, there will be no calculations or output from the import, just definitions of functions. But in case you need to write a module that can be run standalone, then put all script statements for the standalone part of the module inside a <b>test block</b> (the if-block described above).

### Command line arguments  

Test blocks are especially useful when your module can be also run as a standalone Python script that takes in **command-line arguments**. [Here](cmd_find_primes.py) is a modified version of the `mod_find_primes` module now named `cmd_find_primes` that instead of using `input()` function, reads the integer number from the Bash command line. To do so, you need to modify the last part of the original module to the following, using Python's standard `sys` module,
```python
if __name__ == "__main__":
    import sys
    if len( sys.argv ) != 2: # check the number of arguments to be exactly 2.
        print('''
    Error: Exactly two arguments must be given on the command line.
    Usage:''')
        print("     ", sys.argv[0], "<a positive integer number>", '\n')
        sys.exit('     Program stopped.\n')
    else:
        n = int(sys.argv[1])
        print('Here is a list of all prime numbers smaller than {}:'.format(n))
        get_primes(n)
```

Now if you run this code, from the Bash command line, or inside IPython, like the following,
```python
run cmd_find_primes.py
```
    Error: Exactly two arguments must be given on the command line.
    Usage:
      cmd_find_primes.py <a positive integer number>

An exception has occurred, use %tb to see the full traceback.

SystemExit:      Program stopped.


The code will expect you to enter an integer right after the name of the script,
```python
run cmd_find_primes.py 13
```
    Here is a list of all prime numbers smaller than 13:
    13
    11
    7
    5
    3
    2

In general, I recommend you to use the `sys` module for input arguments instead of Python's `input()` function.  


    <b>Modules and main functions</b><br><br>
    If you have some functions and the main program in some program file, just move the main program to the test-block. Then the file can act as a module, giving access to all the functions in other files, or the file can be executed from the command line, in the same way as the original program.

### Test blocks for module code verification  

It is a good programming habit to let the test block do one or more of three things:
1. provide information on how the module or program is used,  
2. test if the module functions work properly,  
3. offer interaction with users such that the module file can be applied as a useful program.  

To achieve the second task, we have to write functions that verify the implementation in a module. The general advice is to write test functions that,  
1. have names starting with `test_`,  
2. express the success or failure of a test through a boolean variable, say `success`,  
3. run `assert success, msg` to raise an `AssertionError` with an optional message `msg` in case the test fails.  

We talk about this later on in the notes.  

<b>Doc-strings in modules</b><br>It is a good habit to include a doc-string in the beginning of your module file. This docstring should explain the purpose and use of the module.

<br>

### Scope of definitions in your module    

Once you have created your module, you can import it just like any other module into our program, for example,
```python
import cmd_find_primes
dir(cmd_find_primes)
```
    ['__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'get_primes',
     'is_prime']

However, more often than not, you may want to define variables that are to be used only within the module itself and not be accessed by the user. The convention is to start the names of these variables by an underscore. For example,
```python
_topic = "Python programming"
```

This, however, does not prevent the import of the variable `_topic` into your code from your the [module](mod_cmd_find_primes_del.py) containing it. One solution is to delete the variables to which we do not want the user to have access, at the end of the module,
```python
del _topic
```

such that the [module]() containing the above statement will give,

```python
import mod_cmd_find_primes_del
dir( mod_cmd_find_primes_del )
```
    ['__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'get_primes',
     'is_prime']

However, note that if you import all definitions in [your module](mod_cmd_find_primes_all.py) as standalone definitions like the following,  

```python
from mod_cmd_find_primes_all import *
dir()
```
    ['In',
     'Out',
     '_',
     '_3',
     '__',
     '___',
     '__builtin__',
     '__builtins__',
     '__doc__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     '_dh',
     '_i',
     '_i1',
     '_i2',
     '_i3',
     '_i4',
     '_i5',
     '_ih',
     '_ii',
     '_iii',
     '_oh',
     '_sh',
     'exit',
     'get_ipython',
     'get_primes',
     'is_prime',
     'quit']

you see that the variable `_topic` is not imported. In general, to avoid confusion, it is best to define an `__all__` variable in your module, which contains a list of all variable and function names that are to be imported as standalone definitions using `from mymodule import *`. For example, add the following to the above module,  

```python
__all__ = ['get_primes']
```

Upon importing this module, now only the function `get_prime` will be imported and not `_topic` or `is_prime`.  

### The path to your modules  

When you create a module, if it is in the current directory of your code, then it will be automatically found by the Python interpreter. This is, however, not generally the case if your module lives in another directory than the current working directory of Python interpreter. To add the module's directory to the path of your Python interpreter, use the following,  

```python
myModuleFolder = ’the path to your module’
import sys
sys.path
```
    ['',
     'C:\\Program Files\\Anaconda3\\Scripts',
     'C:\\Program Files\\Anaconda3\\lib\\site-packages\\lmfit-0.9.5_44_gb2041c3-py3.5.egg',
     'C:\\Program Files\\Anaconda3\\python35.zip',
     'C:\\Program Files\\Anaconda3\\DLLs',
     'C:\\Program Files\\Anaconda3\\lib',
     'C:\\Program Files\\Anaconda3',
     'c:\\program files\\anaconda3\\lib\\site-packages\\setuptools-20.3-py3.5.egg',
     'C:\\Program Files\\Anaconda3\\lib\\site-packages',
     'C:\\Program Files\\Anaconda3\\lib\\site-packages\\Sphinx-1.3.5-py3.5.egg',
     'C:\\Program Files\\Anaconda3\\lib\\site-packages\\win32',
     'C:\\Program Files\\Anaconda3\\lib\\site-packages\\win32\\lib',
     'C:\\Program Files\\Anaconda3\\lib\\site-packages\\Pythonwin',
     'C:\\Program Files\\Anaconda3\\lib\\site-packages\\IPython\\extensions',
     'C:\\Users\\Amir\\.ipython']

```python
sys.path.insert(0,myModuleFolder)
sys.path
```
    [’the path to your module’,
     '',
     'C:\\Program Files\\Anaconda3\\Scripts',
     'C:\\Program Files\\Anaconda3\\lib\\site-packages\\lmfit-0.9.5_44_gb2041c3-py3.5.egg',
     'C:\\Program Files\\Anaconda3\\python35.zip',
     'C:\\Program Files\\Anaconda3\\DLLs',
     'C:\\Program Files\\Anaconda3\\lib',
     'C:\\Program Files\\Anaconda3',
     'c:\\program files\\anaconda3\\lib\\site-packages\\setuptools-20.3-py3.5.egg',
     'C:\\Program Files\\Anaconda3\\lib\\site-packages',
     'C:\\Program Files\\Anaconda3\\lib\\site-packages\\Sphinx-1.3.5-py3.5.egg',
     'C:\\Program Files\\Anaconda3\\lib\\site-packages\\win32',
     'C:\\Program Files\\Anaconda3\\lib\\site-packages\\win32\\lib',
     'C:\\Program Files\\Anaconda3\\lib\\site-packages\\Pythonwin',
     'C:\\Program Files\\Anaconda3\\lib\\site-packages\\IPython\\extensions',
     'C:\\Users\\Amir\\.ipython']

In the above, we added the path to our module to the list of all paths the Python interpreter will search, to find the module requested to be imported (Note that `'the path to your module'` is not a real system path, this was just an example).  

## Some useful Python modules  

One of the greatest strengths of Python as a scientific programming language is that, for almost everything that you could imagine and want to write code, someone has already written it, and so there is *no reason to reinvent the wheel if someone has already done it for you*. Throughout your career, you will get to know many of the most important modules for your domain of science. Here I will introduce only a very few general-purpose modules that have some interesting and rather useful functions in them. 

### The `collections` module  

This module contains some non-standard Python data types that can be very handy at times.

#### The **Counter** data type

The `Counter` function from module `collections` takes in a list and creates a dictionary, whose keys are unique elements in the input list and the values of the keys, are the number of times each key appears in the list. For example,  

```python
from collections import Counter
mylist = [1,1,1,2,3,34,45,34,34,7,8,34,3,3,6,4,4,4,0,34,9,0]
c = Counter(mylist)
c
```
    Counter({0: 2, 1: 3, 2: 1, 3: 3, 4: 3, 6: 1, 7: 1, 8: 1, 9: 1, 34: 5, 45: 1})

There are basically three methods for generating a Counter dictionary,  

```python
c1 = Counter(['a', 'b', 'c', 'a', 'b', 'b']) # input a list directly into Counter
c2 = Counter({'a':2, 'b':3, 'c':1}) # Give it the Counter dictionary
c3 = Counter(a=2, b=3, c=1) # or simply give it the counts
c1 == c2 == c3
```
    True

##### What is Counter useful for?  

Suppose you have a long list of letters, and for some reason, you need to count the number of times each letter appears in your string. You can achieve your goal as in the following example,  

```python
s = 'amirshahmoradijakelucerotravismike'
c = Counter(s)
for key in c.keys():
    print('The letter {} appears only {} times in the string'.format(key,c[key]))
```
    The letter v appears only 1 times in the string
    The letter a appears only 5 times in the string
    The letter u appears only 1 times in the string
    The letter l appears only 1 times in the string
    The letter j appears only 1 times in the string
    The letter d appears only 1 times in the string
    The letter h appears only 2 times in the string
    The letter o appears only 2 times in the string
    The letter i appears only 4 times in the string
    The letter k appears only 2 times in the string
    The letter c appears only 1 times in the string
    The letter t appears only 1 times in the string
    The letter s appears only 2 times in the string
    The letter m appears only 3 times in the string
    The letter r appears only 4 times in the string
    The letter e appears only 3 times in the string  
​

Now suppose you wanted to count the number of times different words appear in a given text,  

```python
from collections import Counter
text = "Data science is a multi-disciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data."
c = Counter(text.split())
for word in c.keys():
    print('The word "{}" appears only {} times in the text'.format(word,c[word]))
```
    The word "Data" appears only 1 times in the text
    The word "science" appears only 1 times in the text
    The word "is" appears only 1 times in the text
    The word "a" appears only 1 times in the text
    The word "multi-disciplinary" appears only 1 times in the text
    The word "field" appears only 1 times in the text
    The word "that" appears only 1 times in the text
    The word "uses" appears only 1 times in the text
    The word "scientific" appears only 1 times in the text
    The word "methods," appears only 1 times in the text
    The word "processes," appears only 1 times in the text
    The word "algorithms" appears only 1 times in the text
    The word "and" appears only 3 times in the text
    The word "systems" appears only 1 times in the text
    The word "to" appears only 1 times in the text
    The word "extract" appears only 1 times in the text
    The word "knowledge" appears only 1 times in the text
    The word "insights" appears only 1 times in the text
    The word "from" appears only 1 times in the text
    The word "structured" appears only 1 times in the text
    The word "unstructured" appears only 1 times in the text
    The word "data." appears only 1 times in the text

Now, you can also apply all different methods that exist for Counter data types on the variable `c` in the above case. For example, you could ask for the 3 most common words in the text,  

```python
c.most_common(3)
```
    [('Engineering', 3), ('the', 2), ('is', 2)]
    
#### The **OrderedDict** data type  

This is also a subclass of dictionary data type, which provides all the methods provided by `dict`, but which also retains the order by which elements are added to the dictionary. Consider the following ordinary dictionary,  

```python
d = {5:5,3:3,6:6,1:1}
```

A normal dictionary does not conserve the order by which elements were added to the dictionary,  

```python
d = {5:5,3:3,6:6,1:1}
for i,j in d.items():
    print(i,j)
```
    1 1
    3 3
    5 5
    6 6

To save the order of the elements, you can use `OrderedDict`,  

```python
from collections import OrderedDict as od
d = od([(5,5),(3,3),(6,6),(1,1)])
for i,j in d.items():
    print(i,j)
```
    5 5
    3 3
    6 6
    1 1

The only difference is that `OrderedDict` preserves the by which the keys are inserted to the dictionary. A regular dict doesn't track the insertion order and **iterating over an ordinary dictionary outputs the dictionary items in an arbitrary order**. By contrast, `OrderedDict` keeps the order the items are inserted in the dictionary for the entire lifetime of the dictionary.  

Keep in mind that two ordered dictionaries with the same contents may not necessarily be equal since the order of their content also matters.

### The `timeit` module  

This is a module that provides some useful functions for timing the performance and speed of pieces of your Python code.  

```python
import timeit as tt
tt.timeit( "-".join(str(n) for n in range(100)) , number=10000 )
```
    0.03779717059364884

The first input to `timeit` function above is the operation which we would like to time, and the second input, tell the function, how many times repeat the task (If the operation takes a tiny amount, you would want to repeat it many many times, in order to get a sensible timing output). Here is the same operation as above, but now using the [map](http://book.pythontips.com/en/latest/map_filter.html#map) function,  

```python
tt.timeit( "-".join( map(str,range(1000))) , number=10000 )
```
    0.384857713242468  

In IPython or Jupyter, you can do the timing operation in a smarter way using IPython magic function [%timeit](https://ipython.org/ipython-doc/dev/interactive/magics.html#magic-timeit),  

```python
%timeit "-".join(str(n) for n in range(100))
```
    10000 loops, best of 3: 36.6 µs per loop

The IPython's magic function automatically figures how many times it should run the operation to get a sensible timing of the operation.  

```python
%timeit "-".join( map(str,range(100)))
```
    10000 loops, best of 3: 21 µs per loop

In general, as you noticed in the above example, the function `map` performs much better and faster than Python's for-loop.  

### The `time` module  

More generally, if you want to measure the CPU time spent on a specific part of your code, you can use the `clock()` method from `time` module,  

```python
import time
# do some work
t0 = time.clock()   # get the initial CPU time
# do some further work which you want to time
t1 = time.clock()   # get the final CPU time
cpu_time = t1 - t0  # This is the time spent on the task being timed.
```

The `time.clock()` function returns the CPU time spent in the program since its start. If the interest is in the total time, also including reading and writing files, `time.time()` is the appropriate function to call. Now suppose you had a list of functions that performed the same task but using different methods, and you wanted to time their performance. Since in Python, functions are ordinary objects, making a list of functions is no more special than making a list of strings or numbers. You can, therefore, create a list of function names and call them one by one, inside a loop, and time each one respectively.  

```python
import time
functions = [func1, func2, func3, func4,func5, func6, func7, func8,func9, func10]
timings = [] # timings[i] holds CPU time for functions[i]
for function in functions:
    t0 = time.clock()
    function(<input variables>)
    t1 = time.clock()
    cpu_time = t1 - t0
    timings.append(cpu_time)
```
