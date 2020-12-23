"""
File: caesar.py
Name: Po Kai Feng
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    User will give a cipher number to create new alphabet first.
    Then user will type a cipher_string. Finally the code will decipher it.
    """
    cipher_num = int(input('Secret number: '))
    ciphered_str = input('What\'s the ciphered string? ')
    print('The deciphered string is: ' + decipher(ciphered_str.upper(), cipher_num))


def decipher(ciphered_str, cipher_num):
    """
    :param ciphered_str: str, the string that has been ciphered
    :param cipher_num: int, the cipher number
    :return: str, deciphered string
    """
    new_alphabet = ''
    deciphered_str = ''
    for i in range(26 - cipher_num, 26):
        new_alphabet += ALPHABET[i]
    for j in range(0, 26 - cipher_num):
        new_alphabet += ALPHABET[j]
    # Now new_alphabet is wrapped
    for k in range(0, len(ciphered_str)):
        if new_alphabet.find(ciphered_str[k]) == -1:
            # It's not alphabet and doesn't need to decipher
            deciphered_str += ciphered_str[k]
        else:
            deciphered_str += ALPHABET[new_alphabet.find(ciphered_str[k])]
    return deciphered_str


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
