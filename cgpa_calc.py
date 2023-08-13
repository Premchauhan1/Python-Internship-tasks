#CGPA Calculator
subjects = int(input("enter the number of subjects: "))
total_credit_hours = 0
total_weighted_grade = 0

for i in range(subjects):
    print("for",i+1,"subject")
    grade = input("enter the grades for subject: ")
    credit_hours = int(input("enter the hour for subject: "))
    if grade == 'A' or 'a':
        grade_point = 4
    elif grade == 'B' or 'b':
        grade_point = 3
    elif grade == 'C' or 'c':
        grade_point = 2
    elif grade == 'D' or 'd':
        grade_point = 1
    elif grade == 'F' or 'f':
        grade_point = 0
    else:
        print("invalid input")

    weighted_grade = grade_point * credit_hours
    total_weighted_grade += weighted_grade
    total_credit_hours += credit_hours

cgpa = total_weighted_grade / total_credit_hours
print("the cgpa is ", cgpa)
