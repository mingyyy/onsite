import random as rd
import math as m

hero_list = {"Fisib": "you can fly and be invisible.", "Musbit":
             "you have superb physical strength and hacker skills.",
             "Drog": "you can turn to a invisible fire dragon."}


class Hero:
    '''Defines the role of Heros'''
    power = 10

    def __init__(self, user_input="Fisib"):
        self.user_input = user_input
        x = ""
        if self.user_input.capitalize() not in ["Fisib", "Musbit", "Drog"]:
            self.user_input = "Fisib"
        self.x = hero_list[self.user_input.capitalize()]
        if self.user_input.capitalize() == "Fisib":
            self.power += 3
        elif self.user_input.capitalize() == "Musbit":
            self.power += rd.randint(1, 10)
        else:
            self.power += 6

    def __repr__(self):
        return f"You are our hero {self.user_input}! You suddenly find that, {self.x}"


class Sidekick:
    '''Defines the role of Sidekicks'''
    def __init__(self, nickname, function):
        self.nickname = nickname
        self.function = function

    def __str__(self):
        return f'You sidekick is {self.nickname} who can {self.function}.'


def sidekick_effect(alien, side):
    '''Testing what effect the sidekick will have on the hero
    inputs: hero instance, sidekick instance
    '''
    if 20 >len(side.function) > 10:
        alien.iq /= 2
    elif len(side.function)< 5:
        alien.energy = m.log10(max(alien.energy, 1))
    elif 5 < len(side.function) < 10:
        alien.energy = m.log2(max(alien.energy, 1))
    elif len(side.function) == 5 or len(side.function) ==10:
        alien.iq /= 10
    else:
        alien.iq /= 3
    return f"Alien now has an IQ of {int(alien.iq)} and energey level of {int(alien.energy)}. "


class Alien:
    '''Defines the role of Villains'''
    IQ_level = []
    power_level = []
    energy_level = []
    # weakness_list = ["scorpio", "gelato", "tempeh", "water", "coding", "nothing"]
    x = 10 # complexity level

    def __init__(self, name, energy=100, iq=1000, weakness=0):
        self.name = name
        self.energy = energy
        self.iq = iq
        self.weakness = weakness

        self.energy = rd.choice(self.energy_level)
        self.iq = rd.choice(self.IQ_level)
        self.weakness = rd.randint(1, 10)

    # define the options for different combinations
    i = rd.randint(1, x)
    IQ_level.append((i+1) * (x**2))
    energy_level.append(m.pi ** (m.sqrt(i)))

    def __str__(self):

        return f'{self.name.capitalize()} is an alien with an IQ level of {int(self.iq)}, ' \
            f'and energy level of {int(self.energy)}. Also very ugly!'


# sub classes: different aliens with different purposes
class Minerals(Alien):
    def __str__(self):
        return f"Alien is here for our minerals."


class Military(Alien): # conquer other planet
    def __str__(self):
        return f"Alien is here to conquer our world and won't stop."


class Training(Alien): # sending troops for training
    def __str__(self):
        return f"Alien is here to train their soldiers."


def alien_purpose(alien, user_input):
    if user_input <= 3:
        alien = Minerals(alien.name)
    elif user_input <= 6:
        alien = Military(alien.name)
    else:
        alien = Training(alien.name)
    return alien


if __name__ == "__main__":
    martin = Alien("Mr. Martin")
    print(martin)

    mel = Hero("fab")
    print(mel)

    seb = Sidekick("Sadie","vanish into thin air")
    print(seb)

    print(sidekick_effect(martin, seb))
