import random

def woodenPickaxe():
    itemDecider = random.randint(1,100)
    itemType = "Nothing!"

    if itemDecider >= 1 and itemDecider < 20:
        itemType = "Nothing!"

    if itemDecider >= 20 and itemDecider < 40:
        itemType = "cobblestone"

    if itemDecider >= 40 and itemDecider < 60:
        itemType = "andesite"

    if itemDecider >= 60 and itemDecider < 80:
        itemType = "granite"

    if itemDecider >= 80 and itemDecider <= 100:
        itemType = "diortie"

    if itemType == "Nothing!":
        print ("You found nothing! Better Luck next time!")
    else:
        print ("You found " + str(itemType) + ".")

def stonePickaxe():
    itemDecider = random.randint(1, 100)
    itemNumber = 0
    itemType = "Nothing!"

    if itemDecider >= 1 and itemDecider < 45:
        itemNumber = 0

    if itemDecider >= 45 and itemDecider < 75:
        itemType = "coal"
        itemNumber = random.randint(5,10)

    if itemDecider >= 75 and itemDecider < 95:
        itemType = "iron"
        itemNumber = random.randint(1,5)

    if itemDecider >= 95 and itemDecider <= 100:
        itemType = "gold"
        itemNumber = random.randint(1,5)

    if itemNumber == 0:
        print("You found nothing! Better Luck next time!")
    else:
        print ("You find " + str(itemNumber) + " piece(s) of " + str(itemType) + ".")



def ironPickaxe():
    itemDecider = random.randint(1, 100)
    itemNumber = 0
    itemType = "Nothing!"

    if itemDecider >= 1 and itemDecider < 20:
        itemNumber = 0

    if itemDecider >= 20 and itemDecider < 40:
        itemType = "coal"
        itemNumber = random.randint(5,15)

    if itemDecider >= 40 and itemDecider < 60:
        itemType = "iron"
        itemNumber = random.randint(1,10)

    if itemDecider >= 60 and itemDecider < 70:
        itemType = "gold"
        itemNumber = random.randint(1,5)

    if itemDecider >= 70 and itemDecider < 80:
        itemType = "redstone"
        itemNumber = random.randint(5,10)

    if itemDecider >= 80 and itemDecider < 90:
        itemType = "lapis lazuli"
        itemNumber = random.randint(5,10)

    if itemDecider >= 90 and itemDecider < 95:
        itemType = "emerald"
        itemNumber = random.randint(1,2)

    if itemDecider >= 95 and itemDecider <= 100:
        itemType = "diamond"
        itemNumber = random.randint(1,2)

    if itemNumber == 0:
        print ("You found nothing! Better Luck next time!")
    else:
        print ("You find " + str(itemNumber) + " piece(s) of " + str(itemType) + ".")



def goldPickaxe():
    itemDecider = random.randint(1, 100)
    itemNumber = 0
    itemType = "Nothing!"

    if itemDecider >= 1 and itemDecider < 40:
        itemNumber = 0

    if itemDecider >= 40 and itemDecider < 70:
        itemType = "coal"
        itemNumber = random.randint(5,15)

    if itemDecider >= 70 and itemDecider < 90:
        itemType = "iron"
        itemNumber = random.randint(4,10)

    if itemDecider >= 90 and itemDecider <= 100:
        itemType = "gold"
        itemNumber = random.randint(1,10)

    if itemNumber == 0:
        print ("You found nothing! Better Luck next time!")
    else:
        print ("You find " + str(itemNumber) + " piece(s) of " + str(itemType) + ".")



def diamondPickaxe():
    itemDecider = random.randint(1, 100)
    itemNumber = 0
    itemType = "Nothing!"

    if itemDecider >= 1 and itemDecider < 15:
        itemNumber = 0

    if itemDecider >= 15 and itemDecider < 35:
        itemType = "coal"
        itemNumber = random.randint(10,20)

    if itemDecider >= 35 and itemDecider < 55:
        itemType = "iron"
        itemNumber = random.randint(5,15)

    if itemDecider >= 55 and itemDecider < 65:
        itemType = "gold"
        itemNumber = random.randint(5,10)

    if itemDecider >= 65 and itemDecider < 75:
        itemType = "redstone"
        itemNumber = random.randint(5,15)

    if itemDecider >= 75 and itemDecider < 85:
        itemType = "lapis lazuli"
        itemNumber = random.randint(5,15)

    if itemDecider >= 85 and itemDecider < 90:
        itemType = "emerald"
        itemNumber = random.randint(1,4)

    if itemDecider >= 90 and itemDecider <= 95:
        itemType = "diamond"
        itemNumber = random.randint(1,8)

    if itemDecider >= 95 and itemDecider < 98:
        itemType = "obsidian"
        itemNumber = random.randint(1,2)

    if itemDecider >= 98 and itemDecider <=100:
        itemType = "magma block"
        itemNumber = random.randint(1,4)

    if itemNumber == 0:
        print ("You found nothing! Better Luck next time!")
    else:
        print ("You find " + str(itemNumber) + " piece(s) of " + str(itemType) + ".")



print ("Please select a pickaxe:")
print ("1. Wooden Pickaxe")
print ("2. Stone Pickaxe")
print ("3. Iron Pickaxe")
print ("4. Gold Pickaxe")
print ("5. Diamond Pickaxe")

userSelect = input("Pickaxe type: ")
if userSelect == "1":
    woodenPickaxe()

if userSelect == "2":
    stonePickaxe()

if userSelect == "3":
    ironPickaxe()

if userSelect == "4":
    goldPickaxe()

if userSelect == "5":
    diamondPickaxe()
