import random

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
            damageNumber = random.randint(0,8)

            itemType = "ender pearl"
            itemNumber = random.randint(1,2)

            if monsterNumber == 2:
                itemNumber = random.randint(2,3)



        if monsterNumber == 0:
            print "You found nothing! Oh well!"
        else:
            print "You find " + str(monsterNumber) + " " + str(monsterType) + "."
            print "They drop " + str(itemNumber) + " " + str(itemType) + "."


        if expNumber == 0:
            print "You got no Pixel Points! Oh well!"
        else:
            print "You got " + str(expNumber) + " Pixel Points!"

        if damageNumber == 0:
            print "You took no damage! Nice!"
        else:
            print "You took " + str(damageNumber) + " hearts of damage! Oh no!"

def locationSunflowerPlains():
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
            damageNumber = random.randint(0,8)

            itemType = "ender pearl"
            itemNumber = random.randint(1,2)

            if monsterNumber == 2:
                itemNumber = random.randint(2,3)



        if monsterNumber == 0:
            print "You found nothing! Oh well!"
        else:
            print "You find " + str(monsterNumber) + " " + str(monsterType) + "."
            print "They drop " + str(itemNumber) + " " + str(itemType) + "."


        if expNumber == 0:
            print "You got no Pixel Points! Oh well!"
        else:
            print "You got " + str(expNumber) + " Pixel Points!"

        if damageNumber == 0:
            print "You took no damage! Nice!"
        else:
            print "You took " + str(damageNumber) + " hearts of damage! Oh no!"


print "Please select a location:"
print "1. Plains"
print "2. Sunflower Plains"

userSelect = input("Location: ")
if userSelect == 1:
    locationPlains()

if userSelect == 2:
    locationSunflowerPlains()
