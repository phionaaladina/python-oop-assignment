"""
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
"""

#create a class, a class name starts with a capital letter and always in singular
# class Cohort:
#name
#description
#start date
#end date
#total students number

#ASSIGNMENT Deadline Monday evening
#READ ABOUT CONSTRUCTORS & OBJECTS/INSTANCES

#add a condtructor for the Cohort class
#add a method(function) to the class that prints the cohort name and the total number of students
#create a new instance(object) of the cohort class

class Cohort:
    # Constructor to initialize the attributes of the cohort
    def __init__(self, name, description, start_date, end_date, total_students):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.total_students = total_students

    # Method to print the cohort's name and the total number of students
    def print_cohort_info(self):
        print(f"Cohort Name: {self.name}")
        print(f"Total Students: {self.total_students}")

# Creating a new instance (object) of the Cohort class
cohort1 = Cohort(
    name="Python Beginners",
    description="A cohort for beginners learning Python programming.",
    start_date="2024-11-01",
    end_date="2024-12-01",
    total_students=25
)

# Calling the method to print the cohort's information
cohort1.print_cohort_info()
