class AirConditioner:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity
    
    def turn_on(self):
        print('Сейчас в комнате станет холоднее')

Frezze = AirConditioner('Эльбрус-12415', 1009)
Frezze.turn_on()