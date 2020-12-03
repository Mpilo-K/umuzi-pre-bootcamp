def onenum65_or_sumis65():
    num_1 = int(input('Enter the first number: '))
    num_2 = int(input('Enter the second number: '))
    if (num_1 == 65) or (num_2 == 65):
        return 'True'
    elif num_1 + num_2 == 65:
        return 'True'
    else:
        return 'False'


print(onenum65_or_sumis65())