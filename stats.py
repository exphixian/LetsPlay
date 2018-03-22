"""Character stats.
- Right now, the stats are randomly generated between 4 and 18
"""
roll = input("Do you want your stats to be randomized?")
roll = str.lower(roll)
if roll == "yes":
#    print("This is still underdevelopment.")
    while True:
        for i in range(6):
            print(random.randint(4,18))
        reroll = input("Do you want to keep these stats?")
        if reroll == "yes":
            print("Please determine which variables will be used for each stat."
                  "Class, race, and item variables will be added on later.")
            strength = int(input("Enter your base strength:"))
            constitution = int(input("Enter your base constitution:"))
            dexterity = int(input("Enter your base dexterity:"))
            intelligence = int(input("Enter your base intelligence:"))
            wisdom = int(input("Enter your base wisdom:"))
            charisma = int(input("Enter your base charisma:"))
            break
else:
    print ("Please enter only base values."
           "Class, race, and item variables will be added on later.")
    strength = int(input("Enter your base strength:"))
    constitution = int(input("Enter your base constitution:"))
    dexterity = int(input("Enter your base dexterity:"))
    intelligence = int(input("Enter your base intelligence:"))
    wisdom = int(input("Enter your base wisdom:"))
    charisma = int(input("Enter your base charisma:"))

stats = [strength, constitution, dexterity, intelligence, wisdom, charisma]
print(" Str: %s\n Con: %s\n Dex: %s\n Int: %s\n Wis: %s\n Cha: %s\n" % tuple(stats))
