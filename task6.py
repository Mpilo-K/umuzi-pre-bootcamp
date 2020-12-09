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
def maximum_number2(*nums):
    max_number2 = nums[0]
    for num in nums:
        if num > max_number2:
            max_number2 = num
    return max_number2


print(maximum_number2(1, 2, 3, 4, 5, 6, 7))
print(maximum_number2(344, 2, 455, 32, 111, 9))