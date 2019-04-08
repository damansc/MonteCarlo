""" generating names from two seperate lists at random. """

import sys
import random

def main():
    """ main function that pulls randomly from the first and last list. """

    print("Welcome to the name picker.'\n")
    print("A name just like Sean would pic for Gus: \n\n")

    first = ('test', 'russel', 'george', 'ball')
    last = ('fail', 'tribal', 'is life', 'gotem')

    while True:

        first_name = random.choice(first)
        last_name = random.choice(last)

        print('\n\n')
        print('{} {}\n'.format(first_name, last_name), file=sys.stderr)
        print('\n\n')

        try_again = input('\n\nTry again? (Press enter to continue or type n to quit)\n ')
        if try_again.lower() == 'n':
            break

    input('\npress enter to exit.\n')

if __name__ == "__main__":
    main()