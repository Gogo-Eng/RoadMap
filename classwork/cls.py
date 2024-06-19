#!/usr/bin/python3
import json

class Student:
    School = "ALX"
    Student_type = "Remote"

    def __init__(self, name, cohort, age):
        self.student_name = name
        self.student_age = age
        self.student_cohort = cohort
    
    def __str__(self):
        return(
            f"Student name = {self.student_name}\n"
            f"Student age = {self.student_age}\n"
            f"Student cohort = {self.student_cohort}\n"
        )
    
    def defer(self, new_cohort, option="start afresh"):
        if self.student_cohort == new_cohort:
            print("You are not able to defer to the same cohort")
            return
        print(f"you have successfully deferred from {self.student_cohort} to {new_cohort} with the option to {option}")
                

    @classmethod
    def update_school(cls, new_school):
        cls.School = new_school

    @staticmethod
    def check_for_captains_log_day(date):
        if 5 <= date.isoweekday() <= 7:
            return True
        else:
            return False

    def dict(self):
        return self.__dict__
    
    def save(self, **kwargs):
        with open(f"{self.__class__.__name__}.json", "w") as file:
            json.dump(kwargs, file)

class RemoteStudent(Student):
    School = "ALT School"
    
    def __init__(self, name, cohort, age, freeday="Friday"):
        Student.__init__(self, name, cohort, age)
        self.day_off = freeday

    def __str__(self):
        return f"{super().__str__()}{self.Student_type = }"