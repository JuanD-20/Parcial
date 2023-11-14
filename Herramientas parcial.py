from OperationsH import char_to_ascii_and_binary, word_to_binary_representation
import sys

def main():
    print('Menu\n=====\n1. Character\n2. Word')
    menu = int(input('Enter your choice (1 or 2): '))

    if menu == 1:
        char = input('Enter a character: ')
        ascii_value, char_binary = char_to_ascii_and_binary(char)
        print(f'ASCII character value of "{char}" is {ascii_value}. Binary representation of "{char}" in a byte is {char_binary}')
    elif menu == 2:
        word = input('Enter a word: ')
        binary_representation = word_to_binary_representation(word)
        print(f'Total: {binary_representation}')
    else:
        print('Invalid choice. Exiting...')
        sys.exit()
main()
