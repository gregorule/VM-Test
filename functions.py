'''
def add_calc(number1, number2):
    answer = number1 + number2
    return answer

added_number = add_calc(5,5)
print(added_number + 20)
'''

firstName = str(input("What is your first name? "))
surname = str(input("What is your surname? "))
homework = int(input("What was your homework grade out of 25? "))
assignment = int(input("What was your assignment grade out of 50? "))
exam = int(input("What was your final exam score out of 100? "))

def final(firstName, surname, homework, assignment, exam):
    top = homework + assignment + exam
    decimal = top / 175
    answer = decimal * 100
    return answer

print1 = final(firstName, surname, homework, assignment, exam)
print(f"{firstName} {surname} your final score was {print1}")

if print1 >= 85:
    print("This is a distinction!")
elif print1 >=65 and print1 <85:
    print("This is a pass!")
else:
    print("This mark is a fail", firstName)