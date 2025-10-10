import json
import urllib.request


def retrieve_all():
    my_request = urllib.request.urlopen("https://suaps.it/api/course/available?type=1")
    courses_bytes = my_request.read()
    all_courses = json.loads(courses_bytes)
    info_cours = all_courses["courses"]

    for course in info_cours:
        dispos = course["limit"] - course["registrationsNumber"]
        if dispos > 0 and "Personnel" not in course["name"]:
            if course["startDay"] == 4:
                print(course["name"], "jeudi", course["startTime"], dispos)
            if course["startDay"] == 5:
                print(course["name"], "vendredi", course["startTime"], dispos)

    return all_courses


def main():
    retrieve_all()

if __name__ == "__main__":
    main()
