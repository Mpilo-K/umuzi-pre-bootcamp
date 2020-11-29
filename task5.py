def task5_function(num1, num2, num3):
    semi_perimeter = 0.5 * (num1 + num2 + num3)
    tri_area = ((semi_perimeter*((semi_perimeter - num1) * (semi_perimeter - num2) * (semi_perimeter - num3))) ** 0.5)
    return tri_area


task5_output = task5_function(7, 8, 9)
print("Area of the triangle is: " + str(task5_output))