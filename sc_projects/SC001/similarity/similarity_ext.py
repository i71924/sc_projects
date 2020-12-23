"""
File: similarity.py
Name: Po Kai Feng
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    User will types a long DNA sequence. Then user will type a short DNA
    sequence to match the long DNA sequence. Finally the code will calculate
    and return the homology of two DNA sequences.
    """
    long_seq = input('Please give me a DNA sequence to search: ')
    while True:
        long_seq = long_seq.upper()
        # Makes case insensitive.
        if is_dna(long_seq):
            break
        else:
            # Not DNA format and ask user to key in again.
            long_seq = input('Not DNA format!\nPlease give me a DNA sequence to search: ')
    short_seq = input('What DNA sequence would you like to match? ')
    while True:
        short_seq = short_seq.upper()
        # Makes case insensitive.
        if is_dna(short_seq):
            if len(short_seq) > len(long_seq):
                short_seq = input('The DNA sequence is too long!\nWhat DNA sequence would you like to match? ')
            else:
                break
        else:
            # Not DNA format and ask user to key in again.
            short_seq = input('Not DNA format!\nWhat DNA sequence would you like to match? ')
    print('The best match is '+find_homology(long_seq, short_seq))


def find_homology(long_seq, short_seq):
    """
    :param long_seq: str, the base DNA sequence user wants to search in
    :param short_seq: str, the DNA sequence user wants to match
    :return: the homology in long_seq
    """
    homology = ''
    similarity = 0
    for i in range(len(long_seq) - len(short_seq) + 1):
        # Search from [0] to [long_seq - short_seq] in long_seq
        new_homology = ''
        new_similarity = 0
        for j in range(i, i + len(short_seq)):
            # Get the similarity of short_seq and the string from long_seq[i] to long_seq[i+len(short_seq)-1]
            if long_seq[j] == short_seq[j - i]:
                # The two DNA match and should add up similarity
                new_similarity += 1
            else:
                pass
        if new_similarity > similarity:
            # The new DNA section in long_seq has more similarity and should replace the homology
            similarity = new_similarity
            for k in range(i, i + len(short_seq)):
                # Assign new homology
                new_homology += long_seq[k]
            homology = new_homology
    return homology


def is_dna(dna):
    """
    :param dna: str, the strand that user gives(all letters are upper case)
    :return: bool, is DNA or not
    """
    for base in dna:
        if base == 'A':
            pass
        elif base == 'T':
            pass
        elif base == 'G':
            pass
        elif base == 'C':
            pass
        else:
            return False
    return True


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
