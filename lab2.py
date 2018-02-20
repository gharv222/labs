### George Harvey
### Homework 1
### COMP 525

import math
import random


def circle_area(radius):
	"""Calculates the area of a circle with a given radius
	radius: non negative float
	Returns: float
	"""
	radius = float(radius)
	return (radius * 2 * math.pi)


def miles_per_gallon(miles, gallons):
    """Calculates miles per gallon
    miles: positive float
    gallons: positive float
    """
    miles = float(miles)
    gallons = float(gallons)
    mpg = miles/gallons
    print('miles per gallon = ', mpg)

def is_even(number):
    """
    Checks if number is even
    number: integer
    Returns: True if number is even, False otherwise
    """
    number = int(number)
    if ((number % 2) == 0):
        return True
    else:
        return False

def ten_random_numbers(start, stop):
    """
    Prints ten random integers between start and stop
    """
    for i in range(10):
        print(random.randint(start,stop)) 

def sum_of_odd_to(n):
    """
    Calculates the sum of all odd numbers 
    from 1 to given n
    n: positive integer
    Returns: integer
    """
    sum = 0
    for i in range(1,n):
        if((i%2)!=0):
            sum = sum+i             
    return sum

def average_random_1_to_10(n):
    """
    Calculates the average of random numbers
    between 1 and 10  generated n times
    n: positive integer - how many times random numbers are generate
    Returns: integer
    """
    average = 0
    for i in range(n):
        average = average + int(random.randint(1,10))

    average = average/n
    return average

def is_even(n):
    """
    Decides if number is even
    n:integer
    Returns: True if n is even, False otherwise
    """
    if ((n%2)==0):
        return True
    else:
        return False

def is_odd(n):
    """
    Determoines if a number is odd
    n: integer
    Returns" True if n is odd, fals otherwise
    """
    if ((n%2)==0):
        return False
    else:
        return True
        

if __name__ == '__main__':
    import doctest
    doctest.testmod( )






