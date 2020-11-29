def task3_function():
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    if (num_1 == 65) or (num_2 == 65):
        return 'true, at least one of the numbers is 65.'
    elif num_1 + num_2 == 65:
        return 'true, the sum of both numbers is 65.'
    else:
        return 'false, neither of the numbers is 65 and the sum of both is not 65.'


task3_output = task3_function()
print(task3_output)