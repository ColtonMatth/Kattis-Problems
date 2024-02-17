#Name: Colton Matthews
#File: deathtaxes.py
#Date: 9/22/2022

class Taxmania:
    
    def __init__(self):
        self.share = 0
        self.cost = 0
        self.profit = 0
        self.death = False

    def buy(self, x, y):
        share_count = self.share + x
        self.cost = (self.share * self.cost + x * y) / share_count
        self.share = share_count

    def sell(self, x, y):
        self.share -= x

    def split(self, x):
        self.share *= x
        self.cost /= x
    
    def merge(self, x):
        self.cost *= x
        self.share //= x

    def die(self, y):
        self.death = True
        if y > self.cost:
            self.profit = self.share * (y - (y - self.cost) * 0.3)
        else:
            self.profit = self.share * y

    def action(self, cmd, *args):
        if cmd == 'buy':
            self.buy(*map(int, args))
        elif cmd == 'sell':
            self.sell(*map(int, args))
        elif cmd == 'split':
            self.split(*map(int, args))
        elif cmd == 'merge':
            self.merge(*map(int, args))
        else:
            self.die(*map(int, args))
    
    def __str__(self):
        return '%0.2f' % self.profit

def main():
    Mittens = Taxmania()
    while not Mittens.death:
        Mittens.action(*input().split())
    print(Mittens)

if __name__ == "__main__":
    main()