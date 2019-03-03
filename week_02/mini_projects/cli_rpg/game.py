
import random as rd
import datetime as dt
from roles import Hero, Sidekick, Alien, sidekick_effect


def main():
    print_rules()
    play()

def print_rules():
    print("""
***********************************************************
***********************************************************
***********************************************************
***********************************************************
************ Welcome to the world of ALIENs! **************
***********************************************************
***********************************************************
***********************************************************
***********************************************************

The lands of Codingnomads are under alien attack in year 
2020. You are the leader of the United Action Squad. Your
best friend is the lead scientist who just developed some 
magical pills which can transform you into the hero we need!
Unfortunately, your friend went missing before he could 
tell you which pill does what...

You have received three bottles in a parcel sent to Outpost,
1. First one read: Fisib
2. Second one says: Musbit
3. The last one shows: Drog
....................The choice is your....................
""")


def play():
    # define the Hero.
    user_input = input("Now tell us your choice please ('Fisib','Musbit','Drog'): ")
    you = Hero(user_input)
    print(you)
    print("""
    --------------------------------------------------------------
    You need more time to adapt to your newly gained powers...
    But, there is NO TIME!!!
    Alien is approaching Nyuh Kuning, the heart of Codingnomads...
    --------------------------------------------------------------
    """)

    # define the Alien
    user_input = input("Rumor says, the alien is called: ")
    alien = Alien(user_input)
    print(alien)

    find_weakness = False
    sidekick_here = False
    while int(alien.IQ / 5) + int(alien.energy) > int(you.power) and find_weakness is False:
        print("""
            --------------------------------------------------------------
            Now, Alien is here!!!!!
            You have to do something. What are you going to choose?
            1. Attack
            2. Run away
            3. Find some help
            --------------------------------------------------------------
            """)
        user_input = input("Enter your choice (1 for Attack, 2 for Run, 3 for help) ")
        if user_input == "1":
            you.power /= max(rd.choice([.05, 0.1, 0.5, 1, 1,2, 1,5, 2, 3, 4]),0)
            alien.energy = max(alien.energy+rd.randint(-5, 10), 0)
            if sidekick_here is True:
                sidekick_effect(alien, helper)
                print("With the help of your sidekick...")
                print(sidekick_effect(alien, helper))
                print(f"You, on the other hand, have power of {int(you.power)}. ")
            else:
                # display the status of you and your enemy
                print(f"Alien now has an IQ of {int(alien.IQ)} and energy level of {int(alien.energy)}, "
                      f"while you have power of {int(you.power)}.")
            if int(alien.IQ / 5) + int(alien.energy) > int(you.power) >= int(alien.energy):
                print(f"You are kicking his ass! but the Alien is very smart with an IQ of {int(alien.IQ)}.")
            elif int(you.power) < int(alien.energy):
                print("Ohhhh, Noooooo.........\nYou are not his match right now! Sorry...You can try again though.")
                continue

        elif user_input == "2":
            alien.energy += 2
            print("Alien is getting stronger by the minute!")
            if rd.randint(1, 4) == 4:
                you.power = max(you.power * 2, + 10)
                print("However, you have rested and re-gained some power!")
        elif user_input == "3":
            alien.energy += 1
            print("Alien is getting stronger by the day!")
            # sidekick or weakness
            print("""
            --------------------------------------------------------------
            On your way to your friends in the Holy Spirited Monkey Forest, 
            You saved a dying spy. With his last breath, he told you that 
                           "The alien has ONE WEAKNESS."
            
            Now you have to decide whether you want to:
                  "go find a sidekick" Or "find the weakness alone"
            --------------------------------------------------------------
            """)
            user_input = input("Please enter your choice (1 for sidekick, 2 for weakness): ")
            if user_input == "1":
                name = input("Please enter the name of your sidekick: ")
                func = input("Please enter the ability of your sidekick: ")
                helper = Sidekick(name, func)
                print(helper)
                sidekick_here = True
                print(f"From now on, you will be accompanied by your friend {name}! Bravo!")
            elif user_input == "2":
                print("Your bravery just gained you a chance to destroy him for good!")
                user_input = input("Pleaes give me a number from 1 to 10: ")
                if alien.weakness == int(user_input):
                    print("Wowowow! You have found the weakness!")
                    find_weakness = True
                else:
                    print("Sorry, maybe you will find it next time!")
            else:
                print("I see you have decided to move on from this opportunity...")
                alien.energy += 1
                print("Alien is getting stronger by the day!")
        elif user_input == "q":
            find_weakness = True
        else:
            print("You are the chosen one! You have to do something! Luckily, "
                  "you have another chance before it's too late!")
    print("Congratulations! You have defeated the alien and saved the land of Codingnomads!")


if __name__ == "__main__":
    main()





