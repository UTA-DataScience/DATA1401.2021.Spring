---
title: Vectorization and array computing
tags: [vectorization, array_computing, Fortran, performance, scientific_computing]
keywords: vectorization, array_computing, Fortran, performance, scientific_computing
summary: "Vectorization, an extremely important concept in high-performance scientific computing, is the process of simultaneous execution of a set of computer instructions. This is contrary to the idea of looping and iteration which performs all program instructions sequentially. Vectorization can lead to significant runtime speed-up of the code."
#permalink: /notes/scientific-computing/vectorization/index.html

last_updated: July 9, 2019
---

## Is Python the optimal choice of programming language for scientific computing?

With regards to the capabilities of Python for scientific calculations, there are conflicting opinions. On the scientific side of the opinion spectrum, some people think that Python is not good enough for number crunching (as a result of which, new programming languages such as [Julia](https://en.wikipedia.org/wiki/Julia_(programming_language)) have been developed). However, there are people at the other extreme who believe that Python is too much oriented towards scientific computation (as a result of which, new programming languages have emerged, such as Google's [Go language](https://en.wikipedia.org/wiki/Go_(programming_language)).  

Regardless of personal opinions, the fact is that Python was not originally intended for scientific computing. However, an enormous number of Python packages have been developed with the dawn of the new millennium specifically for the purpose of numerical computing and data analysis, making Python one of the most popular languages world-wide for scientific inference and data analysis. In addition, many prominent implementations of Python are also open-source or available free of charge as opposed to rival programming languages such as MATLAB and Mathematica. These considerations together make Python a viable choice for *high-level* scientific computing, parallel to MATLAB, Mathematica, Julia, and other high-level programming languages for scientific computing and data analysis.  

## Vectorization and array computing  

So far in the notes, you may have noticed that all numerical vector calculations were either performed with lists, tuples, or dictionaries. Sadly, Python standard does not have an intrinsic special way of defining and manipulating numerical vectors and arrays, unlike most High-Performance Computing (HPC) languages for scientific computations (such as Fortran, Ada, or C). However, there are powerful Python modules that enable a Python programmer to use Python efficiently for numerical analysis as well.  

> If you expect to use Python heavily and mostly for scientific computation in the future, you should keep in mind that as of 2019, Python's built-in list, tuple and dictionary types can be very slow for number crunching.

## Vectors, arrays and the Numerical Python (numpy) package  

In Python, a list can be **heterogeneous** meaning that not all its elements are of the same type. An **array object** in Python can be viewed as a variant of a list, but with the following assumptions:  
- All elements must be of the same type, preferably integer, real, or complex numbers, for efficient numerical computing and storage.  
- The number of elements must be known when the array is created.  
- Arrays are not part of standard Python – one needs an additional package called **Numerical Python**, often abbreviated as **NumPy**. The Python name of the package, to be used in import statements, is `numpy`.  
- With numpy, a wide range of mathematical operations can be done directly on complete arrays, thereby removing the need for loops over array elements. This is commonly called **vectorization**.  
- Arrays with one index are often called **vectors**. Arrays with two indices are used as an efficient data structure for tables, instead of lists of lists. Arrays can also have three or more indices.  

The number of elements of an array can be changed, but keep in mind that this can cause significant computational cost. Creating an array of a given length is frequently referred to as **allocating the
array**. It means that a part of the computer’s memory is marked for being occupied by this array.  

To create a numpy array, you will have to first import it,
```python
import numpy as np
```

The tradition is to import `numpy` as `np`. To convert a list to a numpy array,
```python
import numpy as np
a = [1,2,3,4,5]
a = np.array(a)
type(a)
```
    numpy.ndarray

```python
a
```
    array([1, 2, 3, 4, 5])

To create a new array of length $n$, filled with zeros,
```python
a = np.zeros(n)
```

Note that numpy automatically identifies the appropriate type for all array elements, whether `int`, `float`, or etc.
```python
a[1]
```
    2

```python
type(a[1])
```
    numpy.int32

Even if there is a single `float` element in the list, then all elements in the list will be converted to float in the numpy array by default,
```python
type(a[1])
```
    numpy.int32

```python
a = [1,2,3,4,5.0]
a = np.array(a)
type(a[1])
```
    numpy.float64

If you want to get the desired element type, then you will have to ask numpy for it explicitly,
```python
a = [1,2,3.5,4.9,5.0]
a = np.array(a, int)   # convert all elements in the list to integer
a
```
    array([1, 2, 3, 4, 5])

You can see the full list of input arguments to np.array function [here](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html).  

A similar function `np.zeros_like(c)` generates an array of zeros where the length of the generated array is that of the input array c and the element type is the same as those in c.  
```python
b = [1,2,3,4,5,6,7]
a = np.zeros_like(b)
a
```
    array([0, 0, 0, 0, 0, 0, 0])

Often one wants an array to have $n$ elements with uniformly distributed values in an interval $[p,q]$. The numpy function `linspace` creates such arrays,
```python
a = np.linspace(1, 100, 53)
a
```
    array([ 1.        ,    2.90384615,    4.80769231,    6.71153846,
            8.61538462,    10.51923077,   12.42307692,   14.32692308,
            16.23076923,   18.13461538,   20.03846154,   21.94230769,
            23.84615385,   25.75      ,   27.65384615,   29.55769231,
            31.46153846,   33.36538462,   35.26923077,   37.17307692,
            39.07692308,   40.98076923,   42.88461538,   44.78846154,
            46.69230769,   48.59615385,   50.5       ,   52.40384615,
            54.30769231,   56.21153846,   58.11538462,   60.01923077,
            61.92307692,   63.82692308,   65.73076923,   67.63461538,
            69.53846154,   71.44230769,   73.34615385,   75.25      ,
            77.15384615,   79.05769231,   80.96153846,   82.86538462,
            84.76923077,   86.67307692,   88.57692308,   90.48076923,
            92.38461538,   94.28846154,   96.19230769,   98.09615385,  100.        ])

## Vectorized computing vs. looping  

Loops over very long arrays may run slowly. An advantage of arrays is that, with arrays, loops can be avoided the whole array be manipulated directly and simultaneously. If you are a programmer, you are likely already quite familiar with the powerful idea of array computing and vectorization. If not, then consider the following example,  
```python
x = np.linspace(0, 2, 201)
x
```
    array([ 0.  ,  0.02,  0.04,  0.06,  0.08,  0.1 ,  0.12,  0.14,  0.16,
            0.18,  0.2 ,  0.22,  0.24,  0.26,  0.28,  0.3 ,  0.32,  0.34,
            0.36,  0.38,  0.4 ,  0.42,  0.44,  0.46,  0.48,  0.5 ,  0.52,
            0.54,  0.56,  0.58,  0.6 ,  0.62,  0.64,  0.66,  0.68,  0.7 ,
            0.72,  0.74,  0.76,  0.78,  0.8 ,  0.82,  0.84,  0.86,  0.88,
            0.9 ,  0.92,  0.94,  0.96,  0.98,  1.  ,  1.02,  1.04,  1.06,
            1.08,  1.1 ,  1.12,  1.14,  1.16,  1.18,  1.2 ,  1.22,  1.24,
            1.26,  1.28,  1.3 ,  1.32,  1.34,  1.36,  1.38,  1.4 ,  1.42,
            1.44,  1.46,  1.48,  1.5 ,  1.52,  1.54,  1.56,  1.58,  1.6 ,
            1.62,  1.64,  1.66,  1.68,  1.7 ,  1.72,  1.74,  1.76,  1.78,
            1.8 ,  1.82,  1.84,  1.86,  1.88,  1.9 ,  1.92,  1.94,  1.96,
            1.98,  2.  ])

Now, if you wanted to calculate the `sin` of the elements of `x` in the traditional way, you would do,  
```python
from math import sin
sinX = [sin(i) for i in x]
```

This approach, however, can be a quite time-consuming and computationally costly, because **for-loops are very slow in Python**, up to a few hundred times than what you get in Fortran or C.  

A more appropriate solution to the above problem is to use the `sin` function from the numpy module, which enables vectorization,  
```python
sinX = np.sin(x)
```

You see, with the above numpy call, there is no need for a for-loop. The above Python code is an example of a **vectorized code** and the previous code which contained for-loop is an example **scalar code**. The numpy functions are capable of handling arrays as input. Compare the performance of the two codes in the above example,  
```python
%timeit np.sin(x)
The slowest run took 11.73 times longer than the fastest. This could mean that an intermediate result is being cached.
100000 loops, best of 3: 2.21 µs per loop
```

```python
%timeit [sin(i) for i in x]
10000 loops, best of 3: 23.1 µs per loop
```

The vectorized code in this example appears to be more than one order of magnitude (more than 10 times) faster than the scalar version of the code.  

### Why is the vectorized code faster in Python?  

The reason is that numpy uses precompiled Fortran and C loops to loop over the elements of the input array. loops in Fortran and C have far less overhead than loops in Python. Similar to the above example, you can define your own functions that are also vectorized, for example,  
```python
def f(x):
    return x**2*np.exp(-x**2)
x = np.linspace(-3, 3, 101)
y = f(x)
```

The numpy package also has a method for **Automatic vectorization** of scalar functions (function that only take scalar arguments), for example,
```python
func_vec = np.vectorize(func_scalar)
```

However, for serious programming, I do not recommend you to use this numpy functionality as it can be slow and inefficient.  

## vectorization of if-blocks  

For vectorization of calculations involving booleans and if conditions, the solution can be problem dependent, but one common easy way of addressing simple boolean problems could be `where` method in numpy package. For example, suppose you have a list of numbers and you would like to perform a task on all negative numbers in the array, say set them all to zero, and leave the positive numbers intact. One solution would be the following,
```python
x = np.array([1,-1,3,-5,-6,8,7,4,10])
np.where(x<0,0,x)
```
    array([ 1,  0,  3,  0,  0,  8,  7,  4, 10])

## Aliasing vs. copying arrays  

If you recall from the topic of **aliasing vs. copying** in the discussion of **values, variables, types**, there is a difference between aliasing and copying sequence-objects in Python. **The same rules also hold for numpy arrays**, meaning that if you need an independent copy of an existing array, then you have to use `copy` method to generate it,
```python
a = np.array([1,2,3,4,5])
b = a.copy()
b[0] = -1
a
```
    array([1, 2, 3, 4, 5])

```python
b
```
    array([-1,  2,  3,  4,  5])

otherwise a simple equality assignment like `b = a` will only create an alias for numpy array `a`.  
```python
a = np.array([1,2,3,4,5])
b = a
b[0] = -1
a
```
    array([-1,  2,  3,  4,  5])

## In-place arithmetic in Python  

Consider two arrays `a` and `b` of the same shape. The expression `a += b` means `a = a + b`. There are however hidden differences between the two. In the statement `a = a + b`, the sum `a + b` is first computed, yielding a new array, and then the name `a` is bound to this new array. The old array is lost unless there are other names assigned to this array. In the statement `a += b`, elements of `b` are added directly into the elements of `a` (in memory). There is no hidden intermediate array as in `a = a + b`. This implies that **`a += b` is more efficient than `a = a + b` since Python avoids making an extra array**. In other words, the operators +=, *=, and similar operators perform **in-place arithmetic** in arrays.  

## Allocating arrays in Python  

We have already seen in the above that the `np.zeros` function is useful for making a new array of a given size. Very often the size and the type of array elements are known a priori or have to match another existing array's shape and type `b`. There are two ways of achieving this goal,
```python
a
```
    array([1, 2, 3, 4, 5])

```python
b
```
    array([-1,  2,  3,  4,  5])

```python
a
```
    array([1, 2, 3, 4, 5])

```python
b = a.copy()
c = np.zeros(a.shape, a.dtype)
```

```python
a.shape
```
    (5,)

```python
a.
```
    a.T            a.argsort      a.compress     a.cumsum       a.dumps        a.imag         a.min          a.prod         a.reshape      a.shape        a.sum          a.tostring
    a.all          a.astype       a.conj         a.data         a.fill         a.item         a.nbytes       a.ptp          a.resize       a.size         a.swapaxes     a.trace
    a.any          a.base         a.conjugate    a.diagonal     a.flags        a.itemset      a.ndim         a.put          a.round        a.sort         a.take         a.transpose
    a.argmax       a.byteswap     a.copy         a.dot          a.flat         a.itemsize     a.newbyteorder a.ravel        a.searchsorted a.squeeze      a.tobytes      a.var
    a.argmin       a.choose       a.ctypes       a.dtype        a.flatten      a.max          a.nonzero      a.real         a.setfield     a.std          a.tofile       a.view
    a.argpartition a.clip         a.cumprod      a.dump         a.getfield     a.mean         a.partition    a.repeat       a.setflags     a.strides      a.tolist

Notice how the attribute `a.dtype` (dtype standing for data type), and `x.shape` (a tuple) were used in the above example. The shape attribute in array objects holds the shape, i.e., the size of each dimension. The method `size` returns the total number of elements in the array.  

Sometimes one may also want to ensure that an object is an array, and if not, turn it into an array. The `np.asarray` function is useful in such cases,  
```python
a = np.asarray(a)
```

Note that one could have also used,  
```python
a = np.array(a)
```

There is no difference in the output, but note that the second approach does one redundant step, because in the first approach, if the input object is already an array, then there is no need in converting it to an array.  

## Multidimensional NumPy arrays  

Creating multidimensional arrays is very much the same as vectors in numpy. The only thing to keep in mind is that the shape of the array is given as a tuple to `np.array()`. For example, to initialize a 3D array of size (0:3,0:5,0:2), you would do,
```python
a = np.zeros((3,5,2))
a
```
    array([[[ 0.,  0.],
            [ 0.,  0.],
            [ 0.,  0.],
            [ 0.,  0.],
            [ 0.,  0.]],

          [[ 0.,  0.],
              [ 0.,  0.],
              [ 0.,  0.],
              [ 0.,  0.],
              [ 0.,  0.]],

          [[ 0.,  0.],
              [ 0.,  0.],
              [ 0.,  0.],
              [ 0.,  0.],
              [ 0.,  0.]]])

The arrays created so far have been of type `ndarray`. NumPy also has a matrix type called `matrix` or `mat` for one- and two-dimensional arrays. One-dimensional arrays are then extended with one extra dimension such that they become matrices, i.e., either a row vector or a column vector,  
```python
x1 = np.array([1, 2, 3], float)
x2 = np.matrix(x1) # or np.mat(x1)
x3 = np.mat(x1).T # transpose = column vector
x3
```
    matrix([[ 1.],
            [ 2.],
            [ 3.]])
    
```python
type(x3)
```
    numpy.matrixlib.defmatrix.matrix

A special feature of matrix objects in NumPy is that the multiplication operator represents the matrix-matrix, vector-matrix, or matrix-vector product as we know from linear algebra. However, keep in mind that **the multiplication operator between standard ndarray objects is different from multiplication between numpy matrices**. The `ndarray` multiplication is simply a vectorized version of scalar multiplication,  
```python
a = np.array([1,2,3])
b = np.array([1,2,3])
a*b
```
    array([1, 4, 9])

whereas, the matrix multiplication would yield,  
```python
aMat = np.mat(a)
bMat = np.mat(b)
aMat*bMat.T
```
    matrix([[14]])

```python
aMat.T*bMat
```
    matrix([[1, 2, 3],
            [2, 4, 6],
            [3, 6, 9]])


If you intend to use Python and MATLAB together for your projects, then I recommend you to consider programming with matrices in Python instead of `ndarray` objects, because the matrix type in Python behaves quite similar to matrices in MATLAB.
Numpy has a lot more to offer for linear algebra operation, that far beyond the scope of this lecture. More information about algebraic operations in NumPy can be found [here](https://docs.scipy.org/doc/numpy/reference/routines.linalg.html).  

## Symbolic linear algebra  

There also a package [SymPy](http://www.sympy.org/en/index.html) that supports symbolic computations for linear algebra operations as well,  
```python
import sympy as sym
a = sym.Matrix([[2, 0], [0, 5]])
a**-1     # inverse of matrix a
```
    Matrix([
    [1/2,   0],
    [  0, 1/5]])

```python
a.inv()   # same as above, inverse of a
```
    Matrix([
    [1/2,   0],
    [  0, 1/5]])

```python
a.det()   # determinant of a
```
    10

```python
a.eigenvals() # eigenvalues of a
```
    {2: 1, 5: 1}

```python
a.eigenvects()    # eigenvectors of a
```
    [(2, 1, [Matrix([
       [1],
       [0]])]), (5, 1, [Matrix([
       [0],
       [1]])])]

A tutorial on `sympy` can be found [here](http://docs.sympy.org/dev/tutorial/matrices.html).  
