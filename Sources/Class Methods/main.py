class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"Name: {self.name}, GPA: {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total Students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"


student1 = Student("John", 3.5)
student2 = Student("Jane", 3.8)
student3 = Student("Doe", 3.9)

print(Student.get_count())
print(Student.get_average_gpa())
