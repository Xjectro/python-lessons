class Car:
    def __init__(self, model, year, color, for_sale=False):
        self.model = model
        self.year = year
        self.color = color
        self.__for_sale = for_sale  # Private attribute

    def drive(self):
        print(f"The {self.color} {self.model} is driving.")

    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")
