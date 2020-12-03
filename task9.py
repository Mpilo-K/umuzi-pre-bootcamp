sum_3or5_multiples = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum_3or5_multiples += i

print(sum_3or5_multiples)