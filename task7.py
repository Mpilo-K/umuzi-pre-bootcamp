# Converting from Celsius to Fereignheit
def celsius_to_fereignheit(temp_in_celcius):
    temp_fereignheit = round(((temp_in_celcius * (9/5)) + 32), 1)
    return temp_fereignheit


print(celsius_to_fereignheit(32))

# Converting from Fereignheit to Celsius
def fereignheit_to_celsius(temp_in_fereignheit):
    temp_celcius = round(((temp_in_fereignheit - 32) * (5/9)), 1)
    return temp_celcius


print(fereignheit_to_celsius(20))