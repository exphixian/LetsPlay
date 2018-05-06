"""
Character stats.
- Right now, the stats are randomly generated between 4 and 18 (4 6-sided dice, dropping the lowest roll.)
"""
import random

def setstats():
    global strength, constitution, dexterity, intelligence, wisdom, charisma
    roll = str.lower(input("Do you want your stats to be randomized?\n"))
    
    #Change roll to no in order to remove random stat generation.
    #roll = no
    
    if roll == "yes":
        while True:
            for i in range(6):
                print(random.randint(4,18))
            reroll = input("Do you want to keep these stats?\n")
            if reroll == "yes":
                print("Please determine which variable will be used for which stat.")
                break
    else:
        print("Please enter only base values.")

    print("Class, race, and item variables will be added on later.\n")
    
    #The name of stats can be changed as needed.  Since this is D&D 3.5, we will be using the following.
    strength = int(input("Enter your base strength:\n"))
    constitution = int(input("Enter your base constitution:\n"))
    dexterity = int(input("Enter your base dexterity:\n"))
    intelligence = int(input("Enter your base intelligence:\n"))
    wisdom = int(input("Enter your base wisdom:\n"))
    charisma = int(input("Enter your base charisma:\n"))
    print()
    
setstats()

#If the stats are going to be adjusted later, define the stats list after to ensure accuracy...
#Or just run this again I guess lol.
stats = [strength, constitution, dexterity, intelligence, wisdom, charisma]

#For troubleshooting
#print(stats)
