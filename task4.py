def onenum3_and_sumhas3(num_1, num_2):
    sum_nums = str(num_1 + num_2)
    if (num_1 == 3 or num_2 == 3) and (str(3) in sum_nums):
            return 'True'
    else:
        return 'False'


print(onenum3_and_sumhas3(3, 50))