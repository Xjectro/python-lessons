class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"Student: {self.name}, GPA: {self.gpa}"

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):  # Greater Then
        return self.gpa > other.gpa

    def __lt__(self, other):  # Less Then
        return self.gpa < other.gpa

    def __add__(self, other):
        return self.gpa + other.gpa

    def __contains__(self, item):
        return item in self.name

    def __getitem__(self, key):
        match key:
            case "name":
                return self.name
            case "gpa":
                return self.gpa
            case _:
                raise KeyError(f"Unknown key: {key}")


student1 = Student("John", 3.5)
student2 = Student("Jane", 3.8)

print(student1)
print(student1 > student2)
print(student1 < student2)
print(student1["name"])
print(student1 + student2)
