import random as rd
import math as m

class Hero:
    '''Defines the role of Heros'''
    hero_list = ["feriro","negari","rapidee","dargonniang", "hacker"]
    def __init__(self, name, user_input=0):
        self.name = name
        self.user_input = user_input
        if int(self.user_input) not in [0,1,2,3,4]:
            self.user_input = 0
        self.user_input = self.hero_list[int(self.user_input)]

    def __repr__(self):
        return f"You are our hero: {self.name}! But you are called {self.user_input} now! "

class Sidekick:
    '''Defines the role of Sidekicks'''
    def __init__(self, nickname, function):
        self.nickname = nickname
        self.function = function

    def __str__(self):
        return f'You sidekick is {self.nickname} who can {self.function}.'

class Alien:
    '''Defines the role of Villains'''
    IQ_level = []
    power_level = []
    energy_level = []
    weakness_list = ["scorpio", "gelato", "tempeh", "water", "coding", "nothing"]
    x = 10 #complexity

    for i in range(x): # define the options for different combinations
        IQ_level.append((i+1) * (x**2))
        power_level.append(m.exp((i/2)*m.sqrt(x)))
        energy_level.append(m.pi ** (m.sqrt(x)))

    def __init__(self, name, energy=100, power=100, IQ=1000):
        self.name = name
        self.energy = energy
        self.power = power
        self.IQ = IQ

    def __str__(self):
        self.power = rd.choice(self.power_level)
        self.weakness_list = rd.choice(self.weakness_list)
        self.energy = rd.choice(self.energy_level)
        self.IQ = rd.choice(self.IQ_level)
        w = rd.choice(self.weakness_list)
        return f'{self.name} is an alien with an IQ level of {int(self.IQ)}, ' \
            f'power level of {int(self.power)}, and energy level of {int(self.energy)}, ' \
            f'who is afraid of {rd.choice( ["scorpio", "gelato", "tempeh", "water", "coding", "nothing"])}.'


# subclasses
class Weapon(Alien):
    def __init__(self,name, use):
        super().__init__(self, name)
        self.use = use


class Military(Alien):
    def __init__(self, name, rank):
        super().__init__(self, name)
        self.rank = rank


class Experience(Alien):
    def __init__(self, name, num_of_battle):
        super().__init__(self, name)
        self.num_of_battle = num_of_battle






martin = Alien("Mr. Martin")
print(martin)

mel = Hero("casey", 7)
print(mel)

seb = Sidekick("Seleni","escape into thin air")
print(seb)
