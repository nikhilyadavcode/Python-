# why the need of creating different scripts for student and teacher?
# >> To maintain the code,to improve the understanding of the code.
# Best practise is to keep differenet components in different scripts.
# examples>>model training and EDA should be kept in different scripts.
# modules:A module is a single file (with.py extension) that contains python cdoe.
# inside module function class and variable or some python code.
# Example>> student_details.py and teacher_details.py are module.


# package:A package is a collection of modules organised in directories.
# each directory can have multiple python scripts
# example>>student and teacher folder is a packages
# version before python 3.3 make a package it was necessary to include 
# __init__.py in package (to initialise package and expose required modules and function) or required anymore.
# __pycache__ also known as pyc file >>these are compiled python file>>source code to byte code>>stored in .pyc file inside __pycache__ directory 
# this help in speedup loading the module next time it is imported 


# library >> pre-written code to perform commom task>> library is a collection of multiple package and modules
# Example>> pandas,numpy

# importing student_details module from student package.

#from teacher import teacher_details # from is used with package,import is used with module>> generic use from wherever you want to import something from module/packages
import os,sys # os provides functionality to interact with operating system
# sys >> provides access to system specific parameter and function such as python path
from os.path import dirname,join,abspath



# dirname >>will give the directory containing the current scripts
# example:dir(__file__)   c:\Users\91921\OneDrive\Desktop\Python\pwskills\student
#print("The directory of the script",dirname(__file__))
#print("This is the file directory",__file__) # __file__>> gives path to current scripts,example:this scripts is at c:\Users\91921\OneDrive\Desktop\Python\pwskills\student\student_details.py

# join>>Join two or more paths,inserting '/' as needed.
# join(dirname(__file__),".." >> move one directory up from the current script directory
#print("The directory of the script",join(dirname(__file__),".."))
parent_dir_path=abspath(join(dirname(__file__),"..")) #>> convert the relative path to absolute path
sys.path.insert(0,parent_dir_path)
# At index 0,add this directory to the beginning of module search/system path
# it allows to search module and package

from teacher import teacher_details
def student():
   print("This is a Student details")
teacher_details.teacher() 