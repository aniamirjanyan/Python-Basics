# these are couple of ways to import modules

import basic_functions as bf
from basic_functions import hello_func
from basic_functions import *

import sys

# USEFUL LIBRARIES

import random
import math
import datetime
import calendar
import os

sys.path.append('/users/blahblah')  # you can change the directory
print(sys.path)                     # list of directories

rads = math.radians(90)
print(math.sin(rads))

today = datetime.date.today()       # gives today's date
print(calendar.isleap(2017))        # if the year is leap

print(os.getcwd())                  # current working directory
print(os.__file__)                  # location of this file 


