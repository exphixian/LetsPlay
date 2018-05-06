"""
Character stats.
- Right now, the stats are randomly generated between 4 and 18 (4 6-sided dice, dropping the lowest roll.)
"""

def setstats():
    global stats
    stats = []
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
    for i in range(6):
        stat = ['strength', 'constitution', 'dexterity', 'intelligence', 'wisdom', 'charisma']
        stats.append(int(input("Enter your base %s\n" % (stat[i]))))
    print()

setstats()
print(stats)
