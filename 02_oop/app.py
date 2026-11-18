class student:

    def __init__(self, name, age, city, std):
        self.name = name
        self.age = age
        self.city = city
        self.std = std

    def get_info(self):
        print("This is Student Information")
        print("Student name is :- ", self.name)
        print("Student age :-", self.age)
        print("Student city :-", self.city)
        print("Student std :-", self.std)


s = student("Raju", 21, "Surat", "12th")

