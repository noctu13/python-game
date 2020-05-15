import random

HP_BASE = 100
SP_BASE = 100
MP_BASE = 100
SPEED_BASE = 100
INITIATIVE_BASE = 100
ATTRIBUTES = ['name', 'status', 'klass', 'race']

class unit():
    def __init__(self, **feature):
        self.heals_point = HP_BASE
        self.stamina_point = SP_BASE
        self.mana_point = MP_BASE
        self.speed = SPEED_BASE
        self.initiative = INITIATIVE_BASE
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
            elif item == 'human':
                self.initiative *= 2

    def show(self):
        for item in ATTRIBUTES:
            print(item + ':', ' '.join(self.__dict__[item]))

def shuffle_slice(a, start, stop):
    i = start
    while(i < stop):
        idx = random.randint(i, stop)
        a[i], a[idx] = a[idx], a[i]
        i += 1

def init_group():
    xiorun = unit(
        name=['Xiorun'], 
        race=['human'], 
        klass=['warrior'],
        status=['raged'])
    inlae = unit(
        name=['Inlae'], 
        race=['human'], 
        klass=['mage'])
    sigmir = unit(
        name=['Sigmir'],
        race=['silf'], 
        klass=['mage'],
        status=['obsessed', 'immortal'])
    return [xiorun, inlae, sigmir]

def main():
    random.seed()
    group = init_group()
    tick = 0
    while tick < 201:
        equal_speed_list = []
        start = -1
        for item in group:
            if not tick % round(100 * SPEED_BASE/item.speed):
                equal_speed_list += [item]
        equal_speed_list.sort(key=lambda x: x.initiative, reverse=True)
        for i in range(len(equal_speed_list)-1):
            if equal_speed_list[i].initiative == equal_speed_list[i+1].initiative:
                if start < 0:
                    start = i
            elif start >= 0:
                shuffle_slice(equal_speed_list, start, i)
                start = -1
        if start >= 0:
            shuffle_slice(equal_speed_list, start, len(equal_speed_list)-1)
        for item in equal_speed_list:
            print(tick, item.name, item.speed, item.initiative)
        tick += 1

if __name__ == '__main__':
    main()