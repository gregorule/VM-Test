'''
number = int(input("Give me a number between 1 and 10 "))

def x(number):
    for i in range(1, number + 1):
        print(number * i)


y = x(number)
'''

def timesTable(n):
    line = ""
    for row in range(1, n + 1):
        for column in range(1, n + 1):
            line = line + str(row * column) + "\t"
        line = line + "\n"
    print(line)

number = int(input("Enter number "))
timesTable(number)