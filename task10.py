def print_all_vowels(string):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I' , 'o', 'O', 'u', 'U']
    for character in string:
        if character in vowels:
            print(character)


print_all_vowels("There is too many envelopes! I nEEd tO tAkE A brEAk!")