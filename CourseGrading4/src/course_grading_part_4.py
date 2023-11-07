# tee ratkaisu tänne
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    course_info = input("Course information: ")
# else:
#     # hard-coded input
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"
#     exam_data = "exam_points1.csv"
#     course_info = "course1.txt"

names = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        names[parts[0]] = f"{parts[1]} {parts[2].strip()}"

exercises = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exercises[parts[0]] = []
        for exercise in parts[1:]:
            exercises[parts[0]].append(int(exercise))

exams = {}

with open(exam_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exams[parts[0]] = []
        for exam in parts[1:]:
            exams[parts[0]].append(int(exam))

def grader(exercises: int, examz: int):
    # total exercises points = 40

    exercise_pts = int((exercises / 0.4) // 10)
    grade_pts = examz + exercise_pts

    if grade_pts <= 14:
        return 0
    elif grade_pts <= 17:
        return 1
    elif grade_pts <= 20:
        return 2
    elif grade_pts <= 23:
        return 3
    elif grade_pts <= 27:
        return 4
    else:
        return 5

def course_provider(filename: str):
    course = []
    with open(filename) as new_file:
        for line in new_file:
            parts = line.replace("\n", "")
            split_part = parts.split(":")
            course.append(split_part[1].lstrip())
    return f"{course[0]}, {course[1]} credits"

def writer(filename: str):
    filename = course_info
    with open("results.txt", "w") as new_file:
        new_file.write(f"{course_provider(filename)}\n")
        new_file.write(f'{"="*len(course_provider(filename))}\n')
        new_file.write(f'{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}\n')
        for pic, name in names.items():
            if pic in exercises:
                exercizez = exercises[pic]
            if pic in exams:
                exam_results = exams[pic]
                one = 30-len(name)+len(str(sum(exercizez)))
                two = 10+len(str(int(((sum(exercizez)) / 0.4) // 10)))-len(str(sum(exercizez)))
                three = 10-len(str(int(((sum(exercizez)) / 0.4) // 10)))+len(str(sum(exam_results)))
                four = 10-len(str(sum(exam_results)))+len(str((int(((sum(exercizez)) / 0.4) // 10)) + (sum(exam_results))))
                five = 10-len(str((int(((sum(exercizez)) / 0.4) // 10)) + (sum(exam_results))))+len(str(grader(sum(exercizez), sum(exam_results))))
                new_file.write(f"{name}{sum(exercizez):>{one}}{int(((sum(exercizez)) / 0.4) // 10):>{two}}{sum(exam_results):>{three}}{(int(((sum(exercizez)) / 0.4) // 10)) + (sum(exam_results)):>{four}}{grader(sum(exercizez), sum(exam_results)):>{five}}\n")

    with open("results.csv", "w") as new_file:
        for pic, name in names.items():
            if pic in exercises:
                exercizez = exercises[pic]
            if pic in exams:
                exam_results = exams[pic]
                line = f"{pic};{name};{grader(sum(exercizez), sum(exam_results))}"
                new_file.write(line+"\n")

# txt_writer()
writer(course_info)
