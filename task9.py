# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

lista = [3 * i for i in range(334)]
sum_lista = sum(lista)
print(sum_lista)

listb = [5 * i for i in range(200)]
sum_listb = sum(listb)
print(sum_listb)

sum_of_all = sum_lista + sum_listb
print(f"The sume of all multiples of 3 or 5 below 1000 is {sum_of_all}")