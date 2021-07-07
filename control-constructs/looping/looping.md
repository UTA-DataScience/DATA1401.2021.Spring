---
title: Loops and iteration constructs
tags: [for, loop, while, list_comprehension, iteration, dictionary, list, python]
keywords: for, loop, while, list_comprehension, iteration, dictionary, list, python
summary: "This note aims at explaining the concept of iterations and loop constructs in Python."
#permalink: /notes/control-constructs/looping/index.html
last_updated: July 9, 2019
---

## Loops in Python  

We have already seen, both in homework and midterm, what a pain it can be if you wanted to repeat a certain number of tasks using recursive functions and if-blocks. Fortunately, Python has loop statements that can highly simplify the task of repeating certain statements for a certain number of times.  

### While loop  

One such statement is the while-loop:
```python
while this_logical_statement_holds_true : 
    perform_statements
```

For example, here is a code that prints all positive integers smaller than a given input integer,
```python
n = int(input('input a positive integer: '))
print( 'Here are all positive integers smaller than {}'.format(n) )
while n > 1:
    n -= 1
    print(n)
```
    input a positive integer: 7
    Here are all positive integers smaller than 7
    6
    5
    4
    3
    2
    1

Another useful way of writing while-loops is the following (using the example above),
```python
n = int(input('input a positive integer: '))
print( 'Here are all positive integers smaller than {}'.format(n) )
while True:
    n -= 1
    print(n)
    if n == 1: break
```
    input a positive integer: 7
    Here are all positive integers smaller than 7
    6
    5
    4
    3
    2
    1

In this case, the loop will continue forever, unless the condition `n==1` is met at some point during the iteration.  

### For loop  

If you are from a Fortran, C, C++ background you may be already accustomed to counting loops than while loops. Python does not have a direct method for counting loops, however, there is a for-loop syntax that loops over the elements of a list or tuple. For example, if we wanted to rewrite the above code using for-loop, one solution would be like the following,
```python
n = int(input('input a positive integer: '))
print( 'Here are all positive integers smaller than {}'.format(n) )
my_range = range(n-1,0,-1)
for n in my_range:
    print(n)
```
    input a positive integer: 7
    Here are all positive integers smaller than 7
    7
    6
    5
    4
    3
    2
    1

Here the Python's builtin function `range([start,] stop [, step])` creates a list of integer that starts from `start` to `end` *but not including `end`*, with a distance of size `step` between the elements. Here is another way of doing the same thing as in the above example,
```python
n = int(input('input a positive integer: '))
print( 'Here are all positive integers smaller than {}'.format(n) )
mylist = list(range(n-1,0,-1))
for n in mylist:
    print(n)
```
    input a positive integer: 7
    Here are all positive integers smaller than 7
    6
    5
    4
    3
    2
    1

Note how I have used the `range` function in order to get the same output as in the previous example.  
```python
n = int(input('input a positive integer: '))
mylist = list(range(n-1,0,-1))
print(mylist)
```
    input a positive integer: 7  
    [6, 5, 4, 3, 2, 1]

#### ​For-loop with list indices

Instead of iterating over a list directly, as illustrated above, one could iterate over the indices of a list,
```python
mylist = ['amir','jake','lecero','mike','travis']
for i in range(len(mylist)):
    print(mylist[i])
```
    amir
    jake
    lecero
    mike
    travis

Iterating over list indices, instead of list elements, is particularly useful, when you have to work with multiple lists in a for-loop.

#### Manipulating lists using for-loop

Note that when you want to change the elements of a list in a for-loop, you have to change the list itself, and not simply the for-loop variable.
```python
mydigits = [1,3,5,7,9]
for i in mydigits:
    i -= 1
mydigits
```
    [1, 3, 5, 7, 9]
    
The above code won't change the values in the list, instead only the for-loop variable. If you want to change the list itself, you have to operate on the list elements directly,
```python
mydigits = [1,3,5,7,9]
for i in range(len(mydigits)):
    mydigits[i] -= 1
mydigits
```
    [0, 2, 4, 6, 8]

#### List comprehension  

Frequently in Python programming, you may need to create long lists of regularly-ordered item. As a result, Python has a special concise syntax for such tasks, called **list comprehension** which uses for-loop. For example, suppose you have a list of odd digits as in the example above, and you want to create a list of even digits from it. You could achieve this using the following simple syntax,  

```python
odd_digits = [1,3,5,7,9]
even_digits = [i-1 for i in odd_digits]
even_digits
```
    [0, 2, 4, 6, 8]

#### Simultaneous looping over multiple lists

Suppose you have two or more lists of the same length over the elements of which you want to perform a specific set of tasks simultaneously. To do so, it suffices to create a **list of tuples** using Python's builtin function `zip` and loop over the tuple elements of this list. For example, let's assume that you wanted to create a list of the addition of individual elements in the above two lists: `odd_digits` and `even_digits`. One way to do it would be the following,  

```python
sum_even_odd = []
for i,j in zip(odd_digits,even_digits):
    sum_even_odd.append(i+j) 
sum_even_odd
```
    [1, 5, 9, 13, 17]

#### ​Looping over dictionary items  

Dictionaries in Python are composed on key-value pairs, therefore looping over them is slight different than looping over lists,  

```python
name_dict = {'amir':'teacher','jake':'student','lecero':'student','mike':'student','travis':'student'}
for key, value in name_dict.items():
    print( "{0} is a {1}.".format(key,value) )
```
    amir is a teacher.
    jake is a student.
    lecero is a student.
    mike is a student.
    travis is a student.

Here in order to extract the key-value pairs from inside the dictionary, we have used the `items()` method belonging to dictionary objects in Python.  


## Exercise

1. The while-loop implementation of for-loop: [web-link](https://www.cdslab.org/recipes/programming/while-loop-to-for-loop/while-loop-to-for-loop)  

1. Modifying the index of a for-loop: [web-link](https://www.cdslab.org/recipes/programming/modifying-loop-index-value/modifying-loop-index-value)  

1. Impact of machine precision on numerical computation: [web-link](https://www.cdslab.org/recipes/programming/precision-error-paradox/precision-error-paradox)  

1. Impact of round-off errors on numerical computations: [web-link](https://www.cdslab.org/recipes/programming/roundoff-error-paradox/roundoff-error-paradox)  

1. String concatenation using for-loop: [web-link](https://www.cdslab.org/recipes/programming/string-concatenation-using-for-loop/string-concatenation-using-for-loop)  

1. Computing the Fibonacci sequence via for-loop: [web-link](https://www.cdslab.org/recipes/programming/fibonacci-sequence-via-for-loop/fibonacci-sequence-via-for-loop)  


