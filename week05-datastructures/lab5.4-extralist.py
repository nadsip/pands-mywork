student = {
    "name": input("Enter student name: "),
    "modules": []
}

# a. Collect module names
modules = []
while True:
    course = input("Enter module name (press Enter to finish): ").strip()
    if not course:
        break
    modules.append(course)

# b. Collect grades for each module
for course in modules:
    grade = int(input(f"Enter grade for {course}: "))
    student["modules"].append({
        "courseName": course,
        "grade": grade
    })

# Display results
print(f"\nStudent: {student['name']}")
for module in student["modules"]:
    print(f"\t{module['courseName']} \t: {module['grade']}")