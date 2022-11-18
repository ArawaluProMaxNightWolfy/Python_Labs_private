import random
class Dice:
    def __init__(self, edges=6, dice_quantity=1):
        self.edges = 6
        self.dice_quantity = 1

    def choose_dice_and_edges_quantity(self):
        self.edges = int(input('Введите число граней: '))
        self.dice_quantity = int(input('Введите число кубиков: '))
    
    def roll_the_dice(self, seed=None):
        lst = []
        random.seed(a = seed)
        for i in range(self.dice_quantity):
            lst.append(random.randrange(start=1, stop=self.edges+1))
        return lst

kubik = Dice()
kubik.choose_dice_and_edges_quantity()
dct = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
for i in range(100000): #подсчёт кол-ва чисел от 2 до 12 в последовательности
    random.setstate(random.getstate())
    summa = kubik.roll_the_dice()[0]+kubik.roll_the_dice()[1]
    for key in dct:
        if key == summa:
            dct[key] += 1
    random.seed(a = None)

sequence_range = 0 #создаём процентную статистику
for key in dct: 
    sequence_range += dct[key]
for key in dct:
    print(str(key) + ':' + str(round(dct[key]/sequence_range*100, 2)) + '%', end='   ')