class Person:
    def __init__(self, name, last_name='No Last Nime', birth_year=0):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculate_age(self):
        self.age = 2019-self.birth_year

    def print_name(self):
        print(self.name)

    def print_full_name(self):
        print(self.name + ' ' + self.last_name)

    def can_drink_beer(self):
        if self.age >= 18:
            return True

    def is_older_than(self, other_person):
        if self.age > other_person.age:
            return True
        else:
            return False


if __name__ == '__main__':
    me = Person('Aquiles', 'Carattino', 1986)
    me.calculate_age()
    you = Person('José', birth_year=2005)
    you.calculate_age()
    print(me.is_older_than(you))
    print(you.is_older_than(me))