---
title: Values in Python
tags: [value, type, Python]
keywords: value, type, Python
summary: "This note aims at introducing the basic value types in Python."
#permalink: /notes/values-variables-types/values/index.html
last_updated: July 9, 2019
---


<a name="python-values-types"></a>
## Values and their types in Python
Values are one of the most fundamental entities in programming. Like any other language, a value in Python can be of different types, most importantly **Numeric** (plain integer, long integer, float (real number), complex), **Boolean** (logical) which is a subtype of Numeric, or **String**.  

The following are a few example arithmetic operations with values in Python. You can perform very simple arithmetic on the Python command line, and the result immediately by pressing `enter`.  

```python
2 + 5 # Just typing some comment on the Python command line. Anything after # is a comment and will be ignored.
```
    7

```python
2 - 7 # difference
```
    -5

```python
2 * 7 # product
```
    14

<a name="python-values-types-function"></a>
### Obtaining the type of a value  

You can use the Python's built-in function `type` to get the type of a value in Python (Of course, this is somewhat obvious and redundant for a value input as we already readily know the type of a value).  

```python
type(2*7) # type function gives you the type of the input object to function "type"
```
    int
```python
type('This is a Python string') # a string value in Python
```
    str

```python
type("This is a Python string") # you can also use quotation marks for representing string values, but keep in mind to be consistent!
```
    str

```python
type(True) # type of a boolean True value
```
    bool

```python
type(True) # type of a boolean False value
```
    bool

<a name="python-values-types-coercion"></a>
### Value coercion in Python  
Value coercion is the **implicit** process by which the Python interpreter/compiler automatically converts a value of one type into a value of another type when that second type is required by the surrounding context. For example:  

```python
2.0 * 7 # Note that the product of float and integer is coerced into a float.
type(2.*7)
```
    14.0
    float

```python
2 / 7 # floating point division (in Python 3!).
```
    0.2857142857142857


> In Python 2, the above division would give you 0, that is, in Python 2, the division operator performs an <i>integer division</i>  for two input integer operands. I recommend you to always coerce the result into float (if a float is what you demand) by adding a decimal point to one of the operands in your operation.

<!--
<div class="center">
    <div class="rcbox" style="text-align:center">
        <b>ATTENTION: Python 2 Alert!</b><br><br>
        In Python 2, the above division would give you 0, that is, in Python 2, the division operator performs an <i>integer division</i> for two input integer operands.
        <br><br>
        <b>
        I recommend you to always coerce the result into float (if float is what you demand) by adding a decimal point to one of the operands in your operation.
        </b>
    </div>
</div>
-->

```python
2.0 / 7 # Also floating point division
```
    0.2857142857142857

```python
2 // 7 #  integer division, or floor division
```
    0

```python
2.0 // 7.0
```
    0.0

```python
12 // 7 #  another integer division, or floor division
```
    1

```python
12.0 // 7 #  Also an integer division, or floor division, BUT NOTE THAT the output is now a real number 
```
    1.0

## Mathemtical and logical operations in Python  

### Summary of difference in division between Python 2 and Python 3
Note that there is a difference between Python 2 and 3 for **integer division**.  

#### Python 2  
**input:**  
```python
print 'Python', python_version()
print '3 / 2 =', 3 / 2
print '3 // 2 =', 3 // 2
print '3 / 2.0 =', 3 / 2.0
print '3 // 2.0 =', 3 // 2.0
```

**output:**  
```
Python 2.7.6
3 / 2 = 1
3 // 2 = 1
3 / 2.0 = 1.5
3 // 2.0 = 1.0
```

#### Python 3  
**input:**  
```python
print('Python', python_version())
print('3 / 2 =', 3 / 2)
print('3 // 2 =', 3 // 2)
print('3 / 2.0 =', 3 / 2.0)
print('3 // 2.0 =', 3 // 2.0)
```  
<br>
**output:**  
```  
Python 3.5.2
3 / 2 = 1.5
3 // 2 = 1
3 / 2.0 = 1.5
3 // 2.0 = 1.0
```  

In other words, in **Python 3**, 3 / 2  performs a **floating point division**, whereas in **Python 2**, 3 / 2  performs a **floor division**, also called **integer division**.  

If you want to get the Python version you are using, use the following commands. The first command imports from the Python <b>platform</b> module, the command <b>python_version</b>. Later on, we will discuss what Python modules are and how and why you should use them.

<!--
<div class="center">
    <div class="rcbox" style="text-align:center">
        <b>NOTE</b><br><br>
        If you want to get the Python version you are using, use the following commands. The first command imports from the Python <b>platform</b> module, the command <b>python_version</b>. Later on, we will discuss what Python modules are and how and why you should use them.
    </div>
</div>
-->

```python
from platform import python_version
python_version()

```
    '3.5.2'

```python
2**7 # This is an exponentiation operation. The notation is taken from Fortran exponentiation
```
    128

```python
2.0**7 # This is float exponentiation.
```
    128.0

```python
2**7.0 # ATTN: Avoid this format, if not necessary.
```
    128.0

```python
12 % 7  # This is a remainder operation
```
    5

```python
12.0 % 7 # Another remainder operation, with its result coerced into a float
```
    5.0

### Some useful built-in operations/functions in Python  

```python
pow(2,7) # same operation as 2**7. This is the same exponentiation function as in C language.
```
    128

```python
pow(2.0,7) # same thing but now the result is coerced into a float
```
    128.0

```python
abs(-999) # absolute value
```
    999

```python
int(-999.9) # removes the decimal points and keeps the integer part
```
    -999

```python
int(999.9) # removes the decimal points and keeps the integer part
```
    999

```python
complex(-999.9) # complex number with real part -999.9 and no (zero) imaginary part
```
    (-999.9+0j)

```python
complex(-999.9, 2) # complex number with real part -999.9 and imaginary part value of 2
```
    (-999.9+2j)

```python
complex(-999.9, 2).conjugate() # the conjugate of the complex number
```
    (-999.9-2j)

```python
type(complex(-999.9, 2).conjugate()) # type function can take complex arguments as input!
```
    complex

```python
divmod(5, 2.0) # gives out the pair (x // y, x % y)
```
    (2.0, 1.0)

```python
type(divmod(5, 2.0)) # the type of output from divmod
```
    tuple

<a name="python-order-of-operation"></a>
### Order of operations in Python  

The order of operation in Python is pretty much the same as in any other sane language: **anything inside Paratheses** has precendence over **Exponentiation (\*\*)** has precedence over **Multiplication & Division (/ & *)** has precedence over **Addition & Subtraction (+ & -)**. In abbreviation, the rule of operation precendence is **PEMDAS**.  

```python
print("3 + 2.0 - 3 * 2 / 3 =",3 + 2.0 - 3 * 2 / 3)
```
    3 + 2.0 - 3 * 2 / 3 = 3.0

<a name="python-string-operation"></a>
### Operations on string values in Python  

You can concatenate strings in Python just like **adding** numbers together. Also, you can **multiply** string values by a number, to get mutiple copies of the string value.  

```python
'Amir ' + 'Shahmoradl ' + 'is my full name!' # You can add strings together just like numbers. This is called string concatenation.
```
    'Amir Shahmoradl is my full name!'

```python
'amir' - 'shahmoradi' # This is meaningless and syntactically invalid in Python
```
    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-41f5035ed36a> in <module>()
    ----> 1 'amir' - 'shahmoradi' # This is meaningless and syntactically invalid in Python
    

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

```python
'amir ' * 5 + 'is 5 amirs concatenated!' # multiplying string values by some number
```
    'amir amir amir amir amir is 5 amirs concatenated!'

```python
'amir ' * 's' # meaningless
```
    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-11-ddce79744de9> in <module>()
    ----> 1 'amir ' * 'r' # meaningless
    

    TypeError: can't multiply sequence by non-int of type 'str'

```python
'amir' / 's' # also meaningless
```
    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-12-b6e45f1a8ab1> in <module>()
    ----> 1 'amir' / 's' # also meaningless
    

    TypeError: unsupported operand type(s) for /: 'str' and 'str'

<br>
<blockquote>
    <b>COOL FEATURE FOR STRING MANIPULATION</b><br><br>
    Note that string values are like vectors of characters in Python! you can call a specific element of it!  
</blockquote>
<br>

<!--
<br>
<div class="center">
    <div class="rcbox" style="text-align:center">
        <b>COOL FEATURE FOR STRING MANIPULATION</b><br><br>
        Note that string values are like vectors of characters in Python! you can call a specific element of it!  
    </div>
</div>
<br>
-->

```python
'amir'[0] # first letter in the string
```
    'a'

<blockquote>
    <b>NOTE</b><br><br>
    In order to count elements from the end of the string, use negative in the index.
</blockquote>

<!--
<br>
<div class="center">
    <div class="rcbox" style="text-align:center">
        <b>NOTE</b><br><br>
        In order to count elements from the end of the string, use negative in the index.
    </div>
</div>
<br>
-->

```python
'amir'[-2] # the second letter from the end of the string
```
    'i'

```python
'amir'[-2:-3] # you get nothing because of incorrect indices
```
    ''

```python
'amir'[-3:-2] # you get something because of correct indices!
```
    'm'

```python
'amir'[-3] # this is the same as 'amir'[-3:-2] 
```
    'm'

```python
'amir'[-3:] # This outputs the three last letters of the string
```
    'mir'

```python
'amirShahmoradi'[:-3] # This outputs the letters of the string from the beginning up to the fourth letter from the end.
```
    'amirShahmor'

```python
'amirShahmoradi'[::-1] # This outputs ALL the letters in the string in reverse, from the end to the beginning.
```
    'idaromhahSrima'

```python
'amirShahmoradi'[::-2] # This outputs every other letter in the string in reverse, from the end to the beginning.
```
    'iaohhrm'

```python
'amirShahmoradi'[-3:].upper() # This outputs the third last letters of the string
```
    'ADI'

> **A complete list of methods string manipulation**  
> To see the full list of powerfull string methods that can manipulate strings, like the above example, see [this page](https://docs.python.org/2/library/stdtypes.html#string-methods).  

<!--
<div class="center">
    <div class="rcbox" style="text-align:center">
        <b>NOTE: List of string manipulation methods</b><br><br>
        To see the full list of powerfull string methods that can manipulate strings, like the above example, see <a href="https://docs.python.org/2/library/stdtypes.html#string-methods" target="_blank">this page</a>.
    </div>
</div>
<br>
-->

<a name="python-boolean-operations"></a>
### Boolean operations in Python  
As we mentioned before, Boolean types are a subclass of Integers. Boolean operations are essential in branching statements.  

```python
True or False # This is OR logical operation
```
    True

```python
True and False # This is AND logical operation
```
    False

```python
not True # This is not logical operation
```
    False

```python
'amir' is 'amir' # object identity comparison
```
    True

```python
'amir' is not 'Jake!' # negated object identity
```
    True

In addition, to the above operations, there also other more complex Boolean operations in Python, some of which you can study further [here](https://docs.python.org/2/library/stdtypes.html#bitwise-operations-on-integer-types).  


<b> The identity of objects in Python</b><br>
To get the  identity of an object, use Python's built-in <code>id()</code> command. <code>id()</code> is a built-in function in Python 3, which returns the identity of an object. This identity is a unique integer for that object during its lifetime. This unique id is also the address of the object in the device memory. Keep in mind that the object's id might change from one computer to another, from one run to another run.



As per Python standard, two objects with **non-overlapping** lifetimes may have the same id() value.


The bottom line is, compare objects with the `is` operator, only if you want to check whether two object share the same computer memory space, meaning that they are the same objects, but with different values.

<!--
<div class="center">
    <div class="rcbox" style="text-align:center">
        <b>NOTE: Object's identity in Python</b><br><br>
        To get the  identity of an object, use Python's <code>id()</code> command. <code>id()</code> is a built-in function in Python 3, which returns the identity of an object. This identity is a unique integer for that object during its lifetime. This unique id is also the address of the object in the device memory. Keep in mind that the object's id might change from one computer to another, from one run to another run.  
    </div>
</div>
<br>
-->

```python
id('amir')
```
    81758280

```python
id(2)
```
    501744144

```python
id(2) == id(3) # equality operation: tests for the same value
```
    False

```python
id(2) != id(3) # inequality operation
```
    True

> Be very careful with operations <code>is</code> and <code>equality</code> ! These two are not the same! See the examples below.

> 
Note that the return value of id() is dependent on the specific Python implementation that you are using. For example, with some Python implementations, the result of `(1,1) is (1,1)` may be `True` (or as in the above example, `False`.


<!--
<div class="center">
    <div class="rcbox" style="text-align:center">
        <b>ATTENTION</b><br><br>
        Be very careful with operations `is` and `equality` ! These two are not the same! See the examples below.
    </div>
</div>
<br>
-->

```python
(1,1) is (1,1) # Two similar tuples have not the same identifiers in Python! Will soon see what tuples are.
```
    False

```python
(1,1) == (1,1) # Two similar tuples have the same value in Python!
```
    True

<a name="python-boolean-operations-string-comparison"></a>
#### String comparison  
Strings are compared lexicographically using the numeric equivalents in ASCII codes (the result of the built-in Python function `ord()` of their characters.  

```python
'amir' > 'jake' # String comparison. Basically, the character ASCII codes are compared here.
```
    False

```python
'amir' > 'Jake' # 'J' is ahead of 'a' in ASCII characters.
```
    True

```python
'amir' > 'Amir' # 'A' is ahead of (smaller than) 'a' in ASCII characters.
```
    True

```python
'amir' > 'amis' # Comparison is performed is equality for each character holds, until the end is reached.
```
    False

## Exercise

1. Operator precedence: [web-link](https://www.cdslab.org/recipes/programming/operator-precedence/operator-precedence)  

2. Integer overflow: [web-link](https://www.cdslab.org/recipes/programming/integer-overflow/integer-overflow)