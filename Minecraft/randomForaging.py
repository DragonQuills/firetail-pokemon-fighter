import random

def woodenShovel():
    itemDecider = random.randint(1,100)
    itemType = "Nothing!"
    itemNumber = random.randint(1,3)

    if itemDecider >= 1 and itemDecider < 20:
        itemType = "Nothing!"

    if itemDecider >= 20 and itemDecider < 30:
        itemType = "wheat seed(s)"

    if itemDecider >= 30 and itemDecider < 40:
        itemType = "wood"
        itemNumber = "some"

    if itemDecider >= 50 and itemDecider < 60:
        itemType = "apple(s)"

    if itemDecider >= 60 and itemDecider < 70:
        itemType = "poisonous potato(s)"

    if itemDecider >= 70 and itemDecider < 80:
        itemType = "feather(s)"

    if itemDecider >= 80 and itemDecider < 90:
        itemType = "flint"

    if itemDecider >= 90 and itemDecider <= 100:
        itemType = "dandelion(s)"

    if itemType == "Nothing!":
        print ("You found nothing! Better Luck next time!")
    else:
        print ("You found " + str(itemNumber) + " " + str(itemType) + ".")

def stoneShovel():
    itemDecider = random.randint(1, 100)
    itemNumber = 0
    itemType = "Nothing!"

    if itemDecider >= 1 and itemDecider < 20:
        itemType = "Nothing!"

    if itemDecider >= 20 and itemDecider < 30:
        itemType = "wheat seed(s)"
        itemNumber = random.randint(1,5)

    if itemDecider >= 3 and itemDecider < 35:
        itemType = "wood"
        itemNumber = "some"

    if itemDecider >= 35 and itemDecider < 40:
        itemType = "apple(s)"
        itemNumber = random.randint(1,5)

    if itemDecider >= 40 and itemDecider < 45:
        itemType = "poisonous potato(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 45 and itemDecider < 50:
        itemType = "feather(s)"
        itemNumber  = random.randint(1,5)

    if itemDecider >= 50 and itemDecider < 55:
        itemType = "flint"
        itemNumber = random.randint(1,4)

    if itemDecider >= 55 and itemDecider < 60:
        itemType = "charcoal"
        itemNumber = random.randint(1,5)

    if itemDecider >= 60 and itemDecider < 65:
        itemType = "dandelion(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 65 and itemDecider < 70:
        itemType = "beetroot seed(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 70 and itemDecider < 75:
        itemType = "carrot(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 75 and itemDecider < 80:
        itemType = "egg(s)"
        itemNumber = random.randint(1,4)

    if itemDecider >= 80 and itemDecider < 85:
        itemType = "potato(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 85 and itemDecider < 90:
        itemType = "sugar cane"
        itemNumber = random.randint(1,2)

    if itemDecider >= 90 and itemDecider < 95:
        itemType = "clay"
        itemNumber = random.randint(1,3)

    if itemDecider >= 95 and itemDecider <= 100:
        itemType = "poppy(s)"
        itemNumber = random.randint(1,3)

    if itemNumber == 0:
        print("You found nothing! Better Luck next time!")
    else:
        print ("You find " + str(itemNumber) + " " + str(itemType) + ".")



def ironShovel():

    itemDecider = random.randint(1,100)
    itemType = "Nothing!"
    itemNumebr = 0

    if itemDecider >= 1 and itemDecider < 20:
        itemType = "Nothing!"

    if itemDecider >= 20 and itemDecider < 30:
        itemType = "wheat seed(s)"
        itemNumber = random.randint(1,8)

    if itemDecider >= 30 and itemDecider < 35:
        itemType = "wood"
        itemNumber = "some"

    if itemDecider >= 35 and itemDecider < 40:
        itemType = "apple(s)"
        itemNumber = random.randint(1,8)

    if itemDecider >= 40 and itemDecider < 45:
        itemType = "poisonous potato(s)"
        itemNumber = random.randint(1,5)

    if itemDecider >= 45 and itemDecider < 50:
        itemType = "feather(s)"
        itemNumber  = random.randint(1,8)

    if itemDecider >= 50 and itemDecider < 55:
        itemType = "flint"
        itemNumber = random.randint(1,6)

    if itemDecider >= 55 and itemDecider < 60:
        itemType = "charcoal"
        itemNumber = random.randint(1,7)

    if itemDecider >= 60 and itemDecider < 65:
        itemType = "dandelion(s)"
        itemNumber = random.randint(1,4)

    if itemDecider >= 65 and itemDecider < 70:
        itemType = "beetroot seed(s)"
        itemNumber = random.randint(1,5)

    if itemDecider >= 70 and itemDecider < 75:
        itemType = "carrot(s)"
        itemNumber = random.randint(1,5)

    if itemDecider >= 75 and itemDecider < 80:
        itemType = "egg(s)"
        itemNumber = random.randint(1,6)

    if itemDecider >= 80 and itemDecider < 85:
        itemType = "potato(s)"
        itemNumber = random.randint(1,6)

    if itemDecider >= 85 and itemDecider < 90:
        itemType = "sugar cane"
        itemNumber = random.randint(1,4)

    if itemDecider >= 90 and itemDecider < 95:
        itemType = "clay"
        itemNumber = random.randint(1,5)

    if itemDecider >= 95 and itemDecider <= 100:
        itemType = "poppy(s)"
        itemNumber = random.randint(1,4)


    if itemNumber == 0:
        print ("You found nothing! Better Luck next time!")
    else:
        print ("You find " + str(itemNumber) + " " + str(itemType) + ".")



def goldShovel():
    itemDecider = random.randint(1, 100)
    itemNumber = 0
    itemType = "Nothing!"

    if itemDecider >= 1 and itemDecider < 20:
        itemType = "Nothing!"

    if itemDecider >= 20 and itemDecider < 30:
        itemType = "wheat seed(s)"
        itemNumber = random.randint(1,5)

    if itemDecider >= 30 and itemDecider < 35:
        itemType = "wood"
        itemNumber = "some"

    if itemDecider >= 35 and itemDecider < 40:
        itemType = "apple(s)"
        itemNumber = random.randint(1,5)

    if itemDecider >= 40 and itemDecider < 45:
        itemType = "poisonous potato(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 45 and itemDecider < 50:
        itemType = "feather(s)"
        itemNumber  = random.randint(1,5)

    if itemDecider >= 50 and itemDecider < 55:
        itemType = "flint"
        itemNumber = random.randint(1,4)

    if itemDecider >= 55 and itemDecider < 60:
        itemType = "charcoal"
        itemNumber = random.randint(1,5)

    if itemDecider >= 60 and itemDecider < 65:
        itemType = "dandelion(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 65 and itemDecider < 70:
        itemType = "beetroot seed(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 70 and itemDecider < 75:
        itemType = "carrot(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 75 and itemDecider < 80:
        itemType = "egg(s)"
        itemNumber = random.randint(1,4)

    if itemDecider >= 80 and itemDecider < 85:
        itemType = "potato(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 85 and itemDecider < 90:
        itemType = "sugar cane"
        itemNumber = random.randint(1,2)

    if itemDecider >= 90 and itemDecider < 95:
        itemType = "clay"
        itemNumber = random.randint(1,3)

    if itemDecider >= 95 and itemDecider <= 100:
        itemType = "poppy(s)"
        itemNumber = random.randint(1,3)


    if itemNumber == 0:
        print ("You found nothing! Better Luck next time!")
    else:
        print ("You find " + str(itemNumber) + " " + str(itemType) + ".")



def diamondShovel():
    itemDecider = random.randint(1, 100)
    itemNumber = 0
    itemType = "Nothing!"

    if itemDecider >= 1 and itemDecider < 3:
        itemType = "Nothing!"

    if itemDecider >= 3 and itemDecider < 5:
        itemType = "wheat seed(s)"
        itemNumber = random.randint(1,5)

    if itemDecider >= 5 and itemDecider < 10:
        itemType = "wood"
        itemNumber = "some"

    if itemDecider >= 10 and itemDecider < 15:
        itemType = "apple(s)"
        itemNumber = random.randint(1,5)

    if itemDecider >= 15 and itemDecider < 20:
        itemType = "poisonous potato(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 20 and itemDecider < 25:
        itemType = "feather(s)"
        itemNumber  = random.randint(1,5)

    if itemDecider >= 25 and itemDecider < 30:
        itemType = "flint"
        itemNumber = random.randint(1,4)

    if itemDecider >= 30 and itemDecider < 35:
        itemType = "charcoal"
        itemNumber = random.randint(1,5)

    if itemDecider >= 35 and itemDecider < 40:
        itemType = "dandelion(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 40 and itemDecider < 45:
        itemType = "beetroot seed(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 45 and itemDecider < 50:
        itemType = "carrot(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 50 and itemDecider < 55:
        itemType = "egg(s)"
        itemNumber = random.randint(1,4)

    if itemDecider >= 55 and itemDecider < 60:
        itemType = "potato(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 60 and itemDecider < 65:
        itemType = "sugar cane"
        itemNumber = random.randint(1,2)

    if itemDecider >= 65 and itemDecider < 70:
        itemType = "clay"
        itemNumber = random.randint(1,3)

    if itemDecider >= 70 and itemDecider <= 78:
        itemType = "poppy(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 78 and itemDecider <= 80:
        itemType = "ender pearl(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 80 and itemDecider <= 85:
        itemType = "bone(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 85 and itemDecider <= 90:
        itemType = "pumpkin seed(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 90 and itemDecider <= 95:
        itemType = "red mushroom(s)"
        itemNumber = random.randint(1,3)

    if itemDecider >= 95 and itemDecider <= 100:
        itemType = "brown mushroom(s)"
        itemNumber = random.randint(1,3)


    if itemNumber == 0:
        print ("You found nothing! Better Luck next time!")
    else:
        print ("You find " + str(itemNumber) + " " + str(itemType) + ".")



print ("Please select a Shovel:")
print ("1. Wooden Shovel")
print ("2. Stone Shovel")
print ("3. Iron Shovel")
print ("4. Gold Shovel")
print ("5. Diamond Shovel")

userSelect = input("Shovel type: ")
if userSelect == "1":
    woodenShovel()

if userSelect == "2":
    stoneShovel()

if userSelect == "3":
    ironShovel()

if userSelect == "4":
    goldShovel()

if userSelect == "5":
    diamondShovel()
