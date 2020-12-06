def calculate_triangle_area(side1_length, side2_length, side3_length):
    semi_perimeter = 0.5 * (side1_length + side2_length + side3_length)
    tringle_area = ((semi_perimeter*((semi_perimeter - side1_length)*(semi_perimeter - side2_length)*(semi_perimeter - side3_length))) ** 0.5)
    return round(tringle_area, 2)


print(calculate_triangle_area(3, 4, 5))