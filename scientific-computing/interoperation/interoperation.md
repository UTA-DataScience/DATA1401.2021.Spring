---
title: Interoperation with other programming languages
tags: [random_numbers, python]
keywords: random_numbers, python
summary: "This note attempts to provide a brief introduction to performing simple Monte Carlo simulations via Python."
#permalink: /notes/scientific-computing/interoperation/index.html

last_updated: July 9, 2019
---

## Using Python as a wrapper or interface  

Python has gained popularity for implementing scientific computations, partly because of its rather-convenient occasionally-Fortran-looking syntax as opposed C/C++ languages, but more recently, because of the vast number of scientific libraries that are nowadays available in Python.

Nevertheless, the execution speed of a Python code is significantly lower than what can be obtained by
programming in languages such as Fortran, C, or C++. For example, see the following performance comparisons and tests in [NASA modeling guru webpage](https://modelingguru.nasa.gov/docs/DOC-1762) or the updated version [here](https://modelingguru.nasa.gov/docs/DOC-2676). As you can see there, the **performance of Python code can be significantly lower, up to 500 times and more, compared to compiled languages such as Fortran and C**. These languages compile the program to machine language, which enables the computing resources to be utilized with very high efficiency. Knowing the performance hit in Python, the scientific programming paradigm in Python is to write compute-intensive parts of the code in lower level languages such as Fortran or C and use Python as wrapper and glue between lower level codes and as a handy tool for high-level tasks.  

Python was initially designed for being integrated with C. This feature has spawned the development of several techniques and tools for calling compiled languages from Python, allowing us to relatively easily reuse fast and well-tested scientific libraries in Fortran, C, or C++ from Python, or migrate slow Python code to compiled languages. It often turns out that only smaller parts of the code, usually for loops doing heavy numerical computations, suffer from low speed and can benefit from being implemented in Fortran, C, or C++.  

There are already several Python wrappers developed for integrating Python with other programming language codes. Most prominent examples include [F2PY](https://docs.scipy.org/doc/numpy/f2py/) for Fortran and C codes, [SWIG](http://www.swig.org/) for C, C++, Perl, Java, and many others, [Cython](http://cython.org/) for C, [Jython](http://www.jython.org/) for Java, and several others.  

The usage of some of these wrappers can be tricky and requires some work and good familiarity with the wrapper. This is, in particular, true about SWIG, which involves a significant amount of manual modifications to the interfaces, compared to F2PY, for example. At the moment, F2PY only works with Python 2.x standard.  

There is also a Python module [pymat](http://pymat.sourceforge.net/) developed for direct interaction of Python code with MATLAB.  
