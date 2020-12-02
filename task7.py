# Write a function that takes in a number representing the temperature in Celsius
# and returns the temperature in Fahrenheit.
# Write another function that does the opposite (Fereignheit to Celsius)


def task7_imperial_temp(temp_celcius):
    temp_fereignheit = round(((temp_celcius * (9/5)) + 32), 1)
    return f"Temperature is {temp_fereignheit} Fahrenheit"


output1 = task7_imperial_temp(32)
print(output1)


def task7_metric_temp(temp_fereignheit):
    temp_celcius = round(((temp_fereignheit - 32) * (5/9)), 1)
    return f"Temperature is {temp_celcius} Celsius"


output2 = task7_metric_temp(20)
print(output2)