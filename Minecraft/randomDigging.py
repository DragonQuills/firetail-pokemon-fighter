import random

def locationPlains():
    itemDecider = random.randint(1,100)
    itemType = "Nothing!"
    itemNumber = 0

    if itemDecider >= 1 and itemDecider < 20:
        itemType = "Nothing!"
        itemNumber = 0

    if itemDecider >= 20 and itemDecider < 40:
        itemType = "dirt"
        itemNumber = "some"

    if itemDecider >= 40 and itemDecider < 60:
        itemType = "coarse dirt"
        itemNumber = "some"

    if itemDecider >= 60 and itemDecider < 80:
        itemType = "gravel"
        itemNumber = "some"

    if itemDecider >= 80 and itemDecider <= 100:
        itemType = "sand"
        itemNumber = random.randint(1,5)

    if itemType == "Nothing!":
        print ("You found nothing! Better Luck next time!")
    else:
        print ("You found " + str(itemNumber) + " " + str(itemType) + ".")

print ("Please select a loaction:")
print ("1. Plains")

userSelect = input("Location: ")
if userSelect == "1":
    locationPlains()
