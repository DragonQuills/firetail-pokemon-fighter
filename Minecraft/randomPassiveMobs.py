import random

def haveArt():
    def locationPlains():
        mobDecider = random.randint(1, 100)
        mobNumber = 0
        mobType = "Nothing!"

        if mobDecider >= 1 and mobDecider < 20:
            mobNumber = 0

        if mobDecider >= 20 and mobDecider < 50:
            mobType = "pig(s)"
            mobNumber = random.randint(1,4)

        if mobDecider >= 50 and mobDecider < 70:
            mobType = "cow(s)"
            mobNumber = random.randint(1,3)

        if mobDecider >= 70 and mobDecider < 85:
            mobType = "sheep"
            mobNumber = random.randint(1,4)

        if mobDecider >= 85 and mobDecider < 95:
            mobType = "chicken(s)"
            mobNumber = random.randint(1,3)

        if mobDecider >= 95 and mobDecider <= 100:
            mobType = "horse(s)"
            mobNumber = random.randint(1,2)

        if mobNumber == 0:
            print("You found nothing! Oh welL!")
        else:
            print("You found " + str(mobNumber) + " " + str(mobType) + "!")


            def huntMob():
                expNumber = 0
                mobDropNumber = 0
                mobDrop = "Nothing!"

                if mobType == "cow(s)":

                    lootNumber = random.randint(1,2)
                    if lootNumber == 1:
                        mobDropNumber = randint(1,3)
                        mobDrop = "raw beef"

                    if lootNumber == 2:
                        mobDropNumber = random.randint(1,3)
                        mobDrop = "leather"

                    expNumber = random.randint(1,5)


                if mobType == "cow(s)":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " " + str(mobDrop) + " and " + str(expNumber) + " Pixel Point(s).")

                if mobType == "pig(s)":

                    expNumber = random.randint(1,5)

                if mobType == "pig(s)":
                    print("You slay the creature(s) with your sword and gain some raw porchops and " + str(expNumber) + " Pixel Point(s).")

                if mobType == "sheep":

                    lootNumber = random.randint(1,2)
                    if lootNumber == 1:
                        mobDropNumber = random.randint(1,3)
                        mobDrop = "raw mutton"

                    if lootNumber == 2:
                        mobDropNumber = random.randint(1,3)
                        mobDrop = "white wool"

                    expNumber = random.randint(1,5)

                if mobType == "sheep":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " " + str(mobDrop) + " and " + str(expNumber) + " Pixel Point(s).")

                if mobType == "chicken(s)":

                    lootNumber = random.randint(1,3)
                    if lootNumber == 1:
                        mobDropNumber = random.randint(1,3)
                        mobDrop = "raw chicken"

                    if lootNumber == 2:
                        mobDropNumber = random.randint(1,4)
                        mobDrop = "feather(s)"

                    if lootNumber == 3:
                        mobDropNumber = random.randint(1,2)
                        mobDrop = "egg(s)"

                    expNumber = random.randint(1,3)

                if mobType == "chicken(s)":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " " + str(mobDrop) + " and " + str(expNumber) + " Pixel Point(s).")


                if mobType == "horse(s)":

                    mobDropNumber = random.randint(1,4)

                    expNumber = random.randint(3,8)

                if mobType == "horse(s)":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " leather and " + str(expNumber) + " Pixel Point(s)")

            def tameMob():
                mobTameResults = random.randint(1,100)

                if mobTameResults >= 1 and mobTameResults < 70:
                    print ("The creature does not trust you and gets away before you can lasso them! Oh well!")

                if mobTameResults >= 70 and mobTameResults <= 100:
                    print("You tame the creature! Take good care of your new friend!")

            def leaveMob():
                print("You leave the mob alone and continue on your way.")

            print("What do you want to do?")
            print ("1. -hunt the creature(s)!")
            print ("2. -tame (one of) the creature(s)!")
            print ("3. -leave the creature(s) alone!")

            userSelect = input("I will-")
            if userSelect == "1":
                huntMob()

            if userSelect == "2":
                tameMob()

            if userSelect == "3":
                leaveMob()

    def locationSunflowerFields():
        mobDecider = random.randint(1, 100)
        mobNumber = 0
        mobType = "Nothing!"

        if mobDecider >= 1 and mobDecider < 35:
            mobNumber = 0

        if mobDecider >= 35 and mobDecider < 45:
            mobType = "pig(s)"
            mobNumber = random.randint(1,4)

        if mobDecider >= 45 and mobDecider < 55:
            mobType = "cow(s)"
            mobNumber = random.randint(1,3)

        if mobDecider >= 55 and mobDecider < 65:
            mobType = "sheep"
            mobNumber = random.randint(1,4)

        if mobDecider >= 65 and mobDecider < 85:
            mobType = "chicken(s)"
            mobNumber = random.randint(1,3)

        if mobDecider >= 85 and mobDecider <= 95:
            mobType = "horse(s)"
            mobNumber = random.randint(1,4)

        if mobDecider >= 95 and mobDecider <= 100:
            mobType = "donkey(s)"
            mobNumber = random.randint(1,2)

        if mobNumber == 0:
            print("You found nothing! Oh welL!")
        else:
            print("You found " + str(mobNumber) + " " + str(mobType) + "!")


            def huntMob():
                expNumber = 0
                mobDropNumber = 0
                mobDrop = "Nothing!"

                if mobType == "cow(s)":

                    lootNumber = random.randint(1,2)
                    if lootNumber == 1:
                        mobDropNumber = "some"
                        mobDrop = "raw beef"

                    if lootNumber == 2:
                        mobDropNumber = random.randint(1,3)
                        mobDrop = "leather"

                    expNumber = random.randint(1,5)


                if mobType == "cow(s)":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " " + str(mobDrop) + " and " + str(expNumber) + " Pixel Point(s).")

                if mobType == "pig(s)":

                    expNumber = random.randint(1,5)

                if mobType == "pig(s)":
                    print("You slay the creature(s) with your sword and gain some raw porchops and " + str(expNumber) + " Pixel Point(s).")

                if mobType == "sheep":

                    lootNumber = random.randint(1,2)
                    if lootNumber == 1:
                        mobDropNumber = "some"
                        mobDrop = "raw mutton"

                    if lootNumber == 2:
                        mobDropNumber = random.randint(1,3)
                        mobDrop = "white wool"

                    expNumber = random.randint(1,5)

                if mobType == "sheep":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " " + str(mobDrop) + " and " + str(expNumber) + " Pixel Point(s).")

                if mobType == "chicken(s)":

                    lootNumber = random.randint(1,3)
                    if lootNumber == 1:
                        mobDropNumber = "a(a few)"
                        mobDrop = "raw chicken"

                    if lootNumber == 2:
                        mobDropNumber = random.randint(1,4)
                        mobDrop = "feather(s)"

                    if lootNumber == 3:
                        mobDropNumber = random.randint(1,2)
                        mobDrop = "egg(s)"

                    expNumber = random.randint(1,3)

                if mobType == "chicken(s)":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " " + str(mobDrop) + " and " + str(expNumber) + " Pixel Point(s).")


                if mobType == "horse(s)":

                    mobDropNumber = random.randint(1,4)

                    expNumber = random.randint(3,8)

                if mobType == "horse(s)":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " leather and " + str(expNumber) + " Pixel Point(s)")

                if mobType == "donkey(s)":

                    mobDropNumber = random.randint(1,4)

                    expNumber = random.randint(3,8)

                if mobType == "donkey(s)":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " leather and " + str(expNumber) + " Pixel Point(s)")


            def tameMob():
                mobTameResults = random.randint(1,100)

                if mobTameResults >= 1 and mobTameResults < 70:
                    print ("The creature does not trust you and gets away before you can lasso them! Oh well!")

                if mobTameResults >= 70 and mobTameResults <= 100:
                    print("You tame the creature! Take good care of your new friend!")

            def leaveMob():
                print("You leave the mob alone and continue on your way.")

            print("What do you want to do?")
            print ("1. -hunt the creature(s)!")
            print ("2. -tame (one of) the creature(s)!")
            print ("3. -leave the creature(s) alone!")

            userSelect = input("I will-")
            if userSelect == "1":
                huntMob()

            if userSelect == "2":
                tameMob()

            if userSelect == "3":
                leaveMob()

    print ("Please select a location:")
    print ("1. Plains")
    print ("2. Sunflower Plains")

    userSelect = input("Location: ")
    if userSelect == "1":
        locationPlains()

    if userSelect == "2":
        locationSunflowerFields()


def noArt():
    def locationPlains():
        mobDecider = random.randint(1, 100)
        mobNumber = 0
        mobType = "Nothing!"

        if mobDecider >= 1 and mobDecider < 20:
            mobNumber = 0

        if mobDecider >= 20 and mobDecider < 50:
            mobType = "pig(s)"
            mobNumber = random.randint(1,4)

        if mobDecider >= 50 and mobDecider < 70:
            mobType = "cow(s)"
            mobNumber = random.randint(1,3)

        if mobDecider >= 70 and mobDecider < 85:
            mobType = "sheep"
            mobNumber = random.randint(1,4)

        if mobDecider >= 85 and mobDecider < 95:
            mobType = "chicken(s)"
            mobNumber = random.randint(1,3)

        if mobDecider >= 95 and mobDecider <= 100:
            mobType = "horse(s)"
            mobNumber = random.randint(1,2)

        if mobNumber == 0:
            print("You found nothing! Oh welL!")
        else:
            print("You found " + str(mobNumber) + " " + str(mobType) + "!")


            def huntMob():
                expNumber = 0
                mobDropNumber = 0
                mobDrop = "Nothing!"

                if mobType == "cow(s)":

                    lootNumber = random.randint(1,2)
                    if lootNumber == 1:
                        mobDropNumber = "some"
                        mobDrop = "raw beef"

                    if lootNumber == 2:
                        mobDropNumber = random.randint(1,3)
                        mobDrop = "leather"

                    expNumber = random.randint(1,5)


                if mobType == "cow(s)":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " " + str(mobDrop) + " and " + str(expNumber) + " Pixel Point(s).")

                if mobType == "pig(s)":

                    expNumber = random.randint(1,5)

                if mobType == "pig(s)":
                    print("You slay the creature(s) with your sword and gain some raw porchops and " + str(expNumber) + " Pixel Point(s).")

                if mobType == "sheep":

                    lootNumber = random.randint(1,2)
                    if lootNumber == 1:
                        mobDropNumber = random.randint(1,3)
                        mobDrop = "raw mutton"

                    if lootNumber == 2:
                        mobDropNumber = random.randint(1,3)
                        mobDrop = "white wool"

                    expNumber = random.randint(1,5)

                if mobType == "sheep":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " " + str(mobDrop) + " and " + str(expNumber) + " Pixel Point(s).")

                if mobType == "chicken(s)":

                    lootNumber = random.randint(1,3)
                    if lootNumber == 1:
                        mobDropNumber = "a(a few)"
                        mobDrop = "raw chicken"

                    if lootNumber == 2:
                        mobDropNumber = random.randint(1,4)
                        mobDrop = "feather(s)"

                    if lootNumber == 3:
                        mobDropNumber = random.randint(1,2)
                        mobDrop = "egg(s)"

                    expNumber = random.randint(1,3)

                if mobType == "chicken(s)":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " " + str(mobDrop) + " and " + str(expNumber) + " Pixel Point(s).")


                if mobType == "horse(s)":

                    mobDropNumber = random.randint(1,4)

                    expNumber = random.randint(3,8)

                if mobType == "horse(s)":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " leather and " + str(expNumber) + " Pixel Point(s)")

            def tameMob():
                mobTameResults = random.randint(1,100)

                if mobTameResults >= 1 and mobTameResults < 70:
                    print ("The creature does not trust you and gets away before you can lasso them! Oh well!")

                if mobTameResults >= 70 and mobTameResults <= 100:
                    print("You tame the creature! Take good care of your new friend!")

            def leaveMob():
                print("You leave the mob alone and continue on your way.")

            print("What do you want to do?")
            print ("1. -hunt the creature(s)!")
            print ("2. -tame (one of) the creature(s)!")
            print ("3. -leave the creature(s) alone!")

            userSelect = input("I will-")
            if userSelect == "1":
                huntMob()

            if userSelect == "2":
                tameMob()

            if userSelect == "3":
                leaveMob()

    def locationSunflowerFields():
        mobDecider = random.randint(1, 100)
        mobNumber = 0
        mobType = "Nothing!"

        if mobDecider >= 1 and mobDecider < 35:
            mobNumber = 0

        if mobDecider >= 35 and mobDecider < 45:
            mobType = "pig(s)"
            mobNumber = random.randint(1,4)

        if mobDecider >= 45 and mobDecider < 55:
            mobType = "cow(s)"
            mobNumber = random.randint(1,3)

        if mobDecider >= 55 and mobDecider < 65:
            mobType = "sheep"
            mobNumber = random.randint(1,4)

        if mobDecider >= 65 and mobDecider < 85:
            mobType = "chicken(s)"
            mobNumber = random.randint(1,3)

        if mobDecider >= 85 and mobDecider <= 95:
            mobType = "horse(s)"
            mobNumber = random.randint(1,4)

        if mobDecider >= 95 and mobDecider <= 100:
            mobType = "donkey(s)"
            mobNumber = random.randint(1,2)

        if mobNumber == 0:
            print("You found nothing! Oh welL!")
        else:
            print("You found " + str(mobNumber) + " " + str(mobType) + "!")


            def huntMob():
                expNumber = 0
                mobDropNumber = 0
                mobDrop = "Nothing!"

                if mobType == "cow(s)":

                    lootNumber = random.randint(1,2)
                    if lootNumber == 1:
                        mobDropNumber = "some"
                        mobDrop = "raw beef"

                    if lootNumber == 2:
                        mobDropNumber = random.randint(1,3)
                        mobDrop = "leather"

                    expNumber = random.randint(1,5)


                if mobType == "cow(s)":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " " + str(mobDrop) + " and " + str(expNumber) + " Pixel Point(s).")

                if mobType == "pig(s)":

                    expNumber = random.randint(1,5)

                if mobType == "pig(s)":
                    print("You slay the creature(s) with your sword and gain some raw porchops and " + str(expNumber) + " Pixel Point(s).")

                if mobType == "sheep":

                    lootNumber = random.randint(1,2)
                    if lootNumber == 1:
                        mobDropNumber = "some"
                        mobDrop = "raw mutton"

                    if lootNumber == 2:
                        mobDropNumber = random.randint(1,3)
                        mobDrop = "white wool"

                    expNumber = random.randint(1,5)

                if mobType == "sheep":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " " + str(mobDrop) + " and " + str(expNumber) + " Pixel Point(s).")

                if mobType == "chicken(s)":

                    lootNumber = random.randint(1,3)
                    if lootNumber == 1:
                        mobDropNumber = "a(a few)"
                        mobDrop = "raw chicken"

                    if lootNumber == 2:
                        mobDropNumber = random.randint(1,4)
                        mobDrop = "feather(s)"

                    if lootNumber == 3:
                        mobDropNumber = random.randint(1,2)
                        mobDrop = "egg(s)"

                    expNumber = random.randint(1,3)

                if mobType == "chicken(s)":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " " + str(mobDrop) + " and " + str(expNumber) + " Pixel Point(s).")


                if mobType == "horse(s)":

                    mobDropNumber = random.randint(1,4)

                    expNumber = random.randint(3,8)

                if mobType == "horse(s)":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " leather and " + str(expNumber) + " Pixel Point(s)")

                if mobType == "donkey(s)":

                    mobDropNumber = random.randint(1,4)

                    expNumber = random.randint(3,8)

                if mobType == "donkey(s)":
                    print("You slay the creature(s) with your sword and gain " + str(mobDropNumber) + " leather and " + str(expNumber) + " Pixel Point(s)")


            def tameMob():
                mobTameResults = random.randint(1,100)

                if mobTameResults >= 1 and mobTameResults < 70:
                    print ("The creature does not trust you and gets away before you can lasso them! Oh well!")

                if mobTameResults >= 70 and mobTameResults <= 100:
                    print("You tame the creature! Take good care of your new friend!")

            def leaveMob():
                print("You leave the mob alone and continue on your way.")

            print("What do you want to do?")
            print ("1. -hunt the creature(s)!")
            print ("2. -tame (one of) the creature(s)!")
            print ("3. -leave the creature(s) alone!")

            userSelect = input("I will-")
            if userSelect == "1":
                huntMob()

            if userSelect == "2":
                tameMob()

            if userSelect == "3":
                leaveMob()

    print ("Please select a location:")
    print ("1. Plains")
    print ("2. Sunflower Plains")

    userSelect = input("Location: ")
    if userSelect == "1":
        locationPlains()

    if userSelect == "2":
        locationSunflowerFields()


print("Do you have art?")
print("1. Yes they have art")
print("2. No they do not have art")

userSelect = input("Art: ")
if userSelect == "1":
    haveArt()

if userSelect == "2":
    noArt()
