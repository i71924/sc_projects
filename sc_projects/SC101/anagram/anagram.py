"""
File: anagram.py
Name: Po Kai Feng
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

# Global constants
index_list = []
dictionary_list = []   # Lists of words in dictionary
searched_words = []    # Lists of words which have been searched
is_searching = False   # Note whether the program is searching

# Tried to accelerate but failed :'(


def main():
    read_dictionary(FILE)
    read_index()
    print('Welcome to stanCode "Anagram Generator" (or', EXIT, 'to quit)')
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        if not s.isalpha():
            print('Not word!')
        else:
            find_anagrams(s)
            clean_list(searched_words)


def read_dictionary(file):
    """
    :param file: file, the dictionary file
    Read the dictionary file and add all the words to dictionary_list
    """
    with open(file, 'r') as f:
        for line in f:
            dictionary_list.append(line[0:len(line) - 1])


def read_index():
    """
    Read the dictionary's index of first character and add to index_list
    """
    for i in range(97, 124):
        for j in range(len(dictionary_list)):
            if dictionary_list[j].startswith(chr(i)):
                index_list.append(j)
                break


def clean_list(lists):
    """
    :param lists: list, the list should be cleaned
    Pop all the elements in the lists
    """
    for i in range(len(lists)):
        lists.pop()


def find_anagrams(s):
    """
    :param s: str, the word which user wants to find anagrams
    Find anagrams of s in dictionary
    """
    global is_searching
    s_list = listing(s)    # Separate s into each character
    find_anagrams_helper(s_list, [])
    print(len(searched_words), 'anagrams: ', searched_words)
    is_searching = False


def listing(word):
    """
    :param word: str, the word which user wants to find anagrams
    :return: list, list of every characters in s
    """
    word_list = []
    for ch in word:
        word_list.append(ch)
    return word_list


def find_anagrams_helper(s_list, current):
    """
    :param s_list: list, list of every characters in the word which user wants to find anagrams
    :param current: list, the temporary list of words
    Print all anagrams
    """
    global is_searching
    if not is_searching:
        print('Searching...')
        is_searching = True
    if len(current) == len(s_list):
        # Base case
        s = ''
        for ele in current:
            s += ele
            if not has_prefix(s):
                break
            if len(s) == len(s_list):
                index = ord(s[0]) - 97
                if index < 25:
                    for i in range(index_list[index], index_list[index+1]):
                        if s == dictionary_list[i]:
                            if not in_lists(searched_words, s):
                                print('Found: ', s)
                                searched_words.append(s)
                                is_searching = False
                                break
                else:
                    for i in range(index_list[index], len(dictionary_list)):
                        if s == dictionary_list[i]:
                            if not in_lists(searched_words, s):
                                print('Found: ', s)
                                searched_words.append(s)
                                is_searching = False
                                break
    else:
        # Recursive case
        # Explore
        for ele in s_list:
            if ele in current and count(current, ele) == count(s_list, ele):
                pass
            else:
                current.append(ele)
                find_anagrams_helper(s_list, current)
                # Un-choose
                current.pop()


def count(lists, target):
    """
    :param lists: list, the basis that need to be searched in
    :param target: str, the searching target
    :return: int, numbers of target in lists
    """
    counts = 0
    for ele in lists:
        if ele == target:
            counts += 1
    return counts


def in_lists(lists, target):
    """
    :param lists: list, the basis that need to be searched in
    :param target: str, the searching target
    :return: bool, whether the target is in lists or not
    """
    for ele in lists:
        if ele == target:
            return True
    return False


def has_prefix(sub_s):
    """
    :param sub_s: str, the searching target
    :return: bool, whether the dictionary has words startswith sub_s
    """
    index = ord(sub_s[0])-97
    if index < 25:
        for i in range(index_list[index], index_list[index+1]):
            if dictionary_list[i].startswith(sub_s):
                return True
    else:
        for i in range(index_list[index], len(dictionary_list)):
            if dictionary_list[i].startswith(sub_s):
                return True
    return False


if __name__ == '__main__':
    main()
