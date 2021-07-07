---
title: Variables in Python
tags: [variable, type, python]
keywords: variable, type, python
summary: "This note aims at introducing the variables and the basic variable types in Python."
#permalink: /notes/values-variables-types/variables/index.html
last_updated: July 9, 2019
---

  
## Variable naming convention in Python  

The variable naming convention in Python is that each variable starts with a letter and can contain only letters, numbers or underscore "_".

```python
var1 = 1
```

```python
print('value of var1 is ',var1,'.')
```
    value of var1 is 1.
    
```python
a_long_variable_name = 2.5 # The variable name can be almost as long as you wish
print(a_long_variable_name)
```
    2.5
  
Numbers are only valid if they appear inside or at the end of the variable name. Other symbols are syntactically invalid anywhere in a variable name.  

```python
123new_var = 2.5 # This is an invalid name
```

      File "<ipython-input-10-0e3e63931842>", line 1
        123new_var = 2.5 # This is an invalid name
                 ^
    SyntaxError: invalid syntax
    
```python
new_var$ = 2.5 # symbols are not valid in Python variable names
```

      File "<ipython-input-12-71f3fbc68938>", line 1
        new_var$ = 2.5 # symbols are not valid in Python variable names
               ^
    SyntaxError: invalid syntax
    
```python
amir = "teacher"
print('Amir is a', amir)
```
    Amir is a teacher

```python
123amir = "teacher" # Wrong name for variable
```

      File "<ipython-input-38-85ed673cd303>", line 1
        123amir = "teacher"
              ^
    SyntaxError: invalid syntax
    
```python
life_expectancy = 120; print( "The life expectancy for the millennials is projected to be %d years! (But don't believe it...)" % (life_expectancy) );
```
    The life expectancy for the millennials is projected to be 120 years! (But don't believe it...)
    
```python
# Now lets do a Physics calculation.
v0 = 5; # initial velocity for a projectile motion.
g = 9.81 # Earth gravity acceleration.
t = 0.6
y = v0*t - 0.5*g*t**2
print('''
At t = %f seconds, a ball with initial velocity v0 = %.3E m/s is located at the height %.2f m.
''' % (t,v0,y) )
```
    
    At t = 0.600000 seconds, a ball with initial velocity v0 = 5.000E+00 m/s is located at the height 1.23 m.

```python
# or on multi-line:
print('''
At t = %f seconds,
a ball with initial velocity v0 = %.3E m/s
is located at the height %.2f m.
100%% accurate!
''' % (t,v0,y) )
```
    
    At t = 0.600000 seconds,
    a ball with initial velocity v0 = 5.000E+00 m/s
    is located at the height 1.23 m.
    100% accurate!
    
Here are some `printf` format specifications, that can be used with `print` function:

- %s   for string
- %d   for integer 
- %0xd for integer padded with x zeros
- %f   for decimal notation with 6 decimals
- %e   for scientific notation
- %E   for scientific notation
- %%   percentage sign itself  

There is also a more recent, recommended way of determining the string format in Python, using `.format()` method, about which you find some more useful information [here](https://pyformat.info/).  


### Python reserved names (keywords)  

There are some limitation as what names you can choose for your variables, even if they completely obey the Python syntax standard. Variable names in Python cannot be the same as **Python keywords**, which are simply names that reserved for a specific purpose in Python programming.  A keyword as variable name, function name or any other identifier. They are used to define the syntax and structure of the Python language. Note that **Python keywords are case-sensitive**.  There are already more than 30 keywords in Python 3. In order to see a complete list of all keywords use the following python codes,  

```python
import keyword

print(keyword.<press tab>
keyword.iskeyword keyword.kwlist    keyword.main

print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

keyword.kwlist # same thing as above, but each keyword printed on a new line.
```
    ['False',
     'None',
     'True',
     'and',
     'as',
     'assert',
     'break',
     'class',
     'continue',
     'def',
     'del',
     'elif',
     'else',
     'except',
     'finally',
     'for',
     'from',
     'global',
     'if',
     'import',
     'in',
     'is',
     'lambda',
     'nonlocal',
     'not',
     'or',
     'pass',
     'raise',
     'return',
     'try',
     'while',
     'with',
     'yield']

Note that all keywords except `True`, `False` and `None` are in lowercase and they must be written as lowercase. To understand the meaning and function of each of these keywords, see [this page](https://www.programiz.com/python-programming/keyword-list).  

### Meanings of underscore _ in Python  

Frequently, as you learn more about Python, you will notice the presence of underscores in Python variables, function and method names. Depending on where and how underscore appears in a Python name, it can have a different meaning.  

#### Underscore as word separator in variable/function naming  

The convention in Python programming is to separate multiple words in Python variable names by underscore. For example,  

```python
an_example_long_variable_name = 123
```

Of course, this is totally a convension. But I highly recommend you to follow the conventions that everyone else follows, so that you can understand other people's codes and others can understand your code easily.  

#### Underscore meaning in Python interpreter  

A variable named solely by underscore **_** in Python interpreter points to the result of the **last executed statement** in the interactive interpreter session. This convention was first implemented by the standard CPython interpreter, but now other implementations are also following the convention.  

```python  
_
```
    ''

```python
a = 120
_
```
    ''

```python
a + a
```
    240

```python
_
```  
    240

#### Underscroe _ as a dummy name in Python scripts  

The underscore _ can be used as a dummy name in Python scripts, a name for an entity that does play an important role in the code, for example, the index of a loop. This allows the next person who reads the code to know which entites (variables, ...) are dummy and not intended to be used.  

```python
a = 1
b = 2
print("a =",a,"b =",b)
```
    a = 1 b = 2

```python
_ = a
a = b
b = _
print("a =",a,"b =",b) # the values are swapped. _ is just a dummy indtermediate variable.
```
    a = 2 b = 1

#### Underscore as an indicator of the local-scope of a variable/function  

A single underscore that appears at the beginning of a name in Python code indicates that the name has to be treated as *private* by the programmer. In other words, a name starting with _ is for internal use. In Python documentation the following note exists about such names:  

A name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.

For Python module functions, if you use `from module_name import __all__` instead of `from module_name import *`, then all internal names in the module (that begin with _) will be imported to your environment as well.  

#### Double underscore before and after a name (e.g., `__init__`)  

Such names are special method names used by Python. This is just a convention, that is, a way for the Python system to use names that won’t conflict with user-defined names. These names can be typically overridden to define the desired behaviour for when Python calls them. For example, the `__init__` method is often overridden when writing a Python class. We will get to these topics later on.  

A good review of underscore in Python can be found [here](https://shahriar.svbtle.com/underscores-in-python).  

## Variables in Python  

Python has 6 main variable types:  

- **Number**
- **String**
- **List**
- **Tuple**
- **Dictionary**  
- **Sets**  

### Number variables  

We have already extensively discussed number values in the previous lecture. Basically, everything that we have said about number values, holds also for variables of type number. But here is a very cool fear of number values and variables, that we skipped over in our previous lecture. When you define a Python number variable (or value), then python interpreter automatically allows you to perform some pre-defined operations on the variable/value by default. To access these operations, the dot `.` syntax has to be used. Type the variable name, followed by `.`, and then press `tab` in your IPython/Jupyter editor.  Depending on the type of number (integer/float/complex) you will get a different set of operations that are allowed on the variable. The following shows some examples in IPython environment.  

```python
a = 120 # This is an integer variable
a.<press tab>
a.bit_length  a.conjugate   a.denominator a.from_bytes  a.imag        a.numerator   a.real        a.to_bytes

a.conjugate
```
    <function int.conjugate>

```python
a.conjugate()
```
    120

```python
a.imag
```
    0

```python
a.real
```  
    120

```python
a = 120.5  # Now 'a' is a float variable
a.<press tab>
a.as_integer_ratio a.conjugate        a.fromhex          a.hex              a.imag             a.is_integer       a.real

a.as_integer_ratio()  # Gives out the two numbers whose division is the value of the variable 'a'.
```
    (241, 2)

```python
a.is_integer()   # 120.5 is not a whole number! (it would be True if a = 120.0)
```
    False

You can repeat the above for a complex number and see what you get.  

```python
a = 1+1j
a.<press tab>
a.conjugate a.imag      a.real

a.conjugate()
```
    (1-1j)

### String variables  

Just as with numbers, string is another variable/value type in Python with many handy features that come withit. For example, if you create a string variable or value, fllowed by `.` and then press `tab` you will see a long list of methods that can be applied on the string,  

```python
my_string = 'this is a String'
my_string.<press tab>
my_string.capitalize   my_string.find         my_string.isdigit      my_string.isupper      my_string.replace      my_string.split        my_string.upper
my_string.casefold     my_string.format       my_string.isidentifier my_string.join         my_string.rfind        my_string.splitlines   my_string.zfill
my_string.center       my_string.format_map   my_string.islower      my_string.ljust        my_string.rindex       my_string.startswith
my_string.count        my_string.index        my_string.isnumeric    my_string.lower        my_string.rjust        my_string.strip
my_string.encode       my_string.isalnum      my_string.isprintable  my_string.lstrip       my_string.rpartition   my_string.swapcase
my_string.endswith     my_string.isalpha      my_string.isspace      my_string.maketrans    my_string.rsplit       my_string.title
my_string.expandtabs   my_string.isdecimal    my_string.istitle      my_string.partition    my_string.rstrip       my_string.translate

my_string.upper()
```
    'THIS IS A STRING'

```python
my_string.swapcase()
```
    'THIS IS A sTRING'


#### Strings are immutable  

Although strings (both values and variables) can be indexed letter by letter, keep in mind that they cannot be changed (mutated) to something new. In other words, string are immutable.
```python
my_string = 'Amir Shahmoradi'
my_string[0] = 'a'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-13-27fc86283e06> in <module>()
----> 1 my_string[0] = 'a'

TypeError: 'str' object does not support item assignment
```

The correct way of doing this would be through the indirect use of string methods or string slicing.  

```python
my_string = my_string[:4] + ' ' + my_string[4:] # mutating my_string: add a space between first and last names.
my_string
```
    'Amir  Shahmoradi'

It is often very useful to know the length of a string. This can be done using `len()` function.
```python
len(my_string)
```
    16

```python
len(my_string[0:5])
```
    5



#### Testing if a string is part of another string  

We have already discussed some boolean string operations in Lecture 4. There are howver two more boolean operations that deserve to be mentioned here.  

```python
text = "Data science is a multi-disciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data."
"Science" in text     # test if "Science" is part of the "text" string variable.
```
    False

```python
"science" in text
```
    True

```python
"Science" not in text     # test if "Science" is NOT part of the "text" string variable.
```
    True

To know more about string values and variables in general, visit [this page](https://docs.python.org/2/tutorial/introduction.html#strings).  

### List variables  

List is another standard variable in type in Python and is composed of an ordered set of values (elements), each of which is identified by an index. Lists are defined by brackets `[]`.  
```python
emptyList = [] # initiate an empty list
emptyList
```
    []

```python
myList = [ 0,1,2,'Amir',complex(1,2j) ]
myList
```
    [0, 1, 2, 'Amir', (-1+0j)]

```python
myList[0] # note that list index always begins with 0
```  
    0

#### List slices  

```python
myList[:-1] # all list elements from beginning to end, similar to myList, or myList[:]
```
    [0, 1, 2, 'Amir']

```python
myList[:]
```
    [0, 1, 2, 'Amir', (-1+0j)]

```python
myList[-1:] # select only the last element in list
```
    [(-1+0j)]

```python
myList[::-1] # Creat list in reverse order.
```
    [(-1+0j), 'Amir', 2, 1, 0]

<b>Lists vs. Strings</b><br>You may have already noticed that lists behave very similar to strings in Python. In fact, both List and String are examples of ordered sets in Python known as <b>sequence</b>. The only difference between list and python is that the elements of strings have to be all of type character, whereas lists do not have such restriction, as seen in the example above.

<!--
<br>
<div class="center">
    <div class="rcbox" style="text-align:justify;">
        <b>Lists vs. Strings</b><br><br>
        You may have already noticed that lists behave very similar to strings in Python. In fact, both List and String are examples of ordered sets in Python known as <b>sequence</b>. The only difference between list and python is that the elements of strings have to be all of type character, whereas lists do not have such restriction, as seen in the example above.
    </div>
</div>
<br>
-->

#### Nested lists  

Lists can also contain other lists as elements. This way you can create matrices of numbers as well.  

```python
smallList = [1,2,3]
list_of_lists = [ 10 , 100.0 , ['amir','shahmoradi'] , smallList ]
list_of_lists
```
    [10, 100.0, ['amir', 'shahmoradi'], [1, 2, 3]]

```python
my_matrix = [ [1,2,3] , [4,5,6] , [7,8,9] ]
my_matrix[0][2] # the first index points to the 0th element in the list of lists, and the second index calls the list that is the first element of the big list. 
```
    3

```python
my_matrix[5-5][(2+2)//2]  # note that list indices can be the result of arithmetic operations too.
```
    3

```python
len(my_matrix) # This function gives the length of the list of lists.
```
    3

```python
list_of_lists
```
    [10, 100.0, ['amir', 'shahmoradi'], [1, 2, 3]]

```python
len(list_of_lists[0]) # The first element, being an integer, does not have a length
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-63-11f2bd3dda3d> in <module>()
----> 1 len(list_of_lists[0])

TypeError: object of type 'int' has no len()
```

```python
len(list_of_lists[2]) # but the third element in the list, is itself a list, so it does have a length
```
    2

#### Operations on lists  

Two mathematics operations `+` and `*` are also meaningful for lists, just as it is for string sequences.  
```python
list1 = [1,2,3]
list2 = [4,5,6]
list1 + list2
```
    [1, 2, 3, 4, 5, 6]

```python
list1 * 3
```
    [1, 2, 3, 1, 2, 3, 1, 2, 3]

```python
(list1 + list2) * 3
```
    [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

In addition, once a list is created, by default, a list of pre-defined operations (methods) are available to act on the list content. To access these methods, again use `.` notation, just as you did for strings before.  

```python
list1.<press tab>
list1.append  list1.clear   list1.copy    list1.count   list1.extend  list1.index   list1.insert  list1.pop     list1.remove  list1.reverse list1.sort

list1
```
    [1, 2, 3]

```python
list1.append(4) # append number 4 to the end of list1
list1
```
    [1, 2, 3, 4]

```python
list1.append([1,1,1]) # append the given list to the end of list1
list1
```
    [1, 2, 3, 4, [1, 1, 1]]

```python
list1.count(1) # count the number of times 1 appears as element of list1
```
    1

```python
list1[-1].count(1) # count the number of times 1 appears as element in the list appearing as the element in list1.
```
    3

```python
list1[-2].count(4)  # Note that count is a method only for lists, and therefore cannot be applied to numbers.
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-21-2add981bfc56> in <module>()
----> 1 list1[-2].count(4)

AttributeError: 'int' object has no attribute 'count'
```

```python
list1.extend([1,1,1])  # extend list1 by 3 more members
list1
```
    [1, 2, 3, 4, [1, 1, 1], 1, 1, 1]

```python
list1.count(1) # This time counting 1, gives 4, since the list was extended by 3 more '1'.
```
    4

[Here](https://linuxconfig.org/python-list-methods) is a useful reference for available list methods in Python.  

#### Lists are mutable (unlike Strings)  

Another major difference between list sequences and string sequences in Python is that the elements of lists can be changed (mutated) to something new.  

```python
people = [ 'Amir' , 'Jake' , 'Travis' ]
people
```
    ['Amir', 'Jake', 'Travis']

```python
people[0] = 'Brandon'
people
```
    ['Brandon', 'Jake', 'Travis']

```python
people.remove('Brandon')
people
```
    ['Jake', 'Travis']

#### Deleting list elements  

Deleting list elements can be done by either value of the element, or using its index, like the following,  

```python
a = [1,2,3,1,2,3]
a.remove(1)   # remove the first element correponding to value of 1.
a
```
    [2, 3, 1, 2, 3]

```python
a.remove(1)   # remove the first element correponding to value of 1.
a
```
    [2, 3, 2, 3]

```python
del a[0:3:2]      # delete element indices 0, 2
a
```
    [3, 3]

#### Concatenating a list of strings  

If a list is all string values, you can use the following string method `.join()` to concatenate the contents of the list.  

```python
mylist = ['The' , 'weather' , 'is' , 'rainy' , 'today' , 'and' , 'cold' , 'only' , '22' , 'F.']
" ".join(mylist)
```
    'The weather is rainy today and cold only 22 F.'
 
### Tuple variables  

Tuples are a type of Python variables very similar to list sequences, except that they are **immutable**, meaning that, once generated, they cannot be changed. Another difference is that, tuples use parentheses for definition, whereas lists use square brackets.  

```python
emptyTuple = ()
single_element_tuple = (1,)  # ATTN: note the comma after the element
tuple1 = (1, 2, 3, 'amir', 'Jake')
single_element_tuple
```
    (1,)

```python
type(single_element_tuple)
```
    tuple

```python
single_element_tuple = (1)
single_element_tuple
```
    1

```python
type(single_element_tuple)
```
    int

Creating a tuple is as simple as putting different comma-separated values. Optionally you can put these comma-separated values between parentheses also.  

```python
tuple2 = 1,2,3,4   # another way of creating a tuple
type(tuple2)
```
    tuple

#### Modifying the content of Tuples  

Tuples are an example of data structure in Python, used for organizing and grouping data. Once a tuple is created, its content cannot be changed or manipulated anymore. However, its elements can be called just like lists.  
```python
tuple2[0]
```
    1

```python
tuple2[1:3]
```
    (2, 3)

```python
tuple2.<press tab>    # press tab key to get the list methods
tuple2.count tuple2.index

tuple2.count(2) # count the number of members that are 2
```
    1

```python
tuple2.count(5) # count the number of members that are 5
```
    0

```python
tuple2.index(2) # get the index of the first member in tuple that is 2
```
    1

```python
tuple2.index(5) # get the index of the first member in tuple that is 5. (error! 5 is not a member)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-54-f0077f9af98b> in <module>()
----> 1 tuple2.index(5)

ValueError: tuple.index(x): x not in tuple
```

Moreover, although the content of tuple cannot be changed, there is nothing to prevent the programmer from redefining the tuple with new content,  

```python
tuple1 = (1, 2, 3, 'amir', 'Jake')
tuple1
```
    (1, 2, 3, 'amir', 'Jake')

```python
tuple1 = ('Travis','Caleb','Lucero') + tuple1[-1:]    # redefining tuple1
tuple1
```
    ('Travis', 'Caleb', 'Lucero', 'Jake')

But pay attention that the above, all the terms in the assigment must be a tuple, otherwise you will get an error like the following (e.g., a single member of a tuple, is not a tuple by itself),  

```python
tuple1 = (1, 2, 3, 'amir', 'Jake')
tuple1 = ('Travis','Caleb','Lucero') + tuple1[-1] # Note that tuple1[-1] is a string, and not a tuple!
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-111-4c6018fb7529> in <module>()
----> 1 tuple1 = ('Travis','Caleb','Lucero') + tuple1[-1]

TypeError: can only concatenate tuple (not "str") to tuple
```

```python
type(tuple1[-1])
```
    str

```python
type(tuple1[-1:])
```
    tuple

Note also the difference between `+` operations in the above tuple redefinition, and `,` operations below,
```python
tuple1 = (1, 2, 3, 'amir', 'Jake')
tuple1 = ('Travis','Caleb','Lucero') + tuple1[-1:]
tuple1
```
    ('Travis', 'Caleb', 'Lucero', 'Jake')

```python
tuple1 = (1, 2, 3, 'amir', 'Jake')
tuple1 = ('Travis','Caleb','Lucero') , tuple1[-1:]
tuple1
```
    (('Travis', 'Caleb', 'Lucero'), ('Jake',))

Tuples can be **heterogeneous**, as in the above example, meaning that each member of tuple can be a tuple itself, a list, or any other variable type.  


### Dictionary variables  
The past three data types discussed in the previous secitons — strings, lists, and tuples — are of type **sequence**. For sequences, we have seen above that we use integers as indices to access the values these variables contain. Dictionaries are yet another built-in variable type in Python. A dictionary variable is a sequence of pairs of {key: value}. Instead of using numbers to index elements (as in list, string, tuple), dictionaries use keys in order to retrieve the key's value.  The keys can be any immutable type (string, number and tuple). Values can be any type (heterogeneous, mutable), just like the elements of a list or tuple. Dictionaries are also called **associative arrays** since they associate a key with a value. One way to create a dictionary is to start with the empty dictionary and add `key:value` pairs.  

```python
age = {}   # empty dictionary
age
```
    {}

```python
type(age)
```
    dict

```python
age = { 'amir':120 , 'jake':22 , 'Lucero':19 , 'Travis':20 }
age
```
    {'Lucero': 19, 'Travis': 20, 'amir': 120, 'jake': 22}

```python
age['Lucero']
```
    19

Some important features of dictionaries are the following:  
- A dictionary is a collection of key-value pairs.  
- A dictionary is a set of key:value pairs.  
- All keys in a dictionary must be unique.  
- In a dictionary, a key and its value are separated by a colon (:).  
- Each key-value pair is separated by a comma from another pair in dictionary.  
- All the key-value pairs together are listed between curly brackets `{ }`.  
- Query the dictionary using square brackets `[ ]`, inside of which you type the key, and the output will be the value correponding to the key.  

#### Three ways of constructing distionaries  

The are three basic ways for creating dictionaries in Python.  

**1.** Create empty dictionary and then add key-value pairs to it.  

```python
classroom = {}
classroom['amir'] = 'teacher'
classroom
```
    {'amir': 'teacher'}

```python
classroom['Jake'] = 'student'
classroom['Travis'] = 'student'
classroom
```
    {'Jake': 'student', 'Travis': 'student', 'amir': 'teacher'}

**2.** Create a dictionary from a list if tuples, using Python's built-in function `dict()`. The input argument of `dict()` is **a list of tuples**,
```python
month = dict( [ ( 1 , 'Jan') \
              , ( 2 , 'Feb') \
              , ( 3 , 'Mar') \
              , ( 4 , 'Apr') \
              , ( 5 , 'May') \
              , ( 6 , 'Jun') \
              , ( 7 , 'Jul') \
              , ( 8 , 'Aug') \
              , ( 9 , 'Sep') \
              , (10 , 'Oct') \
              , (11 , 'Nov') \
              , (12 , 'Dec') ] )
month
```
    {1: 'Jan',
     2: 'Feb',
     3: 'Mar',
     4: 'Apr',
     5: 'May',
     6: 'Jun',
     7: 'Jul',
     8: 'Aug',
     9: 'Sep',
     10: 'Oct',
     11: 'Nov',
     12: 'Dec'}

```python
month[5]
```
    'May'

But, be careful to not override the Python's function `dict()` by your user-defined variable or function of the same name, otherwise you will get an error like the following,  

```python
dict = 5
classroom = dict([('amir','teacher')])   # This will give error because dict is not pointing to the built-in function dict() anymore! It was overridden by the above assignment.
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-10-271a21fe772b> in <module>()
----> 1 classroom = dict([('amir','teacher')])

TypeError: 'int' object is not callable
```

**3.** Create a dictionary from two lists in parallel. Let's say the keys and values of our desired dictionary, each are in the form of a list. The question is now, if there is an easy Pythonic way to combine these two lists of keys and values to get a dictionary? The answer is yes, and it is achieved by a Python function named [`zip()`](https://docs.python.org/2/library/functions.html#zip).  

```python
person = ['amir','jake','travis']
role = ['teacher','student','student']
person_role_dict = dict( zip( person , role ) )
type(person_role_dict)
```
    dict

```python
person_role_dict
```
    {'amir': 'teacher', 'jake': 'student', 'travis': 'student'}

#### Manipulating dictionary variables  

**1. Removing a dictionary key-value pair**  

This can be done using Python's `del` command,
```python
person_role_dict
```
    {'amir': 'teacher', 'jake': 'student', 'travis': 'student'}

```python
del person_role_dict['amir']
person_role_dict
```
    {'jake': 'student', 'travis': 'student'}

**2. Adding a dictionary key**  
```python
person_role_dict
```
    {'jake': 'student', 'travis': 'student'}

```python
person_role_dict['amir'] = 'teacher'  # adding a new key-value pair ('amir' : 'teacher')
person_role_dict
```
    {'amir': 'teacher', 'jake': 'student', 'travis': 'student'}

**2. Changing the value of a key**  

```python
person_role_dict['amir'] = 'instructor' # changing the value of the key 'amir'
person_role_dict
```
    {'amir': 'instructor', 'jake': 'student', 'travis': 'student'}

**3. Getting the length of dictionary (number of key-value pairs)**  

```python
len(person_role_dict)
```
    3

**4. Using dictionary methods**  

Just as with other Python variable types, typing the name of a dictionary that is already defined, followed by `.` followed by pressing the `tab` key (in a good Python editor) will show you the list of methods that can act on the dictionary.  
```python
person_role_dict.<press tab>
                           person_role_dict.clear      person_role_dict.get        person_role_dict.pop        person_role_dict.update
                           person_role_dict.copy       person_role_dict.items      person_role_dict.popitem    person_role_dict.values
                           person_role_dict.fromkeys   person_role_dict.keys       person_role_dict.setdefault

person_role_dict.keys()
```
    dict_keys(['amir', 'jake', 'travis'])

```python
list ( person_role_dict.keys() )
```
    ['amir', 'jake', 'travis']

```python
type ( person_role_dict.keys() )
```
    dict_keys

```python
type ( list ( person_role_dict.keys() ) )
```
    list

```python
person_role_dict.values()
```
    dict_values(['instructor', 'student', 'student'])

```python
person_role_dict
```
    {'amir': 'teacher', 'jake': 'student', 'travis': 'student'}

```python
person_role_dict.pop('amir')  # remove the key-value pair ('amir':'teacher') and return the corresponding value of the key as output.
```
    'instructor'

```python
person_role_dict
```
    {'jake': 'student', 'travis': 'student'}

#### Dictionary representation of sparse matrices  

We already discussed in the above, the usefulness of nested lists in creating matrices. Now suppose we have a sparse matrix, whose most elements are zero, except a few non-zero elements. An alternative to using nested lists, which can also take less memory of the device, is to use a dictionary representation of the sparse matrix.  

```python
sparseMatrixList = [ [ 0 , 0 , 0 , 1 ]
                   , [ 2 , 0 , 0 , 0 ]
                   , [ 0 , 5 , 0 , 0 ]
                   , [ 0 , 0 , 0 , 3 ]
                   , [ 0 , 0 , 8 , 0 ]
                   ]
sparseMatrixList
```
    [[0, 0, 0, 1], [2, 0, 0, 0], [0, 5, 0, 0], [0, 0, 0, 3], [0, 0, 8, 0]]

```python
sparseMatrixDict = { (0,3): 1 , (1,0): 2 , (2,1): 5 , (3,3): 3 , (4,2): 8 }
sparseMatrixDict
```
    {(0, 3): 1, (1, 0): 2, (2, 1): 5, (3, 3): 3, (4, 2): 8}

### Set variables  

Besides all the aforementioned variable types in Python, there is another Python variable type that is useful for constructing and manipulating **unordered collection of unique elements**. Common uses of sets include **membership testing**, **removing duplicates from a sequence**, and **computing standard math operations on sets** such as intersection, union, difference, and symmetric difference.  

Like other collections, sets support `x in set` and `len(set)` operations. Being an unordered collection, **sets do not record element position or order of insertion**. Accordingly, sets do not support indexing, slicing, or other sequence-like behavior.  

There are currently **two built-in set types**, **set** and **frozenset**. The set type is mutable — the contents can be changed using methods like add() and remove().  

```python 
a = set( [ 1,2,3,(1,2),'amir' ] )
a.<press tab>
a.add                         a.difference                  a.intersection                a.issubset                    a.remove                      a.union
a.clear                       a.difference_update           a.intersection_update         a.issuperset                  a.symmetric_difference        a.update
a.copy                        a.discard                     a.isdisjoint                  a.pop                         a.symmetric_difference_update

a.add('jake')
a
```
    {(1, 2), 1, 2, 3, 'jake', 'amir'}

```python
a.add([1,3])   # Note that mutable types cannot appear in a set!
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-64-2a5b54498213> in <module>()
----> 1 a.add([1,3])

TypeError: unhashable type: 'list'
```

Sets can be also simply created by `{}`.  

```python
a = {1,2,3}
type(a)
```
    set

The **frozenset type** is **immutable** and **hashable** (i.e., its contents cannot be altered after it is created). It can therefore be used as a dictionary key or as an element of another set.  

```python
a = frozenset( [ 1,2,3,(1,2),'amir' ] )
a.<press tab>
a.copy                 a.intersection         a.issubset             a.symmetric_difference
a.difference           a.isdisjoint           a.issuperset           a.union

type(a)
```
    frozenset

**Note** that mutable types can neither appear in a set nor a frozenset. You can obtain more information about sets and frozensets and the methods that can act on them in the [Python library reference](https://docs.python.org/2.4/lib/types-set.html).  

## Assignment statements in Python  

In Python, an assignment statement is one line of Python code that contains **at least** one equal sign `=` and the purpose of it is to associate name(s) with a certain value in the program. **Assignment statements are the only Python statements that do not start with a keyword**. In most cases, the assignment statement will only contain one target name, one equal sign, and one expression (reduced to one single value that is assigned to the name).  

A **binding** is an association between a name and a value. Note that in Python, unlike many other languages, **names themselves are not associated with a specific variable types**. A name is just a label, and therefore it can be bound to any value of any type at any time. For example,  
```python
a = 'some text'
a
```
    'some text'

```python
a = 2
a
```
    2

### Aliasing vs. copying  

It is very important to understand the difference between **alias** assignment statements and **copy** assignment statements. As far as assignments are concerned, all data types in Python can be divided into two categories:  

1. simple data types (e.g., int, float, string, tuple)  
2. container data types (e.g., list, dict, set, ...)  

For **simple data types**, an assignment means that their value is **copied** to the assigned variable.  
```python
x = 1
y = x   # An assignment statement that copies the value of x into y.
x = 2   # Now changing the value of x, won't change the value of y.
x
```
    2

```python
y
```
    1

For **container data types**, an assignment in the form of copy can be computationally and memory-wise very expensive, and so it makes sense, when an assignment involves container types as values, then the new name would only **point** to the original container. In other words, the new assignment provides an **alias** for the container value.  
```python
a = [1,2,3]
b = a      # In this assignment, b is simply an alias for a. The value of a is NOT copied into b
a
```
    [1, 2, 3]

```python
b
```
    [1, 2, 3]

```python
a is b     # a and b have the same identity
```
    True

```python
a == b     # a and b have the same value
```
    True

```python
a = [1,2,3]
b = [1,2,3]
a is b     # a and b don't have the same identity anymore, since they are not pointing to the same value anymore.
```
    False

```python
a == b     # Despite not being identical, a and b still have the same value.
```
    True

If you want to get a copy of a container object, instead of an alias for it, you should use the `copy` method of the container object.
```python
a = [1,2,3]
b = a.copy()   # Copy the content of a into b
a is b
```
    False

```python
a == b
```
    True

> **Conclusion:**
> So, keep in mind that, assignments in which the value to be assigned is a container type (e.g., list, dict, set) will result in an alias, and not a fresh copy of the original value.


### Multiple simultaneous assignments in one line  

A shortcut way of aliasing multiple variables with one single value is the following,  
```python
a = b = c = 3
a is b
```
    True

```python
a is b is c
```
    True

```python
a == b == c
```
    True

Here, an integer object is created with the value 1, and all three variables are assigned to the same memory location. This is also true for container variable types.  
```python
a = b = c = [1,2,3]
a is b is c
```
    True

You can also assign multiple objects to multiple variables all in the same asignment statement. But keep in mind that the number of assignments on both sides of equal sign must be equal.  
```python
a, b, c = 1, 2, "amir"
a
```
    1

```python
b
```
    2

```python
c
```
    'amir'

Here, two integer objects with values 1 and 2 are assigned to variables a and b respectively, and one string object with the value "amir" is assigned to the variable c. This form of assignment in the above is basically like setting the tuple `(a,b,c) = (1,2,"amir")`. This is why it is important that both sides of the equal sign have the same number of elements. Here are some other examples:  

```python
a, b, c = 3, 3, 3
a is b
```
    True

```python
a == b
```
    True

```python
[ a , b ] = [ 5 , 4 ]
a
```
    5

```python
[ a , b ] = ( 5 , 4 )
a
```
    5

```python
[a,b] = [c,d] = [4,5]
a is b
```
    False

```python
a is c
```
    True

```python
[a,b] is [c,d]
```
    False

```python
[a,b] is [4,5]
```
    False

```python
[a,b] == [c,d]
```
    True

```python
[a,b] == [4,5]
```
    True

### Value swapping  

The traditional way of swapping values of two variables in mostprogramming languages is like the following,  

```python
a = 5
b = 7
_ = a
a = b
b = _
a
```
    7

```python
b
```
    5

With either Python lists or tuples, this swapping can be achived neatly in just one line of code,  

```python
(a,b) = (b,a) # swaping using tuples
a
```
    5

```python
b
```
    7

```python
[a,b] = [b,a] # swaping using lists
a
```
    7

```python
b
```
    5

## Exercise

1. Value, variable, type, syntax error: [web-link](https://www.cdslab.org/recipes/programming/values-variables-types-syntax-error/values-variables-types-syntax-error)  

1. Python aliasing vs. copying variables: [web-link](https://www.cdslab.org/recipes/programming/python-variable-aliasing-copying/python-variable-aliasing-copying)  

1. Single-line Python input and string manipulation (only part A): [web-link](https://www.cdslab.org/recipes/programming/python-single-line-input-string-manipulation/python-single-line-input-string-manipulation)  

1. Python script full of syntax errors: [web-link](https://www.cdslab.org/recipes/programming/python-script-full-of-syntax-errors/python-script-full-of-syntax-errors)  

1. Python script full of errors: [web-link](https://www.cdslab.org/recipes/programming/python-script-full-of-errors/python-script-full-of-errors)  

1. Time required for cooking a refrigerated egg: [web-link](https://www.cdslab.org/recipes/programming/time-to-cook-frozen-egg/time-to-cook-frozen-egg)  

1. Python dictionary of class members: [web-link](https://www.cdslab.org/recipes/programming/python-dictionary-of-class-members/python-dictionary-of-class-members)

1. Python script call from the Bash command line: [web-link](https://www.cdslab.org/recipes/programming/python-call-script-from-bash/python-call-script-from-bash)  
