grades = {"Alice": 85, "Bob": 90, "Charlie": 78, "David": 92}

student = input("Enter the name of the student: ")

if student in grades:
    print(f"Student found: {student}, Grade: {grades[student]}")
else:
    print(f"Student not found: {student}")
