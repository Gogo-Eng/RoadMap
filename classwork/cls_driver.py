#!/usr/bin/python3
from cls import Student, RemoteStudent
from datetime import date
import json


Student_1 = Student("Gogo", 20, 25)
Student_2 = Student("Igben", 20, 25)
print(Student_1)

print()

print(f"{Student_1.School = }")
print(f"{Student_2.School = }")

print()

Student_1.School = ("Plural Academy")
print(f"{Student_1.School = }")
print(f"{Student_2.School = }")

print()
Student_1.defer(22, "continue from where stopped")

print()

Student_1.update_school("Plural Academy") # it can also be accessed with either Student_1 or Student_2
print(f"{Student_1.School = }")
print(f"{Student_2.School = }")

print()

result = Student_1.check_for_captains_log_day(date(2024, 5, 26))
if result is True:
    print("Today is a captains log day")
else:
    print("Today is not captains log day")

print()

r_1 = RemoteStudent("Wisdom", 22, 21, "Teusday")
print(r_1)

print()

print(f"{r_1.School = }")

print()

print(f"{r_1.day_off = }")

r1_dictionary = r_1.dict()
r_1.save(**r1_dictionary)

try: 
    with open("RemoteStudent.json", "r") as file:
        content_str = file.read()
        print(content_str)
        print()
        content = json.loads(content_str)
        print(f"{content} / Content class: {type(content)}")
except Exception:
    pass

