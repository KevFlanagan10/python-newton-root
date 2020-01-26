#! /usr/bin/env python3

# Kevin Flanagan 
# Calculate Sqaure root of a number.

#function
def sqrt(x):

  """
  Calculate the square root of the argument x.
  # and "x3 are used for comments in python
  """
  #Example of if statement
  #Check if x is positive.
  if x < 0:
    print("Error: negative value supplied")
    return -1

  #Example of else statement
  else:
    print("Here we go...")

  #Inital guess for the square root.

  z = x / 2.0

  #Continuously improves the guess
  # Adapted from www.example.com
  
  while abs (x - (z*z)) > 0.000001:
    z = z - (((z*z) - x) / (2*z)) 
  
  return z  
#end of function

#myVal = -63.0 #for negative testing

myVal = 63.0
print("The square root of", myVal, "is", sqrt(myVal))


