import requests
from copy import deepcopy
from functools import reduce
import random


class TeamMatcher:

    def __init__(self, link):
        self.data = self._set_data(link)
        self.courses_dictionary = self._set_courses_dictionary(self.data)
        self.students = []

    def _set_data(self, link):
        r = requests.get(link, verify=False)
        return r.json()

    def _set_courses_dictionary(self, data):
        # make a list of the unique courses
        lst = deepcopy(data)
        lst = list(map(lambda x: x['courses'], lst))
        lst = list(reduce(lambda x, y: x + y, lst))
        lst = list(map(lambda x: x['name'], lst))
        lst = list(set(lst))
        # link every course to id number
        dictionary = {}
        num = len(lst)
        while num > 0:
            dictionary[num] = lst[num - 1]
            num -= 1
        # return courses with their id
        return dictionary

    def list_courses(self):
        print("Here are the courses:")
        index = 1
        while index <= len(self.courses_dictionary):
            print("[{}] {}".format(index, self.courses_dictionary[index]))
            index += 1

    def match_teams(self, course_id, team_size, group_time):
        self.students = self._set_students(course_id, group_time)
        if self.students != []:
            self.students = sorted(self.students,
                                   key=lambda *args: random.random())
            for index, student in enumerate(self.students):
                if index % team_size == 0:
                    print("==========")
                print(student)
        else:
            print("There aren't students in this group at this time.")

    def _set_students(self, course_id, group_time):
        course = self.courses_dictionary[course_id]
        lst = deepcopy(self.data)
        lst = list(filter(lambda x: self._is_from_the_course(
            x, course, group_time), lst))
        lst = list(map(lambda x: x['name'], lst))
        return lst

    def _is_from_the_course(self, student, c, gr):
        courses = student['courses']
        for course in courses:
            if course['name'] == c and course['group'] == gr:
                return True
        return False

    def get_user_opinion(self):
        print("\nHello, you can use one of the following commands:"
              "\nlist_courses - this lists all the courses that are available"
              " now.\nmatch_teams <course_id> <team_size> <group_time>"
              "\nexit - to exit from the program")

        while True:
            reply = input("\nYour choice: ")
            if reply == 'exit':
                break
            elif reply == 'list_courses':
                self.list_courses()
            elif reply.count('match_teams') == 1:
                lst = reply.split()
                lst = lst[1:]
                lst = list(map(lambda x: int(x), lst))
                self.match_teams(lst[0], lst[1], lst[2])
            else:
                print("There is no such option...")


def main():
    TeamMatcher('https://hackbulgaria.com/api/students/').get_user_opinion()

if __name__ == '__main__':
    main()
