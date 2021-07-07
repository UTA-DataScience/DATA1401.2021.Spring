---
title: Data output methods
tags: [data, output, IO, python]
keywords: data, output, IO, python
summary: "This note aims at providing an overview of data-input methods in Python."
#permalink: /notes/data-transfer/output/index.html
last_updated: July 9, 2019
---

There are two major methods of data-output:  
1. writing to the terminal window, as previously done using `print()` function, or,
2. writing to an output file.  

We have already extensively discussed printing output to the terminal window. Writing data to file is also easy.  

## Writing to a file
Similar to reading from a file, in order to write to a file, one has to first open the file, this time for the purpose of writing, which is indicated by `'w'` or `'a'`,
```python
outfile = open(filename, 'w') # write to a new file, or overwrite file
```

One could also **append** some output to an **existing file** using the `'a'` indicator as input to `open()`,
```python
outfile = open(filename, 'a') # append to the end of an existing file
```

In both cases, the string valued variable `filename` contains the path to the file that should be created or manipulated. Suppose we want to write the output of the above code in previous section to a new file. All you would need to do is the following,
```python
myfile = open('data.in', 'r')
numbers = [float(x) for x in myfile.read().split()]
mean = sum(numbers)/len(numbers)
outfile = open('data.out','w')
outfile.write(str(mean) + '\n')
myfile.close()
outfile.close()
```

This will result in the creation of [a new file](data.out) named `data.out` which contains the value of `mean` variable. Note that the addition of the character `'\n'` at the end of the `write` statement is necessary, otherwise the next write to the file will not appear on a new line.  

## Writing a table of data to a file  

Now suppose you were to write the following list to an output file,
```python
data = [[ 0.75, 0.29619813, -0.29619813, -0.75 ],
[ 0.29619813, 0.11697778, -0.11697778, -0.29619813],
[-0.29619813, -0.11697778, 0.11697778, 0.29619813],
[-0.75, -0.29619813, 0.29619813, 0.75 ]]
```

One solution would be the following,
```python
outfile = open('table.out', 'w')
for row in data:
    for column in row:
        outfile.write( '{:14.8f}'.format(column) )
    outfile.write('\n')
outfile.close()
```

This code would result in the creation of an [output file](table.out) named `table.out` which contain the content of `data` variable, in a nice formatted style as the following,
```text
    0.75000000    0.29619813   -0.29619813   -0.75000000
    0.29619813    0.11697778   -0.11697778   -0.29619813
   -0.29619813   -0.11697778    0.11697778    0.29619813
   -0.75000000   -0.29619813    0.29619813    0.75000000
```

## Writing data in HTML format  

Doing research at a professional level requires reporting the results professionally as well. That is, the results of the project, including the final report itself have to be **auto-generated** and **reproducile** as much as possible, and reachable to the widest audience, which nowadays means, availibility on the World-Wide Web.  

Suppose you have worked on a project which has resulted in a final figure that you wanted to put on a single webpage in your repository on Github, together with some information about the and project and the figure. Let's say the figure is a [Growth Curve Fit](growthCurveFit.png). Now we write a code that automatically generates an HTML (or Markdown) file which contains the correct HTML code for displaying the figure on your desired page for the project. You could for example write the following Python code to achieve this goal,
```python
with open('SampleProjectReport.html', 'w') as html:
    html.write('<HTML><BODY BGCOLOR="white">\n')
    html.write('<H1>Sample Project: Tumor growth modeling Result</H1> \n')
    html.write('<H2>Project summary:</H2> \n')
    html.write('<p>In this project, we tried to model the growth of a tumor in a rat\'s brain using the Gompertzian growth model. The fit is shown in the figure below.</p><br> \n')
    figReposPrefix = 'https://www.cdslab.org/python/notes/data-transfer/output/'
    figures = ['growthCurveFit.png']
    for figure in figures:
        html.write( '<img src="{}" width="100%"><br><br>\n'.format(figure) )
    html.write('<H2>Conclusions:</H2>\n')
    html.write('<p>The survival odds for this rat are virtually zero.</p><br>\n')
    html.write('</BODY></HTML>\n')
```

This code will generate an HTML file, which you can view in your browser [here](SampleProjectReport.html).

