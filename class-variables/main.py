class Student:
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

print(student1.name)
print(student2.age)
print(student1.class_year)

print(f"Total number of students: {Student.num_students}")
