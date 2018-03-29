import random
import datetime

print()
print(str.upper("Welcome to D&D 3.5 character creation.\n"))

def setstats():
    """Character stats.
    - Right now, the stats are randomly generated between 4 and 18
    """
    roll = str.lower(input("Do you want your stats to be randomized?\n"))
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
    global strength
    strength = int(input("Enter your base strength:\n"))
    global constitution
    constitution = int(input("Enter your base constitution:\n"))
    global dexterity
    dexterity = int(input("Enter your base dexterity:\n"))
    global intelligence
    intelligence = int(input("Enter your base intelligence:\n"))
    global wisdom
    wisdom = int(input("Enter your base wisdom:\n"))
    global charisma
    charisma = int(input("Enter your base charisma:\n"))
    print()

setstats()
stats = [strength, constitution, dexterity, intelligence, wisdom, charisma]
print(" STR: %s\n CON: %s\n DEX: %s\n INT: %s\n WIS: %s\n CHA: %s\n" % tuple(stats))

"""First the character needs a name, race, and a gender
Need to figure out how to randomize names from multiple databases or multiple columns.
Since random name will be influenced by race and gender, should probably have that last...
Need to look through the 3.5 book for race stat variables."""

def charsettings():
    global gender
    gender = str.lower(input("Are you going to be playing as a male or a female?\n"))
    while True:
        if gender in ["female", "girl", "woman", "chick", "gal"]:
            gender = "female"
            break
        elif gender in ["male", "boy", "man", "dude", "guy"]:
            gender = "male"
            break
        else:
            gender = str.lower(input("Sorry, didn't quite get that.  Is your character a boy or a girl?"))
    print()

    #For troubleshooting
    #print(gender)

    """Choosing Character Race
    -This will need to add to the stats based on race.  Will do using loops wooo.
    """
    print("Please select your character's species")
    while True:
    global race
    race = str.lower(input("This can be: human, dwarf, elf, gnome, half-elf, half-orc, or halfling.\n"))
        if race == "human":
            print("This race does not have any attribute adjustments")
            language = ["common"]
            size = "medium"
            break
        elif race == "dwarf":
            constitution += 2
            charisma -= 2
            print("Your CON is now %s and your CHA is now %s\n" % (constitution, charisma))
            language = ["dwarven", "common"]
            size = "medium"
            break
        elif race == "elf":
            dexterity += 2
            constitution -= 2
            print("Your DEX is now %s and your CON is now %s\n" % (dexterity, constitution))
            language = ["elven", "common"]
            size = "medium"
            break
        elif race == "gnome":
            constitution += 2
            strength -= 2
            print("Your CON is now %s and your STR is now %s\n" % (constitution, strength))
            language = ["gnome", "common"]
            size = "small"
            break
        elif race == "half-elf":
            print("This race does not have any attribute adjustments")
            language = ["elven", "common"]
            size = "medium"
            break
        elif race == "half-orc":
            strength += 2
            charisma -= 2
            intelligence -= 2
            print("Your STR is now %s, your INT is now %s, and your CHA is now %s" % (strength, intelligence, charisma))
            language = ["orc", "common"]
            size = "medium"
            break
        elif race == "halfling":
            dexterity += 2
            strength -= 2
            print("Your DEX is now %s and your STR is now %s" % (dexterity, strength))
            language = ["halfling", "common"]
            size = "small"
            break
        else:
            print("That is not a valid race.")
    #For Troubleshooting
    #print(race)
    print()

    global name
    name = str(input("Choose a name for your %s %s.\n" % (gender, race)))



    """Picking a class.
    Need to go through 3.5 core for classes to get stat variables."""
    global job
    job = str.lower(input("Please choose your character's class:"))

    """Skills, languages, & saves
    Need to go through and add stuff based on race and class.  Use if since it is automatically done."""

charsettings()
