from people import Person


class Student(Person):
    def __init__(self, first_name, last_name, birth_year, course):
        super().__init__(first_name, last_name, birth_year)
        self.course = course

    def can_enroll(self):
        if self.birth_year<2000:
            return True
        else:
            return False

aquiles = Student('Aquiles', 'Carattino', 1986, 'Python')
aquiles.calculate_age()
print(aquiles.can_drink_beer())
if aquiles.can_enroll():
    print(aquiles.name, 'can enroll to', aquiles.course)

