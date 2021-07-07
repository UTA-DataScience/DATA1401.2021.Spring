---
title: Unit testing
tags: [unit_testing, error_handling, python]
keywords: unit_testing, error_handling, python
summary: "This note aims at providing a brief introduction to the concept of Unit Testing in computer programming and the unit testing frameworks in Python."
#permalink: /notes/exceptions-errors/unit-testing/index.html

last_updated: July 9, 2019
---

## Code verification and unit testing  

In the previous sections we discussed the process of creating modules and collecting all functions in one file as a personal user-defined **Python module** that can be used later. As soon as the list of your codes and functions grow, you will need to have **a unified way of ensuring all your functions work appropriately, regardless of the potential future internal changes that are made to the functions**. This is called **unit testing**: *a software development process in which the smallest testable parts of an application, called **units**, are individually and independently scrutinized for proper operation*. Unit testing can be done manually, but if you have a long list of functions (which you most often have), you'd want to automate the testing process.

The grand goal in unit testing is to reduce the risk of encountering potential problems when running the code in the smallest possible units of the code. This means,  
1. ensuring the code has the **correct behavior** when given the proper input data.  
2. ensuring the **code robustness** to exceptions and invalid input data, meaning that it does not crash when it reaches unexpected situations during the code execution and gracefully handles the error, without interruption.  

Because of the goals for which the unit tests are designed, they are mostly written and used by the developers of the code. 

## Unit test frameworks  

There are many ways to write tests for codes. Now, if you asked each software developer to write a unit test for specific software, each would likely come up with their own set of rules and tests of the software. You will end up with many tests, that will generally only be usable by the developer that wrote the tests. That is why you should select a unit test framework. A unit test framework provides consistency for how the unit tests for your project are written. There are many test frameworks to choose from for just about any language you want to program with, including Python.  

Just like the case for the choice of programming language, almost every programmer has a strong opinion their own as to which test framework is the best. Research what's out there and use the one that meets the needs of your organization (For example, I had once an experienced Python programmer in my computer programming class, who did not like any of the existing unit-testing frameworks in Python and wanted to write his own unit-test from scratch).   

The framework will provide a consistent testing structure to create maintainable tests with reproducible results. From a product-quality and business point of view, those are the most valuable reasons to use a unit test framework. When you write software, you should also think of a quick and simple way to develop and verify your logic in isolation. Once you make sure you have it working solidly by itself, then you can proceed to integrate it into the larger project solutions with great confidence.  

Python offers three unit testing frameworks,
1. [**unittest**](https://docs.python.org/2/library/unittest.html) (Python's standard unit testing framework)  
2. [**nose**](http://nose.readthedocs.io/en/latest/index.html)  
3. [**pytest**](https://docs.pytest.org/en/latest/)  

which automate as much as possible the process of testing all of your codes, whenever required. The last, `pytest` appears to be the most popular unit testing framework as of today.    

## Conventions for test functions  

The simplest way of using the testing frameworks (e.g., pytest or nose) is to write a set of test functions, scattered around in files, such that pytest or nose can automatically find and run all of these test functions. To achieve the goal, the test functions need to follow certain conventions:  
1. The name of a test function starts with `test_`.  
2. A test function cannot take any arguments.  
3. Any test must be formulated as a boolean condition.  
4. An `AssertionError` exception is raised if the boolean condition is `False` (i.e., when the test fails).  
<br>

## Testing function accuracy  

Suppose we have written the following function which runs the Newton's method for solving an algebraic equation of the form $f(x)=0$, and we would like to write a test function that ensures its correct behavior.  
```python
def newton(f, dfdx, x, eps=1E-7):
    n = 0 # iteration counter
    while abs(f(x)) > eps:
        x = x - f(x)/dfdx(x)
        n += 1
    return x, f(x), n
```

Our goal is to write a function that tests the validity of the output of the function for a special case for which we know the results a priori. In the case of the above code, the function output is a not a fixed result, but an approximate float number $x_0$ which satisfies the condition $f(x_0)<\epsilon$ where $\epsilon$ is a prescribed number close to zero. Therefore, we have to first come up with a mathematical test input function to the function `newton`, for which we have calculated the correct answer a priori, and we want to make sure if the above code gives the same answer. Since the output of the function `newton` is a float that depends on the machine precision, we cannot expect the function to output the same result every time the code is run on any computer. Therefore, we have to define our test such that the function passes the test even if the result is not exactly what we expect, but still close enough to the correct answer. Here is an example test function for the above code using the `sin(x)` function as the test input function to `newton()`,
```python
def test_newton_sin():
    
    from math import sin, cos, pi

    def f(x):
        return sin(x)
    
    def dfdx(x):
        return cos(x)
    
    x_ref = 0.000769691024206
    f_x_ref = 0.000769690948209
    n_ref = 3
    x, f_x, n = newton(f, dfdx, x=-pi/3, eps=1E-2)
    tol = 1E-15 # tolerance for comparing real numbers
    assert abs(x_ref - x) < tol , "The test for the value of x_0 failed" # is x correct?
    assert abs(f_x_ref - f_x) < tol , "The test for the function value failed" # is f_x correct?
    assert n == 3 , "The test for the number of iterations failed" # is f_x correct? # is n correct?
```

Note that in the above test function, the function name begins with `test_`, takes no arguments, and raises an `assertionError` at the end. Now if you run the test,  
```python
test_newton_sin()
```

you will notice that the function passed the test. However, if in the above test, we set `eps=1E-10`, and run the test again, you will get an assertion error like the following,  

    ---------------------------------------------------------------------------
    AssertionError                            Traceback (most recent call last)
    <ipython-input-20-8be9faac8d8e> in <module>()
    ----> 1 test_newton_sin()

    <ipython-input-18-263651ba410f> in test_newton_sin()
         14     x, f_x, n = newton(f, dfdx, x=-pi/3, eps=1E-10)
         15     tol = 1E-15 # tolerance for comparing real numbers
    ---> 16     assert abs(x_ref - x) < tol , "The test for the value of x_0 failed" # is x correct?
         17     assert abs(f_x_ref - f_x) < tol , "The test for the function value failed" # is f_x correct?
         18     assert n == 3 , "The test for the number of iterations failed" # is f_x correct? # is n correct?

    AssertionError: The test for the value of x_0 failed

One could also write exact tests for the function `newton` which test for an exact result which is known a priori, for example, a mathematical linear input function to `newton`.  
<br>

## Testing function robustness  

The above `newton` function is very basic and suffers from several problems:  
- for divergent iterations, it will iterate forever,
- it can divide by zero in f(x)/dfdx(x),
- it can perform integer division in f(x)/dfdx(x),
- it does not test whether the arguments have acceptable types and values.  

A more robust implementation dealing with these potential problems would look like the following:
```python
def Newton(f, dfdx, x, eps=1E-7, maxit=100):
    if not callable(f): raise TypeError( 'f is %s, should be function or class with __call__' % type(f) )
    if not callable(dfdx): raise TypeError( 'dfdx is %s, should be function or class with __call__' % type(dfdx) )
    if not isinstance(maxit, int): raise TypeError( 'maxit is %s, must be int' % type(maxit) )
    if maxit <= 0: raise ValueError( 'maxit=%d <= 0, must be > 0' % maxit )
    n = 0 # iteration counter
    while abs(f(x)) > eps and n < maxit:
        try:
            x = x - f(x)/float(dfdx(x))
        except ZeroDivisionError:
            raise ZeroDivisionError( 'dfdx(%g)=%g - cannot divide by zero' % (x, dfdx(x)) )
        n += 1
    return x, f(x), n
```

Now, for this more robust code (than the earlier version: `newton`), we have to also write a set of tests, examining the robustness of the code, subject to potential exceptions. For example, one can write a test function that examines the behavior of `Newton` subject to an input mathematical function that is known to lead to divergent (infinite) iterations, if the initial starting point $x$ is not sufficiently close to the root of the function. One such example is $f(x)=tanh(x)$, for which a starting search value of $x=20$ would lead to infinite iterations in Newton's method. So we can set `maxit=12` in our robust `Newton` code, and test that the actual number of iterations reaches this limit. Given our prior knowledge for this function, that the value of $x$ will also diverge after 12 iterations, we could also add a test for the value of $x$, like the following,
```python
def test_Newton_divergence():
    from math import tanh
    f = tanh
    dfdx = lambda x: 10./(1 + x**2)
    
    x, f_x, n = Newton(f, dfdx, 20, eps=1E-4, maxit=12)
    assert n == 12
    assert x > 1E+50
```
```python
test_Newton_divergence()
```

The example above only tests for the robustness of `Newton()` in handling divergent situations. For other potential problems, one has to write other test functions, some which will be given as exercise.  

## Summary: unit testing  

Unit testing is a component of [test-driven development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development), a pragmatic methodology that takes a meticulous approach to build a product using *continual testing and revision*.  

Unit testing has a steep learning curve. The programmer or the development-team needs to learn what unit testing is, how to unit test, what to unit test and how to use automated software tools to facilitate the process on an on-going basis.  The great benefit to unit testing is that the earlier a problem is identified, the fewer compound errors occur. A compound error is one that doesn't seem to break anything at first but eventually conflicts with something down the line and results in a problem.  

There is a lot more to unit testing and the existing Python frameworks for it than we discussed here. However, covering all those topics would require a dedicated course for unit testing, which is certainly beyond the capacity of this course. But if you are interested to know more, I recommend you to refer to one of the three unit-testing frameworks mentioned [above](#unit-test-frameworks). There are also many books already written on this topic.  
