class CPerson():
    def __init__(self, surname, firstname, lastname, date, month, year, gender):
        self.surname = surname
        self.firstname = firstname
        self.lastname = lastname
        self.date = date
        self.month = month
        self.year = year
        self.gender = gender

    def sey_hello(self):
        self.date_alive = self.date, self.month, self.year
        self.fullname = self.surname, self.firstname, self.lastname
        return f'Hello, my full name is {self.fullname}, my gender is {self.gender}, date of alive {self.date_alive}'

    def __del__(self):
        print('Object destroyed')

oleg = CPerson('Barankov', 'Oleg', 'Ivanovich', '16', '08', '1980', 'male')


print(oleg.surname)
oleg.surname = 'Johorov'
print(oleg.surname)
print(oleg.sey_hello())

del oleg