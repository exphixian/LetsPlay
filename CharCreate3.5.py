import random
import datetime

"""
Need to set up dice rolls to be random each time. Currently static
d100 = random.randint(1, 100)
d20 = random.randint(1, 20)
d12 = random.randint(1, 12)
d10 = random. randint(1, 10)
d8 = random.randint(1, 8)
d6 = random.randint(1, 6)
d4 = random.randint(1, 4)

print(d20)
print(d20)
"""

print()
print(str.upper("Welcome to D&D 3.5 character creation.\n"))

def setstats():
    """Character stats.
    - Right now, the stats are randomly generated between 4 and 18 (4 6-sided dice, dropping the lowest roll.)
    """
    global strength, constitution, dexterity, intelligence, wisdom, charisma
    roll = str.lower(input("Do you want your stats to be randomized?\n"))

    # Change roll to no in order to remove random stat generation.
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

    print("Class, race, and item variables will be added on later.\n")

    #The name of stats can be changed as needed.  Since this is D&D 3.5, we will be using the following.
    strength = int(input("Enter your base strength:\n"))
    constitution = int(input("Enter your base constitution:\n"))
    dexterity = int(input("Enter your base dexterity:\n"))
    intelligence = int(input("Enter your base intelligence:\n"))
    wisdom = int(input("Enter your base wisdom:\n"))
    charisma = int(input("Enter your base charisma:\n"))
    print()


"""The character needs a name, race, and a gender
Need to figure out how to randomize names from multiple databases or multiple columns.
Since random name will be influenced by race and gender, should probably have that last...
Need to look through the 3.5 book for race stat variables."""

def charsettings():
    global strength, constitution, dexterity, charisma, intelligence, wisdom, race, job, language, size, modifiers

    """Choosing Character Race
    -This will need to add to the stats based on race.  Will do using loops wooo.
    """
    print("Please select your character's species")
    while True:
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
    #For troubleshooting
    #print(race)
    print()

    """Right now, negative numbers are off.  Need to adj"""
    modifiers = [int((strength - 10)/2), int((constitution - 10)/2), int((dexterity - 10)/2), int((intelligence - 10)/2), int((wisdom - 10)/2), int((charisma - 10)/2)]
    #For troubleshooting
    #print(modifiers)


    """Picking a class.
    Need to go through 3.5 core for classes to get stat variables."""
    print("Please choose your character's class:")
    while True:
        job = str.lower(input("This can be: barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, or wizard.\n"))
        if job == "barbarian":
            hpDie = 'd12'
            hp = 12 + modifiers[1]
            break
        elif job == "bard":
            hpDie = 'd6'
            hp = 6 + modifiers[1]
            break
        elif job == "cleric":
            hpDie = 'd8'
            hp = 8 + modifiers[1]
            break
        elif job == "druid":
            hpDie = 'd8'
            hp = 8 + modifiers[1]
            break
        elif job == "fighter":
            hpDie = 'd10'
            hp = 10 + modifiers[1]
            break
        elif job == "monk":
            hpDie = 'd8'
            hp = 8 + modifiers[1]
            break
        elif job == "paladin":
            hpDie = 'd10'
            hp = 10 + modifiers[1]
            break
        elif job == "ranger":
            hpDie = 'd8'
            hp = 8 + modifiers[1]
            break
        elif job == "rogue":
            hpDie = 'd6'
            hp = 6 + modifiers[1]
            break
        elif job == "sorcerer":
            hpDie = 'd4'
            hp = 4 + modifiers[1]
            break
        elif job == "wizard":
            hpDie = 'd4'
            hp = 4 + modifiers[1]
            break
        else:
            print("That is not a valid class.")
    print()
    print("At level one, your HP is " + str(hp) + " and you will be using a %s when you level up." % (hpDie))


    """Skills, languages, & saves
    Need to go through and add stuff based on race and class.  Use if since it is automatically done."""

def chardesign():
    global name, gender, age

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

    name = str(input("Choose a name for your %s %s.\n" % (gender, race)))
    age = int(input("How old is your character?"))

    #For troubleshooting
    #print(gender)

setstats()
charsettings()
chardesign()

stats = [strength, constitution, dexterity, intelligence, wisdom, charisma]

print("%s will be a %s year old %s %s %s" % (name, age, gender, job, race) +
      " with the following stats:\n STR: %s\n CON: %s\n DEX: %s\n INT: %s\n WIS: %s\n CHA: %s\n" % tuple(stats))
print()
