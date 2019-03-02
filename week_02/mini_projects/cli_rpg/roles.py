import random as rd
import math as m

hero_list = {"Fisib": "You can fly and be invisible.", "Musbit":
    "You have superb physical strength and hacker skills",
             "Drog": "You can turn to a fire dragon with invisible skins."}


class Hero:
    '''Defines the role of Heros'''
    def __init__(self, user_input="Fisib"):
        self.user_input = user_input
        x=""
        if self.user_input.capitalize() not in ["Fisib", "Musbit", "Drog"]:
            self.user_input = "Fisib"
        self.x = hero_list[self.user_input.capitalize()]

    def __repr__(self):
        return f"You are our hero: {self.user_input} now! {self.x}"


class Sidekick:
    '''Defines the role of Sidekicks'''
    def __init__(self, nickname, function):
        self.nickname = nickname
        self.function = function

    def __str__(self):
        return f'You sidekick is {self.nickname} who can {self.function}.'


def Sidekick_effect(hero, side):
    '''Testing what effect the sidekick will have on the hero
    inputs: hero instance, sidekick instance
    '''
    if 20 >len(Sidekick.function) > 10:
        Alien.IQ /= 2
    elif len(Sidekick.function)< 5:
        Alien.energy = m.log10(Alien.energy)
    elif 5 < len(Sidekick.function) < 10:
        Alien.energy = m.log2(Alien.energy)
    elif len(Sidekick.function) == 5 or len(Sidekick.function) ==10:
        Alien.IQ /=10


class Alien:
    '''Defines the role of Villains'''
    IQ_level = []
    power_level = []
    energy_level = []
    weakness_list = ["scorpio", "gelato", "tempeh", "water", "coding", "nothing"]
    x = 10 #complexity


    def __init__(self, name, energy=100, IQ=1000, weakness="nothing"):
        self.name = name
        self.energy = energy
        self.IQ = IQ
        self.weakness = weakness

        self.weakness_list = rd.choice(self.weakness_list)
        self.energy = rd.choice(self.energy_level)
        self.IQ = rd.choice(self.IQ_level)
        self.weakness = rd.choice(self.weakness_list)

    for i in range(x): # define the options for different combinations
        IQ_level.append((i+1) * (x**2))
        energy_level.append(m.pi ** (m.sqrt(x)))

    def __str__(self):

        return f'{self.name} is an alien with an IQ level of {int(self.IQ)}, ' \
            f'and energy level of {int(self.energy)}, ' \
            f'who is afraid of {self.weakness}.'


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

mel = Hero("fab")
print(mel)

seb = Sidekick("Sadie","vanish into thin air")
print(seb)
