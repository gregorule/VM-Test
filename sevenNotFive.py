#find all numbers, between 2000 and 3200 (both included),
# that are divisible by 7, but are not a multiple of 5

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
