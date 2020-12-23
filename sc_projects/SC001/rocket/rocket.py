"""
File: rocket.py
Name: Po Kai Feng
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	This code prints the rocket's head, belt, upper,
	lower, head and belt depends on its SIZE.
	"""
	head(SIZE)
	belt(SIZE)
	upper(SIZE)
	lower(SIZE)
	belt(SIZE)
	head(SIZE)


def head(size):
	"""
	:param size: int, the size of the rocket
	Print the rocket's head.
	"""
	for i in range(size):
		# Print raw of the number of size.
		for j in range(size - i):
			# Each raw has (size-i)'s space at first.
			print(' ', end='')
		for k in range(i + 1):
			# Each raw has (i+1) '/'.
			print('/', end='')
		for m in range(i + 1):
			# Each raw has (i+1) '\\'.
			print('\\', end='')
		print('')


def belt(size):
	"""
	:param size: int, the size of the rocket
	Print the rocket's belt.
	"""
	for i in range(2 * (size + 1)):
		# There are 2*(size+1) icons in the belt.
		if i == 0:
			# The first of the belt.
			print('+', end='')
		elif i == 2 * (size + 1) - 1:
			# The end of the belt.
			print('+', end='')
		else:
			print('=', end='')
	print('')


def upper(size):
	"""
	:param size: int, the size of the rocket
	Print the rocket's upper.
	"""
	for i in range(size):
		print('|', end='')
		for j in range(size - 1 - i):
			# Each raw has (size-1-i)'s '.' after the first '|'.
			print('.', end='')
		for k in range(i + 1):
			# Each raw has (i+1)'s '/' and '\\'.
			print('/', end='')
			print('\\', end='')
		for m in range(size - 1 - i):
			# Each raw has (size-1-i)'s '.' before the second '|'.
			print('.', end='')
		print('|', end='')
		print('')


def lower(size):
	"""
	:param size: int, the size of the rocket
	Print the rocket's lower.
	"""
	for i in range(size):
		print('|', end='')
		for j in range(i):
			# Each raw has i's '.' after the first '|'.
			print('.', end='')
		for k in range(size - i):
			# Each raw has (size-i)'s '\\' and '/'.
			print('\\', end='')
			print('/', end='')
		for j in range(i):
			# Each raw has (i)'s '.' before the second '|'.
			print('.', end='')
		print('|', end='')
		print('')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
