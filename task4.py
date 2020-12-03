def onenum3_and_sumhas3():
    num_1 = input('Enter the first number: ')
    num_2 = input('Enter the second number: ')
    if (num_1 == str(3) or num_2 == (3)) and (str(3) in str((num_1 + num_2))):
            return 'True'
    else:
        return 'False'


print(onenum3_and_sumhas3())