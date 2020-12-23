"""
File: boggle.py
Name: Po Kai Feng
----------------------------------------
Use quick sorting method by Max Chang to find every words in boggle board
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
EXIT = '-1'

# global variable
dictionary_list = [set() for i in range(26)]   # Add 26 dict for characters a to z
board_list = []
checked = []
word_list = []
moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def main():
	read_dictionary(FILE)
	count = 1
	while True:
		if count == 5:   # Has collected four legal string sets
			boggle_start(board_list)
			count = 1
		letters = input(f'{count} row of letters: (or {EXIT} to quit)')
		if letters == EXIT:
			break
		if is_legal(letters):
			count += 1
			letters = letters.lower()
			board_list.append([letters[0], letters[2], letters[4], letters[6]])
		else:
			print('Illegal format')


def is_legal(letters):
	"""
	:param letters:str, the string that user inputs
	:return:bool, letters is legal type or not
	"""
	if len(letters) == 7:   # Legal input combines with four characters and three empty spaces
		if letters[1] == letters[3] == letters[5] == ' ':
			if letters[0].isalpha() and letters[2].isalpha() and letters[4].isalpha() and letters[6].isalpha():
				return True
	else:
		return False


def read_dictionary(file):
	"""
	:param file: file, the dictionary file
	Read the dictionary file and add all the words to dictionary_list and sorted by first character
	"""
	with open(file, 'r') as f:
		for line in f:
			dictionary_list[ord(line[0])-97].add(line.strip())


def boggle_start(board):
	"""
	:param board:list, the boggle board
	Start to find words in boggle board
	"""
	for i in range(4):
		for j in range(4):   # Start with every word in 4 x 4 board
			boggle_start_helper(board, '', i, j)
	print('There are', len(word_list), 'words in total.')
	clean(board_list)  # Clean the board_list
	clean(word_list)  # Clean the word_list


def boggle_start_helper(board, current, x, y):
	"""
	:param board:list, the boggle board
	:param current:str, current string in boggle board
	:param x:int, column index in 4 x 4 board
	:param y:int, raw index in 4 x 4 board
	Find words in boggle board
	"""
	current += board_list[x][y]
	checked.append((x, y))
	for ele in moves:
		if len(current) >= 4:
			if has_prefix(current):   # Base Case
				if current in dictionary_list[ord(current[0])-97]:
					if current not in word_list:
						word_list.append(current)
						print(f'Found "{current}"')
			else:
				break   # Doesn't has prefix
		if -1 < x+ele[0] < 4 and -1 < y+ele[1] < 4:
			if (x+ele[0], y+ele[1]) not in checked:   # Recursive Case
				boggle_start_helper(board, current, x+ele[0], y+ele[1])
	checked.remove((x, y))


def in_dict(word):
	"""
	:param word:str, string found in boggle
	:return:bool, whether the word is in dictionary or not
	"""
	if word in dictionary_list:
		return True
	return False


def has_prefix(sub_s):
	"""
	:param sub_s:str, sub_string of the word which need to be checked
	:return:bool, whether there is and word startswith the sub_s in the dictionary
	"""
	for ele in dictionary_list[ord(sub_s[0])-97]:
		if ele.startswith(sub_s):
			return True
	return False


def clean(lists):
	"""
	:param lists:list, the list that needs to be cleaned
	Pop all elements in the list
	"""
	for i in range(len(lists)):
		lists.pop()


if __name__ == '__main__':
	main()
