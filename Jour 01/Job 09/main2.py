class Student:
    def __init__(self, first_name, last_name, student_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_number = student_number
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()

    def get_credits(self):
        return self.__credits

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print("Nom :", self.__last_name)
        print("Prénom :", self.__first_name)
        print("Identifiant :", self.__student_number)
        print("Niveau :", self.__level)