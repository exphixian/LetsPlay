"""
Character stats.
- Right now, the stats are randomly generated between 4 and 18 (4 6-sided dice, dropping the lowest roll.)
"""

import random

def setstats():
    global stat, stats
    stats = []
    roll = str.lower(input("Do you want your stats to be randomized?\n"))
    
    # Change roll to no in order to remove random stat generation:
    # roll = no
    
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

    print("Class, race, and item variables will be added on later.")
    for i in range(6):
    
        #The name of stats can be changed as needed.  Since this is D&D 3.5, I will be using the following.
        stat = ['strength', 'constitution', 'dexterity', 'intelligence', 'wisdom', 'charisma']
        
        stats.append(int(input("Enter your base %s\n" % (stat[i]))))
    print()

setstats()

#For troubleshooting
#print(stats)

strength, constitution, dexterity, intelligence, wisdom, charisma = stats[0], stats[1], stats[2], stats[3], stats[4], stats[5]

#For troubleshooting
#print(strength, constitution, dexterity, intelligence, wisdom, charisma)


"""
"""


