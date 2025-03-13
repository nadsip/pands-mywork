students = []

while True:
    # Read student name (stop if blank)
    name = input("\nEnter student name (press Enter to finish): ").strip()
    if not name:
        break
    
    # Initialize student structure
    student = {
        "name": name,
        "modules": []
    }
    
    # Collect module names
    courses = []
    while True:
        course = input("Enter module name (press Enter to finish modules): ").strip()
        if not course:
            break
        courses.append(course)
    
    # Collect grades for each course
    for course in courses:
        grade = int(input(f"Enter grade for {course}: "))
        student["modules"].append({
            "courseName": course,
            "grade": grade
        })
    
    students.append(student)

# Display all students and their results
print("\nStudent Results:")
for student in students:
    print(f"\nStudent: {student['name']}")
    for module in student["modules"]:
        print(f"\t{module['courseName']} \t: {module['grade']}")
    if not student["modules"]:
        print("\tNo modules entered")

print("\nEnd of student list")