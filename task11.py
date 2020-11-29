# Make a function that takes two strings as input, and outputs the common characters/letters that they share.
# (For example, Input: ‘house’, ‘computers’ . Output: ‘Common letters: o, u, e, s’)

def compare_fun():
    string1 = input("Write a word: ")
    string2 = input("Write a second word: ")
    for character in string1 and string2:
        if character in string1 and string2:
            print(character)


print(compare_fun())