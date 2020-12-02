# Write a function that takes in three numbers. 
# These numbers represent the lengths of the sides of a triangle. 
# The function should return the area of a triangle.

def task5_function(length1, length2, length3):
    semi_perimeter = 0.5 * (length1 + length2 + length3)
    tri_area = ((semi_perimeter*((semi_perimeter - length1) * (semi_perimeter - length2) * (semi_perimeter - length3))) ** 0.5)
    return round(tri_area, 2)


task5_output = task5_function(7, 8, 9)
print(f"The area of the triangle is: {task5_output} square units.")