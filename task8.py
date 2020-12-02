# Make a function to convert any number into hours and minutes.
# (For example, 71 will become “1 hour, 11 minutes”; 133 will become “2 hours, 13 minutes”.)

def number_conversion_function(number):
    hours = round(number/60)
    minutes = round(number % 60)
    return f"{hours} hour(s), {minutes} minutes"


print(number_conversion_function(71))