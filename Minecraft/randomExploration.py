import random

def amountOfLoot(monsterNumber):
    itemNumber = random.randint(1,3)

    if monsterNumber == 2:
        itemNumber = random.randint(3,6)

    if monsterNumber == 3:
        itemNumber = random.randint(6,9)

    if monsterNumber == 4:
        itemNumber = random.randint(9,12)

    if monsterNumber == 5:
        itemNumber = random.randint(12,16)

    if monsterNumber == 6:
        itemNumber = random.randint(16,20)

    if monsterNumber == 7:
        itemNumber = random.randint(20,24)

    return itemNumber

def artTrue():

    def locationPlains():
        explorationSuccess = random.randint(1,100)
        dungeonDecider = random.randint(1,100)
        lootDecider = random.randint(1,10)
        monsterDecider = random.randint(1,10)
        lootTypeGen = random.randint(1,10)
        monsterNumber = 0
        expNumber = 0
        damageNumber = 0
        lootNumber = 0
        dungeonType = "Nothing!"
        lootTypeOne = "Nothing!"
        lootTypeTwo = "Nothing!"
        lootTypeThree = "Nothing!"
        monsterType = "Nothing!"

        if explorationSuccess >= 1 and explorationSuccess < 60:
            print("You explore around the area but quickly get tired and return home...")
        else:
            if explorationSuccess >= 60 and explorationSuccess <= 100:

                if dungeonDecider >= 1 and dungeonDecider < 35:
                    dungeonType = "large rock"

                    def exploreDungeonLargeRock():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint(4,8)
                        monsterNumber = 0

                        if lootDecider >= 1 and lootDecider < 5:
                            print("Upon closer inspection you realize that this is just a normal rock.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "iron"
                                lootNumber = "1"

                            if lootTypeGen >= 4 and lootTypeGen < 6:
                                lootTypeOne = "gold"
                                lootNumber = "1"

                            if lootTypeGen >= 6 and lootTypeGen < 8:
                                lootTypeOne = "redstone"
                                lootNumber = random.randint(4,8)

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "lapis lazuli"
                                lootNumber = random.randint(4,8)

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "diamond"
                                lootNumber = "1"

                            print("Oh! There's " + str(lootTypeOne) + " in the stone! You mine it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")


                    def leaveDungeonLargeRock():
                        print("You leave the large rock alone and return home.")


                if dungeonDecider >= 35 and dungeonDecider < 48:
                    dungeonType = "scarecrow"

                    def exploreDungeonScarecrow():
                            print("Do you want to take the scarecrow's jack-o-lantern head?")
                            print("1. Yes, I will take the head")
                            print("2. No, I will leave it be")

                            userSelect = input("I will-")
                            if userSelect == "1":
                                print("You take the scarecrow's head. You gained +1 jack-o-lantern.")

                            if userSelect == "2":
                                print("You leave the scarecrow's head alone and return home.")

                if dungeonDecider >= 48 and dungeonDecider < 50:
                    dungeonType = "castle dungeon"

                    def enterDungeon():
                        print("You have found a castle dungeon... these are very rare, and dangerous.")

                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint (1,10)
                        monsterDecider = random.randint(1,10)
                        monsterType = "Nothing!"
                        monsterNumber = 0


                        if lootDecider >= 1 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 2:
                                lootTypeOne = "leather shirt"
                                lootNumber = "a"

                            if lootTypeGen >= 2 and lootTypeGen < 3:
                                lootTypeOne = "bread"
                                lootNumber = "4"

                            if lootTypeGen >= 3 and lootTypeGen < 4:
                                lootTypeOne = "strange potion"
                                lootNumber = "a"

                            if lootTypeGen >= 4 and lootTypeGen < 5:
                                lootTypeOne = "gold"
                                lootNumber = random.randint(3,6)

                            if lootTypeGen >= 6 and lootTypeGen < 7:
                                lootTypeOne = "enchanted sword"
                                lootNumber = "an"

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "bone"
                                lootNumber = random.randint(8,10)

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "potatoes"
                                lootNumber = "3"

                            print("Oh! You found a chest! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")

                        if monsterDecider >= 1 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(4,6)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(3,6)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 5:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 6:
                                    itemNumber = random.randint(12,16)


                        if monsterDecider >= 1 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "skeleton(s)"
                                monsterNumber = random.randint(4,6)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(4,8)

                                itemType = "bones"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 5:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 6:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider < 9:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(4,6)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(4,6)


                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 2

                                    if monsterNumber == 5 or monsterNumber == 6:
                                        itemNumber = 4

                            if monsterDecider >= 9 and monsterDecider <= 10:
                                monsterType = "creeper"
                                monsterNumber = random.randint(4,6)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(5,10)

                                itemType = "gunpowder"
                                itemNumber = amountOfLoot(monsterNumber)

                            def enterDungeonTwo():

                                lootDecider = random.randint(1,10)
                                lootTypeOne = "Nothing!"
                                lootNumber = random.randint (1,10)
                                monsterDecider = random.randint(1,10)
                                monsterType = "Nothing!"
                                monsterNumber = 0


                                if lootDecider >= 1 and lootDecider <= 10:

                                    if lootTypeGen >= 1 and lootTypeGen < 2:
                                        lootTypeOne = "enchanted sword"
                                        lootNumber = "an"

                                    if lootTypeGen >= 2 and lootTypeGen < 3:
                                        lootTypeOne = "bread"
                                        lootNumber = "6"

                                    if lootTypeGen >= 3 and lootTypeGen < 4:
                                        lootTypeOne = "gunpowder"
                                        lootNumber = random.randint(8,10)

                                    if lootTypeGen >= 4 and lootTypeGen < 5:
                                        lootTypeOne = "books"
                                        lootNumber = "3"

                                    if lootTypeGen >= 6 and lootTypeGen < 7:
                                        lootTypeOne = "iron helmet"
                                        lootNumber = "an"

                                    if lootTypeGen >= 8 and lootTypeGen < 9:
                                        lootTypeOne = "strange potion"
                                        lootNumber = "a"

                                    if lootTypeGen >= 9 and lootTypeGen <= 10:
                                        lootTypeOne = "lapis lazuli"
                                        lootNumber = random.randint(3,6)

                                    print("Oh! You found a chest! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")

                                if monsterDecider >= 1 and monsterDecider <= 10:
                                    monsterDecider = random.randint(1,10)

                                    if monsterDecider >= 1 and monsterDecider < 2:
                                        monsterType = "zombie(s)"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 3 * monsterNumber
                                        damageNumber = random.randint(3,6)

                                        itemType = "rotten flesh"
                                        itemNumber = random.randint(1,4)

                                        if monsterNumber == 4:
                                            itemNumber = random.randint(4,8)

                                        if monsterNumber == 5:
                                            itemNumber = random.randint(8,12)

                                        if monsterNumber == 6:
                                            itemNumber = random.randint(12,16)


                                if monsterDecider >= 1 and monsterDecider <= 10:
                                    monsterDecider = random.randint(1,10)

                                    if monsterDecider >= 2 and monsterDecider < 4:
                                        monsterType = "skeleton(s)"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 3 * monsterNumber
                                        damageNumber = random.randint(4,8)

                                        itemType = "bones"
                                        itemNumber = random.randint(1,4)

                                        if monsterNumber == 4:
                                            itemNumber = random.randint(4,8)

                                        if monsterNumber == 5:
                                            itemNumber = random.randint(8,12)

                                        if monsterNumber == 6:
                                            itemNumber = random.randint(12,16)


                                    if monsterDecider >= 4 and monsterDecider < 9:
                                        monsterType = "spider(s)"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 6 * monsterNumber
                                        damageNumber = random.randint(4,6)


                                        lootNumber = random.randint(1,2)
                                        if lootNumber == 1:
                                            itemType = "string"
                                            itemNumber = amountOfLoot(monsterNumber)

                                        if lootNumber == 2:
                                            itemType = "spider eye(s)"
                                            itemNumber = 2

                                            if monsterNumber == 5 or monsterNumber == 6:
                                                itemNumber = 4

                                    if monsterDecider >= 9 and monsterDecider <= 10:
                                        monsterType = "creeper"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 6 * monsterNumber
                                        damageNumber = random.randint(5,10)

                                        itemType = "gunpowder"
                                        itemNumber = amountOfLoot(monsterNumber)

                                    def enterDungeonThree():

                                        lootDecider = random.randint(1,10)
                                        lootTypeOne = "Nothing!"
                                        lootNumber = random.randint (1,10)
                                        monsterDecider = random.randint(1,10)
                                        monsterType = "Nothing!"
                                        monsterNumber = 0
                                        expNumber = 0


                                        if lootDecider >= 1 and lootDecider <= 10:

                                            if lootTypeGen >= 1 and lootTypeGen < 2:
                                                lootTypeOne = "enchanted sword"
                                                lootNumber = "an"

                                            if lootTypeGen >= 2 and lootTypeGen < 3:
                                                lootTypeOne = "bread"
                                                lootNumber = "10"

                                            if lootTypeGen >= 3 and lootTypeGen < 4:
                                                lootTypeOne = "cat"
                                                lootNumber = "a"

                                            if lootTypeGen >= 4 and lootTypeGen < 5:
                                                lootTypeOne = "sunflower"
                                                lootNumber = "1"

                                            if lootTypeGen >= 6 and lootTypeGen < 7:
                                                lootTypeOne = "iron"
                                                lootNumber = "12"

                                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                                lootTypeOne = "rotten flesh"
                                                lootNumber = random.randint(8,10)

                                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                                lootTypeOne = "diamonds"
                                                lootNumber = random.randint(1,2)

                                            print("Oh! You found a chest! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")

                                            if monsterDecider >= 1 and monsterDecider <= 10:
                                                monsterDecider = random.randint(1,10)
                                                damageNumber = 0
                                                itemNumber = 0
                                                itemType = "Nothing!"

                                                if monsterDecider >= 1 and monsterDecider < 2:
                                                    monsterType = "zombie(s)"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 3 * monsterNumber
                                                    damageNumber = random.randint(3,6)

                                                    itemType = "rotten flesh"
                                                    itemNumber = random.randint(1,4)

                                                    if monsterNumber == 4:
                                                        itemNumber = random.randint(4,8)

                                                    if monsterNumber == 5:
                                                        itemNumber = random.randint(8,12)

                                                    if monsterNumber == 6:
                                                        itemNumber = random.randint(12,16)

                                                if monsterDecider >= 1 and monsterDecider < 4:
                                                    monsterType = "skeleton(s)"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 3 * monsterNumber
                                                    damageNumber = random.randint(4,8)

                                                    itemType = "bones"
                                                    itemNumber = random.randint(1,4)

                                                    if monsterNumber == 4:
                                                        itemNumber = random.randint(4,8)

                                                    if monsterNumber == 5:
                                                        itemNumber = random.randint(8,12)

                                                    if monsterNumber == 6:
                                                        itemNumber = random.randint(12,16)


                                                if monsterDecider >= 4 and monsterDecider < 9:
                                                    monsterType = "spider(s)"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 6 * monsterNumber
                                                    damageNumber = random.randint(4,6)


                                                    lootNumber = random.randint(1,2)
                                                    if lootNumber == 1:
                                                        itemType = "string"
                                                        itemNumber = amountOfLoot(monsterNumber)

                                                    if lootNumber == 2:
                                                        itemType = "spider eye(s)"
                                                        itemNumber = 2

                                                    if monsterNumber == 5 or monsterNumber == 6:
                                                        itemNumber = 4

                                                if monsterDecider >= 9 and monsterDecider <= 10:
                                                    monsterType = "creeper"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 6 * monsterNumber
                                                    damageNumber = random.randint(5,10)

                                                    itemType = "gunpowder"
                                                    itemNumber = amountOfLoot(monsterNumber)

                                                print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                                                print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")
                                                print("You've reached the end of the dungeon, you return home with your new loot!")

                                    print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                                    print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")
                                    print("Continue?")
                                    print("1. Yes")
                                    print("2. No")
                                    userSelect = input("Answer")

                                    if userSelect == ("1"):
                                        enterDungeonThree()

                                    if userSelect == ("2"):
                                        print("You leave the castle and return home with your loot.")

                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")
                            print("Continue?")
                            print("1. Yes")
                            print("2. No")
                            userSelect = input("Answer")

                            if userSelect == ("1"):
                                enterDungeonTwo()

                            if userSelect == ("2"):
                                print("You leave the castle and return home with your loot.")

                if dungeonDecider >= 50 and dungeonDecider < 53:
                    dungeonType = "single villager house"

                    def lootVillagerHouse():
                        print ("You go inside the villager house whilst they're not looking and find an anvil.")

                    def tradeVillagerHouse():
                        print ('The villager lays out his wears; 3 bread, suspicious stew, 4 iron, and an enchanted golden sword...')

                if dungeonDecider >= 53 and dungeonDecider < 55:
                    dungeonType = "abandoned camp"

                    def exploreAbandonedCamp():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint(4,8)
                        monsterNumber = 0

                        if lootDecider >= 1 and lootDecider < 5:
                            print("You find nothing of interest in the empty tents but find 3 charcoal in the fire pit.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "bread"
                                lootNumber = "some"

                            if lootTypeGen >= 4 and lootTypeGen < 6:
                                lootTypeOne = "iron shovel"
                                lootNumber = "an"

                            if lootTypeGen >= 6 and lootTypeGen < 8:
                                lootTypeOne = "iron"
                                lootNumber = random.randint(4,8)

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "gold"
                                lootNumber = random.randint(1,3)

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "of leather boots"
                                lootNumber = "a pair"

                            print("Oh! You found a chest in one of the abandoned tents! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")



                if dungeonDecider >= 55 and dungeonDecider < 60:
                    dungeonType = "spawn alter"

                    def exploreSpawnAlter():
                        monsterType = "Nothing!"
                        monsterDecider = random.randint(1,10)
                        monsterNumber = 0

                        if monsterDecider >= 1 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(0,3)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 2:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 3:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider < 9:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(0,3)


                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 1

                                    if monsterNumber == 3 or monsterNumber == 4:
                                        itemNumber = 2

                            if monsterDecider >= 9 and monsterDecider <= 10:
                                monsterType = "creeper"
                                monsterNumber = random.randint(1,4)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(0,8)

                                itemType = "gunpowder"
                                itemNumber = amountOfLoot(monsterNumber)

                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")


                if dungeonDecider >= 60 and dungeonDecider < 65:
                    dungeonType = "well"

                    def exploreWell():
                        lootDecider = random.randint(1,10)
                        itemNumber = random.randint(1,10)

                        if lootDecider >= 1 and lootDecider < 6:
                            print("You find nothing of interest in the well, only fresh water.")

                        if lootDecider >= 6 and lootDecider < 8:
                            print("You find " + str(itemNumber) + " iron nuggets at the bottom of the well!")

                        if lootDecider >= 8 and lootDecider <= 10:
                            print("Yoi find " + str(itemNumber) + " gold nuggets at the bottom of the well!")

                if dungeonDecider >= 65 and dungeonDecider < 70:
                    dungeonType = "small dungeon"

                    def exploreSmallDungeon():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootTypeTwo = "Nothing!"
                        lootNumberOne = 0
                        lootNumberTwo = 0
                        monsterType = "Nothing!"
                        monsterDecider = random.randint(1,10)
                        monsterNumber = 0
                        damageNumber = 0

                        if monsterDecider >= 1 and monsterDecider <= 2:
                            lootNumberOne = random.randint(1,10)
                            lootDecider = random.randint(1,10)

                            if lootDecider == 1:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " rotten flesh in a chest!")

                            if lootDecider == 2:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " bones in a chest!")

                            if lootDecider == 3:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " rotten flesh in a chest!")

                            if lootDecider == 4:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " bones in a chest!")

                            if lootDecider == 5:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " books in a chest!")

                            if lootDecider == 6:
                                print("There are no monsters inside, lucky you! You find an Enchanted Book with the enchant Sharpness I in a chest!")

                            if lootDecider == 7:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " gunpowder in a chest!")

                            if lootDecider == 8:
                                print("There are no monsters inside, lucky you! You find an Enchanted Book with the enchant Protection I in a chest!")

                            if lootDecider == 9:
                                print("There are no monsters inside, lucky you! You find a strange potion in a chest!")

                            if lootDecider == 10:
                                print("There are no monsters inside, lucky you! You find a golden apple in a chest!")

                        if monsterDecider >= 3 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider <= 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(0,3)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 2:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 3:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider <= 6:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(1,3)
                                expNumber = 4 * monsterNumber
                                damageNumber = random.randint(0,3)
                                itemNumber = 0

                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 1

                                    if monsterNumber == 3 or monsterNumber == 4:
                                        itemNumber = 2

                            if monsterDecider >= 6 and monsterDecider <= 10:
                                monsterType = "skeleton(s)"
                                monsterNumber = random.randint(1,3)
                                expNumber = 4 * monsterNumber
                                damageNumber = random.randint(0,3)
                                itemNumber = 0

                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "bone(s)"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "broken bow"
                                    itemNumber = 1

                            lootDecider = random.randint(1,10)
                            lootNumberOne = 0
                            lootNumberTwo = 0
                            lootTypeOne = "Nothing!"
                            lootTypeTwo = "Nothing!"

                            if lootDecider == 1:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "rotten flesh"

                            if lootDecider == 2:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "bones"

                            if lootDecider == 3:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "rotten flesh"

                            if lootDecider == 4:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "bones"

                            if lootDecider == 5:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "gunpowder"

                            if lootDecider == 6:
                                lootNumberOne = "an"
                                lootTypeOne = "Enchanted Book with Sharpness I"

                            if lootDecider == 7:
                                lootNumberOne = "a"
                                lootTypeOne = "golden sword"

                            if lootDecider == 8:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "iron"

                            if lootDecider == 9:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "wheat"

                            if lootDecider == 10:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "carrots"

                            lootDecider = random.randint(1,10)
                            lootNumberTwo = 0
                            lootTypeTwo = "Nothing!"

                            if lootDecider == 1:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "rotten flesh"

                            if lootDecider == 2:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "bones"

                            if lootDecider == 3:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "rotten flesh"

                            if lootDecider == 4:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "bones"

                            if lootDecider == 5:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "gunpowder"

                            if lootDecider == 6:
                                lootNumberTwo = "an"
                                lootTypeTwo = "Enchanted Book with Protection I"

                            if lootDecider == 7:
                                lootNumberTwo = "a"
                                lootTypeTwo = "strange potion"

                            if lootDecider == 8:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "coal"

                            if lootDecider == 9:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "potatoes"

                            if lootDecider == 10:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "golden nuggets"

                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points." )
                            print("You also find " + str(lootNumberOne) + " " + str(lootTypeOne) + " and " + str(lootNumberTwo) + " " + str(lootTypeTwo) + " in a chest!")


                if dungeonDecider >= 70 and dungeonDecider < 85:
                    dungeonType = "shallow cave"

                    def exploreShallowCave():
                        lootDecider = random.randint(1,10)
                        lootTypeGen = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = 0

                        if lootDecider >= 1 and lootDecider < 5:
                            print("You find there is nothing of interest in the cave.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "iron"
                                lootNumber = random.randint(1,6)

                            if lootTypeGen >= 4 and lootTypeGen <= 10:
                                lootTypeOne= "coal"
                                lootNumber = random.randint(4,8)

                            print("You found " + str(lootNumber) + " " + str(lootTypeOne) + " in the cave! You mine it and return home.")


                if dungeonDecider >= 85 and dungeonDecider < 90:
                    dungeonType = "tiny mossy cobble structure"

                    def exploreDungeonTinyMoss():
                        monsterType = "Nothing!"
                        monsterDecider = random.randint(1,10)
                        monsterNumber = 0

                        if monsterDecider >= 1 and monsterDecider < 5:
                            print("There's nothing inside it, you can take some of the mossy stone if you want but that's about all there is of interest.")

                        if monsterDecider >= 5 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(0,3)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 2:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 3:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider < 6:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(1,3)
                                expNumber = 4 * monsterNumber
                                damageNumber = random.randint(0,3)

                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 1

                                    if monsterNumber == 3 or monsterNumber == 4:
                                        itemNumber = 2

                            if monsterDecider >= 9 and monsterDecider <= 10:
                                monsterType = "creeper"
                                monsterNumber = random.randint(1,4)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(0,8)

                                itemType = "gunpowder"
                                itemNumber = amountOfLoot(monsterNumber)


                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")

                        def leaveDungeonTinyMoss():
                            print("You leave the tiny mossy cobble structure alone and return home.")

                if dungeonDecider >= 90 and dungeonDecider < 95:
                    dungeonType = "pond"

                    def exploreDungeonPond():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint(4,8)

                        if lootDecider >= 1 and lootDecider < 5:
                            print("Upon closer inspection you realize that this is just a regular pond. The water must be cool and clean, but there's not much else of interest.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "leather boots"

                            if lootTypeGen >= 4 and lootTypeGen < 6:
                                lootTypeOne = "stone axe"

                            if lootTypeGen >= 6 and lootTypeGen < 8:
                                lootTypeOne = "stone shovel"

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "iron shovel"

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "diamond"

                            print("Oh! You can see (a) " + str(lootTypeOne) + " in the pond! You fish the " + str(lootTypeOne) + " out of the water.")


                        def leaveDungeonPond():
                            print("You leave the pond alone and return home.")

                if dungeonDecider >= 95 and dungeonDecider < 98:
                    dungeonType = "horse"

                    def huntDungeonHorse():
                        mobDropNumber = random.randint(1,3)
                        expNumber = random.randint(1,5)

                        print("You slay the beast with your sword, you gain " + str(mobDropNumber) + " leather and " + str(expNumber) + " Pixel Point(s).")

                    def tameDungeonHorse():
                        mobDecider = random.randint(1,100)

                        if mobDecider >= 1 and mobDecider < 60:
                            print("The horse doesn't trust you and gets away before you can lasso it! Better luck next time!")

                        if mobDecider >= 60 and mobDecider <= 100:
                            print("You manage to get the horse's trust and tame it! You have a new friend now!")


                if dungeonDecider >= 98 and dungeonDecider <= 100:
                    dungeonType = "donkey"

                    def huntDungeonDonkey():
                        mobDropNumber = random.randint(1,3)
                        expNumber = random.randint(1,5)

                        print("You slay the beast with your sword, you gain " + str(mobDropNumber) + " leather and " + str(expNumber) + " Pixel Point(s).")

                    def tameDungeonDonkey():
                        mobDecider = random.randint(1,100)

                        if mobDecider >= 1 and mobDecider < 60:
                            print("The donkey doesn't trust you and gets away before you can lasso it! Better luck next time!")

                        if mobDecider >= 60 and mobDecider <= 100:
                            print("You manage to get the donkey's trust and tame it! You have a new friend now!")

                print("Whoa! You found something! It's a " + str(dungeonType) + "!")

                if dungeonType == "castle dungeon":

                    print("You have found a castle dungeon... these are very rare, and dangerous.")
                    print("What do you want to do?")
                    print("1. -explore!")
                    print("2. -leave!")

                    userSelect = input("I will- ")
                    if userSelect == "1":
                        enterDungeon()

                    if userSelect == "2":
                        print("You wisely leave the dungeon alone, perhaps you should gear up first...")

                if dungeonType == "single villager house":
                    print("What do you want to do?")
                    print("1. -loot the house!")
                    print ("2. -trade with the villager!")
                    print ("3. -leave!")

                    userSelect = input("I will- ")
                    if userSelect == "1":
                        lootVillagerHouse()

                    if userSelect == "2":
                        tradeVillagerHouse()

                    if userSelect == "3":
                        print ("You leave the villager house alone for now.")

                if dungeonType == "abandoned camp":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreAbandonedCamp()

                    if userSelect == "2":
                        print("You decide not to look around and return home...")

                if dungeonType == "spawn alter":
                    print("what do you want to do?")
                    print("1. -explore further!")
                    print("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreSpawnAlter()

                    if userSelect == "2":
                        print("You decider to leave the strange alter alone and return home.")

                if dungeonType == "well":
                    print("what do you want to do?")
                    print("1. -explore further!")
                    print("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreWell()

                    if userSelect == "2":
                        print("You decide to leave the well alone and return home.")

                if dungeonType == "small dungeon":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreSmallDungeon()

                    if userSelect == "2":
                        print("You decide not to look inside and return home...")

                if dungeonType == "large rock":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonLargeRock()

                    if userSelect == "2":
                        leaveDungeonLargeRock()


                if dungeonType == "scarecrow":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonScarecrow()

                    if userSelect == "2":
                        leaveDungeonScarecrow()

                if dungeonType == "shallow cave":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreShallowCave()

                    if userSelect == "2":
                        print("You leave the cave be for now and return home.")

                if dungeonType == "tiny mossy cobble structure":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonTinyMoss()

                    if userSelect == "2":
                        leaveDungeonTinyMoss()

                if dungeonType == "pond":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonPond()

                    if userSelect == "2":
                        leaveDungeonPond()

                if dungeonType == "horse":
                    print("What do you want to do?")
                    print ("1. -hunt the horse!")
                    print ("2. -tame the horse!")
                    print ("3. -leave the horse alone!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        huntDungeonHorse()

                    if userSelect == "2":
                        tameDungeonHorse()

                    if userSelect == "3":
                        print("You leave the horse alone and return home.")

                if dungeonType == "donkey":
                    print("What do you want to do?")
                    print ("1. -hunt the donkey!")
                    print ("2. -tame the donkey!")
                    print ("3. -leave the donkey alone!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        huntDungeonDonkey()

                    if userSelect == "2":
                        tameDungeonDonkey()

                    if userSelect == "3":
                        print("You leave the donkey alone and return home.")

    def locationSunflowerFields():
        explorationSuccess = random.randint(1,100)
        dungeonDecider = random.randint(1,100)
        lootDecider = random.randint(1,10)
        monsterDecider = random.randint(1,10)
        lootTypeGen = random.randint(1,10)
        monsterNumber = 0
        expNumber = 0
        damageNumber = 0
        lootNumber = 0
        dungeonType = "Nothing!"
        lootTypeOne = "Nothing!"
        lootTypeTwo = "Nothing!"
        lootTypeThree = "Nothing!"
        monsterType = "Nothing!"

        if explorationSuccess >= 1 and explorationSuccess < 80:
            print("You explore around the area but quickly get tired and return home...")
        else:
            if explorationSuccess >= 80 and explorationSuccess <= 100:

                if dungeonDecider >= 1 and dungeonDecider < 35:
                    dungeonType = "large rock"

                    def exploreDungeonLargeRock():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint(4,8)
                        monsterNumber = 0

                        if lootDecider >= 1 and lootDecider < 5:
                            print("Upon closer inspection you realize that this is just a normal rock.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "iron"
                                lootNumber = "1"

                            if lootTypeGen >= 4 and lootTypeGen < 6:
                                lootTypeOne = "gold"
                                lootNumber = "1"

                            if lootTypeGen >= 6 and lootTypeGen < 8:
                                lootTypeOne = "redstone"
                                lootNumber = random.randint(4,8)

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "lapis lazuli"
                                lootNumber = random.randint(4,8)

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "diamond"
                                lootNumber = "1"

                            print("Oh! There's " + str(lootTypeOne) + " in the stone! You mine it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")


                    def leaveDungeonLargeRock():
                        print("You leave the large rock alone and return home.")


                if dungeonDecider >= 35 and dungeonDecider < 48:
                    dungeonType = "scarecrow"

                    def exploreDungeonScarecrow():
                            print("Do you want to take the scarecrow's jack-o-lantern head?")
                            print("1. Yes, I will take the head")
                            print("2. No, I will leave it be")

                            userSelect = input("I will-")
                            if userSelect == "1":
                                print("You take the scarecrow's head. You gained +1 jack-o-lantern.")

                            if userSelect == "2":
                                print("You leave the scarecrow's head alone and return home.")

                if dungeonDecider >= 48 and dungeonDecider < 50:
                    dungeonType = "castle dungeon"

                    def enterDungeon():
                        print("You have found a castle dungeon... these are very rare, and dangerous.")

                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint (1,10)
                        monsterDecider = random.randint(1,10)
                        monsterType = "Nothing!"
                        monsterNumber = 0


                        if lootDecider >= 1 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 2:
                                lootTypeOne = "leather shirt"
                                lootNumber = "a"

                            if lootTypeGen >= 2 and lootTypeGen < 3:
                                lootTypeOne = "bread"
                                lootNumber = "4"

                            if lootTypeGen >= 3 and lootTypeGen < 4:
                                lootTypeOne = "strange potion"
                                lootNumber = "a"

                            if lootTypeGen >= 4 and lootTypeGen < 5:
                                lootTypeOne = "gold"
                                lootNumber = random.randint(3,6)

                            if lootTypeGen >= 6 and lootTypeGen < 7:
                                lootTypeOne = "enchanted sword"
                                lootNumber = "an"

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "bone"
                                lootNumber = random.randint(8,10)

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "potatoes"
                                lootNumber = "3"

                            print("Oh! You found a chest! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")

                        if monsterDecider >= 1 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(4,6)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(3,6)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 5:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 6:
                                    itemNumber = random.randint(12,16)


                        if monsterDecider >= 1 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "skeleton(s)"
                                monsterNumber = random.randint(4,6)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(4,8)

                                itemType = "bones"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 5:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 6:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider < 9:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(4,6)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(4,6)


                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 2

                                    if monsterNumber == 5 or monsterNumber == 6:
                                        itemNumber = 4

                            if monsterDecider >= 9 and monsterDecider <= 10:
                                monsterType = "creeper"
                                monsterNumber = random.randint(4,6)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(5,10)

                                itemType = "gunpowder"
                                itemNumber = amountOfLoot(monsterNumber)

                            def enterDungeonTwo():

                                lootDecider = random.randint(1,10)
                                lootTypeOne = "Nothing!"
                                lootNumber = random.randint (1,10)
                                monsterDecider = random.randint(1,10)
                                monsterType = "Nothing!"
                                monsterNumber = 0


                                if lootDecider >= 1 and lootDecider <= 10:

                                    if lootTypeGen >= 1 and lootTypeGen < 2:
                                        lootTypeOne = "enchanted sword"
                                        lootNumber = "an"

                                    if lootTypeGen >= 2 and lootTypeGen < 3:
                                        lootTypeOne = "bread"
                                        lootNumber = "6"

                                    if lootTypeGen >= 3 and lootTypeGen < 4:
                                        lootTypeOne = "gunpowder"
                                        lootNumber = random.randint(8,10)

                                    if lootTypeGen >= 4 and lootTypeGen < 5:
                                        lootTypeOne = "books"
                                        lootNumber = "3"

                                    if lootTypeGen >= 6 and lootTypeGen < 7:
                                        lootTypeOne = "iron helmet"
                                        lootNumber = "an"

                                    if lootTypeGen >= 8 and lootTypeGen < 9:
                                        lootTypeOne = "strange potion"
                                        lootNumber = "a"

                                    if lootTypeGen >= 9 and lootTypeGen <= 10:
                                        lootTypeOne = "lapis lazuli"
                                        lootNumber = random.randint(3,6)

                                    print("Oh! You found a chest! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")

                                if monsterDecider >= 1 and monsterDecider <= 10:
                                    monsterDecider = random.randint(1,10)

                                    if monsterDecider >= 1 and monsterDecider < 2:
                                        monsterType = "zombie(s)"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 3 * monsterNumber
                                        damageNumber = random.randint(3,6)

                                        itemType = "rotten flesh"
                                        itemNumber = random.randint(1,4)

                                        if monsterNumber == 4:
                                            itemNumber = random.randint(4,8)

                                        if monsterNumber == 5:
                                            itemNumber = random.randint(8,12)

                                        if monsterNumber == 6:
                                            itemNumber = random.randint(12,16)


                                if monsterDecider >= 1 and monsterDecider <= 10:
                                    monsterDecider = random.randint(1,10)

                                    if monsterDecider >= 2 and monsterDecider < 4:
                                        monsterType = "skeleton(s)"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 3 * monsterNumber
                                        damageNumber = random.randint(4,8)

                                        itemType = "bones"
                                        itemNumber = random.randint(1,4)

                                        if monsterNumber == 4:
                                            itemNumber = random.randint(4,8)

                                        if monsterNumber == 5:
                                            itemNumber = random.randint(8,12)

                                        if monsterNumber == 6:
                                            itemNumber = random.randint(12,16)


                                    if monsterDecider >= 4 and monsterDecider < 9:
                                        monsterType = "spider(s)"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 6 * monsterNumber
                                        damageNumber = random.randint(4,6)


                                        lootNumber = random.randint(1,2)
                                        if lootNumber == 1:
                                            itemType = "string"
                                            itemNumber = amountOfLoot(monsterNumber)

                                        if lootNumber == 2:
                                            itemType = "spider eye(s)"
                                            itemNumber = 2

                                            if monsterNumber == 5 or monsterNumber == 6:
                                                itemNumber = 4

                                    if monsterDecider >= 9 and monsterDecider <= 10:
                                        monsterType = "creeper"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 6 * monsterNumber
                                        damageNumber = random.randint(5,10)

                                        itemType = "gunpowder"
                                        itemNumber = amountOfLoot(monsterNumber)

                                    def enterDungeonThree():

                                        lootDecider = random.randint(1,10)
                                        lootTypeOne = "Nothing!"
                                        lootNumber = random.randint (1,10)
                                        monsterDecider = random.randint(1,10)
                                        monsterType = "Nothing!"
                                        monsterNumber = 0
                                        expNumber = 0


                                        if lootDecider >= 1 and lootDecider <= 10:

                                            if lootTypeGen >= 1 and lootTypeGen < 2:
                                                lootTypeOne = "enchanted sword"
                                                lootNumber = "an"

                                            if lootTypeGen >= 2 and lootTypeGen < 3:
                                                lootTypeOne = "bread"
                                                lootNumber = "10"

                                            if lootTypeGen >= 3 and lootTypeGen < 4:
                                                lootTypeOne = "cat"
                                                lootNumber = "a"

                                            if lootTypeGen >= 4 and lootTypeGen < 5:
                                                lootTypeOne = "sunflower"
                                                lootNumber = "1"

                                            if lootTypeGen >= 6 and lootTypeGen < 7:
                                                lootTypeOne = "iron"
                                                lootNumber = "12"

                                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                                lootTypeOne = "rotten flesh"
                                                lootNumber = random.randint(8,10)

                                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                                lootTypeOne = "diamonds"
                                                lootNumber = random.randint(1,2)

                                            print("Oh! You found a chest! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")

                                            if monsterDecider >= 1 and monsterDecider <= 10:
                                                monsterDecider = random.randint(1,10)
                                                damageNumber = 0
                                                itemNumber = 0
                                                itemType = "Nothing!"

                                                if monsterDecider >= 1 and monsterDecider < 2:
                                                    monsterType = "zombie(s)"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 3 * monsterNumber
                                                    damageNumber = random.randint(3,6)

                                                    itemType = "rotten flesh"
                                                    itemNumber = random.randint(1,4)

                                                    if monsterNumber == 4:
                                                        itemNumber = random.randint(4,8)

                                                    if monsterNumber == 5:
                                                        itemNumber = random.randint(8,12)

                                                    if monsterNumber == 6:
                                                        itemNumber = random.randint(12,16)

                                                if monsterDecider >= 1 and monsterDecider < 4:
                                                    monsterType = "skeleton(s)"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 3 * monsterNumber
                                                    damageNumber = random.randint(4,8)

                                                    itemType = "bones"
                                                    itemNumber = random.randint(1,4)

                                                    if monsterNumber == 4:
                                                        itemNumber = random.randint(4,8)

                                                    if monsterNumber == 5:
                                                        itemNumber = random.randint(8,12)

                                                    if monsterNumber == 6:
                                                        itemNumber = random.randint(12,16)


                                                if monsterDecider >= 4 and monsterDecider < 9:
                                                    monsterType = "spider(s)"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 6 * monsterNumber
                                                    damageNumber = random.randint(4,6)


                                                    lootNumber = random.randint(1,2)
                                                    if lootNumber == 1:
                                                        itemType = "string"
                                                        itemNumber = amountOfLoot(monsterNumber)

                                                    if lootNumber == 2:
                                                        itemType = "spider eye(s)"
                                                        itemNumber = 2

                                                    if monsterNumber == 5 or monsterNumber == 6:
                                                        itemNumber = 4

                                                if monsterDecider >= 9 and monsterDecider <= 10:
                                                    monsterType = "creeper"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 6 * monsterNumber
                                                    damageNumber = random.randint(5,10)

                                                    itemType = "gunpowder"
                                                    itemNumber = amountOfLoot(monsterNumber)

                                                print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                                                print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")
                                                print("You've reached the end of the dungeon, you return home with your new loot!")

                                    print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                                    print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")
                                    print("Continue?")
                                    print("1. Yes")
                                    print("2. No")
                                    userSelect = input("Answer")

                                    if userSelect == ("1"):
                                        enterDungeonThree()

                                    if userSelect == ("2"):
                                        print("You leave the castle and return home with your loot.")

                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")
                            print("Continue?")
                            print("1. Yes")
                            print("2. No")
                            userSelect = input("Answer")

                            if userSelect == ("1"):
                                enterDungeonTwo()

                            if userSelect == ("2"):
                                print("You leave the castle and return home with your loot.")

                if dungeonDecider >= 50 and dungeonDecider < 53:
                    dungeonType = "single villager house"

                    def lootVillagerHouse():
                        print ("You go inside the villager house whilst they're not looking and find an anvil.")

                    def tradeVillagerHouse():
                        print ('The villager lays out his wears; 3 bread, suspicious stew, 4 iron, and an enchanted golden sword...')

                if dungeonDecider >= 53 and dungeonDecider < 55:
                    dungeonType = "abandoned camp"

                    def exploreAbandonedCamp():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint(4,8)
                        monsterNumber = 0

                        if lootDecider >= 1 and lootDecider < 5:
                            print("You find nothing of interest in the empty tents but find 3 charcoal in the fire pit.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "bread"
                                lootNumber = "some"

                            if lootTypeGen >= 4 and lootTypeGen < 6:
                                lootTypeOne = "iron shovel"
                                lootNumber = "an"

                            if lootTypeGen >= 6 and lootTypeGen < 8:
                                lootTypeOne = "iron"
                                lootNumber = random.randint(4,8)

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "gold"
                                lootNumber = random.randint(1,3)

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "of leather boots"
                                lootNumber = "a pair"

                            print("Oh! You found a chest in one of the abandoned tents! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")



                if dungeonDecider >= 55 and dungeonDecider < 60:
                    dungeonType = "spawn alter"

                    def exploreSpawnAlter():
                        monsterType = "Nothing!"
                        monsterDecider = random.randint(1,10)
                        monsterNumber = 0

                        if monsterDecider >= 1 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(0,3)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 2:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 3:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider < 9:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(0,3)


                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 1

                                    if monsterNumber == 3 or monsterNumber == 4:
                                        itemNumber = 2

                            if monsterDecider >= 9 and monsterDecider <= 10:
                                monsterType = "creeper"
                                monsterNumber = random.randint(1,4)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(0,8)

                                itemType = "gunpowder"
                                itemNumber = amountOfLoot(monsterNumber)

                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")


                if dungeonDecider >= 60 and dungeonDecider < 65:
                    dungeonType = "well"

                    def exploreWell():
                        lootDecider = random.randint(1,10)
                        itemNumber = random.randint(1,10)

                        if lootDecider >= 1 and lootDecider < 6:
                            print("You find nothing of interest in the well, only fresh water.")

                        if lootDecider >= 6 and lootDecider < 8:
                            print("You find " + str(itemNumber) + " iron nuggets at the bottom of the well!")

                        if lootDecider >= 8 and lootDecider <= 10:
                            print("Yoi find " + str(itemNumber) + " gold nuggets at the bottom of the well!")

                if dungeonDecider >= 65 and dungeonDecider < 70:
                    dungeonType = "small dungeon"

                    def exploreSmallDungeon():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootTypeTwo = "Nothing!"
                        lootNumberOne = 0
                        lootNumberTwo = 0
                        monsterType = "Nothing!"
                        monsterDecider = random.randint(1,10)
                        monsterNumber = 0
                        damageNumber = 0

                        if monsterDecider >= 1 and monsterDecider <= 2:
                            lootNumberOne = random.randint(1,10)
                            lootDecider = random.randint(1,10)

                            if lootDecider == 1:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " rotten flesh in a chest!")

                            if lootDecider == 2:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " bones in a chest!")

                            if lootDecider == 3:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " rotten flesh in a chest!")

                            if lootDecider == 4:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " bones in a chest!")

                            if lootDecider == 5:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " books in a chest!")

                            if lootDecider == 6:
                                print("There are no monsters inside, lucky you! You find an Enchanted Book with the enchant Sharpness I in a chest!")

                            if lootDecider == 7:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " gunpowder in a chest!")

                            if lootDecider == 8:
                                print("There are no monsters inside, lucky you! You find an Enchanted Book with the enchant Protection I in a chest!")

                            if lootDecider == 9:
                                print("There are no monsters inside, lucky you! You find a strange potion in a chest!")

                            if lootDecider == 10:
                                print("There are no monsters inside, lucky you! You find a golden apple in a chest!")

                        if monsterDecider >= 3 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider <= 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(0,3)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 2:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 3:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider <= 6:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(1,3)
                                expNumber = 4 * monsterNumber
                                damageNumber = random.randint(0,3)
                                itemNumber = 0

                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 1

                                    if monsterNumber == 3 or monsterNumber == 4:
                                        itemNumber = 2

                            if monsterDecider >= 6 and monsterDecider <= 10:
                                monsterType = "skeleton(s)"
                                monsterNumber = random.randint(1,3)
                                expNumber = 4 * monsterNumber
                                damageNumber = random.randint(0,3)
                                itemNumber = 0

                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "bone(s)"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "broken bow"
                                    itemNumber = 1

                            lootDecider = random.randint(1,10)
                            lootNumberOne = 0
                            lootNumberTwo = 0
                            lootTypeOne = "Nothing!"
                            lootTypeTwo = "Nothing!"

                            if lootDecider == 1:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "rotten flesh"

                            if lootDecider == 2:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "bones"

                            if lootDecider == 3:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "rotten flesh"

                            if lootDecider == 4:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "bones"

                            if lootDecider == 5:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "gunpowder"

                            if lootDecider == 6:
                                lootNumberOne = "an"
                                lootTypeOne = "Enchanted Book with Sharpness I"

                            if lootDecider == 7:
                                lootNumberOne = "a"
                                lootTypeOne = "golden sword"

                            if lootDecider == 8:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "iron"

                            if lootDecider == 9:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "wheat"

                            if lootDecider == 10:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "carrots"

                            lootDecider = random.randint(1,10)
                            lootNumberTwo = 0
                            lootTypeTwo = "Nothing!"

                            if lootDecider == 1:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "rotten flesh"

                            if lootDecider == 2:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "bones"

                            if lootDecider == 3:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "rotten flesh"

                            if lootDecider == 4:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "bones"

                            if lootDecider == 5:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "gunpowder"

                            if lootDecider == 6:
                                lootNumberTwo = "an"
                                lootTypeTwo = "Enchanted Book with Protection I"

                            if lootDecider == 7:
                                lootNumberTwo = "a"
                                lootTypeTwo = "strange potion"

                            if lootDecider == 8:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "coal"

                            if lootDecider == 9:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "potatoes"

                            if lootDecider == 10:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "golden nuggets"

                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points." )
                            print("You also find " + str(lootNumberOne) + " " + str(lootTypeOne) + " and " + str(lootNumberTwo) + " " + str(lootTypeTwo) + " in a chest!")


                if dungeonDecider >= 70 and dungeonDecider < 85:
                    dungeonType = "shallow cave"

                    def exploreShallowCave():
                        lootDecider = random.randint(1,10)
                        lootTypeGen = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = 0

                        if lootDecider >= 1 and lootDecider < 5:
                            print("You find there is nothing of interest in the cave.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "iron"
                                lootNumber = random.randint(1,6)

                            if lootTypeGen >= 4 and lootTypeGen <= 10:
                                lootTypeOne= "coal"
                                lootNumber = random.randint(4,8)

                            print("You found " + str(lootNumber) + " " + str(lootTypeOne) + " in the cave! You mine it and return home.")


                if dungeonDecider >= 85 and dungeonDecider < 90:
                    dungeonType = "tiny mossy cobble structure"

                    def exploreDungeonTinyMoss():
                        monsterType = "Nothing!"
                        monsterDecider = random.randint(1,10)
                        monsterNumber = 0

                        if monsterDecider >= 1 and monsterDecider < 5:
                            print("There's nothing inside it, you can take some of the mossy stone if you want but that's about all there is of interest.")

                        if monsterDecider >= 5 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(0,3)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 2:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 3:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider < 6:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(1,3)
                                expNumber = 4 * monsterNumber
                                damageNumber = random.randint(0,3)

                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 1

                                    if monsterNumber == 3 or monsterNumber == 4:
                                        itemNumber = 2

                            if monsterDecider >= 9 and monsterDecider <= 10:
                                monsterType = "creeper"
                                monsterNumber = random.randint(1,4)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(0,8)

                                itemType = "gunpowder"
                                itemNumber = amountOfLoot(monsterNumber)


                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")

                        def leaveDungeonTinyMoss():
                            print("You leave the tiny mossy cobble structure alone and return home.")

                if dungeonDecider >= 90 and dungeonDecider < 95:
                    dungeonType = "pond"

                    def exploreDungeonPond():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint(4,8)

                        if lootDecider >= 1 and lootDecider < 5:
                            print("Upon closer inspection you realize that this is just a regular pond. The water must be cool and clean, but there's not much else of interest.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "leather boots"

                            if lootTypeGen >= 4 and lootTypeGen < 6:
                                lootTypeOne = "stone axe"

                            if lootTypeGen >= 6 and lootTypeGen < 8:
                                lootTypeOne = "stone shovel"

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "iron shovel"

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "diamond"

                            print("Oh! You can see (a) " + str(lootTypeOne) + " in the pond! You fish the " + str(lootTypeOne) + " out of the water.")


                        def leaveDungeonPond():
                            print("You leave the pond alone and return home.")

                if dungeonDecider >= 95 and dungeonDecider < 98:
                    dungeonType = "horse"

                    def huntDungeonHorse():
                        mobDropNumber = random.randint(1,3)
                        expNumber = random.randint(1,5)

                        print("You slay the beast with your sword, you gain " + str(mobDropNumber) + " leather and " + str(expNumber) + " Pixel Point(s).")

                    def tameDungeonHorse():
                        mobDecider = random.randint(1,100)

                        if mobDecider >= 1 and mobDecider < 60:
                            print("The horse doesn't trust you and gets away before you can lasso it! Better luck next time!")

                        if mobDecider >= 60 and mobDecider <= 100:
                            print("You manage to get the horse's trust and tame it! You have a new friend now!")


                if dungeonDecider >= 98 and dungeonDecider <= 100:
                    dungeonType = "donkey"

                    def huntDungeonDonkey():
                        mobDropNumber = random.randint(1,3)
                        expNumber = random.randint(1,5)

                        print("You slay the beast with your sword, you gain " + str(mobDropNumber) + " leather and " + str(expNumber) + " Pixel Point(s).")

                    def tameDungeonDonkey():
                        mobDecider = random.randint(1,100)

                        if mobDecider >= 1 and mobDecider < 60:
                            print("The donkey doesn't trust you and gets away before you can lasso it! Better luck next time!")

                        if mobDecider >= 60 and mobDecider <= 100:
                            print("You manage to get the donkey's trust and tame it! You have a new friend now!")

                print("Whoa! You found something! It's a " + str(dungeonType) + "!")

                if dungeonType == "castle dungeon":

                    print("You have found a castle dungeon... these are very rare, and dangerous.")
                    print("What do you want to do?")
                    print("1. -explore!")
                    print("2. -leave!")

                    userSelect = input("I will- ")
                    if userSelect == "1":
                        enterDungeon()

                    if userSelect == "2":
                        print("You wisely leave the dungeon alone, perhaps you should gear up first...")

                if dungeonType == "single villager house":
                    print("What do you want to do?")
                    print("1. -loot the house!")
                    print ("2. -trade with the villager!")
                    print ("3. -leave!")

                    userSelect = input("I will- ")
                    if userSelect == "1":
                        lootVillagerHouse()

                    if userSelect == "2":
                        tradeVillagerHouse()

                    if userSelect == "3":
                        print ("You leave the villager house alone for now.")

                if dungeonType == "abandoned camp":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreAbandonedCamp()

                    if userSelect == "2":
                        print("You decide not to look around and return home...")

                if dungeonType == "spawn alter":
                    print("what do you want to do?")
                    print("1. -explore further!")
                    print("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreSpawnAlter()

                    if userSelect == "2":
                        print("You decider to leave the strange alter alone and return home.")

                if dungeonType == "well":
                    print("what do you want to do?")
                    print("1. -explore further!")
                    print("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreWell()

                    if userSelect == "2":
                        print("You decide to leave the well alone and return home.")

                if dungeonType == "small dungeon":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreSmallDungeon()

                    if userSelect == "2":
                        print("You decide not to look inside and return home...")

                if dungeonType == "large rock":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonLargeRock()

                    if userSelect == "2":
                        leaveDungeonLargeRock()


                if dungeonType == "scarecrow":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonScarecrow()

                    if userSelect == "2":
                        leaveDungeonScarecrow()

                if dungeonType == "shallow cave":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreShallowCave()

                    if userSelect == "2":
                        print("You leave the cave be for now and return home.")

                if dungeonType == "tiny mossy cobble structure":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonTinyMoss()

                    if userSelect == "2":
                        leaveDungeonTinyMoss()

                if dungeonType == "pond":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonPond()

                    if userSelect == "2":
                        leaveDungeonPond()

                if dungeonType == "horse":
                    print("What do you want to do?")
                    print ("1. -hunt the horse!")
                    print ("2. -tame the horse!")
                    print ("3. -leave the horse alone!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        huntDungeonHorse()

                    if userSelect == "2":
                        tameDungeonHorse()

                    if userSelect == "3":
                        print("You leave the horse alone and return home.")

                if dungeonType == "donkey":
                    print("What do you want to do?")
                    print ("1. -hunt the donkey!")
                    print ("2. -tame the donkey!")
                    print ("3. -leave the donkey alone!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        huntDungeonDonkey()

                    if userSelect == "2":
                        tameDungeonDonkey()

                    if userSelect == "3":
                        print("You leave the donkey alone and return home.")

    print("Please select a location:")
    print ("1. Plains")
    print ("2. Sunflower Fields")

    userSelect = input("Location: ")

    if userSelect == "1":
        locationPlains()

    if userSelect == "2":
        locationSunflowerFields()

def artFalse():

    def locationPlains():
        explorationSuccess = random.randint(1,100)
        dungeonDecider = random.randint(1,100)
        lootDecider = random.randint(1,10)
        monsterDecider = random.randint(1,10)
        lootTypeGen = random.randint(1,10)
        monsterNumber = 0
        expNumber = 0
        damageNumber = 0
        lootNumber = 0
        dungeonType = "Nothing!"
        lootTypeOne = "Nothing!"
        lootTypeTwo = "Nothing!"
        lootTypeThree = "Nothing!"
        monsterType = "Nothing!"

        if explorationSuccess >= 1 and explorationSuccess < 80:
            print("You explore around the area but quickly get tired and return home...")
        else:
            if explorationSuccess >= 80 and explorationSuccess <= 100:

                if dungeonDecider >= 1 and dungeonDecider < 35:
                    dungeonType = "large rock"

                    def exploreDungeonLargeRock():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint(4,8)
                        monsterNumber = 0

                        if lootDecider >= 1 and lootDecider < 5:
                            print("Upon closer inspection you realize that this is just a normal rock.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "iron"
                                lootNumber = "1"

                            if lootTypeGen >= 4 and lootTypeGen < 6:
                                lootTypeOne = "gold"
                                lootNumber = "1"

                            if lootTypeGen >= 6 and lootTypeGen < 8:
                                lootTypeOne = "redstone"
                                lootNumber = random.randint(4,8)

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "lapis lazuli"
                                lootNumber = random.randint(4,8)

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "diamond"
                                lootNumber = "1"

                            print("Oh! There's " + str(lootTypeOne) + " in the stone! You mine it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")


                    def leaveDungeonLargeRock():
                        print("You leave the large rock alone and return home.")


                if dungeonDecider >= 35 and dungeonDecider < 48:
                    dungeonType = "scarecrow"

                    def exploreDungeonScarecrow():
                            print("Do you want to take the scarecrow's jack-o-lantern head?")
                            print("1. Yes, I will take the head")
                            print("2. No, I will leave it be")

                            userSelect = input("I will-")
                            if userSelect == "1":
                                print("You take the scarecrow's head. You gained +1 jack-o-lantern.")

                            if userSelect == "2":
                                print("You leave the scarecrow's head alone and return home.")

                if dungeonDecider >= 48 and dungeonDecider < 50:
                    dungeonType = "castle dungeon"

                    def enterDungeon():
                        print("You have found a castle dungeon... these are very rare, and dangerous.")

                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint (1,10)
                        monsterDecider = random.randint(1,10)
                        monsterType = "Nothing!"
                        monsterNumber = 0


                        if lootDecider >= 1 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 2:
                                lootTypeOne = "leather shirt"
                                lootNumber = "a"

                            if lootTypeGen >= 2 and lootTypeGen < 3:
                                lootTypeOne = "bread"
                                lootNumber = "4"

                            if lootTypeGen >= 3 and lootTypeGen < 4:
                                lootTypeOne = "strange potion"
                                lootNumber = "a"

                            if lootTypeGen >= 4 and lootTypeGen < 5:
                                lootTypeOne = "gold"
                                lootNumber = random.randint(3,6)

                            if lootTypeGen >= 6 and lootTypeGen < 7:
                                lootTypeOne = "enchanted sword"
                                lootNumber = "an"

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "bone"
                                lootNumber = random.randint(8,10)

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "potatoes"
                                lootNumber = "3"

                            print("Oh! You found a chest! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")

                        if monsterDecider >= 1 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(4,6)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(3,6)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 5:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 6:
                                    itemNumber = random.randint(12,16)


                        if monsterDecider >= 1 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "skeleton(s)"
                                monsterNumber = random.randint(4,6)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(4,8)

                                itemType = "bones"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 5:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 6:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider < 9:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(4,6)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(4,6)


                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 2

                                    if monsterNumber == 5 or monsterNumber == 6:
                                        itemNumber = 4

                            if monsterDecider >= 9 and monsterDecider <= 10:
                                monsterType = "creeper"
                                monsterNumber = random.randint(4,6)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(5,10)

                                itemType = "gunpowder"
                                itemNumber = amountOfLoot(monsterNumber)

                            def enterDungeonTwo():

                                lootDecider = random.randint(1,10)
                                lootTypeOne = "Nothing!"
                                lootNumber = random.randint (1,10)
                                monsterDecider = random.randint(1,10)
                                monsterType = "Nothing!"
                                monsterNumber = 0


                                if lootDecider >= 1 and lootDecider <= 10:

                                    if lootTypeGen >= 1 and lootTypeGen < 2:
                                        lootTypeOne = "enchanted sword"
                                        lootNumber = "an"

                                    if lootTypeGen >= 2 and lootTypeGen < 3:
                                        lootTypeOne = "bread"
                                        lootNumber = "6"

                                    if lootTypeGen >= 3 and lootTypeGen < 4:
                                        lootTypeOne = "gunpowder"
                                        lootNumber = random.randint(8,10)

                                    if lootTypeGen >= 4 and lootTypeGen < 5:
                                        lootTypeOne = "books"
                                        lootNumber = "3"

                                    if lootTypeGen >= 6 and lootTypeGen < 7:
                                        lootTypeOne = "iron helmet"
                                        lootNumber = "an"

                                    if lootTypeGen >= 8 and lootTypeGen < 9:
                                        lootTypeOne = "strange potion"
                                        lootNumber = "a"

                                    if lootTypeGen >= 9 and lootTypeGen <= 10:
                                        lootTypeOne = "lapis lazuli"
                                        lootNumber = random.randint(3,6)

                                    print("Oh! You found a chest! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")

                                if monsterDecider >= 1 and monsterDecider <= 10:
                                    monsterDecider = random.randint(1,10)

                                    if monsterDecider >= 1 and monsterDecider < 2:
                                        monsterType = "zombie(s)"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 3 * monsterNumber
                                        damageNumber = random.randint(3,6)

                                        itemType = "rotten flesh"
                                        itemNumber = random.randint(1,4)

                                        if monsterNumber == 4:
                                            itemNumber = random.randint(4,8)

                                        if monsterNumber == 5:
                                            itemNumber = random.randint(8,12)

                                        if monsterNumber == 6:
                                            itemNumber = random.randint(12,16)


                                if monsterDecider >= 1 and monsterDecider <= 10:
                                    monsterDecider = random.randint(1,10)

                                    if monsterDecider >= 2 and monsterDecider < 4:
                                        monsterType = "skeleton(s)"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 3 * monsterNumber
                                        damageNumber = random.randint(4,8)

                                        itemType = "bones"
                                        itemNumber = random.randint(1,4)

                                        if monsterNumber == 4:
                                            itemNumber = random.randint(4,8)

                                        if monsterNumber == 5:
                                            itemNumber = random.randint(8,12)

                                        if monsterNumber == 6:
                                            itemNumber = random.randint(12,16)


                                    if monsterDecider >= 4 and monsterDecider < 9:
                                        monsterType = "spider(s)"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 6 * monsterNumber
                                        damageNumber = random.randint(4,6)


                                        lootNumber = random.randint(1,2)
                                        if lootNumber == 1:
                                            itemType = "string"
                                            itemNumber = amountOfLoot(monsterNumber)

                                        if lootNumber == 2:
                                            itemType = "spider eye(s)"
                                            itemNumber = 2

                                            if monsterNumber == 5 or monsterNumber == 6:
                                                itemNumber = 4

                                    if monsterDecider >= 9 and monsterDecider <= 10:
                                        monsterType = "creeper"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 6 * monsterNumber
                                        damageNumber = random.randint(5,10)

                                        itemType = "gunpowder"
                                        itemNumber = amountOfLoot(monsterNumber)

                                    def enterDungeonThree():

                                        lootDecider = random.randint(1,10)
                                        lootTypeOne = "Nothing!"
                                        lootNumber = random.randint (1,10)
                                        monsterDecider = random.randint(1,10)
                                        monsterType = "Nothing!"
                                        monsterNumber = 0
                                        expNumber = 0


                                        if lootDecider >= 1 and lootDecider <= 10:

                                            if lootTypeGen >= 1 and lootTypeGen < 2:
                                                lootTypeOne = "enchanted sword"
                                                lootNumber = "an"

                                            if lootTypeGen >= 2 and lootTypeGen < 3:
                                                lootTypeOne = "bread"
                                                lootNumber = "10"

                                            if lootTypeGen >= 3 and lootTypeGen < 4:
                                                lootTypeOne = "cat"
                                                lootNumber = "a"

                                            if lootTypeGen >= 4 and lootTypeGen < 5:
                                                lootTypeOne = "sunflower"
                                                lootNumber = "1"

                                            if lootTypeGen >= 6 and lootTypeGen < 7:
                                                lootTypeOne = "iron"
                                                lootNumber = "12"

                                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                                lootTypeOne = "rotten flesh"
                                                lootNumber = random.randint(8,10)

                                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                                lootTypeOne = "diamonds"
                                                lootNumber = random.randint(1,2)

                                            print("Oh! You found a chest! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")

                                            if monsterDecider >= 1 and monsterDecider <= 10:
                                                monsterDecider = random.randint(1,10)
                                                damageNumber = 0
                                                itemNumber = 0
                                                itemType = "Nothing!"

                                                if monsterDecider >= 1 and monsterDecider < 2:
                                                    monsterType = "zombie(s)"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 3 * monsterNumber
                                                    damageNumber = random.randint(3,6)

                                                    itemType = "rotten flesh"
                                                    itemNumber = random.randint(1,4)

                                                    if monsterNumber == 4:
                                                        itemNumber = random.randint(4,8)

                                                    if monsterNumber == 5:
                                                        itemNumber = random.randint(8,12)

                                                    if monsterNumber == 6:
                                                        itemNumber = random.randint(12,16)

                                                if monsterDecider >= 1 and monsterDecider < 4:
                                                    monsterType = "skeleton(s)"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 3 * monsterNumber
                                                    damageNumber = random.randint(4,8)

                                                    itemType = "bones"
                                                    itemNumber = random.randint(1,4)

                                                    if monsterNumber == 4:
                                                        itemNumber = random.randint(4,8)

                                                    if monsterNumber == 5:
                                                        itemNumber = random.randint(8,12)

                                                    if monsterNumber == 6:
                                                        itemNumber = random.randint(12,16)


                                                if monsterDecider >= 4 and monsterDecider < 9:
                                                    monsterType = "spider(s)"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 6 * monsterNumber
                                                    damageNumber = random.randint(4,6)


                                                    lootNumber = random.randint(1,2)
                                                    if lootNumber == 1:
                                                        itemType = "string"
                                                        itemNumber = amountOfLoot(monsterNumber)

                                                    if lootNumber == 2:
                                                        itemType = "spider eye(s)"
                                                        itemNumber = 2

                                                    if monsterNumber == 5 or monsterNumber == 6:
                                                        itemNumber = 4

                                                if monsterDecider >= 9 and monsterDecider <= 10:
                                                    monsterType = "creeper"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 6 * monsterNumber
                                                    damageNumber = random.randint(5,10)

                                                    itemType = "gunpowder"
                                                    itemNumber = amountOfLoot(monsterNumber)

                                                print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                                                print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")
                                                print("You've reached the end of the dungeon, you return home with your new loot!")

                                    print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                                    print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")
                                    print("Continue?")
                                    print("1. Yes")
                                    print("2. No")
                                    userSelect = input("Answer")

                                    if userSelect == ("1"):
                                        enterDungeonThree()

                                    if userSelect == ("2"):
                                        print("You leave the castle and return home with your loot.")

                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")
                            print("Continue?")
                            print("1. Yes")
                            print("2. No")
                            userSelect = input("Answer")

                            if userSelect == ("1"):
                                enterDungeonTwo()

                            if userSelect == ("2"):
                                print("You leave the castle and return home with your loot.")

                if dungeonDecider >= 50 and dungeonDecider < 53:
                    dungeonType = "single villager house"

                    def lootVillagerHouse():
                        print ("You go inside the villager house whilst they're not looking and find an anvil.")

                    def tradeVillagerHouse():
                        print ('The villager lays out his wears; 3 bread, suspicious stew, 4 iron, and an enchanted golden sword...')

                if dungeonDecider >= 53 and dungeonDecider < 55:
                    dungeonType = "abandoned camp"

                    def exploreAbandonedCamp():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint(4,8)
                        monsterNumber = 0

                        if lootDecider >= 1 and lootDecider < 5:
                            print("You find nothing of interest in the empty tents but find 3 charcoal in the fire pit.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "bread"
                                lootNumber = "some"

                            if lootTypeGen >= 4 and lootTypeGen < 6:
                                lootTypeOne = "iron shovel"
                                lootNumber = "an"

                            if lootTypeGen >= 6 and lootTypeGen < 8:
                                lootTypeOne = "iron"
                                lootNumber = random.randint(4,8)

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "gold"
                                lootNumber = random.randint(1,3)

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "of leather boots"
                                lootNumber = "a pair"

                            print("Oh! You found a chest in one of the abandoned tents! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")



                if dungeonDecider >= 55 and dungeonDecider < 60:
                    dungeonType = "spawn alter"

                    def exploreSpawnAlter():
                        monsterType = "Nothing!"
                        monsterDecider = random.randint(1,10)
                        monsterNumber = 0

                        if monsterDecider >= 1 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(0,3)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 2:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 3:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider < 9:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(0,3)


                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 1

                                    if monsterNumber == 3 or monsterNumber == 4:
                                        itemNumber = 2

                            if monsterDecider >= 9 and monsterDecider <= 10:
                                monsterType = "creeper"
                                monsterNumber = random.randint(1,4)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(0,8)

                                itemType = "gunpowder"
                                itemNumber = amountOfLoot(monsterNumber)

                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")


                if dungeonDecider >= 60 and dungeonDecider < 65:
                    dungeonType = "well"

                    def exploreWell():
                        lootDecider = random.randint(1,10)
                        itemNumber = random.randint(1,10)

                        if lootDecider >= 1 and lootDecider < 6:
                            print("You find nothing of interest in the well, only fresh water.")

                        if lootDecider >= 6 and lootDecider < 8:
                            print("You find " + str(itemNumber) + " iron nuggets at the bottom of the well!")

                        if lootDecider >= 8 and lootDecider <= 10:
                            print("Yoi find " + str(itemNumber) + " gold nuggets at the bottom of the well!")

                if dungeonDecider >= 65 and dungeonDecider < 70:
                    dungeonType = "small dungeon"

                    def exploreSmallDungeon():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootTypeTwo = "Nothing!"
                        lootNumberOne = 0
                        lootNumberTwo = 0
                        monsterType = "Nothing!"
                        monsterDecider = random.randint(1,10)
                        monsterNumber = 0
                        damageNumber = 0

                        if monsterDecider >= 1 and monsterDecider <= 2:
                            lootNumberOne = random.randint(1,10)
                            lootDecider = random.randint(1,10)

                            if lootDecider == 1:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " rotten flesh in a chest!")

                            if lootDecider == 2:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " bones in a chest!")

                            if lootDecider == 3:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " rotten flesh in a chest!")

                            if lootDecider == 4:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " bones in a chest!")

                            if lootDecider == 5:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " books in a chest!")

                            if lootDecider == 6:
                                print("There are no monsters inside, lucky you! You find an Enchanted Book with the enchant Sharpness I in a chest!")

                            if lootDecider == 7:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " gunpowder in a chest!")

                            if lootDecider == 8:
                                print("There are no monsters inside, lucky you! You find an Enchanted Book with the enchant Protection I in a chest!")

                            if lootDecider == 9:
                                print("There are no monsters inside, lucky you! You find a strange potion in a chest!")

                            if lootDecider == 10:
                                print("There are no monsters inside, lucky you! You find a golden apple in a chest!")

                        if monsterDecider >= 3 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider <= 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(0,3)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 2:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 3:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider <= 6:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(1,3)
                                expNumber = 4 * monsterNumber
                                damageNumber = random.randint(0,3)
                                itemNumber = 0

                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 1

                                    if monsterNumber == 3 or monsterNumber == 4:
                                        itemNumber = 2

                            if monsterDecider >= 6 and monsterDecider <= 10:
                                monsterType = "skeleton(s)"
                                monsterNumber = random.randint(1,3)
                                expNumber = 4 * monsterNumber
                                damageNumber = random.randint(0,3)
                                itemNumber = 0

                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "bone(s)"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "broken bow"
                                    itemNumber = 1

                            lootDecider = random.randint(1,10)
                            lootNumberOne = 0
                            lootNumberTwo = 0
                            lootTypeOne = "Nothing!"
                            lootTypeTwo = "Nothing!"

                            if lootDecider == 1:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "rotten flesh"

                            if lootDecider == 2:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "bones"

                            if lootDecider == 3:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "rotten flesh"

                            if lootDecider == 4:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "bones"

                            if lootDecider == 5:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "gunpowder"

                            if lootDecider == 6:
                                lootNumberOne = "an"
                                lootTypeOne = "Enchanted Book with Sharpness I"

                            if lootDecider == 7:
                                lootNumberOne = "a"
                                lootTypeOne = "golden sword"

                            if lootDecider == 8:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "iron"

                            if lootDecider == 9:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "wheat"

                            if lootDecider == 10:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "carrots"

                            lootDecider = random.randint(1,10)
                            lootNumberTwo = 0
                            lootTypeTwo = "Nothing!"

                            if lootDecider == 1:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "rotten flesh"

                            if lootDecider == 2:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "bones"

                            if lootDecider == 3:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "rotten flesh"

                            if lootDecider == 4:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "bones"

                            if lootDecider == 5:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "gunpowder"

                            if lootDecider == 6:
                                lootNumberTwo = "an"
                                lootTypeTwo = "Enchanted Book with Protection I"

                            if lootDecider == 7:
                                lootNumberTwo = "a"
                                lootTypeTwo = "strange potion"

                            if lootDecider == 8:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "coal"

                            if lootDecider == 9:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "potatoes"

                            if lootDecider == 10:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "golden nuggets"

                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points." )
                            print("You also find " + str(lootNumberOne) + " " + str(lootTypeOne) + " and " + str(lootNumberTwo) + " " + str(lootTypeTwo) + " in a chest!")


                if dungeonDecider >= 70 and dungeonDecider < 85:
                    dungeonType = "shallow cave"

                    def exploreShallowCave():
                        lootDecider = random.randint(1,10)
                        lootTypeGen = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = 0

                        if lootDecider >= 1 and lootDecider < 5:
                            print("You find there is nothing of interest in the cave.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "iron"
                                lootNumber = random.randint(1,6)

                            if lootTypeGen >= 4 and lootTypeGen <= 10:
                                lootTypeOne= "coal"
                                lootNumber = random.randint(4,8)

                            print("You found " + str(lootNumber) + " " + str(lootTypeOne) + " in the cave! You mine it and return home.")


                if dungeonDecider >= 85 and dungeonDecider < 90:
                    dungeonType = "tiny mossy cobble structure"

                    def exploreDungeonTinyMoss():
                        monsterType = "Nothing!"
                        monsterDecider = random.randint(1,10)
                        monsterNumber = 0

                        if monsterDecider >= 1 and monsterDecider < 5:
                            print("There's nothing inside it, you can take some of the mossy stone if you want but that's about all there is of interest.")

                        if monsterDecider >= 5 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(0,3)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 2:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 3:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider < 6:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(1,3)
                                expNumber = 4 * monsterNumber
                                damageNumber = random.randint(0,3)

                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 1

                                    if monsterNumber == 3 or monsterNumber == 4:
                                        itemNumber = 2

                            if monsterDecider >= 9 and monsterDecider <= 10:
                                monsterType = "creeper"
                                monsterNumber = random.randint(1,4)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(0,8)

                                itemType = "gunpowder"
                                itemNumber = amountOfLoot(monsterNumber)


                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")

                        def leaveDungeonTinyMoss():
                            print("You leave the tiny mossy cobble structure alone and return home.")

                if dungeonDecider >= 90 and dungeonDecider < 95:
                    dungeonType = "pond"

                    def exploreDungeonPond():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint(4,8)

                        if lootDecider >= 1 and lootDecider < 5:
                            print("Upon closer inspection you realize that this is just a regular pond. The water must be cool and clean, but there's not much else of interest.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "leather boots"

                            if lootTypeGen >= 4 and lootTypeGen < 6:
                                lootTypeOne = "stone axe"

                            if lootTypeGen >= 6 and lootTypeGen < 8:
                                lootTypeOne = "stone shovel"

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "iron shovel"

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "diamond"

                            print("Oh! You can see (a) " + str(lootTypeOne) + " in the pond! You fish the " + str(lootTypeOne) + " out of the water.")


                        def leaveDungeonPond():
                            print("You leave the pond alone and return home.")

                if dungeonDecider >= 95 and dungeonDecider < 98:
                    dungeonType = "horse"

                    def huntDungeonHorse():
                        mobDropNumber = random.randint(1,3)
                        expNumber = random.randint(1,5)

                        print("You slay the beast with your sword, you gain " + str(mobDropNumber) + " leather and " + str(expNumber) + " Pixel Point(s).")

                    def tameDungeonHorse():
                        mobDecider = random.randint(1,100)

                        if mobDecider >= 1 and mobDecider < 60:
                            print("The horse doesn't trust you and gets away before you can lasso it! Better luck next time!")

                        if mobDecider >= 60 and mobDecider <= 100:
                            print("You manage to get the horse's trust and tame it! You have a new friend now!")


                if dungeonDecider >= 98 and dungeonDecider <= 100:
                    dungeonType = "donkey"

                    def huntDungeonDonkey():
                        mobDropNumber = random.randint(1,3)
                        expNumber = random.randint(1,5)

                        print("You slay the beast with your sword, you gain " + str(mobDropNumber) + " leather and " + str(expNumber) + " Pixel Point(s).")

                    def tameDungeonDonkey():
                        mobDecider = random.randint(1,100)

                        if mobDecider >= 1 and mobDecider < 60:
                            print("The donkey doesn't trust you and gets away before you can lasso it! Better luck next time!")

                        if mobDecider >= 60 and mobDecider <= 100:
                            print("You manage to get the donkey's trust and tame it! You have a new friend now!")

                print("Whoa! You found something! It's a " + str(dungeonType) + "!")

                if dungeonType == "castle dungeon":

                    print("You have found a castle dungeon... these are very rare, and dangerous.")
                    print("What do you want to do?")
                    print("1. -explore!")
                    print("2. -leave!")

                    userSelect = input("I will- ")
                    if userSelect == "1":
                        enterDungeon()

                    if userSelect == "2":
                        print("You wisely leave the dungeon alone, perhaps you should gear up first...")

                if dungeonType == "single villager house":
                    print("What do you want to do?")
                    print("1. -loot the house!")
                    print ("2. -trade with the villager!")
                    print ("3. -leave!")

                    userSelect = input("I will- ")
                    if userSelect == "1":
                        lootVillagerHouse()

                    if userSelect == "2":
                        tradeVillagerHouse()

                    if userSelect == "3":
                        print ("You leave the villager house alone for now.")

                if dungeonType == "abandoned camp":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreAbandonedCamp()

                    if userSelect == "2":
                        print("You decide not to look around and return home...")

                if dungeonType == "spawn alter":
                    print("what do you want to do?")
                    print("1. -explore further!")
                    print("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreSpawnAlter()

                    if userSelect == "2":
                        print("You decider to leave the strange alter alone and return home.")

                if dungeonType == "well":
                    print("what do you want to do?")
                    print("1. -explore further!")
                    print("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreWell()

                    if userSelect == "2":
                        print("You decide to leave the well alone and return home.")

                if dungeonType == "small dungeon":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreSmallDungeon()

                    if userSelect == "2":
                        print("You decide not to look inside and return home...")

                if dungeonType == "large rock":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonLargeRock()

                    if userSelect == "2":
                        leaveDungeonLargeRock()


                if dungeonType == "scarecrow":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonScarecrow()

                    if userSelect == "2":
                        leaveDungeonScarecrow()

                if dungeonType == "shallow cave":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreShallowCave()

                    if userSelect == "2":
                        print("You leave the cave be for now and return home.")

                if dungeonType == "tiny mossy cobble structure":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonTinyMoss()

                    if userSelect == "2":
                        leaveDungeonTinyMoss()

                if dungeonType == "pond":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonPond()

                    if userSelect == "2":
                        leaveDungeonPond()

                if dungeonType == "horse":
                    print("What do you want to do?")
                    print ("1. -hunt the horse!")
                    print ("2. -tame the horse!")
                    print ("3. -leave the horse alone!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        huntDungeonHorse()

                    if userSelect == "2":
                        tameDungeonHorse()

                    if userSelect == "3":
                        print("You leave the horse alone and return home.")

                if dungeonType == "donkey":
                    print("What do you want to do?")
                    print ("1. -hunt the donkey!")
                    print ("2. -tame the donkey!")
                    print ("3. -leave the donkey alone!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        huntDungeonDonkey()

                    if userSelect == "2":
                        tameDungeonDonkey()

                    if userSelect == "3":
                        print("You leave the donkey alone and return home.")

    def locationSunflowerFields():
        explorationSuccess = random.randint(1,100)
        dungeonDecider = random.randint(1,100)
        lootDecider = random.randint(1,10)
        monsterDecider = random.randint(1,10)
        lootTypeGen = random.randint(1,10)
        monsterNumber = 0
        expNumber = 0
        damageNumber = 0
        lootNumber = 0
        dungeonType = "Nothing!"
        lootTypeOne = "Nothing!"
        lootTypeTwo = "Nothing!"
        lootTypeThree = "Nothing!"
        monsterType = "Nothing!"

        if explorationSuccess >= 1 and explorationSuccess < 80:
            print("You explore around the area but quickly get tired and return home...")
        else:
            if explorationSuccess >= 80 and explorationSuccess <= 100:

                if dungeonDecider >= 1 and dungeonDecider < 35:
                    dungeonType = "large rock"

                    def exploreDungeonLargeRock():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint(4,8)
                        monsterNumber = 0

                        if lootDecider >= 1 and lootDecider < 5:
                            print("Upon closer inspection you realize that this is just a normal rock.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "iron"
                                lootNumber = "1"

                            if lootTypeGen >= 4 and lootTypeGen < 6:
                                lootTypeOne = "gold"
                                lootNumber = "1"

                            if lootTypeGen >= 6 and lootTypeGen < 8:
                                lootTypeOne = "redstone"
                                lootNumber = random.randint(4,8)

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "lapis lazuli"
                                lootNumber = random.randint(4,8)

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "diamond"
                                lootNumber = "1"

                            print("Oh! There's " + str(lootTypeOne) + " in the stone! You mine it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")


                    def leaveDungeonLargeRock():
                        print("You leave the large rock alone and return home.")


                if dungeonDecider >= 35 and dungeonDecider < 48:
                    dungeonType = "scarecrow"

                    def exploreDungeonScarecrow():
                            print("Do you want to take the scarecrow's jack-o-lantern head?")
                            print("1. Yes, I will take the head")
                            print("2. No, I will leave it be")

                            userSelect = input("I will-")
                            if userSelect == "1":
                                print("You take the scarecrow's head. You gained +1 jack-o-lantern.")

                            if userSelect == "2":
                                print("You leave the scarecrow's head alone and return home.")

                if dungeonDecider >= 48 and dungeonDecider < 50:
                    dungeonType = "castle dungeon"

                    def enterDungeon():
                        print("You have found a castle dungeon... these are very rare, and dangerous.")

                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint (1,10)
                        monsterDecider = random.randint(1,10)
                        monsterType = "Nothing!"
                        monsterNumber = 0


                        if lootDecider >= 1 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 2:
                                lootTypeOne = "leather shirt"
                                lootNumber = "a"

                            if lootTypeGen >= 2 and lootTypeGen < 3:
                                lootTypeOne = "bread"
                                lootNumber = "4"

                            if lootTypeGen >= 3 and lootTypeGen < 4:
                                lootTypeOne = "strange potion"
                                lootNumber = "a"

                            if lootTypeGen >= 4 and lootTypeGen < 5:
                                lootTypeOne = "gold"
                                lootNumber = random.randint(3,6)

                            if lootTypeGen >= 6 and lootTypeGen < 7:
                                lootTypeOne = "enchanted sword"
                                lootNumber = "an"

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "bone"
                                lootNumber = random.randint(8,10)

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "potatoes"
                                lootNumber = "3"

                            print("Oh! You found a chest! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")

                        if monsterDecider >= 1 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(4,6)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(3,6)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 5:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 6:
                                    itemNumber = random.randint(12,16)


                        if monsterDecider >= 1 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "skeleton(s)"
                                monsterNumber = random.randint(4,6)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(4,8)

                                itemType = "bones"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 5:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 6:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider < 9:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(4,6)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(4,6)


                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 2

                                    if monsterNumber == 5 or monsterNumber == 6:
                                        itemNumber = 4

                            if monsterDecider >= 9 and monsterDecider <= 10:
                                monsterType = "creeper"
                                monsterNumber = random.randint(4,6)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(5,10)

                                itemType = "gunpowder"
                                itemNumber = amountOfLoot(monsterNumber)

                            def enterDungeonTwo():

                                lootDecider = random.randint(1,10)
                                lootTypeOne = "Nothing!"
                                lootNumber = random.randint (1,10)
                                monsterDecider = random.randint(1,10)
                                monsterType = "Nothing!"
                                monsterNumber = 0


                                if lootDecider >= 1 and lootDecider <= 10:

                                    if lootTypeGen >= 1 and lootTypeGen < 2:
                                        lootTypeOne = "enchanted sword"
                                        lootNumber = "an"

                                    if lootTypeGen >= 2 and lootTypeGen < 3:
                                        lootTypeOne = "bread"
                                        lootNumber = "6"

                                    if lootTypeGen >= 3 and lootTypeGen < 4:
                                        lootTypeOne = "gunpowder"
                                        lootNumber = random.randint(8,10)

                                    if lootTypeGen >= 4 and lootTypeGen < 5:
                                        lootTypeOne = "books"
                                        lootNumber = "3"

                                    if lootTypeGen >= 6 and lootTypeGen < 7:
                                        lootTypeOne = "iron helmet"
                                        lootNumber = "an"

                                    if lootTypeGen >= 8 and lootTypeGen < 9:
                                        lootTypeOne = "strange potion"
                                        lootNumber = "a"

                                    if lootTypeGen >= 9 and lootTypeGen <= 10:
                                        lootTypeOne = "lapis lazuli"
                                        lootNumber = random.randint(3,6)

                                    print("Oh! You found a chest! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")

                                if monsterDecider >= 1 and monsterDecider <= 10:
                                    monsterDecider = random.randint(1,10)

                                    if monsterDecider >= 1 and monsterDecider < 2:
                                        monsterType = "zombie(s)"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 3 * monsterNumber
                                        damageNumber = random.randint(3,6)

                                        itemType = "rotten flesh"
                                        itemNumber = random.randint(1,4)

                                        if monsterNumber == 4:
                                            itemNumber = random.randint(4,8)

                                        if monsterNumber == 5:
                                            itemNumber = random.randint(8,12)

                                        if monsterNumber == 6:
                                            itemNumber = random.randint(12,16)


                                if monsterDecider >= 1 and monsterDecider <= 10:
                                    monsterDecider = random.randint(1,10)

                                    if monsterDecider >= 2 and monsterDecider < 4:
                                        monsterType = "skeleton(s)"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 3 * monsterNumber
                                        damageNumber = random.randint(4,8)

                                        itemType = "bones"
                                        itemNumber = random.randint(1,4)

                                        if monsterNumber == 4:
                                            itemNumber = random.randint(4,8)

                                        if monsterNumber == 5:
                                            itemNumber = random.randint(8,12)

                                        if monsterNumber == 6:
                                            itemNumber = random.randint(12,16)


                                    if monsterDecider >= 4 and monsterDecider < 9:
                                        monsterType = "spider(s)"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 6 * monsterNumber
                                        damageNumber = random.randint(4,6)


                                        lootNumber = random.randint(1,2)
                                        if lootNumber == 1:
                                            itemType = "string"
                                            itemNumber = amountOfLoot(monsterNumber)

                                        if lootNumber == 2:
                                            itemType = "spider eye(s)"
                                            itemNumber = 2

                                            if monsterNumber == 5 or monsterNumber == 6:
                                                itemNumber = 4

                                    if monsterDecider >= 9 and monsterDecider <= 10:
                                        monsterType = "creeper"
                                        monsterNumber = random.randint(4,6)
                                        expNumber = 6 * monsterNumber
                                        damageNumber = random.randint(5,10)

                                        itemType = "gunpowder"
                                        itemNumber = amountOfLoot(monsterNumber)

                                    def enterDungeonThree():

                                        lootDecider = random.randint(1,10)
                                        lootTypeOne = "Nothing!"
                                        lootNumber = random.randint (1,10)
                                        monsterDecider = random.randint(1,10)
                                        monsterType = "Nothing!"
                                        monsterNumber = 0
                                        expNumber = 0


                                        if lootDecider >= 1 and lootDecider <= 10:

                                            if lootTypeGen >= 1 and lootTypeGen < 2:
                                                lootTypeOne = "enchanted sword"
                                                lootNumber = "an"

                                            if lootTypeGen >= 2 and lootTypeGen < 3:
                                                lootTypeOne = "bread"
                                                lootNumber = "10"

                                            if lootTypeGen >= 3 and lootTypeGen < 4:
                                                lootTypeOne = "cat"
                                                lootNumber = "a"

                                            if lootTypeGen >= 4 and lootTypeGen < 5:
                                                lootTypeOne = "sunflower"
                                                lootNumber = "1"

                                            if lootTypeGen >= 6 and lootTypeGen < 7:
                                                lootTypeOne = "iron"
                                                lootNumber = "12"

                                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                                lootTypeOne = "rotten flesh"
                                                lootNumber = random.randint(8,10)

                                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                                lootTypeOne = "diamonds"
                                                lootNumber = random.randint(1,2)

                                            print("Oh! You found a chest! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")

                                            if monsterDecider >= 1 and monsterDecider <= 10:
                                                monsterDecider = random.randint(1,10)
                                                damageNumber = 0
                                                itemNumber = 0
                                                itemType = "Nothing!"

                                                if monsterDecider >= 1 and monsterDecider < 2:
                                                    monsterType = "zombie(s)"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 3 * monsterNumber
                                                    damageNumber = random.randint(3,6)

                                                    itemType = "rotten flesh"
                                                    itemNumber = random.randint(1,4)

                                                    if monsterNumber == 4:
                                                        itemNumber = random.randint(4,8)

                                                    if monsterNumber == 5:
                                                        itemNumber = random.randint(8,12)

                                                    if monsterNumber == 6:
                                                        itemNumber = random.randint(12,16)

                                                if monsterDecider >= 1 and monsterDecider < 4:
                                                    monsterType = "skeleton(s)"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 3 * monsterNumber
                                                    damageNumber = random.randint(4,8)

                                                    itemType = "bones"
                                                    itemNumber = random.randint(1,4)

                                                    if monsterNumber == 4:
                                                        itemNumber = random.randint(4,8)

                                                    if monsterNumber == 5:
                                                        itemNumber = random.randint(8,12)

                                                    if monsterNumber == 6:
                                                        itemNumber = random.randint(12,16)


                                                if monsterDecider >= 4 and monsterDecider < 9:
                                                    monsterType = "spider(s)"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 6 * monsterNumber
                                                    damageNumber = random.randint(4,6)


                                                    lootNumber = random.randint(1,2)
                                                    if lootNumber == 1:
                                                        itemType = "string"
                                                        itemNumber = amountOfLoot(monsterNumber)

                                                    if lootNumber == 2:
                                                        itemType = "spider eye(s)"
                                                        itemNumber = 2

                                                    if monsterNumber == 5 or monsterNumber == 6:
                                                        itemNumber = 4

                                                if monsterDecider >= 9 and monsterDecider <= 10:
                                                    monsterType = "creeper"
                                                    monsterNumber = random.randint(4,6)
                                                    expNumber = 6 * monsterNumber
                                                    damageNumber = random.randint(5,10)

                                                    itemType = "gunpowder"
                                                    itemNumber = amountOfLoot(monsterNumber)

                                                print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                                                print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")
                                                print("You've reached the end of the dungeon, you return home with your new loot!")

                                    print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                                    print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")
                                    print("Continue?")
                                    print("1. Yes")
                                    print("2. No")
                                    userSelect = input("Answer")

                                    if userSelect == ("1"):
                                        enterDungeonThree()

                                    if userSelect == ("2"):
                                        print("You leave the castle and return home with your loot.")

                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")
                            print("Continue?")
                            print("1. Yes")
                            print("2. No")
                            userSelect = input("Answer")

                            if userSelect == ("1"):
                                enterDungeonTwo()

                            if userSelect == ("2"):
                                print("You leave the castle and return home with your loot.")

                if dungeonDecider >= 50 and dungeonDecider < 53:
                    dungeonType = "single villager house"

                    def lootVillagerHouse():
                        print ("You go inside the villager house whilst they're not looking and find an anvil.")

                    def tradeVillagerHouse():
                        print ('The villager lays out his wears; 3 bread, suspicious stew, 4 iron, and an enchanted golden sword...')

                if dungeonDecider >= 53 and dungeonDecider < 55:
                    dungeonType = "abandoned camp"

                    def exploreAbandonedCamp():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint(4,8)
                        monsterNumber = 0

                        if lootDecider >= 1 and lootDecider < 5:
                            print("You find nothing of interest in the empty tents but find 3 charcoal in the fire pit.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "bread"
                                lootNumber = "some"

                            if lootTypeGen >= 4 and lootTypeGen < 6:
                                lootTypeOne = "iron shovel"
                                lootNumber = "an"

                            if lootTypeGen >= 6 and lootTypeGen < 8:
                                lootTypeOne = "iron"
                                lootNumber = random.randint(4,8)

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "gold"
                                lootNumber = random.randint(1,3)

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "of leather boots"
                                lootNumber = "a pair"

                            print("Oh! You found a chest in one of the abandoned tents! You check inside it and get " + str(lootNumber) + " " + str(lootTypeOne) + "!")



                if dungeonDecider >= 55 and dungeonDecider < 60:
                    dungeonType = "spawn alter"

                    def exploreSpawnAlter():
                        monsterType = "Nothing!"
                        monsterDecider = random.randint(1,10)
                        monsterNumber = 0

                        if monsterDecider >= 1 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(0,3)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 2:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 3:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider < 9:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(0,3)


                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 1

                                    if monsterNumber == 3 or monsterNumber == 4:
                                        itemNumber = 2

                            if monsterDecider >= 9 and monsterDecider <= 10:
                                monsterType = "creeper"
                                monsterNumber = random.randint(1,4)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(0,8)

                                itemType = "gunpowder"
                                itemNumber = amountOfLoot(monsterNumber)

                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")


                if dungeonDecider >= 60 and dungeonDecider < 65:
                    dungeonType = "well"

                    def exploreWell():
                        lootDecider = random.randint(1,10)
                        itemNumber = random.randint(1,10)

                        if lootDecider >= 1 and lootDecider < 6:
                            print("You find nothing of interest in the well, only fresh water.")

                        if lootDecider >= 6 and lootDecider < 8:
                            print("You find " + str(itemNumber) + " iron nuggets at the bottom of the well!")

                        if lootDecider >= 8 and lootDecider <= 10:
                            print("Yoi find " + str(itemNumber) + " gold nuggets at the bottom of the well!")

                if dungeonDecider >= 65 and dungeonDecider < 70:
                    dungeonType = "small dungeon"

                    def exploreSmallDungeon():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootTypeTwo = "Nothing!"
                        lootNumberOne = 0
                        lootNumberTwo = 0
                        monsterType = "Nothing!"
                        monsterDecider = random.randint(1,10)
                        monsterNumber = 0
                        damageNumber = 0

                        if monsterDecider >= 1 and monsterDecider <= 2:
                            lootNumberOne = random.randint(1,10)
                            lootDecider = random.randint(1,10)

                            if lootDecider == 1:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " rotten flesh in a chest!")

                            if lootDecider == 2:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " bones in a chest!")

                            if lootDecider == 3:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " rotten flesh in a chest!")

                            if lootDecider == 4:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " bones in a chest!")

                            if lootDecider == 5:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " books in a chest!")

                            if lootDecider == 6:
                                print("There are no monsters inside, lucky you! You find an Enchanted Book with the enchant Sharpness I in a chest!")

                            if lootDecider == 7:
                                print("There are no monsters inside, lucky you! You find " + str(lootNumberOne) + " gunpowder in a chest!")

                            if lootDecider == 8:
                                print("There are no monsters inside, lucky you! You find an Enchanted Book with the enchant Protection I in a chest!")

                            if lootDecider == 9:
                                print("There are no monsters inside, lucky you! You find a strange potion in a chest!")

                            if lootDecider == 10:
                                print("There are no monsters inside, lucky you! You find a golden apple in a chest!")

                        if monsterDecider >= 3 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider <= 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(0,3)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 2:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 3:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider <= 6:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(1,3)
                                expNumber = 4 * monsterNumber
                                damageNumber = random.randint(0,3)
                                itemNumber = 0

                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 1

                                    if monsterNumber == 3 or monsterNumber == 4:
                                        itemNumber = 2

                            if monsterDecider >= 6 and monsterDecider <= 10:
                                monsterType = "skeleton(s)"
                                monsterNumber = random.randint(1,3)
                                expNumber = 4 * monsterNumber
                                damageNumber = random.randint(0,3)
                                itemNumber = 0

                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "bone(s)"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "broken bow"
                                    itemNumber = 1

                            lootDecider = random.randint(1,10)
                            lootNumberOne = 0
                            lootNumberTwo = 0
                            lootTypeOne = "Nothing!"
                            lootTypeTwo = "Nothing!"

                            if lootDecider == 1:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "rotten flesh"

                            if lootDecider == 2:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "bones"

                            if lootDecider == 3:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "rotten flesh"

                            if lootDecider == 4:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "bones"

                            if lootDecider == 5:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "gunpowder"

                            if lootDecider == 6:
                                lootNumberOne = "an"
                                lootTypeOne = "Enchanted Book with Sharpness I"

                            if lootDecider == 7:
                                lootNumberOne = "a"
                                lootTypeOne = "golden sword"

                            if lootDecider == 8:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "iron"

                            if lootDecider == 9:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "wheat"

                            if lootDecider == 10:
                                lootNumberOne = random.randint(1,10)
                                lootTypeOne = "carrots"

                            lootDecider = random.randint(1,10)
                            lootNumberTwo = 0
                            lootTypeTwo = "Nothing!"

                            if lootDecider == 1:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "rotten flesh"

                            if lootDecider == 2:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "bones"

                            if lootDecider == 3:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "rotten flesh"

                            if lootDecider == 4:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "bones"

                            if lootDecider == 5:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "gunpowder"

                            if lootDecider == 6:
                                lootNumberTwo = "an"
                                lootTypeTwo = "Enchanted Book with Protection I"

                            if lootDecider == 7:
                                lootNumberTwo = "a"
                                lootTypeTwo = "strange potion"

                            if lootDecider == 8:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "coal"

                            if lootDecider == 9:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "potatoes"

                            if lootDecider == 10:
                                lootNumberTwo = random.randint(1,10)
                                lootTypeTwo = "golden nuggets"

                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points." )
                            print("You also find " + str(lootNumberOne) + " " + str(lootTypeOne) + " and " + str(lootNumberTwo) + " " + str(lootTypeTwo) + " in a chest!")


                if dungeonDecider >= 70 and dungeonDecider < 85:
                    dungeonType = "shallow cave"

                    def exploreShallowCave():
                        lootDecider = random.randint(1,10)
                        lootTypeGen = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = 0

                        if lootDecider >= 1 and lootDecider < 5:
                            print("You find there is nothing of interest in the cave.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "iron"
                                lootNumber = random.randint(1,6)

                            if lootTypeGen >= 4 and lootTypeGen <= 10:
                                lootTypeOne= "coal"
                                lootNumber = random.randint(4,8)

                            print("You found " + str(lootNumber) + " " + str(lootTypeOne) + " in the cave! You mine it and return home.")


                if dungeonDecider >= 85 and dungeonDecider < 90:
                    dungeonType = "tiny mossy cobble structure"

                    def exploreDungeonTinyMoss():
                        monsterType = "Nothing!"
                        monsterDecider = random.randint(1,10)
                        monsterNumber = 0

                        if monsterDecider >= 1 and monsterDecider < 5:
                            print("There's nothing inside it, you can take some of the mossy stone if you want but that's about all there is of interest.")

                        if monsterDecider >= 5 and monsterDecider <= 10:
                            monsterDecider = random.randint(1,10)

                            if monsterDecider >= 1 and monsterDecider < 4:
                                monsterType = "zombie(s)"
                                monsterNumber = random.randint(1,4)
                                expNumber = 3 * monsterNumber
                                damageNumber = random.randint(0,3)

                                itemType = "rotten flesh"
                                itemNumber = random.randint(1,4)

                                if monsterNumber == 2:
                                    itemNumber = random.randint(4,8)

                                if monsterNumber == 3:
                                    itemNumber = random.randint(8,12)

                                if monsterNumber == 4:
                                    itemNumber = random.randint(12,16)


                            if monsterDecider >= 4 and monsterDecider < 6:
                                monsterType = "spider(s)"
                                monsterNumber = random.randint(1,3)
                                expNumber = 4 * monsterNumber
                                damageNumber = random.randint(0,3)

                                lootNumber = random.randint(1,2)
                                if lootNumber == 1:
                                    itemType = "string"
                                    itemNumber = amountOfLoot(monsterNumber)

                                if lootNumber == 2:
                                    itemType = "spider eye(s)"
                                    itemNumber = 1

                                    if monsterNumber == 3 or monsterNumber == 4:
                                        itemNumber = 2

                            if monsterDecider >= 9 and monsterDecider <= 10:
                                monsterType = "creeper"
                                monsterNumber = random.randint(1,4)
                                expNumber = 6 * monsterNumber
                                damageNumber = random.randint(0,8)

                                itemType = "gunpowder"
                                itemNumber = amountOfLoot(monsterNumber)


                            print("Oh no! There's a spawner inside! You find yourself face to face with "  + str(monsterNumber) + " " + str(monsterType) + "!")
                            print("You fight them off, taking " + str(damageNumber) + " damage. But they drop " + str(itemNumber) + " " + str(itemType) + " and " + str(expNumber) + " Pixel Points.")

                        def leaveDungeonTinyMoss():
                            print("You leave the tiny mossy cobble structure alone and return home.")

                if dungeonDecider >= 90 and dungeonDecider < 95:
                    dungeonType = "pond"

                    def exploreDungeonPond():
                        lootDecider = random.randint(1,10)
                        lootTypeOne = "Nothing!"
                        lootNumber = random.randint(4,8)

                        if lootDecider >= 1 and lootDecider < 5:
                            print("Upon closer inspection you realize that this is just a regular pond. The water must be cool and clean, but there's not much else of interest.")

                        if lootDecider >= 5 and lootDecider <= 10:

                            if lootTypeGen >= 1 and lootTypeGen < 4:
                                lootTypeOne = "leather boots"

                            if lootTypeGen >= 4 and lootTypeGen < 6:
                                lootTypeOne = "stone axe"

                            if lootTypeGen >= 6 and lootTypeGen < 8:
                                lootTypeOne = "stone shovel"

                            if lootTypeGen >= 8 and lootTypeGen < 9:
                                lootTypeOne = "iron shovel"

                            if lootTypeGen >= 9 and lootTypeGen <= 10:
                                lootTypeOne = "diamond"

                            print("Oh! You can see (a) " + str(lootTypeOne) + " in the pond! You fish the " + str(lootTypeOne) + " out of the water.")


                        def leaveDungeonPond():
                            print("You leave the pond alone and return home.")

                if dungeonDecider >= 95 and dungeonDecider < 98:
                    dungeonType = "horse"

                    def huntDungeonHorse():
                        mobDropNumber = random.randint(1,3)
                        expNumber = random.randint(1,5)

                        print("You slay the beast with your sword, you gain " + str(mobDropNumber) + " leather and " + str(expNumber) + " Pixel Point(s).")

                    def tameDungeonHorse():
                        mobDecider = random.randint(1,100)

                        if mobDecider >= 1 and mobDecider < 60:
                            print("The horse doesn't trust you and gets away before you can lasso it! Better luck next time!")

                        if mobDecider >= 60 and mobDecider <= 100:
                            print("You manage to get the horse's trust and tame it! You have a new friend now!")


                if dungeonDecider >= 98 and dungeonDecider <= 100:
                    dungeonType = "donkey"

                    def huntDungeonDonkey():
                        mobDropNumber = random.randint(1,3)
                        expNumber = random.randint(1,5)

                        print("You slay the beast with your sword, you gain " + str(mobDropNumber) + " leather and " + str(expNumber) + " Pixel Point(s).")

                    def tameDungeonDonkey():
                        mobDecider = random.randint(1,100)

                        if mobDecider >= 1 and mobDecider < 60:
                            print("The donkey doesn't trust you and gets away before you can lasso it! Better luck next time!")

                        if mobDecider >= 60 and mobDecider <= 100:
                            print("You manage to get the donkey's trust and tame it! You have a new friend now!")

                print("Whoa! You found something! It's a " + str(dungeonType) + "!")

                if dungeonType == "castle dungeon":

                    print("You have found a castle dungeon... these are very rare, and dangerous.")
                    print("What do you want to do?")
                    print("1. -explore!")
                    print("2. -leave!")

                    userSelect = input("I will- ")
                    if userSelect == "1":
                        enterDungeon()

                    if userSelect == "2":
                        print("You wisely leave the dungeon alone, perhaps you should gear up first...")

                if dungeonType == "single villager house":
                    print("What do you want to do?")
                    print("1. -loot the house!")
                    print ("2. -trade with the villager!")
                    print ("3. -leave!")

                    userSelect = input("I will- ")
                    if userSelect == "1":
                        lootVillagerHouse()

                    if userSelect == "2":
                        tradeVillagerHouse()

                    if userSelect == "3":
                        print ("You leave the villager house alone for now.")

                if dungeonType == "abandoned camp":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreAbandonedCamp()

                    if userSelect == "2":
                        print("You decide not to look around and return home...")

                if dungeonType == "spawn alter":
                    print("what do you want to do?")
                    print("1. -explore further!")
                    print("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreSpawnAlter()

                    if userSelect == "2":
                        print("You decider to leave the strange alter alone and return home.")

                if dungeonType == "well":
                    print("what do you want to do?")
                    print("1. -explore further!")
                    print("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreWell()

                    if userSelect == "2":
                        print("You decide to leave the well alone and return home.")

                if dungeonType == "small dungeon":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreSmallDungeon()

                    if userSelect == "2":
                        print("You decide not to look inside and return home...")

                if dungeonType == "large rock":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonLargeRock()

                    if userSelect == "2":
                        leaveDungeonLargeRock()


                if dungeonType == "scarecrow":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonScarecrow()

                    if userSelect == "2":
                        leaveDungeonScarecrow()

                if dungeonType == "shallow cave":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreShallowCave()

                    if userSelect == "2":
                        print("You leave the cave be for now and return home.")

                if dungeonType == "tiny mossy cobble structure":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonTinyMoss()

                    if userSelect == "2":
                        leaveDungeonTinyMoss()

                if dungeonType == "pond":
                    print("What do you want to do?")
                    print ("1. -explore further!")
                    print ("2. -leave!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        exploreDungeonPond()

                    if userSelect == "2":
                        leaveDungeonPond()

                if dungeonType == "horse":
                    print("What do you want to do?")
                    print ("1. -hunt the horse!")
                    print ("2. -tame the horse!")
                    print ("3. -leave the horse alone!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        huntDungeonHorse()

                    if userSelect == "2":
                        tameDungeonHorse()

                    if userSelect == "3":
                        print("You leave the horse alone and return home.")

                if dungeonType == "donkey":
                    print("What do you want to do?")
                    print ("1. -hunt the donkey!")
                    print ("2. -tame the donkey!")
                    print ("3. -leave the donkey alone!")

                    userSelect = input("I will-")
                    if userSelect == "1":
                        huntDungeonDonkey()

                    if userSelect == "2":
                        tameDungeonDonkey()

                    if userSelect == "3":
                        print("You leave the donkey alone and return home.")

    print("Please select a location:")
    print ("1. Plains")
    print ("2. Sunflower Fields")

    userSelect = input("Location: ")
    if userSelect == "1":
        locationPlains()

    if userSelect == "2":
        locationSunflowerFields()

print("Please select if the user has art:")
print("1. Yes")
print("2. No")

userSelect = input("Art: ")

if userSelect == "1":
    artTrue()

if userSelect == "2":
    artFalse()
