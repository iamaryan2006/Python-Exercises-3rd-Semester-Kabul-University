students_names = ["A","B","C","D","E","F","G","H","I","J"]
students_scores = [90,76,86,88,90,50,50,97,77,100]

minimum = min(students_scores)
maximum = max(students_scores)
average = sum(students_scores) / len(students_scores)

print(minimum)
print(maximum)
print(average)

new_list = [v for v in students_scores if v >= 60]

print(set(new_list))

students = {
    "S001": "Aryan",
    "S002": "Ahmad",
    "S003": "Ali",
    "S004": "Mohammad"
}

print(students["S001"])

update = sorted(
    zip(students_names, students_scores),
    key=lambda e: e[1],reverse = True
)

print(update)
