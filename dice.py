from random import randint
import sys

class dice:
   def __init__(self, sides, rolls):
     self.sides = sides
     self.rolls = rolls
   def roll(self):
       total = 0
       for i in range(0, self.rolls):
           total = total + randint(1, self.sides)
       return(total)

if __name__ == '__main__':
    sides = int(sys.argv[1])
    rolls = int(sys.argv[2])
    trys = int(sys.argv[3])
    counts = []
    bones2d20 = Dice(sides, rolls)
    for i in range(0,rolls * sides + 1):
        counts.append(0)
    for i in range(0,trys):
       turn = bones2d20.roll()
       counts[turn] = counts[turn] + 1
    for n in range(rolls, sides * rolls + 1):
        print "%d - %d" % (n, counts[n])
