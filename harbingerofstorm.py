HP_BASE = 100
SP_BASE = 100
MP_BASE = 100
SPEED_BASE = 100
ATTRIBUTES = ['name', 'status', 'klass', 'race']

class unit():
    def __init__(self, **feature):
        self.heals_point = HP_BASE
        self.stamina_point = SP_BASE
        self.mana_point = MP_BASE
        self.speed = SPEED_BASE
        for item in ATTRIBUTES:
            self.__dict__[item] = []
        for arg in feature:
            if arg in ATTRIBUTES:
                for item in feature[arg]:
                    self.__dict__[arg] += [item]
            else:
                print('%s - Attribute error!' % arg)
        for item in self.klass:
            if item == 'paladin':
                self.heals_point *= 2
            elif item == 'warrior':
                self.stamina_point *= 2
            elif item == 'mage':
                self.mana_point *= 2
        for item in self.race:
            if item == 'silf':
                self.speed *= 2

    def show(self):
        for item in ATTRIBUTES:
            print(item + ':', ' '.join(self.__dict__[item]))


def init_group():
    xiorun = unit(name=['Xiorun'], status=['raged'], klass=['warrior'])
    inlae = unit(name=['Inlae'], race=['human'], klass=['mage'])
    sigmir = unit(name=['Sigmir'], status=['obsessed', 'immortal'], race=['silf'], klass=['mage'])
    return [xiorun, inlae, sigmir]


def main():
    group = init_group()
    tick = 0
    while tick < 101:
        for item in group:
            if not tick % round(100 * SPEED_BASE/item.speed):
                print(tick, 'name', item.name, round(100 * SPEED_BASE/item.speed))
        tick += 1

if __name__ == '__main__':
    main()