# i. Create a dictionary with student names and their marks
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92
}

# ii. Use a loop to print each student's name and mark
print("Student Marks:")
for name, mark in students.items():
    print(f"{name}: {mark}")

# iii. Calculate and print the average mark
total_marks = sum(students.values())
average_mark = total_marks / len(students)
print(f"\nAverage Mark: {average_mark:.2f}")