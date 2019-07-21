import random

def swordWooden():

    def haveArt():

        def amountOfLoot(monsterNumber):
            itemNumber = random.randint(1,3)

            if monsterNumber == 2:
                itemNumber = random.randint(6,12)

            if monsterNumber == 3:
                itemNumber = random.randint(12,21)

            if monsterNumber == 4:
                itemNumber = random.randint(21,36)

            return itemNumber


        def locationPlains():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
                monsterType = "zombie(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 3 * monsterNumber
                damageNumber = random.randint(0,3)

                itemType = "rotten flesh"
                itemNumber = random.randint(2,8)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,8)

                if monsterNumber == 3:
                    itemNumber = random.randint(8,12)

                if monsterNumber == 4:
                    itemNumber = random.randint(12,16)




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(2,4)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,6)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print("You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")

        def locationSunflowerFields():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
                monsterType = "zombie(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 3 * monsterNumber
                damageNumber = random.randint(0,3)

                itemType = "rotten flesh"
                itemNumber = random.randint(2,8)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,8)

                if monsterNumber == 3:
                    itemNumber = random.randint(8,12)

                if monsterNumber == 4:
                    itemNumber = random.randint(12,16)




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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
                    itemNumber = 2

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 4



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(2,4)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,6)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")

        def locationTaiga():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
                monsterType = "zombie(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 3 * monsterNumber
                damageNumber = random.randint(0,3)

                itemType = "rotten flesh"
                itemNumber = random.randint(2,8)

                if monsterNumber == 2:
                    itemNumber = random.randint(8,16)

                if monsterNumber == 3:
                    itemNumber = random.randint(16,24)

                if monsterNumber == 4:
                    itemNumber = random.randint(24,32)




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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
                    itemNumber = 2

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 4



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(2,4)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,8)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")


        print ("Please select a location:")
        print ("1. Plains")
        print ("2. Sunflower Plains")
        print ("3. Taiga")

        userSelect = input("Location: ")
        if userSelect == "1":
            locationPlains()

        if userSelect == "2":
            locationSunflowerFields()

        if userSelect == "3":
            locationTaiga()

    def noArt():

        def amountOfLoot(monsterNumber):
            itemNumber = random.randint(1,3)

            if monsterNumber == 2:
                itemNumber = random.randint(3,6)

            if monsterNumber == 3:
                itemNumber = random.randint(6,9)

            if monsterNumber == 4:
                itemNumber = random.randint(9,12)

            return itemNumber


        def locationPlains():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
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




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(1,2)

                if monsterNumber == 2:
                    itemNumber = random.randint(2,3)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print("You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")

        def locationSunflowerFields():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
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




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(1,2)

                if monsterNumber == 2:
                    itemNumber = random.randint(2,3)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")

        def locationTaiga():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 20:
                monsterNumber = 0


            if monsterDecider >= 20 and monsterDecider < 65:
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




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(1,2)

                if monsterNumber == 2:
                    itemNumber = random.randint(2,3)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")


        print ("Please select a location:")
        print ("1. Plains")
        print ("2. Sunflower Plains")
        print ("3. Taiga")

        userSelect = input("Location: ")
        if userSelect == "1":
            locationPlains()

        if userSelect == "2":
            locationSunflowerFields()

        if userSelect == "3":
            locationTaiga()

    print ("Please select if you have art or not:")
    print ("1. I have art")
    print ("2. I have no art")

    userSelect = input("Art: ")
    if userSelect == "1":
        haveArt()

    if userSelect == "2":
        noArt()

def swordStone():

    def haveArt():

        def amountOfLoot(monsterNumber):
            itemNumber = random.randint(1,3)

            if monsterNumber == 2:
                itemNumber = random.randint(6,12)

            if monsterNumber == 3:
                itemNumber = random.randint(12,21)

            if monsterNumber == 4:
                itemNumber = random.randint(21,36)

            return itemNumber


        def locationPlains():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
                monsterType = "zombie(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 3 * monsterNumber
                damageNumber = random.randint(0,3)

                itemType = "rotten flesh"
                itemNumber = random.randint(2,8)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,8)

                if monsterNumber == 3:
                    itemNumber = random.randint(8,12)

                if monsterNumber == 4:
                    itemNumber = random.randint(12,16)




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(2,4)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,6)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print("You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove half a heart of damage.")

        def locationSunflowerFields():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
                monsterType = "zombie(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 3 * monsterNumber
                damageNumber = random.randint(0,3)

                itemType = "rotten flesh"
                itemNumber = random.randint(2,8)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,8)

                if monsterNumber == 3:
                    itemNumber = random.randint(8,12)

                if monsterNumber == 4:
                    itemNumber = random.randint(12,16)




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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
                    itemNumber = 2

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 4



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(2,4)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,6)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove half a heart of damage.")

        def locationTaiga():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
                monsterType = "zombie(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 3 * monsterNumber
                damageNumber = random.randint(0,3)

                itemType = "rotten flesh"
                itemNumber = random.randint(2,8)

                if monsterNumber == 2:
                    itemNumber = random.randint(8,16)

                if monsterNumber == 3:
                    itemNumber = random.randint(16,24)

                if monsterNumber == 4:
                    itemNumber = random.randint(24,32)




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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
                    itemNumber = 2

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 4



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(2,4)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,8)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove half a heart of damage.")


        print ("Please select a location:")
        print ("1. Plains")
        print ("2. Sunflower Plains")
        print ("3. Taiga")

        userSelect = input("Location: ")
        if userSelect == "1":
            locationPlains()

        if userSelect == "2":
            locationSunflowerFields()

        if userSelect == "3":
            locationTaiga()

    def noArt():

        def amountOfLoot(monsterNumber):
            itemNumber = random.randint(1,3)

            if monsterNumber == 2:
                itemNumber = random.randint(3,6)

            if monsterNumber == 3:
                itemNumber = random.randint(6,9)

            if monsterNumber == 4:
                itemNumber = random.randint(9,12)

            return itemNumber


        def locationPlains():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
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




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(1,2)

                if monsterNumber == 2:
                    itemNumber = random.randint(2,3)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print("You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove half a heart of damage.")

        def locationSunflowerFields():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
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




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(1,2)

                if monsterNumber == 2:
                    itemNumber = random.randint(2,3)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove half a heart of damage.")

        def locationTaiga():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 20:
                monsterNumber = 0


            if monsterDecider >= 20 and monsterDecider < 65:
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




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(1,2)

                if monsterNumber == 2:
                    itemNumber = random.randint(2,3)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove half a heart of damage.")


        print ("Please select a location:")
        print ("1. Plains")
        print ("2. Sunflower Plains")
        print ("3. Taiga")

        userSelect = input("Location: ")
        if userSelect == "1":
            locationPlains()

        if userSelect == "2":
            locationSunflowerFields()

        if userSelect == "3":
            locationTaiga()

    print ("Please select if you have art or not:")
    print ("1. I have art")
    print ("2. I have no art")

    userSelect = input("Art: ")
    if userSelect == "1":
        haveArt()

    if userSelect == "2":
        noArt()

def swordIron():

    def haveArt():

        def amountOfLoot(monsterNumber):
            itemNumber = random.randint(1,3)

            if monsterNumber == 2:
                itemNumber = random.randint(6,12)

            if monsterNumber == 3:
                itemNumber = random.randint(12,21)

            if monsterNumber == 4:
                itemNumber = random.randint(21,36)

            return itemNumber


        def locationPlains():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
                monsterType = "zombie(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 3 * monsterNumber
                damageNumber = random.randint(0,3)

                itemType = "rotten flesh"
                itemNumber = random.randint(2,8)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,8)

                if monsterNumber == 3:
                    itemNumber = random.randint(8,12)

                if monsterNumber == 4:
                    itemNumber = random.randint(12,16)




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(2,4)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,6)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print("You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print ("Remove one heart of damage.")

        def locationSunflowerFields():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
                monsterType = "zombie(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 3 * monsterNumber
                damageNumber = random.randint(0,3)

                itemType = "rotten flesh"
                itemNumber = random.randint(2,8)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,8)

                if monsterNumber == 3:
                    itemNumber = random.randint(8,12)

                if monsterNumber == 4:
                    itemNumber = random.randint(12,16)




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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
                    itemNumber = 2

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 4



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(2,4)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,6)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print ("Remove one heart of damage.")

        def locationTaiga():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
                monsterType = "zombie(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 3 * monsterNumber
                damageNumber = random.randint(0,3)

                itemType = "rotten flesh"
                itemNumber = random.randint(2,8)

                if monsterNumber == 2:
                    itemNumber = random.randint(8,16)

                if monsterNumber == 3:
                    itemNumber = random.randint(16,24)

                if monsterNumber == 4:
                    itemNumber = random.randint(24,32)




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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
                    itemNumber = 2

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 4



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(2,4)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,8)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove one heart of damage.")


        print ("Please select a location:")
        print ("1. Plains")
        print ("2. Sunflower Plains")
        print ("3. Taiga")

        userSelect = input("Location: ")
        if userSelect == "1":
            locationPlains()

        if userSelect == "2":
            locationSunflowerFields()

        if userSelect == "3":
            locationTaiga()

    def noArt():

        def amountOfLoot(monsterNumber):
            itemNumber = random.randint(1,3)

            if monsterNumber == 2:
                itemNumber = random.randint(3,6)

            if monsterNumber == 3:
                itemNumber = random.randint(6,9)

            if monsterNumber == 4:
                itemNumber = random.randint(9,12)

            return itemNumber


        def locationPlains():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
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




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(1,2)

                if monsterNumber == 2:
                    itemNumber = random.randint(2,3)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print("You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print ("Remove one heart of damage.")

        def locationSunflowerFields():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
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




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(1,2)

                if monsterNumber == 2:
                    itemNumber = random.randint(2,3)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove one heart of damage.")

        def locationTaiga():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 20:
                monsterNumber = 0


            if monsterDecider >= 20 and monsterDecider < 65:
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




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(1,2)

                if monsterNumber == 2:
                    itemNumber = random.randint(2,3)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove one heart of damage.")


        print ("Please select a location:")
        print ("1. Plains")
        print ("2. Sunflower Plains")
        print ("3. Taiga")

        userSelect = input("Location: ")
        if userSelect == "1":
            locationPlains()

        if userSelect == "2":
            locationSunflowerFields()

        if userSelect == "3":
            locationTaiga()

    print ("Please select if you have art or not:")
    print ("1. I have art")
    print ("2. I have no art")

    userSelect = input("Art: ")
    if userSelect == "1":
        haveArt()

    if userSelect == "2":
        noArt()

def swordGold():

    def haveArt():

        def amountOfLoot(monsterNumber):
            itemNumber = random.randint(1,3)

            if monsterNumber == 2:
                itemNumber = random.randint(6,12)

            if monsterNumber == 3:
                itemNumber = random.randint(12,21)

            if monsterNumber == 4:
                itemNumber = random.randint(21,36)

            return itemNumber


        def locationPlains():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
                monsterType = "zombie(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 3 * monsterNumber
                damageNumber = random.randint(0,3)

                itemType = "rotten flesh"
                itemNumber = random.randint(2,8)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,8)

                if monsterNumber == 3:
                    itemNumber = random.randint(8,12)

                if monsterNumber == 4:
                    itemNumber = random.randint(12,16)




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(2,4)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,6)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print("You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove half a heart of damage.")

        def locationSunflowerFields():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
                monsterType = "zombie(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 3 * monsterNumber
                damageNumber = random.randint(0,3)

                itemType = "rotten flesh"
                itemNumber = random.randint(2,8)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,8)

                if monsterNumber == 3:
                    itemNumber = random.randint(8,12)

                if monsterNumber == 4:
                    itemNumber = random.randint(12,16)




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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
                    itemNumber = 2

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 4



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(2,4)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,6)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove half a heart of damage.")

        def locationTaiga():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
                monsterType = "zombie(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 3 * monsterNumber
                damageNumber = random.randint(0,3)

                itemType = "rotten flesh"
                itemNumber = random.randint(2,8)

                if monsterNumber == 2:
                    itemNumber = random.randint(8,16)

                if monsterNumber == 3:
                    itemNumber = random.randint(16,24)

                if monsterNumber == 4:
                    itemNumber = random.randint(24,32)




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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
                    itemNumber = 2

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 4



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(2,4)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,8)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove half a heart of damage.")


        print ("Please select a location:")
        print ("1. Plains")
        print ("2. Sunflower Plains")
        print ("3. Taiga")

        userSelect = input("Location: ")
        if userSelect == "1":
            locationPlains()

        if userSelect == "2":
            locationSunflowerFields()

        if userSelect == "3":
            locationTaiga()

    def noArt():

        def amountOfLoot(monsterNumber):
            itemNumber = random.randint(1,3)

            if monsterNumber == 2:
                itemNumber = random.randint(3,6)

            if monsterNumber == 3:
                itemNumber = random.randint(6,9)

            if monsterNumber == 4:
                itemNumber = random.randint(9,12)

            return itemNumber


        def locationPlains():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
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




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(1,2)

                if monsterNumber == 2:
                    itemNumber = random.randint(2,3)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print("You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove half a heart of damage.")

        def locationSunflowerFields():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
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




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(1,2)

                if monsterNumber == 2:
                    itemNumber = random.randint(2,3)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove half a heart of damage.")

        def locationTaiga():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 20:
                monsterNumber = 0


            if monsterDecider >= 20 and monsterDecider < 65:
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




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(1,2)

                if monsterNumber == 2:
                    itemNumber = random.randint(2,3)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove half a heart of damage.")


        print ("Please select a location:")
        print ("1. Plains")
        print ("2. Sunflower Plains")
        print ("3. Taiga")

        userSelect = input("Location: ")
        if userSelect == "1":
            locationPlains()

        if userSelect == "2":
            locationSunflowerFields()

        if userSelect == "3":
            locationTaiga()

    print ("Please select if you have art or not:")
    print ("1. I have art")
    print ("2. I have no art")

    userSelect = input("Art: ")
    if userSelect == "1":
        haveArt()

    if userSelect == "2":
        noArt()

def swordDiamond():

    def haveArt():

        def amountOfLoot(monsterNumber):
            itemNumber = random.randint(1,3)

            if monsterNumber == 2:
                itemNumber = random.randint(6,12)

            if monsterNumber == 3:
                itemNumber = random.randint(12,21)

            if monsterNumber == 4:
                itemNumber = random.randint(21,36)

            return itemNumber


        def locationPlains():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
                monsterType = "zombie(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 3 * monsterNumber
                damageNumber = random.randint(0,3)

                itemType = "rotten flesh"
                itemNumber = random.randint(2,8)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,8)

                if monsterNumber == 3:
                    itemNumber = random.randint(8,12)

                if monsterNumber == 4:
                    itemNumber = random.randint(12,16)




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(2,4)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,6)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print("You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove three hearts of damage.")

        def locationSunflowerFields():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
                monsterType = "zombie(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 3 * monsterNumber
                damageNumber = random.randint(0,3)

                itemType = "rotten flesh"
                itemNumber = random.randint(2,8)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,8)

                if monsterNumber == 3:
                    itemNumber = random.randint(8,12)

                if monsterNumber == 4:
                    itemNumber = random.randint(12,16)




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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
                    itemNumber = 2

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 4



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(2,4)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,6)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print ("Remove three hearts of damage.")

        def locationTaiga():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
                monsterType = "zombie(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 3 * monsterNumber
                damageNumber = random.randint(0,3)

                itemType = "rotten flesh"
                itemNumber = random.randint(2,8)

                if monsterNumber == 2:
                    itemNumber = random.randint(8,16)

                if monsterNumber == 3:
                    itemNumber = random.randint(16,24)

                if monsterNumber == 4:
                    itemNumber = random.randint(24,32)




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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
                    itemNumber = 2

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 4



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(2,4)

                if monsterNumber == 2:
                    itemNumber = random.randint(4,8)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove three hearts of damage.")


        print ("Please select a location:")
        print ("1. Plains")
        print ("2. Sunflower Plains")
        print ("3. Taiga")

        userSelect = input("Location: ")
        if userSelect == "1":
            locationPlains()

        if userSelect == "2":
            locationSunflowerFields()

        if userSelect == "3":
            locationTaiga()

    def noArt():

        def amountOfLoot(monsterNumber):
            itemNumber = random.randint(1,3)

            if monsterNumber == 2:
                itemNumber = random.randint(3,6)

            if monsterNumber == 3:
                itemNumber = random.randint(6,9)

            if monsterNumber == 4:
                itemNumber = random.randint(9,12)

            return itemNumber


        def locationPlains():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
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




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(1,2)

                if monsterNumber == 2:
                    itemNumber = random.randint(2,3)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print("You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove three hearts of damage.")

        def locationSunflowerFields():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 45:
                monsterNumber = 0


            if monsterDecider >= 45 and monsterDecider < 65:
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




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(1,2)

                if monsterNumber == 2:
                    itemNumber = random.randint(2,3)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove three hearts of damage.")

        def locationTaiga():
            monsterDecider = random.randint(1, 100)
            monsterNumber = 0
            monsterType = "Nothing!"
            itemNumber = 0
            itemType = "Nothing!"
            expNumber = 0
            damageNumber = 0


            if monsterDecider >= 1 and monsterDecider < 20:
                monsterNumber = 0


            if monsterDecider >= 20 and monsterDecider < 65:
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




            if monsterDecider >= 65 and monsterDecider < 75:
                monsterType = "skeleton(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 4 * monsterNumber
                damageNumber = random.randint(0,4)

                lootNumber = random.randint(1,3)
                if lootNumber == 1:
                    itemType = "arrow(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 2:
                    itemType = "bone(s)"
                    itemNumber = amountOfLoot(monsterNumber)

                if lootNumber == 3:
                    itemType = "broken bow"
                    itemNumber = 1

                    if monsterNumber == 3 or monsterNumber == 4:
                        itemNumber = 2



            if monsterDecider >= 75 and monsterDecider < 85:
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



            if monsterDecider >= 85 and monsterDecider < 95:
                monsterType = "creeper(s)"
                monsterNumber = random.randint(1,4)
                expNumber = 6 * monsterNumber
                damageNumber = random.randint(0,8)

                itemType = "gunpowder"
                itemNumber = amountOfLoot(monsterNumber)



            if monsterDecider >= 95 and monsterDecider <= 100:
                monsterType = "endermon"
                monsterNumber = random.randint(1,2)
                expNumber = 10 * monsterNumber
                damageNumber = random.randint(4,8)

                itemType = "ender pearl"
                itemNumber = random.randint(1,2)

                if monsterNumber == 2:
                    itemNumber = random.randint(2,3)



            if monsterNumber == 0:
                print("You found nothing! Oh well!")
            else:
                print( "You find " + str(monsterNumber) + " " + str(monsterType) + ".")
                print ("They drop " + str(itemNumber) + " " + str(itemType) + ".")


            if expNumber == 0:
                print ("You got no Pixel Points! Oh well!")
            else:
                print ("You got " + str(expNumber) + " Pixel Points!")

            if damageNumber == 0:
                print ("You took no damage! Nice!")
            else:
                print ("You took " + str(damageNumber) + " hearts of damage! Oh no!")
                print("Remove three hearts of damage.")


        print ("Please select a location:")
        print ("1. Plains")
        print ("2. Sunflower Plains")
        print ("3. Taiga")

        userSelect = input("Location: ")
        if userSelect == "1":
            locationPlains()

        if userSelect == "2":
            locationSunflowerFields()

        if userSelect == "3":
            locationTaiga()

    print ("Please select if you have art or not:")
    print ("1. I have art")
    print ("2. I have no art")

    userSelect = input("Art: ")
    if userSelect == "1":
        haveArt()

    if userSelect == "2":
        noArt()

print ("Please select a sword:")
print ("1. Wooden sword")
print ("2. Stone sword")
print ("3. Iron sword")
print ("4. Gold sword")
print ("5. Diamond Sword")

userSelect = input("Sword: ")
if userSelect == "2":
    swordStone()

if userSelect == "3":
    swordIron()

if userSelect == "4":
    swordGold()

if userSelect == "5":
    swordDiamond()

if userSelect == "1":
    swordWooden()
