#!/usr/bin/python3

from time import time
from math import *

print("")
print("This program finds the integral of a function")
print("")

function = input("Enter a function f(x): ")

if len(function) == 0:
    exit()

f = lambda x: eval(function)

a = input("Enter starting value a: ")

if len(a) > 0:
    try:
        a = float(a)
    except:
        print("Bad input")
        garbage = input("Press <Enter> to end program")
        exit()
else:
    exit()

try:
    garbage = f(a)
except:
    print("Bad function")
    garbage = input("Press <Enter> to end program")
    exit()

b = input("Enter ending value b: ")

if len(b) > 0:
    try:
        b = float(b)
    except:
        print("Bad input")
        garbage = input("Press <Enter> to end program")
        exit()
else:
    exit()

step = input("Enter step value: ")

if len(step) > 0:
    try:
        step = float(step)
        if step <= 0.0:
            print("Can't have zero or negative step!")
            garbage = input("Press <Enter> to end program")
            exit()
        if a+step == a:
            print("Step too small")
            garbage = input("Press <Enter> to end program")
            exit()
    except:
        print("Bad input")
        garbage = input("Press <Enter> to end program")
        exit()
else:
    exit()

if a > b:
    print("a greater than b, not allowed")
    garbage = input("Press <Enter> to end program")
    exit()

if a+step > b:
    print("step is too big")
    garbage = input("Press <Enter> to end program")
    exit()

if int((b-a)/step) < 100:
    r = range(int((b-a)/step))
else:
    r = range(100)
x = a
area = 0.0
time1 = time()
for n in r:
    area += step*((f(x)+f(x+step))/2)
    x += step
time2 = time()
totaltime = ((time2-time1)/len(r))*(b-a)/step
print("Estimated computation time is",int(totaltime),"seconds")

x = a
area = 0.0
while x <= b-step:
    area += step*((f(x)+f(x+step))/2)
    x += step

print("Integral of",function,"is:",area)
garbage = input("Press <Enter> to end program")
