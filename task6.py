# White a function that takes in three numbers and returns the maximum number. 
# Do this without using any builtin methods. 
# Write your own logic from scratch.

# The first function
def maximum_number(num1, num2, num3):
    list_numbers = [num1, num2, num3]
    max_number = list_numbers[0]
    for num in list_numbers:
        if num > max_number:
            max_number = num
    return max_number


print(maximum_number(4, 5, 9))

# Bonus: How can you change the code so it can take in any number of numbers?
# The second function
def maximum_number2(list_of_numbers):
    list_numbers2 = list()
    for num in list_of_numbers:
        list_numbers2.append(num)
    max_number2 = list_numbers2[0]
    for num in list_numbers2:
        if num > max_number2:
            max_number2 = num
    return max_number2


numbers = [39, 5, 7, 8, 90, 12, 6]
print(maximum_number2(numbers))