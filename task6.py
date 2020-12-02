# White a function that takes in three numbers and returns the maximum number. 
# Do this without using any builtin methods. 
# Write your own logic from scratch.

# The first function
def task6_function1(num1, num2, num3):
    list_numbers1 = [num1, num2, num3]
    max_number1 = list_numbers1[0]
    for num in list_numbers1:
        if num > max_number1:
            max_number1 = num
    return f"The maximum number is: {max_number1}"


print(task6_function1(4, 5, 9))

# Bonus: How can you change the code so it can take in any number of numbers?

# The second function
def task6b_function2(a_list):
    list_numbers2 = list()
    for num in a_list:
        list_numbers2.append(num)
    max_number2 = list_numbers2[0]
    for num in list_numbers2:
        if num > max_number2:
            max_number2 = num
    return f"The maximum number is: {max_number2}"


numbers = [399, 5, 7, 8, 90, 12, 6]
print(task6b_function2(numbers))