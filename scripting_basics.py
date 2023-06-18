# Basics of scripting in Python

# Libraries and Modules
# Module is a collection of functions
# Libraries are like collections of modules

# Seven "core" modules in Python

import sys

# It checks the state/version of things that are running

print(sys.version)

import os

# mainly for files and folders

print(os.getcwd()) # current working directory
# os.chdir() change directory
# os.mkdir() make new directory

import subprocess

# Lets the file interact with other files

subprocess.run(["python", "hello_world.py"])

import math
pi = math.pi
pi_string = str(pi)
print("The value of pi is " + pi_string)

import random

rand = random.randrange(1, 10)
print(rand)

import datetime

# You can use date and time in variety of ways

whatisthedate = datetime.datetime.now()
print(whatisthedate)

# e.g. if time past a certain time, do this thing

import json

# Main use is to transport data between 2 APIs

x = {
    "name": "Kipo",
    "age" : 3,
    "city" : "Sale"
}

y = json.dumps(x)

print(y)
print(type(y))