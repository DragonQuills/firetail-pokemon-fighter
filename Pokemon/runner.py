from bank import PokeBank

def moveChanger(pokeNum):
    global bank
    currPokemon = bank.allPokemon[pokeNum]
    print("You're changing the moves of " + currPokemon.name)


def newPokemon():
    global bank
    newName = None
    species = None
    stats = [0, 0, 0, 0]
    type1 = None
    type2 = None
    moves = ["", "", "", ""]
    allCorrect = "n"
    print ("Got it, create a new Pokeon.")

    while allCorrect != "y":
        print ("Please enter their name.")
        newName = input(">>> ")
        print ("Please enter " + newName + "'s species.")
        species = input(">>> ")
        print("Please enter " + newName + "'s 1st type.")
        type1 = input(">>> ")
        print("Please enter " + newName + "'s 2nd type (or just hit enter if not applicable)")
        type2 = input(">>> ")
        print ("Please enter " + newName + "'s stats.")
        stats[0] = input("HP: ")
        stats[1] = input("Attack: ")
        stats[2] = input("Defense: ")
        stats[3] = input("Speed: ")
        for i in range(0, 4):
            print("Please enter move number " + str(i+1) + " or hit enter to leave it blank.")
            moves[i] = input(">>> ")
        print("")
        print("Here's the info you gave me...")
        print("")
        print("Name: " + newName)
        print("Species: " + species)
        print("Type 1: " + type1)
        if(type2 == ""):
            print("Type 2: N/A")
        else:
            print("Type 2: " + type2)
        print("HP: " + stats[0])
        print("ATK: " + stats[1])
        print("DEF: " + stats[2])
        print("SPD: " + stats[3])
        for i in range(0, 4):
            print("Move number " + str(i+1) + ": " + moves[i])
        print("")
        print("Is that all correct?")
        allCorrect = input(">>> ")
        if len(allCorrect) > 0:
            allCorrect = allCorrect[0].lower()
    print("I'm creating your Pokemon now. This might take a sec, hold on...")
    bank.addPokemon(newName, species, [type1, type2], stats, moves)
    bank.saveBank()
    print("Got all that! Your new Pokemon has been created.")
    print("")
    return

def changePokemon():
    global bank
    pokeList = bank.getAllNames()
    pokeNum = " "
    pokeData = ""
    while(pokeNum != "quit"):
        print("Which Pokemon would you like to change? (Enter their number)")
        for i in range(0, len(pokeList)):
            print(str(i+1) + ". " + pokeList[i])
        pokeNum = input(">>> ")
        try:
            pokeNum = int(pokeNum)
            break
        except:
            if pokeNum == "quit":
                return
            print("Please enter the number of the Pokemon, NOT their name")
            continue
    pokeData = bank.allPokemon[pokeNum-1]

    print("Here's the current data on that Pokemon...")
    print("")
    print("Name: " + pokeData.name)
    print("Species: " + pokeData.species)
    print("Type 1: " + pokeData.types[0])
    if(pokeData.types[1] == ""):
        print("Type 2: N/A")
    else:
        print("Type 2: " + pokeData.types[1])
    print("HP: " + pokeData.stats["hp"])
    print("ATK: " + pokeData.stats["atk"])
    print("DEF: " + pokeData.stats["def"])
    print("SPD: " + pokeData.stats["spd"])
    for i in range(0, 4):
        print("Move number " + str(i+1) + ": " + pokeData.moves[i].name)
    print("")
    print("What would you like to change about " + pokeData.name + "?")
    dataToChange = input(">>> ")
    dataToChange = dataToChange.lower()
    print("")
    if dataToChange == "move" or dataToChange == "moves":
        moveChanger(pokeNum-1)
    elif dataToChange == "stats" or dataToChange == "stat":
        statChange(pokenum-1)
    elif dataToChange == "name":
        pass#code for changing name
    elif dataToChange == "species":
        pass#code for changing Species
    elif dataToChange == "type" or dataToChange == "types":
        pass #code to change type



bank = PokeBank("realBankFile.txt")
bank.loadBank()
choice = "0"
print("Welcome Firetail!")
while choice != "3" and choice != "quit" and choice != "exit":
    print ("What would you like to do?")
    print ("1. Create a new Pokemon")
    print ("2. Change something about an existing Pokemon")
    print ("3. Quit")
    choice = input(">>> ")
    print("")

    if(choice == "1"):
        newPokemon()
    elif(choice == "2"):
        changePokemon()
bank.saveBank()
print("Great, see you again soon!")
