# Write your solution here
import json
import urllib.request
import math


def retrieve_all():
    active_courses = []
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    courses_bytes = my_request.read()
    all_courses = json.loads(courses_bytes)
    
    for course in all_courses:
        sum_exercises = 0
        if course["enabled"] == True:
            for exo in course["exercises"]:
                sum_exercises += exo
            active_courses.append((course["fullName"], course["name"], course["year"], sum_exercises))

    return active_courses


def retrieve_course(course_name: str) -> dict:
    stats_course = {}
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats".replace("****", course_name)
    my_request = urllib.request.urlopen(url)
    courses_bytes = my_request.read()
    course_data = json.loads(courses_bytes)

    weeks = 0
    students = 0
    hours = 0
    hours_average = 0
    exercises = 0
    exercises_average = 0
    for week in course_data:
        weeks += 1
        if course_data[week]["students"] > students:
            students = course_data[week]["students"]
        hours += course_data[week]["hour_total"]
        hours_average = math.floor(hours / students)
        exercises += course_data[week]["exercise_total"]
        exercises_average = math.floor(exercises / students)


    stats_course["weeks"] = weeks
    stats_course["students"] = students
    stats_course["hours"] = hours
    stats_course["hours_average"] = hours_average
    stats_course["exercises"] = exercises
    stats_course["exercises_average"] = exercises_average

    print(stats_course)
    return stats_course


def main():
    retrieve_all()
    course_name = "docker2019"
    retrieve_course(course_name)


if __name__ == "__main__":
    main()

