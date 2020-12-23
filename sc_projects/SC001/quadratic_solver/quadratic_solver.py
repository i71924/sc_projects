"""
File: quadratic_solver.py
Name: Po Kai Feng
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

import math


def main():
	"""
	User will input three int: a, b, and c. Then he will get the root(s)
	of equation: ax^2+bx+c=0.
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	# a!=0
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	discriminant = b*b - 4*a*c
	if discriminant < 0:
		# The square root of discriminant is not real number.
		print('No real roots')
	elif discriminant == 0:
		# The square root of discriminant is zero and there is only one root.
		print('One root: '+str((0-b)/2/a))
	else:
		# There are two roots.
		print('Two roots: '+str((0-b+math.sqrt(discriminant))/2/a)+' , '+str((0-b-math.sqrt(discriminant))/2/a))


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
