---
title: Random numbers
tags: [random_numbers, python]
keywords: random_numbers, python
summary: "This note attempts to provide a summary of some of the most widely-used approaches for generating random numbers in Python."
#permalink: /notes/scientific-computing/random-numbers/index.html
last_updated: July 9, 2019

---

## Random numbers in Python  

One of the most important topics in today's science and computer simulation is [random number generation](https://en.wikipedia.org/wiki/Random_number_generation) and [Monte Carlo simulation](https://en.wikipedia.org/wiki/Monte_Carlo_method) methods. In the simplest scenario for your research, you may need to generate a sequence of uniformly distributed random numbers in Python. There are several approaches to handle such random number generation problems in Python. Here is one, via Python's standard `random` module:  

```python
import random as rnd
rnd.random()   # generates a random number in the half open interval [0,1)
```
    0.012519922307372311

```python
rnd.<press tab>
rnd.BPF             rnd.Random          rnd.betavariate     rnd.gauss           rnd.normalvariate   rnd.randrange       rnd.shuffle         rnd.weibullvariate
rnd.LOG4            rnd.SG_MAGICCONST   rnd.choice          rnd.getrandbits     rnd.paretovariate   rnd.sample          rnd.triangular
rnd.NV_MAGICCONST   rnd.SystemRandom    rnd.expovariate     rnd.getstate        rnd.randint         rnd.seed            rnd.uniform
rnd.RECIP_BPF       rnd.TWOPI           rnd.gammavariate    rnd.lognormvariate  rnd.random          rnd.setstate        rnd.vonmisesvariate
```

As you see in the list of available methods in `random`, you can generate random numbers from a wide variaty of univariate probability distributions, e.g.,  

```python
rnd.betavariate(0.5,0.5)   # Beta variate with the input parameters
```
    0.9281984408820623

```python
rnd.expovariate(1)         # random variable from exponential distribution with mean 1.
```
    2.546912414260747

```python
rnd.gammavariate(1,1)      # random variable from gamma distribution with parameters 1,1.
```
    0.5364897808236537

Recall that if you need help on a method or function in Python, you could use `help()`,  

```python
help(rnd.weibullvariate)
```
    Help on method weibullvariate in module random:
    
    weibullvariate(alpha, beta) method of random.Random instance
        Weibull distribution.
    
        alpha is the scale parameter and beta is the shape parameter.

To generate `float` random numbers between the given input bounds,  

```python
rnd.uniform(50,100)    # generate a random float between 50 and 100
```
    65.59688328558263

> Always make sure to import modules with unique names since different modules with similar component names may overwrite each other's objects and methods in your active session of Python. For example <code>import random</code> followed by <code>from numpy import *</code> will cause the <code>random</code> module to be overwritten by <code>numpy.random</code> module.

Also pay attention to sublte differences between similar functions, with the same names, but in different modules. For example,  

```python
import numpy as np
np.random.randint(1,6,1)
```

will draw a random integer from the interval $\[1,6)$ excluding the value $6$ (the third input, $1$, indicates how many numbers has to be drawn randomly by the function). However,  

```python
import random as rnd
rnd.randint(1,6)
```

will draw a random integer form the interval $[1,6]$. Also note that `randint()` from module `random` is a scalar function, whereas the numpy's version is vectorized.  

## The deterministic aspect of randomness in Python  

There is a truth about random numbers and random number generators and algorithms, not only in Python, but in all programming languages, and that is, **true random numbers do not exist in the world of programming**. What we call a sequence of random numbers, is simply a sequence of numbers that we, the user, to the best of our knowledge, don't know how it was generated, and therefore, **the sequence looks random to us, but not the to the developer of the algorithm!**. To prove this, type the following code in a Python session,  

```python
import numpy as np
np.random.seed(42)
np.random.randint(1,6,6)
```
    array([4, 5, 3, 5, 5, 2])

```python
np.random.randint(1,6,6)
```
    array([3, 3, 3, 5, 4, 3])

```python
np.random.seed(42)
np.random.randint(1,6,6)
```
    array([4, 5, 3, 5, 5, 2])

You notice that every time the random function is called, it generates a new sequence of random numbers, apparently completely random. But as soon as the function `np.random.seed(42)` is called, it appears that the random number generator also restarts from the beginning, generating the same sequence of random numbers as it did before.  

You can even test the same code on a different computer, and as long as you set the seed of the random number generator to a specific value (here 42), `np.random.seed(42)`, you will the same sequence of random numbers. So after all, random numbers are not random at all, as they can be generated deterministically, however, they mimic the behavior of true random numbers. The ability to set the seed for a random number generator is actually very useful since it enables us to replicate the work of code, exactly it has been done in the past. In particular, this is very useful for code debugging. However, beware of cases where you need to get a different result, every time you run the code. If you set the random seed of the random generator to a fixed value, right at the beginning of the code, you will never get a random behavior.  

## Drawing a random element from a list  

Suppose you have the following list,  
```python
import numpy as np
mylist = np.linspace(0,100,51)
mylist
```
    array([   0.,    2.,    4.,    6.,    8.,   10.,   12.,   14.,   16.,
             18.,   20.,   22.,   24.,   26.,   28.,   30.,   32.,   34.,
             36.,   38.,   40.,   42.,   44.,   46.,   48.,   50.,   52.,
             54.,   56.,   58.,   60.,   62.,   64.,   66.,   68.,   70.,
             72.,   74.,   76.,   78.,   80.,   82.,   84.,   86.,   88.,
             90.,   92.,   94.,   96.,   98.,  100.])

and now you wanted to draw a random element from the above list. You could do,  

```python
import random as rnd
rnd.choice(mylist)
```
    80.0 

This will give a random element from the list. You could also generate a random shuffling of the list by,  

```python
import random as rnd
rnd.shuffle(mylist)
mylist
```
    array([  98.,   12.,   76.,   60.,   46.,   22.,   24.,   92.,   66.,
             16.,    6.,   34.,   14.,    8.,   18.,   50.,   30.,   74.,
              4.,    2.,   38.,   90.,   70.,   56.,   94.,   80.,   32.,
             20.,   10.,   44.,   72.,   84.,    0.,   78.,  100.,   88.,
             86.,   96.,   48.,   52.,   62.,   64.,   26.,   36.,   40.,
             54.,   68.,   58.,   82.,   42.,   28.])

## Summary of some important random functions in Python  

As you may have noticed, since none of the random functions are builtin, things can get really confusing very easily, by simply mixing numpy's random module with Python's random module. The following helps to clarify some of the most important differences between these two modules.  

<table class="center">
    <caption class="title" style="padding-bottom:10px">
        Table 1: Some useful functions and their functionalities in <code>random</code> and <code>numpy</code> modules
    </caption>
    <thead>
        <tr>
            <th>Purpose</th>
            <th>random module</th>
            <th>numpy.random module</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>random uniform numbers in <code>[0,1)</code></td>
            <td><code>random()</code></td>
            <td><code>random(N)</code> (vectorized)</td>
        </tr>
        <tr>
            <td>random uniform numbers in <code>[a,b)</code></td>
            <td><code>uniform(a,b)</code></td>
            <td><code>uniform(a,b,N)</code> (vectorized)</td>
        </tr>
        <tr>
            <td>random integers in <code>[a,b]</code></td>
            <td><code>randint(a,b)</code></td>
            <td><code>randint(a,b+1,N)</code> (vectorized) <br> <code>random_integers(a,b+1,N)</code> (vectorized) </td>
        </tr>
        <tr>
            <td>random Gaussian deviate with parameters <code>[\mu, \sigma]=[m,s]</code></td>
            <td><code>gauss(m,s)</code></td>
            <td><code>normal(m,s,N)</code> (vectorized)</td>
        </tr>
        <tr>
            <td>setting random number generator seed <code>i</code></td>
            <td><code>seed(i)</code></td>
            <td><code>seed(i)</code></td>
        </tr>
        <tr>
            <td>shuffling list mylist</td>
            <td><code>shuffle(mylist)</code></td>
            <td><code>shuffle(mylist)</code></td>
        </tr>
        <tr>
            <td>choose a random element from mylist</td>
            <td><code>choice(mylist)</code></td>
            <td> -- </td>
        </tr>
    </tbody>
</table>
