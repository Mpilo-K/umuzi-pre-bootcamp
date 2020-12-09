def onenum65_or_sumis65(num1, num2):
    if (num1 == 65) or (num2 == 65):
        return 'True'
    elif num1 + num2 == 65:
        return 'True'
    else:
        return 'False'


print(onenum65_or_sumis65(65, 0))