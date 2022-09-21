import restoran

class Hookah(restoran.Restoran):
    """"""
    def __init__(self, portion, size, cuisine, price, temperature):
        super().__init__(portion, size, cuisine, price, temperature)
        self.virginia = restoran.Tobacco_varieties()

    def prosto(self):
        print('Е-маё')