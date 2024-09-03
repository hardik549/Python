def calculate_grade(phy, chem, bio, maths, comp):
    total_marks = phy + chem + bio + maths + comp
    percentage = (total_marks / 500) * 100

    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    elif percentage >= 40:
        grade = 'E'
    else:
        grade = 'F'

    return percentage, grade

physics = int(input("Enter marks for Physics: "))
chemistry = int(input("Enter marks for Chemistry: "))
biology = int(input("Enter marks for Biology: "))
mathematics = int(input("Enter marks for Mathematics: "))
computer = int(input("Enter marks for Computer: "))

percentage, grade = calculate_grade(physics, chemistry, biology, mathematics, computer)


print(f"Percentage: {percentage:.2f}%")
print("GRADE: ", grade)
