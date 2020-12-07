def number_to_time(number):
    if number < 60:
        hours = 0
    elif number >= 60:
        hours = round(number/60)
    if hours <= 1:
        time1 = str(hours) + ' hour, '
    elif hours > 1:
        time1 = str(hours) + ' hours, '
    minutes = round(number % 60, 2)
    if minutes <= 1:
        time2 = time1 + str(minutes) + ' minute'
    elif minutes > 1:
        time2 = time1 + str(minutes) + ' minutes'
    return time2


print(number_to_time(33))