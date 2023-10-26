class Reader():
    def __init__(self, surname, firstname, lastname, readbilet, faculty,  date, month, year, number):
        self.surname = surname
        self.firstname = firstname
        self.lastname = lastname
        self.readbilet = readbilet
        self.faculty = faculty
        self.date = date
        self.month = month
        self.year = year
        self.number = number


    def takeBook(self, collected_books):
        fullname = self.surname, self.firstname[0] + '.', self.lastname[0] + '.'
        return print(f'{fullname} взял {collected_books} книги')

    def returnBook(self, returned_books):
        fullname = self.surname, self.firstname[0] + '.', self.lastname[0] + '.'
        return print(f'{fullname} вернул {returned_books} книги')

oleg = Reader('Петров', 'Евгений', 'Александрович', '351-654-33', '30', '12', '12','1983','+78800555535')

oleg.takeBook(3)
oleg.returnBook(3)