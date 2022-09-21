class Computer():
    """Класс про компьютер"""
    def __init__(self, monitor, mouse, system_block, memory, modem):
        """Ициализация компонентов: монитор, мышь, системный блок, клавиатура и модем"""
        self.monitor = monitor
        self.mouse = mouse
        self.system_block = system_block
        self.memory = memory
        self.modem = modem
        self.RAM = 8

    def desc_computer(self):
        """Выводит характеристики данного компьютера"""
        print("Все характеристики данного компьютера:", self.monitor +', '+ self.mouse +', '+ self.system_block +', '+ str(self.memory) + ' Гигабайт' +', '+ self.modem)

    def RAMPLUS(self, gb):
        """Добавляем оперативу"""
        self.RAM += gb
        print('Рам прибыло и её стало вот столько - ' + str(self.RAM) + ' Гигабайт')


    def changing_memory(self, gb):
        """Изменяем значения памяти"""
        memorY = self.memory + gb
        if self.memory < memorY:
            print("Информации стало больше. Вот столько памяти стало: " + str(memorY))
        else:
            print("Информации стало меньше. Вот столько памяти стало: " + str(memorY))


    def MonitOff(self):
        """Ломаем монитор"""
        print('Кто-то кинул в монитор кирпич')
        self.monitor = 'bad'
        print('Теперь у него такое состояние: ' + self.monitor)

    def internet(self, hastota):
        """Определяем качество интернета"""
        if 100 <= hastota <= 200:
            print('Качество интернета прекрасное')
        else:
            print('Качество интернета очень плохое')

PC1 = Computer('Big', 'little', 'Good', 310, 'работает')

PC1.desc_computer()
PC1.RAMPLUS(8)
PC1.changing_memory(20)
PC1.MonitOff()
PC1.internet(100)