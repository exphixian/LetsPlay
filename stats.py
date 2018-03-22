"""Character stats.
- Right now, the stats are randomly generated between 4 and 18
"""
roll = str.lower(input("Do you want your stats to be randomized?"))
if roll == "yes":
    while True:
        for i in range(6):
            print(random.randint(4,18))
        reroll = input("Do you want to keep these stats?")
        if reroll == "yes":
            print("Please determine which variable will be used for which attribute.")
            break
else:
    print("Please enter only base values.")

print("Class, race, and item variables will be added on later.")
strength = int(input("Enter your base strength:"))
constitution = int(input("Enter your base constitution:"))
dexterity = int(input("Enter your base dexterity:"))
intelligence = int(input("Enter your base intelligence:"))
wisdom = int(input("Enter your base wisdom:"))
charisma = int(input("Enter your base charisma:"))

stats = [strength, constitution, dexterity, intelligence, wisdom, charisma]
print(" Str: %s\n Con: %s\n Dex: %s\n Int: %s\n Wis: %s\n Cha: %s\n" % tuple(stats))
