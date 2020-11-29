# The first function
def task6_function(num1, num2, num3):
    list_numbers = [num1, num2, num3]
    max_number = list_numbers[0]
    for num in list_numbers:
        if num > max_number:
            max_number = num
    return "The maximum number is: " + str(max_number)


print(task6_function(4, 5, 9))


# The second function
def task6b_function(a_list):
    list_numbers = list()
    for num in a_list:
        list_numbers.append(num)
    max_number = list_numbers[0]
    for num in list_numbers:
        if num > max_number:
            max_number = num
    return "The maximum number is: " + str(max_number)


numbers = [399, 5, 7, 8, 90, 12, 6]
print(task6b_function(numbers))