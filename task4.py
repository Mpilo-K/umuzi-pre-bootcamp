def task4_function():
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    if (num_1 == 3) or (num_2 == 3):
        return 'true, at least one of the numbers is 3.'
    elif str(3) in str((num_1 + num_2)):
        return 'true, the sum of both numbers contains a 3.'
    else:
        return 'false, neither of the numbers is 3 and the sum of both does not contain a 3.'


task4_output = task4_function()
print(task4_output)