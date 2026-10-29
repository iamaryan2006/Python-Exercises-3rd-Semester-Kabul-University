from typing import TypeVar, Generic

T = TypeVar("T")


class Manager(Generic[T]):
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def get_all(self):
        return self.items


students = {}


def add_student(student_id, name):
    if student_id in students:
        print("Student already exists.")
        return

    students[student_id] = {
        "name": name,
        "courses": set()
    }
    print("Student added successfully.")


def register_course(student_id, course_code):
    if student_id not in students:
        print("Student not found.")
        return

    courses = students[student_id]["courses"]

    if course_code in courses:
        print("Course already registered.")
        return

    courses.add(course_code)
    print("Course registered successfully.")


def drop_course(student_id, course_code):
    if student_id not in students:
        print("Student not found.")
        return

    courses = students[student_id]["courses"]

    if course_code not in courses:
        print("Course not found.")
        return

    courses.remove(course_code)
    print("Course dropped successfully.")


def search_student(student_id):
    student = students.get(student_id)

    if student is None:
        print("Student not found.")
        return

    print(f"ID: {student_id}")
    print(f"Name: {student['name']}")
    print(f"Courses: {student['courses']}")


def all_courses():
    return {
        course
        for student in students.values()
        for course in student["courses"]
    }


def students_by_course(course_code):
    return [
        student["name"]
        for student in students.values()
        if course_code in student["courses"]
    ]


def display_students():
    sorted_students = sorted(
        students.items(),
        key=lambda item: item[1]["name"]
    )

    for student_id, student in sorted_students:
        print(
            f"ID: {student_id}, "
            f"Name: {student['name']}, "
            f"Courses: {student['courses']}"
        )


add_student("S001", "Aryan")
add_student("S002", "Ahmad")
add_student("S003", "Ali")

register_course("S001", "CS101")
register_course("S001", "CS102")
register_course("S002", "CS101")
register_course("S002", "CS103")
register_course("S003", "CS102")

print("\nSearch Student:")
search_student("S001")

print("\nDrop Course:")
drop_course("S001", "CS102")

print("\nAll Unique Courses:")
print(all_courses())

print("\nStudents Registered in CS101:")
print(students_by_course("CS101"))

print("\nStudents Sorted by Name:")
display_students()

manager = Manager[str]()
manager.add("Python")
manager.add("Java")

print("\nGeneric Manager:")
print(manager.get_all())