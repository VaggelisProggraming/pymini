# import pymini
# import pyminiIDE
# import pygram
# pymini.i
# pyminiIDE.i
# pygram.i
HTMLtitle = """

\n\n\n\n
    HTML stands for HyperText Markup Language. It is used to design web pages using a markup language. It is the combination of Hypertext and Markup language. 
    Hypertext defines the link between the web pages. A markup language is used to define the text document within tag which defines the structure of web pages. 
    It is a markup language that is used by the browser to manipulate text, images, and other content to display in the required format.
"""

BaseOfHTML = """
 \n\n\n
    Why to use HTML ?
It helps to structure our website well. The way a skeleton system gives a structure to the human body, in a similar manner, it acts as a skeleton for a website, 
without it a website cannot be made. If you want to work as a Software Developer especially in the Web Development domain, then learning HTML is a must, because without knowledge of it you cannot build a website.

Base for creating websites: It is the basic necessity a developer should know while building a website from scratch.
Learn web development: It is the first step towards learning Web Development. Once you learn it, you can build simple,
static websites very easily.
Can become freelancer: Since web development has the best scope in freelancing, therefore learning it will
surely help you to get the best deals of website development in the market.
 

Basic Format: It is the basic format of create a simple web page.

<!DOCTYPE html>
<html>
 
<head>
    <!-- Head section of website-->
    <title></title>
</head>
 
<body>
    <!-- Body section of website -->
</body>
 
</html><div class="open_grepper_editor" title="Edit & Save To Grepper"></div>
Example: Let’s see a small example of simple web page that display the heading and paragraph content.

<!DOCTYPE html>
<html>
 
<head>
    <title>Simple Web Page</title>
</head>
 
<body>
    <h1>Welcome to GeeksforGeeks</h1>
    <p>A computer science portal for geeks</p>
</body>
 
"""

PythonTitle = """

\n\n\n\n
    Python uses indentation to highlight the blocks of code. Whitespace is used for indentation in Python.
    All statements with the same distance to the right belong to the same block of code. If a block has to be more deeply nested,
    it is simply indented further to the right. You can understand it better by looking at the following lines of code.

    # Python program showing 
    # indentation 
    
    site = 'gfg'
    
    if site == 'gfg': 
        print('Logging on to pymini...') 
    else: 
        print('retype the URL.') 
    print('All set !') 
    Comments are useful information that the developers provide to make the reader understand the source code.
    It explains the logic or a part of it used in the code. There are two types of comment in Python:

    Single line comments: Python single line comment starts with hashtag symbol with no white spaces.
    # This is a comment 
    # Print “pymini !” to console 
    print("Pymini")
    Multi-line string as comment: Python multi-line comment is a piece of text enclosed in a delimiter (“””) on each end of the comment.

    ''' '''
    This would be a multiline comment in Python that 
    spans several lines and describes geeksforgeeks. 
    A Computer Science portal for geeks. It contains  
    well written, well thought  
    and well-explained computer science  
    and programming articles,  
    quizzes and more.  
    … 
    print("pymini")

    Variables in Python are not “statically typed”. We do not need to declare variables
    before using them or declare their type.
    A variable is created the moment we first assign a value to it.

    #!/usr/bin/python 
    # An integer assignment 
    age = 45                     
    
    # A floating point 
    salary = 1456.8            
    
    # A string   
    name = "John"             
    
    print(age) 
    print(salary) 
    print(name) 

    Operators are the main building block of any programming language. Operators 
    allow the programmer to perform different kinds of operations on operands.
    These operators can be categorized based upon their different functionality:

    Arithmetic operators: Arithmetic operators are used to perform mathematical operations like addition, subtraction,
    multiplication and division.
    # Examples of Arithmetic Operator 
    a = 9
    b = 4
    
    # Addition of numbers 
    add = a + b 
    # Subtraction of numbers  
    sub = a - b 
    # Multiplication of number  
    mul = a * b 
    # Division(float) of number  
    div1 = a / b 
    # Division(floor) of number  
    div2 = a // b 
    # Modulo of both number 
    mod = a % b 
    
    # print results 
    print(add) 
    print(sub) 
    print(mul) 
    print(div1) 
    print(div2) 
    print(mod) 
"""


import tkinter as tk
from tkinter import * 
 
root = Tk()
 
# specify size of window.
root.geometry("250x170")
 
# Create text widget and specify size.
T = Text(root, height = 5, width = 52)
 
# Create label

Fact = """watervga@gmail.com"""

T.pack()
 
# Insert The Fact.
T.insert(tk.END, Fact)
 
tk.mainloop()