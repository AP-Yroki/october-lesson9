class Phone():
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def sey_info(self):
        return print(f'Номер: {self.number}, модель телефона:  {self.model} вес телефона: {self.weight}')
    def reciveCall(self, name):
        return print(f'Вам звонит: {name}')

    def getNumber(self):
        return print(self.number)


iphon = Phone(+790920539, "Iphon promax 16", 200)
nakia = Phone(+909777309, 'Nokiea3320', 200)
airponme = Phone(+777555544, 'AiroPhone', 123)

iphon.sey_info(), nakia.sey_info(), airponme.sey_info()

iphon.reciveCall('Боб')
nakia.reciveCall('Джон')
airponme.reciveCall('Александр')

iphon.getNumber()
nakia.getNumber()
airponme.getNumber()
