import requests
from random import shuffle

r = requests.get('https://hackbulgaria.com/api/students/', verify=False)
# print(r.json()[1])
# print(r.json()[1]["name"])
# print(r.json()[1]["courses"])
# print(r.json()[1]["courses"][0]["group"])# values 1 or 2
# print(r.json()[1]["courses"][0]["name"])
# print(len(r.json()))

# for i in r.json()[1]["courses"]:
#     print(r.json[1]["courses"][i]["name"])


def list_courses():
    courses = []
    for i in range(0, len(r.json()) - 1):
        for j in range(len(r.json()[i]["courses"])):
            if not r.json()[i]["courses"][j]["name"] in courses:
                courses.append(r.json()[i]["courses"][j]["name"])
    index = 1
    indexed = {}
    for course in courses:
        indexed[index] = course
        index += 1
    return indexed


def print_courses():
    for indx in list_courses():
        print("[%d] %s" % (indx, list_courses()[indx]))
    return True

# print(print_courses())

def match_command(course_id, team_size, group_time):
# course_id = 1
# team_size = 2
# group_time = 1
    course = list_courses()[course_id]
    people = []
    for i in range(0, len(r.json()) - 1):
        # if r.json()[i]["available"]:
        for j in range(len(r.json()[i]["courses"])):
            if course == r.json()[i]["courses"][j]["name"] and r.json()[i]["courses"][j]["group"] == group_time:
                people.append(r.json()[i]["name"])
    shuffle(people)
    # print(people)
    ts = 0
    person_index = 0
    while ts < 3:
        if person_index < len(people):
            if ts < team_size:
                print(people[person_index])
                person_index += 1
                ts += 1
            if ts == team_size:
                print("=================")
                ts = 0
        else:
            ts = 3
    return True

print(match_command(1, 2, 1))

# print("Here are the courses:")
# print(list_courses)
