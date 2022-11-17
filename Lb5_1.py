import random
class Dice:
    def __init__(self, edges=6, dice_quantity=1):
        self.edges = 6
        self.dice_quantity = 1

    def choose_dice_and_edges_quantity(self):
        self.edges = int(input('Введите число граней: '))
        self.dice_quantity = int(input('Введите число кубиков: '))
    
    def roll_the_dice(self):
        lst = []
        for i in range(self.dice_quantity):
            lst.append(random.randrange(start=1, stop=self.edges+1))
        return lst

kubik = Dice()
kubik.choose_dice_and_edges_quantity()
print(kubik.roll_the_dice())