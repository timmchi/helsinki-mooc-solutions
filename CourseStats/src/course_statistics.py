# Write your solution here
import urllib.request
import json
import math

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")

    course_list = json.load(my_request)
    courses = []

    for course in course_list:
        if course['enabled'] == True:
            courses.append((course['fullName'], course['name'], course['year'], sum(course['exercises'])))


    return courses

def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")

    course_info = json.load(my_request)

    weeks = len(course_info)
    students = 0
    hours = 0
    exercises = 0
    for i in course_info:
        if int(course_info[i]['students']) > students:
            students = int(course_info[i]['students'])
        hours += int(course_info[i]['hour_total'])
        exercises += int(course_info[i]['exercise_total'])

    hours_average = math.floor(hours / students)
    exercises_average = math.floor(exercises / students)

    return {
    'weeks': weeks,
    'students': students,
    'hours': hours,
    'hours_average': hours_average,
    'exercises': exercises,
    'exercises_average': exercises_average
    }

    # for i in course_info:
    #     print(course_info[i])
    

# print(retrieve_course("docker2019"))

# retrieve_all()