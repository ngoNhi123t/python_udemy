import math
# help(math)
## rounding  number
x=6.45
print(math.floor(x))
print(math.ceil(x))
print(round(x))

#mathematical constants
print(math.pi)
from math import pi
print(pi)
print(math.e)
print(math.tau)
math.inf
math.nan
## logarithmic Values
math.e
print(math.log(math.e))

## Custom base

print(math.log(100,10))

print(10**3)

#Trigonometrics Functions
#Radians
print(math.sin(10))
print(math.degrees(pi/2))
print(math.radians(180))
import random
random.randint(1,10)

# The value 101 is completely arbitrary, you can pass in any number you want
print(random.seed(101))
# You can run this cell as many times as you want, it will always return the same number
print(random.randint(0,100))
print(random.randint(0,100))

## random with sequences

# grab a random item form a list
mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))
#Sample with Replacement
print(random.choices(population=mylist,k=5))
#Sample without Replacement
print(random.sample(population=mylist,k=10))

## shuffle
random.shuffle(mylist)
print(mylist)
#Random Distributions
#uniform distribution

#continuous, random picks a value between a and b, each value has equal change of being pick
print(random.uniform(a=0,b=100))
print(random.uniform(a=0,b=100))

#Normal/Gaussian Distribution
print(random.gauss(mu=1,sigma=2))
print(random.gauss(mu=1,sigma=2))
#NumPy library 