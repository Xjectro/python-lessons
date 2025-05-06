class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"Name: {self.name}, Position: {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer"]
        return position in valid_positions


employee1 = Employee("Alice", "Developer")
employee2 = Employee("Bob", "Manager")
employee3 = Employee("Charlie", "Intern")

print(Employee.is_valid_position("Manager"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
