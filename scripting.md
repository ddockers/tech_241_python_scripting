# Scripting

Scripting is code that automates repetitive tasks.

By automating, it saves time and reduces human error.

Scripting is targeted to a specific task or action.

## Basic Scripting in Python

We use scripting in Python by using libraries and modules.

A module is a collection of functions, and a library can be seen as a collection of modules.

## "Core" Modules

There are seven "core" modules for scripting in Python.

### 1. sys

```import sys```

This library checks the state or version of whatever is running.

If we enter
```commandline
print(sys.version)
```
we get
```commandline
3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)]
```
We can see that the version of Python is 3.11.3.

### 2. os
```commandline
import os
```
This is used mainly for files and folders.
```commandline
print(os.getcwd())
```
This gives us the current working directory, i.e., the folder we're currently in.
```commandline
os.chdir()
os.mkdir()
```
These functions allow us to change current working directory and make a new directory, respectively.
### 3. subprocess
```commandline
import subprocess
```
This allows the current file to execute or work with another Python file.

We can use the below prompt to execute the *hello_world* program.
```commandline
subprocess.run(["python", "hello_world.py"])
```
### 4. math
```commandline
import math
```
The *math* library allows us to complete mathematical problems easily.
```commandline
pi = math.pi
pi_string = str(pi)
print("The value of pi is " + pi_string)
```
This will print
```commandline
The value of pi is 3.141592653589793
```

### 5. random
```commandline
import random
```
This generates a random number.

### 6. datetime
```commandline
import datetime
```
This allows us to use the date and time in a variety of ways.
```commandline
whatisthedate = datetime.datetime.now()
print(whatisthedate)
```
This prints the current date and time to the 1000000th of 1 second. 
We can use this to tell a program to do something if the date reaches a certain time.

### 7. json
```commandline
import json
```
The main use is to translate data between two systems.
