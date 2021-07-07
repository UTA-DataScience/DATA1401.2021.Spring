---
title: Functions in Python
tags: [function, python]
keywords: function, python, global, globals
summary: "This note aims at explaining the concepts of functions as program units."
#permalink: /notes/program-units/functions/index.html
last_updated: July 9, 2019
---

## What is a Function?  

In Python, like most other programming languages, **function** is a collection of programming statements that can be executed whenever and wherever requested. Therefore, the definition of function in programming goes far beyond the mathematical definition of the function. For example, programming functions can have no input or output.  

In Python, the syntax of a function is like the following,
```python
def function_name(argument_1, argument_2, ..., argument_N)
    python_statment_1
    python_statment_2
    ...
    return output
```

Here, the line beginning with `def` is referred to as the **function header**, and the statements inside the function are called the **function body**. To use a function, it must be first defined like above and then called where it is needed inside the code.  

### Exercise  

Let's write a Python function that takes in a temperature value in Centigrade and converts it to Fahrenheit.  

```python
def c2f(C):
    return (9.0/5)*C + 32

c_temp = 70.7       # The hottest place on Earth, Lut Desert in Iran 
f_temp = c2f(c_temp)

print("""
The hottest place on Earth as of 2005 is in the Lut Desert in Iran at {0} degrees Celsius.
This corresponds to a temperature of {1} degrees Fahrenheit!
""".format(c_temp,c2f(c_temp)) )
```
    The hottest place on Earth as of 2005 is in the Lut Desert in Iran at 70.7 degrees Celsius.
    This corresponds to a temperature of 159.26 degrees Fahrenheit!


## Function interface  

### Functions with no input arguments  

We can define functions that take no input argument, yet do something predefined for us. Consider the following function which gives information about the Python programming language, when called.  
```python
def get_python_info():
    return "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace."

get_python_info()
```
    'Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.'

<br>

### Functions with no output (return value)  

We can also modify the above function such that it does not return anything specifically.  
```python
def get_python_info():
    print( "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace." )

get_python_info()
```
    Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.

In such cases, you may have already noticed that we can readily skip the `return` statement. In reality, in such cases, what happens is that Python interpreter adds an invisible `return None` statement at the end of the function. `None` is a special reserved keyword of Python that represents **nothing** or **empty data** in Python. It is almost equivalent to the keyword **void** in languages like Java, C, and C++ and mimics the behavior of **subroutine** procedures in the Fortran language.  

```python
def get_python_info():
    print( "Data science is a multi-disciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data." )
    return None
```
```python
get_python_info()
```
    Data science is a multi-disciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data.

If you set a variable equal to this function, the value of the variable will be `None`, because the function returns nothing on the output.  
```python
variable = get_python_info()
type(variable)
print(variable)
```
    NoneType
    None


### Functions with multiple input arguments  

Functions can take almost as many input arguments as we wish. Consider the following,
```python
def power(base,exponent):
    return base**exponent
```
```python
power(2,5)
```
    32

#### The order of input arguments both does and does not matter!  

Note that in the previous code, calling the function with the wrong order of input parameters can lead to a catastrophe and wrong output.  
```python
power(5,2)
```
    25

However, a really cool feature for function input arguments is that, when calling the function, you can also name the argument variable, and if you name them all, then the order by which the arguments appear becomes irrelevant.  
```python
power(exponent=5,base=2)
```
    32

### Functions with multiple output (return values)  

Python functions can return more than one value. For this purpose, tuple variable types become a handy tool. Recall that making a tuple is as simple as writing a sequence of comma-separated values/variable, like the following.  
```python
mytuple = 1, 2
mytuple
type(mytuple)
```
    (1, 2)
    tuple

Now, if you need to write a function that has multiple return value, you can simply return them all in one sequence of comma-separated values/variables. For example, suppose a function takes in two numbers and then outputs the quotient (the result of integer division) and the remainder of the integer division. An example such function would be like the following,
```python
def get_quotient_remainder(dividend,divisor):
    return divmod(dividend,divisor)

get_quotient_remainder(11,3)
```
    (3, 2)

```python
type(get_quotient_remainder(11,3))  # By default, the output is a tuple
```
    tuple

By default, the output of this function is a tuple, since we are returning a tuple in the function. But we could also return the output as a list, or any other appropriate format we wish.  
```python
def get_quotient_remainder(dividend,divisor):
    return list(divmod(dividend,divisor))   # convert the output to list before passing it to main program

type(get_quotient_remainder(11,3))
```
    list

You can also save the output in a variable as well,
```python
def get_quotient_remainder(dividend,divisor):
    return divmod(dividend,divisor)

result = get_quotient_remainder(dividend=11,divisor=3) # You can also name the input variables to make sure you assign them in the correct order.
print(result)
```
    (3, 2)

or save the individual results in separate variables, like,
```python
quotient, remainder = get_quotient_remainder(dividend=11,divisor=3)
print(quotient, remainder)
```
    3 2

or save it in the form of a tuple or list,
```python
[quotient, remainder] = get_quotient_remainder(dividend=11,divisor=3)
print(quotient, remainder)
```
    3 2


### Functions with optional input arguments  

Like many other high-level programming languages, Python allows you to have optional arguments in your input, which you can drop when calling the function. However, an optional argument must have a preassigned value in the function, otherwise dropping the variable at the time of function call will lead to a runtime error.  
```python
def get_quotient_remainder(dividend,divisor=10,message="This is the default message."):
    print( "divmod({},{}) = ".format(divmod(dividend,divisor)) )
    print( message )
    return divmod(dividend,divisor)

result = get_quotient_remainder(dividend=11,divisor=3) # the optional input argument 'message' is set to its default value.
```
    divmod(11,3) = (3, 2)
    This is the default message.

The above function, default the value of optional message argument to `"This is the default message."` since it is not given at the time of calling the function. The function's **optional input arguments** whose values are initialized to a default value are more famously known in Python as **keyword arguments**.

Note that when the optional arguments are named and assigned a value at the time of function call, then their order of appearance in the function call does not matter. Keep in mind that the **ordinary** or **positional** arguments should all appear in order and first before the keyword arguments appear. However, the keyword arguments can appear in any order one may wish.
<br>

For the above example function, the following function calls would be valid,
```python
get_quotient_remainder(dividend=11)
get_quotient_remainder(11,divisor=3)
```

and the following would be invalid,
```python
get_quotient_remainder(divisor=3,11,message="A new message.")   # This is invalid
```
      File "<ipython-input-36-27658299aa76>", line 1
        get_quotient_remainder(divisor=3,11,message="A new message.")   # This is invalid, the order is incorrect.
                                        ^
    SyntaxError: positional argument follows keyword argument

```python
get_quotient_remainder(11,divisor=3, "A new message.")   # Also invalid, all arguments after the first named-argument must appear with name as well.
```
      File "<ipython-input-37-1643cc8d6910>", line 1
        get_quotient_remainder(11,divisor=3,"A new message.")
                                           ^
    SyntaxError: positional argument follows keyword argument

Note that the keyword arguments must be always listed after the positional arguments in the function definition. Note also, as in the above examples, that the sequence of input arguments **at the time of function call** does not matter, so long as the names of all positional and keyword arguments are provided in the function call.

Note also, that the number input arguments at the time of call must be exactly the same as the number of arguments in the function definition.
```python
get_quotient_remainder(11,3, "A new message.",)  # THis works even though, there is an extra comma at the end of the arguments of the function call.
```
    divmod(11,3) = (3, 2)
    A new message.
    
    (3, 2)

<br>

## Local and global variables in functions  
Variables that are defined inside of a function, are by default invisible outside the function scope. For example, let's consider  Let us reconsider the original function defined at the beginning of the lecture, which takes in a temperature value in Centigrade and converts it to Fahrenheit.  
```python
def c2f(C):
    converted_value = (9.0/5)*C + 32
    return converted_value
```

Now, if the variable `converted_value` is called outside the function, it will result in a syntax error since it is undefined outside the function scope.
```python
c2f(70)
```
    158.0

```python
converted_value
```
    NameError                                 Traceback (most recent call last)
    <ipython-input-42-1aa75d9b79c4> in <module>()
    ----> 1 converted_value
    
    NameError: name 'converted_value' is not defined

Local variables are created inside a function and destroyed when the program control goes back to the main code, outside the function.

Now suppose we had the following script,  

```python
def c2f(C):
    converted_value = (9.0/5)*C + 32
    print('Value of C inside function c2f: {}'.format(C))
    return converted_value

C = 70
c2f(50)
print('Value of C outside function c2f: {}'.format(C))
```
    Value of C inside the function c2f: 50
    Value of C outside function c2f: 70

Clearly, the two values are not the same, even though the variable names are the same. But, if you really want to access the global variable `C` inside of the function, then you will have to use Python's `global` keyword inside the function **before declaring or using the variable** `C`,  

```python
def c2f():
    global C
    C = 50
    converted_value = (9.0/5)*C + 32
    print('Value of C inside function c2f: {}'.format(C))
    return converted_value

C = 70
print('Value of C before calling function c2f: {}'.format(C))
c2f()
print('Value of C outside function c2f: {}'.format(C))
```
    Value of C before calling function c2f: 70
    Value of C inside function c2f: 50
    Value of C outside function c2f: 50

In Python, the `global` keyword allows you to modify a variable beyond the scope (i.e., function) within which the variable is defined and used. The basic rules regarding the scope of the definitions of variables and the usage of global keyword in Python include the following,  

- A variable inside a function has local scope by default, meaning that it is only defined and accessible within that function.
- If a variable is defined outside of a function in the main Python programming environment, it has the global scope by default without the use of the `global` keyword, meaning that it can be accessed from everywhere (if needed). Note that the use of the `global` keyword outside a function has no effects.
- Use `global` keyword to manipulate the value of a global variable inside a function.


In the above example, you can also use Python's built-in function `globals()` which returns a **dictionary** of all global variables in the main program, and then use the key `'C'` to get its value inside the function.
```python
type(globals())
```
    dict

```python
globals()['C']
```
    70

Now, the same function as above, but with the global variable value would give you,
```python
def c2f(C):
    converted_value = (9.0/5)*globals()['C'] + 32
    print('Value of C inside function: {}'.format(globals()['C']))
    return converted_value

C = 70
c2f(50)
print('Value of C outside function: {}'.format(C))
```
    Value of C inside the function: 70
    Value of C outside function: 70

As a general rule, when there are <b>several variables with the same name</b>, Python interpreter <b>first</b> tries to look up the variable name among the <b>local variables</b>, <b>then</b> there is a search among <b>global variables</b>, and <b>finally</b> among built-in <b>Python functions</b>.

In order to declare a variable inside the function global, use the keyword `global` as in the following,
```python
a = 20; b = -2.5 # global variables
def f1(x):
    a = 21 # this is a new local variable
    return a*x + b

print (a) # yields 20

def f2(x):
    global a
    a = 21 # the global a is changed
    return a*x + b

f1(3); print (a) # 20 is printed
f2(3); print (a) # 21 is printed
```
    20
    20
    21

Note that in function `f1`, $a = 21$ creates a local variable a. One may think the global `a` has changed, but it does not happen. However, in the second function `f2`, the globally declared variable is assigned a new value and therefore, the global value of `a` outside the function also changes. Test this script yourself and see what you get.  

> Be careful with using global variables inside your functions, because if you do not define them prior to using the function, then you get a runtime error.

Here is an example of the error,
```python
def f2(x):
    global a    # a must be defined outside the function prior to the function call
    return a*x + b

f2(3)
```
    NameError                                 Traceback (most recent call last)
    <ipython-input-55-ea6f63a0f6d6> in <module>()
        3     return a*x + b
        4 
    ----> 5 f2(3)
    
    <ipython-input-55-ea6f63a0f6d6> in f2(x)
        1 def f2(x):
        2     global a    # a must be defined outside the function prior to function call
    ----> 3     return a*x + b
        4 
        5 f2(3)
    
    NameError: name 'a' is not defined

### Avoid function side-effects

A function in which the value of a global variable is changed while the global variable is not the intended output of the function is called a **function with side-effects**. Here is an example,
```python
def f2(x):
    global a
    a = 21 # the global a is changed
    return a*x + b
```

In general, any *lasting effect* that occurs in a function, but not through its `return` value, is called a **side effect**. There are three ways to have side effects:
- Changing the value of a mutable object.
- Changing the binding (the storage space) of a global variable.
- Printing out a value. This doesn’t change any objects or variable bindings, but it does have a potentially lasting effect outside the function execution because a person might see the output and be influenced by it.

In general, avoid defining functions that have side-effects. In large codes and projects, side-effects can create complex semantic errors and become a hurdle for optimization and code debugging.

<br>

## Python's built-in functions

Python has a number of built-in functions, which can be handy. [Here](https://docs.python.org/3/library/functions.html) is a list of Python's built-in functions along with a description of what they do.  


## Function docstring

There is a convention in Python to insert a documentation string right after the `def` line of the function definition (the function header). The documentation string, known as a **doc string** or **docstring**, should contain a short description of the purpose of the function and explain what the different arguments and return values are. Docstrings are usually enclosed in triple-double quotes `"""`, which allow the string to span several lines.
```python
def c2f(C):
    """
    This function converts Celsius degrees (C) to Fahrenheit.
    Uses global variable C.
    """
    converted_value = (9.0/5)*globals()['C'] + 32
    print('Value of C inside function: {}'.format(globals()['C']))
    return converted_value
```

The docstring is then stored in `__doc__` attribute of the function, and can be called like the following,
```python
c2f.__doc__
```
    '\n    This function converts Celsius degrees (C) to Fahrenheit.\n    Uses global variable C.\n    '

If you'd like to get the formatted docstring, use Python's `help()` function,
```python
help(c2f)
```
    Help on function c2f in module __main__:
    
    c2f(C)
        This function converts Celsius degrees (C) to Fahrenheit.
        Uses global variable C.

One can also use `"` in place of `"""`, although less conventional. But then for multiple lines of docstring, one has to use line continuation. 
```python
def c2f(C):
    "\
    This function converts Celsius degrees (C) to Fahrenheit.\
    Uses global variable C.\
    "
    converted_value = (9.0/5)*globals()['C'] + 32
    print('Value of C inside function: {}'.format(globals()['C']))
    return converted_value
```
Note that the docstring must appear before any statement in the function body.

## Functions as input arguments to functions

In happens frequently in scientific programming, that a function needs to use another arbitrary function provided by the user to perform some specific tasks with it inside the function. For example, programs doing calculus frequently need to have functions as arguments in functions. For example,
- a Python function that finds the root of a mathematical function, given as input argument.
- a Python function that differentiates of a mathematical function, given as input argument.
- a Python function that integrates a mathematical function, given as input argument.
- a Python function that solves a mathematical differential equation, given as input argument.

In such cases, Python functions need to have the mathematical function as an input argument with some name(e.g., `func`). Like Fortran, this is straightforward in Python and hardly needs any explanation, but in most other languages special constructions must be used for transferring a function to another function as argument. For example, suppose we want to compute numerically the second-derivative of a user given mathematical function,

```python
def diff2nd(func, x, h=1E-6):
    r = (func(x-h) - 2*func(x) + func(x+h))/float(h*h)
    return r
```
The `func` input argument is like any other argument, i.e., a name for an object, here a function
object that we can call as we normally call functions. An an application, suppose we want to calculate the second derivative of a quadratic function $g(x)$ of the following form at $x=2$,
```python
def diff2nd(func, x, h=1E-6):
    r = (func(x-h) - 2*func(x) + func(x+h))/float(h*h)
    return r

def g(x):
    return x**2 + 4.0*x + 1.0

x = 2
diff2nd_g = diff2nd(g, x)
print ( "g’’(x=%f)=%f" % (x, diff2nd_g) )
```
    g’’(x=2.000000)=2.001954

## Function composition

The ability to call one function from within another function is called **composition**. Suppose we have a function `distance` that calculates the distance between two points on a 2D plane. and another function that takes in value for radius, and then calculates the corresponding area for that radius.
```python
def distance(x1, y1, x2, y2):
    from math import sqrt
    return sqrt( (x2-x1)**2 + (y2-y1)**2 )

def area(x1, y1, x2, y2):
    from math import pi
    return pi*distance(x1, y1, x2, y2)**2

area(0.0,0.0,0.0,1.0)
```
    3.141592653589793

### Recursive functions

Now, note that the function being-called inside the other does not necessarily have to be a different function. It could be the same function calling itself repeatedly, **until a condition is met** (otherwise this would be an endless function call to itself for eternity). For example, a function that would calculate the factorial of an input integer would be like the following,
```python
def factorial(n):
    if isinstance(n,float):
        print('The input number {} is not an integer!'.format(n))
        return None
    if n==0:
        return 1
    elif n==1:
        return n
    else:
        return n*factorial(n-1)

factorial(4)
factorial(4.5)
```
    24
    The input number 4.5 is not an integer!

## Lambda functions  

There is a quick one-line construction of functions that is often convenient to make Python code compact. For example, recall how we defined `g(x)` in the [example above](#functions-as-input-arguments-to-functions). Here is a compact version of it,
```python
g = lambda x: x**2 + 4.0*x + 1.0
```

This code is equivalent to the original code that wrote before,
```python
def g(x):
    return x**2 + 4.0*x + 1.0
```

In general, a function of the form,
```python
def g(arg1, arg2, arg3, ...):
    return expression
```

can be converted to the compact form,
```python
g = lambda arg1, arg2, arg3, ...: expression
```

Lambda functions are very useful for defining simple functions in the argument list that is passed to another function. For example, recall our `diff2nd` function that we defined in the above,
```python
def diff2nd(func, x, h=1E-6):
    r = (func(x-h) - 2*func(x) + func(x+h))/float(h*h)
    return r

def g(x):
    return x**2 + 4.0*x + 1.0

x = 2
diff2nd_g = diff2nd(g, x)
print ( "g’’(x=%f)=%f" % (x, diff2nd_g) )
```
    g’’(x=2.000000)=2.001954

Now instead of defining `g(x)` separately when calling `diff2nd` function, we can use the following compact form,
```python
def diff2nd(func, x, h=1E-6):
    r = (func(x-h) - 2*func(x) + func(x+h))/float(h*h)
    return r

x = 2
print ( "g’’(x=%f)=%f" % (x, diff2nd(lambda x: x**2 + 4.0*x + 1.0, x) ) )
```
    g’’(x=2.000000)=2.001954

Lambda functions may also take **keyword arguments**. For example,
```python
d2 = diff2nd(lambda t, A=1, a=0.5: -a*2*t*A*exp(-a*t**2), 1.2)
```

This format is particularly useful, if the lambda function contains a constant that is repeatedly used in the expression of the function, the value of which may need to be updated in future runs of the code, or later on in the same code.  

## Generator functions  

We have already seen in the above examples, that the returned object of a function can be of any type or size. However, imagine a scenario where your function takes the path to an exteremely large input file, then aims to reads the contents of the file. Given the size of the file, it is likely that the process will be either very slow or impossible, if the computing device does not have enough memory to hold all of the contents of the file and pass a copy of it to the user. The solution in such scenarios, is to use a **generator function**, which instead of **return**ing all of the contents of a collection, it returns one element of it at a time. Consider the following example, 

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('amir'):
    print(char)
```
    r
    i
    m
    a

Notice the use fo the keyword `yield` in the above example instead of `return`. This leads the function to **yield** a generator and pass it to the user so that it can be called to fetch one value from the input collection. We could have also achieved the same functionality of the above function generator using a normal function,  

```python
def reverseOriginal(data):
    reverseData = []
    for index in range(len(data)-1, -1, -1):
        reverseData.append(data[index])
    return reverseData
for char in reverseOriginal('amir'):
    print(char)
```
    r
    i
    m
    a

However, the generator function will be far more efficient in terms of memory requirements and speed.  


## Exercise  

1. Check if number is even in one line function definition: [web-link](https://www.cdslab.org/recipes/programming/one-line-check-even-number/one-line-check-even-number)  

1. Computing the area of a triangle: [web-link](https://www.cdslab.org/recipes/programming/triangle-area/triangle-area)  

1. Getting the largest prime number smaller than the input value: [web-link](https://www.cdslab.org/recipes/programming/largest-prime-number-smaller-than-input/largest-prime-number-smaller-than-input)  

1. Checking if an input is a prime number (via recursive function calls)?: [web-link](https://www.cdslab.org/recipes/programming/isprime-recursive/isprime-recursive)  

1. Computing the Fibonacci sequence via recursive function calls: [web-link](https://www.cdslab.org/recipes/programming/fibonacci-sequence-via-recursive-function-calls/fibonacci-sequence-via-recursive-function-calls)  

1. Finding the maximum value of an array via recursive function calls: [web-link](https://www.cdslab.org/recipes/programming/finding-maximum-value-via-recursive-function/finding-maximum-value-via-recursive-function)  

1. Finding the position of the maximum value of an array via recursive function calls: [web-link](https://www.cdslab.org/recipes/programming/finding-maximum-location-via-recursive-function/finding-maximum-location-via-recursive-function)  
