"""
File: complement.py
Name: Po Kai Feng
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    User will key in a DNA strand, then this code will give him the DNA's complement.
    """
    dna = input('Please give me a DNA strand and I\'ll find the complement: ')
    dna = dna.upper()
    # Makes case insensitive.
    print('The complement of ' + dna + ' is ' + build_complement(dna))


def build_complement(dna):
    """
    :param dna: str, the DNA strand that user gives(all letters are upper case)
    :return: str, the complement of dna
    """
    new_dna = ''
    for base in dna:
        if base == 'A':
            new_dna += 'T'
        elif base == 'T':
            new_dna += 'A'
        elif base == 'G':
            new_dna += 'C'
        elif base == 'C':
            new_dna += 'G'
    return new_dna


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
