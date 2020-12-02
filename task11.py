# Make a function that takes two strings as input, and outputs the common characters/letters that they share.
# (For example, Input: ‘house’, ‘computers’ . Output: ‘Common letters: o, u, e, s’)

def compare_fun():
    string1 = input("Write a word: ")
    string2 = input("Write a second word: ")
    common_letters = [character for character in string1 and string2 if character in string1 and string2]
    #common_letters = []
    #for character in string1 and string2:
        #if character in string1 and string2:
            #common_letters.append(character)
            #print(character)
    return f'Common letters: {common_letters}'


print(compare_fun())