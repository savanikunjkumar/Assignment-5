# Create a dictionary of student marks
student_marks = {
    "Rahul": 85,
    "Ayesha": 92,
    "Karan": 78,
    "Neha": 88
}

# Ask user to input student name
name = input("Enter student name: ")

# Retrieve and display marks
if name in student_marks:
    print(f"Marks of {name}: {student_marks[name]}")
else:
    print("Student not found.")
