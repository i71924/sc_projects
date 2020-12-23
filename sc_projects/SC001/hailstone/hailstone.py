"""
File: hailstone.py
Name: Po Kai Feng
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    First determine the positive number is odd or even to decide to do what action.
    Then add one steps while the new number is not one.
    """
    print('This program computes Hailstone sequences.')
    print('')
    num = int(input('Enter a number: '))
    # num should be positive
    steps = 0
    while True:
        if num == 1:
            # Hailstone Sequence is finished.
            break
        if num % 2 == 0:
            # The number is even and should be taken half.
            num_new = num // 2
            print(str(num)+' is even, so I take half: '+str(num_new))
        else:
            # The number is odd and should times three and plus one.
            num_new = num*3 + 1
            print(str(num) + ' is odd, so I make 3n+1: ' + str(num_new))
        num = num_new
        # To let new number be assigned to variable num.
        steps += 1
    print('It took '+str(steps)+' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
