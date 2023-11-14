def char_to_ascii_and_binary(char):
    ascii_value = ord(char)
    binary_representation = format(ascii_value, '08b')
    return ascii_value, binary_representation

def word_to_binary_representation(word):
    binary_representation = ''
    for char in word:
        ascii_value, char_binary = char_to_ascii_and_binary(char)
        print(f'ASCII character value of "{char}" is {ascii_value}. Binary representation of "{char}" in a byte is {char_binary}')
        binary_representation += char_binary + ' '
    return binary_representation.strip()