from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        self._email = value

    @abstractmethod
    def role_info(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"
    

class Student(Person):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id

    def role_info(self):
        return f"Student: {self.name}, ID: {self.student_id}"

class Lecturer(Person):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def role_info(self):
        return f"Lecturer: {self.name}, Subject: {self.subject}"

    def __str__(self):
        return f"Lecturer: {self.name} Email: {self.email}, Subject: {self.subject}"

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f"Course: {self.course_name}, Students: {len(self.students)}"

stu1 = Student("Aryan", "rahimullaharyan2006@gmail.com", "CS0211")
stu2 = Student("Sahil", "hashmatullahsahil1516@gmail.com", "CS0211")

lec1 = Lecturer("Mr. Khaliqyar","ahmadroheedkhaliqyar@gmail.com", "Advanced Programming")

course = Course("Advanced Programming")

course.add_student(stu1)
course.add_student(stu2)

people = [stu1, stu2, lec1]

for person in people:
    print(person.role_info())

print("\nCourse Information:")
print(course)

print("\nStudents in Course:")
for student in course.students:
    print(student)