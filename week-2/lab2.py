from typing import TypedDict

class Student(TypedDict):
    name: str
    courses: set[str]


students: dict[str, Student] = {
    "S001": {
        "name": "Aryan",
        "courses": {"CS101", "CS102"}
    },
    "S002": {
        "name": "Ahmad",
        "courses": {"CS102", "CS103"}
    },
    "S003": {
        "name": "Ali",
        "courses": {"CS101", "CS104"}
    }
}

def add_course(student_id, course_code):
    if student_id not in students:
        print("Student not found.")
        return

    courses= students[student_id]["courses"]

    if course_code in courses:
        print(f"{course_code} is already registered.")
    else:
        courses.add(course_code)
        print(f"{course_code} registered successfully.")


def drop_course(student_id, course_code):
    if student_id not in students:
        print("Student not found.")
        return

    courses = students[student_id]["courses"]

    if course_code in courses:
        courses.remove(course_code)
        print(f"{course_code} dropped successfully.")
    else:
        print(f"{course_code} is not registered.")


def common_courses(student1_id, student2_id):
    courses1: set[str] = students[student1_id]["courses"]
    courses2: set[str] = students[student2_id]["courses"]

    return courses1 & courses2


def all_courses():
    unique_courses = set()

    for student in students.values():
        unique_courses |= student["courses"]

    return unique_courses


def display_students():
    for student_id, student in students.items():
        print(f"ID: {student_id}")
        print(f"Name: {student['name']}")
        print(f"Courses: {student['courses']}")
        print()



add_course("S001", "CS103")
add_course("S001", "CS101")

drop_course("S001", "CS102")

print("Common courses:", common_courses("S001", "S002"))
print("All unique courses:", all_courses())

print("\nStudent Records:")
display_students()
