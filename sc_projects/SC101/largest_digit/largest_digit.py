"""
File: largest_digit.py
Name: Po Kai Feng
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the number which user wants to find max digit now
	:return: int, the max digit of n
	Call a helper function to find the max digit
	"""
	max_digit = 0    # Assign a basic max_digit to be compared and reset to zero
	return find_largest_digit_helper(n, max_digit)


def find_largest_digit_helper(n, max_digit_now):
	"""
	:param n: int, the number which user wants to find max digit now
	:param max_digit_now: int, the max digit now
	:return: int, the max digit of n
	Reduce one digit in each recursive case to approach base case(n<10)
	"""
	if n < 0:
		# Negative number, should plus -1 to be positive
		n = -n
	if n % 10 > max_digit_now:
		# Explore and assign right max_digit
		max_digit_now = n % 10
	if n < 10:
		# Base Case
		return max_digit_now
	else:
		# Recursive Case
		return find_largest_digit_helper(n // 10, max_digit_now)


if __name__ == '__main__':
	main()
