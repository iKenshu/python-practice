from dataclasses import dataclass
from typing import List


@dataclass
class Courses:
    """ Simple class for courses"""

    name: str
    description: str
    career: str
    quantity_of_students: int
    students_approved: int

    def percentage_of_approved(self):
        percentage = (self.students_approved / self.quantity_of_students) * 100
        return f'{percentage:.2f}% approved this course'


@dataclass
class Careers:
    """ A Class that receive a list of Courses """
    courses: List[Courses]


Python = Courses('Python', 'Learn all about Python', 'Python Developer', 25000, 5234)
Django = Courses('Django', 'Learn all about Django', 'Python Developer', 25000, 5234)

Career = Careers([Python, Django])
print(Career.courses[0].name)
