recu = []

with open("file.txt") as grades_file:
    for line in grades_file:
        student_grade = line
        student_grade = student_grade.split(" ")
        if int(student_grade[1]) < 6:
            recu.append(student_grade[0] + "\n")

with open("newfile.txt", mode="w") as recu_file:
    recu_file.writelines(recu)

with open("newfile.txt", mode="r") as recu_file:
    content = recu_file.read()
    print(content)
