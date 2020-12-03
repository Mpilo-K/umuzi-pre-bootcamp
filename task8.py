def number_to_time(number):
    hours = round(number/60)
    minutes = round(number % 60, 2)
    return f"{hours} hour, {minutes} minutes"


print(number_to_time(133))