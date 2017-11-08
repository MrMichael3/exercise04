ects_earned = 138
points_earned = 67
points_max = 90
ects_required_for_ba = 180
ects_missing = ects_required_for_ba - ects_earned
six_ects_courses = int(ects_missing / 6)
grade = points_earned / points_max * 5 + 1
"""
print("So far you earned", ects_earned, "ECTS points.")
print("In the exam you got", points_earned, "of", points_max ,"points.")
print(ects_missing,"ECTS points are missing.")
print("you need to book",six_ects_courses, "6-ECTS courses.")
print("your grade:",round(grade,2))
"""
# 4.1 Assignment
# a)
""" return the percentage to pass bachelor (max 100%)"""


def percentage_completed(a, b):
    c = str(min(round(a / b * 100), 100))
    return (c + "%")


""" return the grade you get for the points you earned"""


def calculate_grade(points_earned, points_max):
    grade = min(round(points_earned / points_max * 5 + 1, 2), 6)
    return grade


""" return True if the first argument is a multiple of the second argument"""


def multiple_of(first, multiple):
    if (first % multiple == 0):
        return True
    else:
        return False


# print(percentage_completed(ects_earned, ects_required_for_ba))
# print(calculate_grade(points_earned, points_max))
# print(multiple_of(ects_missing, 3))
"""
# b)
while True:
    while True:
        new_ects_points = int(input("new ECTS Points:    (end with -1)"))
        if (new_ects_points == -1):
            break
        ects_earned += new_ects_points
        if (ects_earned >= ects_required_for_ba):
            break
    if (ects_earned >= ects_required_for_ba):
        print("Congratulations, you passed ", percentage_completed(ects_earned, ects_required_for_ba))
        break
    if (ects_required_for_ba - ects_earned < 30):
        print("You have nearly done it")
    else:
        print("There is still a long way to go")
    print("You have earned: %d Points!" % ects_earned)

    if input("Continue?") != "Yes":
        break
"""
# c)
""" add new ECTS Points and show how much ECTS Points already reached"""


def new_ects(n):
    global ects_earned
    if (n == -1):
        print("You have earned: %d Points!" % ects_earned)
        return
    ects_earned += n
    if (ects_earned >= ects_required_for_ba):
        print("Congratulations, you passed ", percentage_completed(ects_earned, ects_required_for_ba))
        return
    if (ects_required_for_ba - ects_earned < 30):
        print("You have nearly done it")
    else:
        print("There is still a long way to go")
    print("You have earned: %d Points!" % ects_earned)


# exercise 3
# Task 7
# a)
"""add new grades to a file, creates a new file if it doesnt already exist"""


def add_grade(file, mode="w"):
    with open(file, mode) as text:
        while input("Do you want to add a new results in %s? (y/n)" % (file)) == "y":
            ECTS_points = int(input("How many ECTS-points did you earned?"))
            max_points = int(input("max points: "))
            reached_points = int(input("reached points: "))
            lecture = input("lecture: ")
            semester = input("semester:")
            grade = calculate_grade(reached_points, max_points)
            text.write("{0:d}\t{1:f}\t{2:s}\t{3:s}\n".format(ECTS_points, grade, lecture, semester))
        return text


# add_grade("grade.txt")

# b)
"""opens a file and print the percentage completed and the average note"""


def get_study_overview(file):
    total_ects = 0
    grades = 0
    counter = 0
    with open(file, "r") as text:
        for line in text:
            line = line.split("\t")
            ects = float(line[0])
            grade = float(line[1])
            lecture = line[2]
            if grade >= 4:
                print(lecture)
                total_ects += ects
                grades += grade
                counter += 1
        if counter == 0:
            print("no lecture passed!")
            return
        print("Percentage completed: " + percentage_completed(total_ects, ects_required_for_ba))
        print("average grade: " + str(round((grades / counter), 2)))

# Exercise 4
# 4.1.b)

def get_list_lectures(file, x="passed"):
    list_of_lectures = []
    with open(file, "r") as text:
        for line in text:
            line = line.split("\t")
            grade = float(line[1])
            lecture = line[2]
            if x == "passed":
                if grade >= 4:
                    list_of_lectures.append(lecture)
            elif x == "failed":
                if grade < 4:
                    list_of_lectures.append(lecture)
        return list_of_lectures

#print(get_list_lectures("my_studies.txt"))

#4.1.c)

def get_lectures_by_semester(file):
    with open(file, "r") as text:
        lectures_by_semester = {}
        for line in text:
            line = line.split("\t")
            lecture = line[2]
            semester = line[3]
            if semester[:-1] not in lectures_by_semester.keys():
                lectures_by_semester[semester[:-1]] = [lecture]
            else:
                lectures_by_semester[semester[:-1]].append(lecture)
        return lectures_by_semester

def get_ects_by_semester(file):
    with open(file, "r") as text:
        ects_by_semester = {}
        for line in text:
            line = line.split("\t")
            ects = line[0]
            semester = line[3]
            if semester[:-1] not in ects_by_semester.keys():
                ects_by_semester[semester[:-1]] = [ects]
            else:
                ects_by_semester[semester[:-1]].append(ects)
        return ects_by_semester

#4.1.d)

add_grade("my_studies.txt")
print(get_list_lectures("my_studies.txt"))
print(get_lectures_by_semester("my_studies.txt"))
print(get_ects_by_semester("my_studies.txt"))