"""
File: weather_master.py
Name: Po Kai Feng
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


# This constant controls when to stop.
QUIT = -100
# This constant controls what degree is cold day.
COLD_DEGREE = 16


def main():
	"""
	This code will present the highest temperature, the lowest temperatures
	and the average temperature of the temperatures data that user types.
	Also it will present how many cold days whose temperature is under COLD_DEGREE.
	"""
	print('stanCode \"Weather Master 4.0\"!')
	temp = int(input('Next Temperature: (or ' + str(QUIT) + ' to quit)? '))
	if temp == QUIT:
		# No temperatures were entered and should end directly.
		print('No temperatures were entered.')
	else:
		# Starts to calculate!
		high = temp
		low = temp
		counts = 0
		sums = 0
		cold_days = 0
		while True:
			if temp < COLD_DEGREE:
				cold_days += 1
			counts += 1
			sums += temp
			high = higher(high, temp)
			low = lower(low, temp)
			temp = int(input('Next Temperature: (or ' + str(QUIT) + ' to quit)? '))
			if temp == QUIT:
				break
		print('Highest temperature = '+str(high))
		print('Lowest temperature = '+str(low))
		print('Average = '+str(average(sums, counts)))
		print(str(cold_days)+' cold day(s)')


def higher(high, temp):
	"""
	:param high: int, the highest temperature data before
	:param temp: int, the new temperature data
	:return: int, the higher one between high and temp, which becomes the highest temperature
	"""
	if temp > high:
		return temp
	return high


def lower(low, temp):
	"""
	:param low: int, the lowest temperature data before
	:param temp: int, the new temperature data
	:return: int, the lower one between high and temp, which becomes the lowest temperature
	"""
	if temp < low:
		return temp
	return low


def average(sums, counts):
	"""
	:param sums: int, the sum of every temperatures user typed
	:param counts: int, the numbers of temperatures being typed
	:return: int, the answer of sums divided by counts
	"""
	return sums / counts


###### DO NOT EDIT CODE BELOW THIS LINE ######


if __name__ == "__main__":
	main()
