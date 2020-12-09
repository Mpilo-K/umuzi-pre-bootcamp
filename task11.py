def compare_fun(string1, string2):
    common_letters = [character for character in string1 and string2 if character in string1 and string2]
    string_of_letters = ', '.join(common_letters)
    return f'Common letters: {string_of_letters}'


print(compare_fun('house', 'computers'))