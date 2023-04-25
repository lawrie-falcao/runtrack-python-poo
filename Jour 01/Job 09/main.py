class Student:
    def __init__(self, first_name, last_name, student_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_number = student_number
        self.__credits = 0

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits

    def get_credits(self):
        return self.__credits


john = Student("John", "Doe", 145)
john.add_credits(10)
john.add_credits(20)
john.add_credits(30)
print(john.get_credits())