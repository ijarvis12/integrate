#!/usr/bin/python3

##                                               ##
## program that integrates a user input function ##
##                                               ##
from time import time
from math import *
from decimal import Decimal

print("")
print("This program finds the integral of a function")
print("")

# user inputed function
function = input("Enter a function f(x): ")

# if no input, exit
if len(function) == 0:
    exit()

# create the function from user input
f = lambda x: eval(function)

# get starting integration value 'a'
a = input("Enter starting value a: ")

# if starting value entered, attempt to make it a decimal object, else exit
if len(a) > 0:
    try:
        a = Decimal(a)
    except:
        print("Bad input")
        _ = input("Press <Enter> to end program")
        exit()
else:
    exit()

# attempt to evaluate the function at a, else exit
try:
    _ = f(a)
except:
    print("Bad function")
    garbage = input("Press <Enter> to end program")
    exit()

# get ending value 'b'
b = input("Enter ending value b: ")

# if user input, attempt to make it a decimal object, else exit
if len(b) > 0:
    try:
        b = Decimal(b)
    except:
        print("Bad input")
        _ = input("Press <Enter> to end program")
        exit()
else:
    exit()

# get integration step value
step = input("Enter step value: ")

# if step value exists, attempt to make it a decimal object and check if sane, else exit
if len(step) > 0:
    try:
        step = Decimal(step)
        if step <= Decimal(0):
            print("Can't have zero or negative step!")
            _ = input("Press <Enter> to end program")
            exit()
        if a+step == a:
            print("Step too small")
            _ = input("Press <Enter> to end program")
            exit()
    except:
        print("Bad input")
        _ = input("Press <Enter> to end program")
        exit()
else:
    exit()

# check if 'a' is smaller than 'b' (can't integrate ending point first), else exit
if a > b:
    print("a greater than b, not allowed")
    _ = input("Press <Enter> to end program")
    exit()

# check if step isn't too big, else exit
if a+step > b:
    print("step is too big")
    _ = input("Press <Enter> to end program")
    exit()

# the following is an estimator for how long the program will run given all the inputs
# variable 'r' is the range to use in the estimation
if (b-a)/step < Decimal(100):
    r = range(int((b-a)/step))
else:
    r = range(100)
# iterate on 'x'. Save 'a' for use again on acutal integration
x = a
# integration area
area = Decimal(0.0)
# start time
time1 = time()
# integrate given range 'r' from above
for n in r:
    area += step*((f(x)+f(x+step))/2)
    x += step
# stop time
time2 = time()
# estimated time to completion
totaltime = ((time2-time1)/len(r))*(b-a)/step
print("Estimated computation time is",int(totaltime),"seconds")

# start over
x = a
area = 0.0
# integrate
while x <= b-step:
    area += step*((f(x)+f(x+step))/2)
    x += step

# output result
print("Integral of",function,"is:",area)
_ = input("Press <Enter> to end program")
