# Write a function that takes 2 numbers as input. 
# If either of the numbers is 3 AND the sum of the numbers contains a 3 then return true. 
# Otherwise return false

def task4_function():
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    if (num_1 == 3) or (num_2 == 3):
        return 'True, at least one of the numbers is 3.'
    elif str(3) in str((num_1 + num_2)):
        return 'True, the sum of both numbers contains a 3.'
    else:
        return 'False, neither of the numbers is 3 and the sum of both does not contain a 3.'


task4_output = task4_function()
print(task4_output)