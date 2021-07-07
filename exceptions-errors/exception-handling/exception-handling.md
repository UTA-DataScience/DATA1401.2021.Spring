---
title: Exception handling
tags: [exception_handling, try_except, raise, python]
keywords: exception_handling, try_except, raise, python
summary: "This note aims at discussing how to deal with exceptions in Python. An <b>exception</b> is an event which occurs during the execution of a program and disrupts the normal flow of the program's instructions. The process to deal with such exceptional events in the program is called <b>Exception handling</b>."
#permalink: /notes/exceptions-errors/exception-handling/index.html

last_updated: July 9, 2019
---

## What is exception handling  

Good code has to be able to handle exceptional (rare) situations that may occur during the code execution. These exceptions may occur during data input from either command line, terminal window, or an input file. They may also occur as a result of repeated operations on the input data, inside the code. For example, division by zero is an exceptional event in the program that any professionally-written program should be able to catch and handle nicely. Another example can be found in the discussion of **data transfer methods**, where we explained a way of handling a wrong number of input command-line arguments. This and similar measures to handle the unexpected runtime situations that could lead to errors nicely is called **exception handling**.  

**Exception vs. error:**  
There is a distinction between an exceptional situation in a program and an error that is often recognized: In general, an error indicates the occurrence of a serious condition in the code that is unrecoverable. If it happens, it crashes the code. On the other hand, an exception indicates the occurrence of an event which, if not properly taken care of, could lead to a runtime error.  


A simple way of error handling is to write multiple if-blocks each of which handles a specific exceptional situation. In other words, let the code execute some statements, and if something goes wrong, write the program in such a way that it can detect this and jump to a set of statements that handle the erroneous situation as desired.

## The *`try-except`* construct  

A more modern and flexible way of handling such potential errors in Python is through the following Python construction,  
```python
try:
    <Python statements>
except <error type>:
    <Python statements>
```

For example, consider the [following code](cmd_find_primes.py) that finds and outputs a list of all prime numbers that are smaller than the given input integer by the user:
```python
#!/usr/bin/env python
def is_prime(n):
    
    is_prime = True
    
    def is_divisible(n,divisor):
        if n<2*divisor: return False
        if n%divisor==0: return True
        else:
            divisor += 1
            return is_divisible(n,divisor)

    if is_divisible(n,divisor=2): is_prime=False
    return is_prime

def get_primes(n):
    if n == 1:
        return
    else:
        if is_prime(n):
            print(n)
        n -= 1
        get_primes(n)

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

We can rewrite the command-line-argument-parsing section of the above code in the following format to make our code more robust and responsive to handle exceptions that arise due to `ValueError` (e.g., not an integer input),
```python
#!/usr/bin/env python
def is_prime(n):
    
    is_prime = True
    
    def is_divisible(n,divisor):
        if n<2*divisor: return False
        if n%divisor==0: return True
        else:
            divisor += 1
            return is_divisible(n,divisor)

    if is_divisible(n,divisor=2): is_prime=False
    return is_prime

def get_primes(n):
    if n == 1:
        return
    else:
        if is_prime(n):
            print(n)
        n -= 1
        get_primes(n)

if __name__ == "__main__":
    import sys
    if len( sys.argv ) != 2: # check the number of arguments to be exactly 2.
        print('''
    Error: Exactly two arguments must be given on the command line.
    Usage:''')
        print("     ", sys.argv[0], "<a positive integer number>", '\n')
        sys.exit('     Program stopped.\n')
    else:
        try:
            n = int(sys.argv[1])
            print('Here is a list of all prime numbers smaller than {}:'.format(n))
            get_primes(n)
        except ValueError:
            print('The input you entered is not an integer!\n Try again...')
            sys.exit(1)
```

The statement `sys.exit(1)` aborts the program. The whole code can be found in [this file](cmd_find_primes_modern.py). Now if we run the [original code](cmd_find_primes.py) with a non-integer input, we would get the following Python error,
```bash
$ cmd_find_primes.py amir
Traceback (most recent call last):
  File "cmd_find_primes.py", line 34, in <module>
    n = int(sys.argv[1])
ValueError: invalid literal for int() with base 10: 'amir'
```

whereas, if we run the [new revised code](cmd_find_primes_modern.py), the non-integer error is nicely handled by outputting a gentle error message to the user and exiting the program gracefully.  
```bash
$ ./cmd_find_primes_modern.py amir
The input you entered is not an integer!
 Try again...
```

The type of error occurring in the above example was `ValueError`. There can be, however, many other types of errors and exceptions. For this reason, Python has a [built-in list of exceptions](https://docs.python.org/2/library/exceptions.html) that frequently occur in programming, that could be used in dealing with common exceptions in Python programs.  

## The *`raise`* statement  

Instead of the print statement in the above `except` block, Python has a builtin function to handle the error together with an input message from the programmer. For example, the previous code could be modified to the following code,
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
        try:
            n = int(sys.argv[1])
            print('Here is a list of all prime numbers smaller than {}:'.format(n))
            get_primes(n)
        except ValueError:
            raise ValueError('The input you entered is not an integer!\n Try again...')
            sys.exit(1)
```

Executing the [code](cmd_find_primes_raise.py) with wrong input would give,
```bash
$ ./cmd_find_primes_raise.py amir
Traceback (most recent call last):
  File "./cmd_find_primes_raise.py", line 35, in <module>
    n = int(sys.argv[1])
ValueError: invalid literal for int() with base 10: 'amir'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "./cmd_find_primes_raise.py", line 39, in <module>
    raise ValueError('The input you entered is not an integer!\n Try again...')
ValueError: The input you entered is not an integer!
 Try again...
```

A more elegant and cleaner way of handling and outputting the error would be use the following syntax, in [this modified code](cmd_find_primes_raise_as_err.py),
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
        try:
            n = int(sys.argv[1])
            print('Here is a list of all prime numbers smaller than {}:'.format(n))
            get_primes(n)
        except ValueError as err:
            print(err)
            sys.exit(1)
```

With the following output,
```bash
$ ./cmd_find_primes_raise_as_err.py amir
invalid literal for int() with base 10: 'amir'
```

In the statement `except ValueError as err:` one could use `Exception` for all types of errors instead of only `ValueError` exceptions, or use a tuple syntax such as `except (ValueError, IndexError) as err:` to cover these two exceptions.  

There are a lot more that could be done with exception handling in Python, such as [user defined exceptions](https://docs.python.org/3/tutorial/errors.html), whose discussion is out of the scope of our goals in the presented notes here.  

