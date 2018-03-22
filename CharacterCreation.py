def main():
    name = input("Please enter your character's name:")
    print("%s can be a fighter, a mage, or a rogue." % (name))
    run = True
    job = input("Please select your class:")
    while True:
        if job == "fighter":
            playerhp = 300
            playerattack = 60
            playerdefense = 60
            playermana = 10
            playermagdef = 10
            stealth = 10
            print(name, "is a fighter.")
            run = False
            break
        elif job == "mage":
            playerhp = 200
            playerattack = 10
            playerdefense = 10
            playermana = 60
            playermagdef = 60
            stealth = 20
            print(name, "is a mage.")
            run = False
            break
        elif job == "rogue":
            playerhp = 200
            playerattack = 30
            playerdefense = 30
            playermana = 30
            playermagdef = 30
            stealth = 50
            print(name, "is a rogue.")
            run = False
            break
        else:
            job = input("Sorry, please select a valid class:")
            
main()
