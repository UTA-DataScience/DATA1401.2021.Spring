---
title: Encapsulation
tags: [object, class, encapsulation, data_hiding, object_oriented_programming, python]
keywords: object, class, encapsulation, data hiding, object_oriented_programming, python
summary: "This note provides a brief review of the notion of encapsulation and data hiding in Object-Oriented Programming (OOP) paradigm via Python."
#permalink: /notes/object-oriented-programming/encapsulation/index.html

last_updated: June 30, 2020
---

## Encapsulation and data hiding  

Classes can be used for many purposes in scientific programming and computation. One of the most frequently encountered tasks is to represent mathematical functions that have a set of parameters in addition to one or more independent variables. These functions, together with all of their essential and auxiliary variables have to be frequently passed to other functions to perform some tasks. Implementing such problems using purely procedural programming tools that we have learned so far can lead to the development of an unsafe, unclean, and undesired codebase, which is not easy to work with either. To understand why and how this happens, consider the following scientific problem.

## A common programming challenge in numerical computing  

Consider a function that takes in some parameters as input, for example, the equation of motion of a stone thrown upward in the air. The physics equation describing this motion is $y(t) = v_0t-\frac{1}{2}gt^2$. This equation gives the position $y$ from the ground as a function of time. Therefore, in physics, $y$ is viewed as a function of $t$.  

Mathematically speaking, however, $y$ also depends on two other parameters, $v_0$ and $g$, although it is unnatural to view $y$ as a function of these parameters. One can therefore write $f(t;v_0,g)$ to emphasize that $t$ is the independent variable, while $v_0$ and $g$ are the parameters of the projectile motion model that we have proposed in the above. Strictly speaking, $g$ is a fixed parameter (as long as the experiment is done on the surface of the earth), so only $v_0$ and $t$ can be arbitrarily chosen in the formula.  

It would then be better to write $y(t;v_0)$. Here is an implementation of this function,  
```python  
def getHeight(time,initVelocity):
    gravityConstant = 9.81
    return initVelocity * time - 0.5*gravityConstant*time**2
```  

```python  
getHeight(1,10)
```  
    5.095  

This function gives the height of the projectile as a function of time. Now suppose we want to differentiate height ($y(t)$) with respect to time ($t$) in order to obtain the velocity at the given moment in time. We could write the following generic code for differentiation to do so,  
```python
def getDiff(getFunc, x, deltaX = 1.e-5):
    return ( getFunc(x+deltaX) - getFunc(x) ) / deltaX
```

But, here is the catch with this problem of differentiation. The `getDiff()` function works with any function `getFunc()` that takes **only** one argument. In other words, if we want to input `getHeight()` to `getDiff()`, then we will have to redefine `getHeight()` so that it takes only one argument.  You may wonder why not change `getDiff()`. For this simple problem, this could be a solution. But, for larger problems, you are more likely to use the sophisticated routines and modules that have been already developed by the community. Many of these routines and libraries are not aware of the specific problem that you are dealing with. Therefore, they write generic library functions that take an input function with a specific interface, in this case, a differentiation function that takes an input differential function that only has one input parameter. This situation is frequently encountered in the case with high-performance integration routines.  

One, perhaps bad, solution to the above problem is to use **global variables**. To do so, we can define a **wrapper** function that wraps around `getHeight()` and hides the extra input parameter `initVelocity` from the view of `getDiff()`,  
```python  
# wrapper function for getHeight
def getHeightWrapper(time):
    return getHeight(time,initVelocity)
```  

This function will work only if `initVelocity` is a global variable, initialized before any attempts to call the function `getHeightWrapper()`. Here is an example call where `getDiff()` differentiates y,  
```python
initVelocity = 10 # note that initVelocity has be passed globally
getHeightWrapper(1)
```
    5.095  

Now, we can pass this wrapper function to `getDiff()` to take its derivative with respect to time,  
```python
initVelocity = 10 # note that initVelocity has be passed globally
getDiff(getHeightWrapper,1)
```
    0.18995094990259528  

The use of global variables is generally considered bad programming. Why global variables are problematic in the present case can be illustrated when there is a need to work with several versions of a function. Suppose we want to work with two versions of `getHeight(time,initVelocity)`, one with `initVelocity=10` and one with `initVelocity=5`. Every time we call `getHeight()`, we must remember which version of the function we work with, and set `initVelocity` accordingly prior to the call,  
```python  
initVelocity = 10
print( getDiff(getHeightWrapper,1) )
initVelocity = 5
print( getDiff(getHeightWrapper,1) )
```  
    0.18995094990259528  
    -4.810049050085752  

Another problem is that the variable names such as `initVelocity` are now exposed in the code and could potentially overwrite (or get overwritten by) some other variables. In the best case scenario, such name clashes will cause a syntax or runtime error, but frequently, they go unnoticed in the code causing the program to yield wrong results which, depending on the context in which they occur, [could be devastating](https://en.wikipedia.org/wiki/Mariner_1).

Another major problem with global variables is that they could cause **side effects**. For example, if the value of `initVelocity` is mistakenly changed inside the function `getHeight()` it will remain unnoticed and **the change affects other parts of the program in an unintentional way**. This is one reason why a golden rule of programming tells us to **limit the use of global variables as much as possible**.  

**So, is there a good remedy?** The answer is yes: the class concept solves all the problems described above.  

### Class representation of a function  

A class contains a set of variables (data) and a set of functions, held together as one unit. The variables are visible in all the functions in the class. That is, we can view the variables as “global” in these functions. These characteristics also apply to modules, and modules can be used to obtain many of the same advantages as classes offer. However, classes are technically very different from modules. You can also make many copies of a class, while there can be only one copy of a module. When you master both modules and classes, you will clearly see the similarities and differences. Now we continue with a specific example of a class.  

Consider the function $y(t;v_0) = v_0t - \frac{1}{2}gt^2$. We may say that $v_0$ and $g$, represented by the variables `initVelocity` and `gravityConstant`, constitute the data. A Python function, say `getHeight(time)`, is then needed to compute the value of $y(t;v_0)$ and this function must have access to the data `initVelocity` and `gravityConstant`, while `time` is an argument. A programmer experienced with classes will then suggest collecting the data `initVelocity` and `gravityConstant`, and the function `getHeight(time)`, together as a **class**.  

A class usually has another function, called **constructor** for **initializing the data**. The constructor is always named `__init__`. Every **class must have a name**, often **starting with a capital** letter. For our problem here, we can choose `Projectile` as the name of the class since it represents a (vertical) projectile motion. The next step is to implement this class in Python. A complete class code `Projectile` for our problem here in Python could look like the following,  
```python
class Projectile():

    gravityConstant = 9.81

    def __init__(self, initVelocity):
        self.initVelocity = initVelocity

    def getHeight(self,time):
        return self.initVelocity * time - 0.5 * self.gravityConstant * time**2
```

**A class creates a new data type**, here of name `Projectile`, so when we use the class to make objects, those objects are of type `Projectile()`. **All the standard Python objects, such as lists, tuples, strings, floating-point numbers, integers, ..., are built-in Python classes**, and each time the user creates on these variable types, one instance of these classes is created by the Python interpreter. A user-defined object class (like Y) is usually called an **instance**. We need such an instance in order to use the data in the class and call the value function. The following statement constructs an instance of `Projectile()` bound to the variable named `projectile`,  
```python  
projectile = Projectile(initVelocity=10)
```  

Seemingly, we *call the class `Projectile()` as if it were a function*. Indeed, `Projectile(3)` is automatically translated by Python to a call to the constructor `__init__()` in class `Projectile`. The arguments in the call, here `initVelocity`, are always passed on as arguments to `__init__()` after the `self` argument. That is, `initVelocity` gets the value `10` and `self` is just dropped in the call. This may be confusing, but it is a rule that the `self` argument is never used in calls to functions in classes. With the instance `projectile`, we can compute the value of y(t=0.1;v_0=10) by the statement,  
```python  
height = projectile.getHeight(0.1)
print(height)
```  
    0.95095

Note that the `self` input argument is dropped in the call to `getHeight()`. To access functions and variables in a class, one must prefix the function and variable names by the name of the instance and a dot: the value function is reached as `projectile.getHeight`, and the variables are reached as `projectile.initVelocity` and `projectile.gravityConstant`. One could, for example, print the value of `initVelocity` in the instance `projectile` by writing,  
```python  
print(projectile.initVelocity)
```  
    10

We have already introduced the term **instance** for an object of a specific class. **Functions** in classes are commonly called **methods**, and **variables (data)** in classes are called **data attributes**. Methods are also known as **method attributes**. For example, in our sample class `Projectile` we have two methods or method attributes, `__init__()` and `getHeight()`, two data attributes, `initVelocity` and `gravityConstant`, and four attributes in total (`__init__`, `getHeight`, `initVelocity`, `gravityConstant`). Note that the names of attributes can be chosen freely, just as names of ordinary Python functions and variables. However, **the constructor must have the name `__init__()`, otherwise it is not automatically called when new instances are created**. You can do whatever you want in whatever method, but it is a common convention to **use the constructor for initializing the variables in the class**.  

With this class, we can now call `getDiff()` to take the derivative of the height of the projectile motion we have defined, *without the need to create global variables*,  
```python  
projectile = Projectile(initVelocity=10)
print( getDiff(projectile.getHeight,1) )
```  
    0.18995094990259528

Now, it may seem a bit redundant to type `projectile.getHeight()` to get the height. Amazingly, Python provides a neat shortcut for such instances via the `__call__()` method to create **callable** objects.  

## Callable objects  

If you recall, computing the value of the mathematical function represented by class `Projectile`, with `projectile` as the name of the instance, is performed by writing `projectile.getHeight()`. If we could write just `projectile()`, the `projectile` instance would look like an ordinary function. Such a syntax is indeed possible and offered by the special method named `__call__`,  
```python
class Projectile():

    gravityConstant = 9.81

    def __init__(self, initVelocity):
        self.initVelocity = initVelocity

    def __call__(self, time):
        return self.getHeight(time)

    def getHeight(self,time):
        return self.initVelocity * time - 0.5 * self.gravityConstant * time**2
```

then writing,  
```python  
projectile = Projectile(initVelocity=10)
print(projectile(1))
print(projectile.getHeight(1))
```  
    5.095  
    5.095  

would yield identical results. With this `__call__` method, the `getHeight` method could be even considered as redundant and the class could be written more concisely as,  
```python  
class Projectile():
    gravityConstant = 9.81
    def __init__(self, initVelocity): self.initVelocity = initVelocity
    def __call__(self, time): return self.initVelocity * time - 0.5 * self.gravityConstant * time**2
```  

A good programming convention is to **include a `__call__` method in all classes that represent a mathematical function**. Objects that are instances of classes with `__call__` methods are said to be **callable objects**, just as plain functions are callable objects as well. The call syntax for callable objects is the same, regardless of whether the object is a function or a class instance.  

You can always test if an instance is callable or not by `callable()`,  
```python
projectile = Projectile(initVelocity=10)
callable(projectile)
```
    True  
