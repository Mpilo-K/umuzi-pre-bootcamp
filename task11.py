def compare_fun():
    string1 = input("Write a word: ")
    string2 = input("Write a second word: ")
    common_letters = [character for character in string1 and string2 if character in string1 and string2]
    #common_letters = []
    #for character in string1 and string2:
        #if character in string1 and string2:
            #common_letters.append(character)
            #print(character)
    string_of_letters = ', '.join(common_letters)
    return f'Common letters: {string_of_letters}'


print(compare_fun())