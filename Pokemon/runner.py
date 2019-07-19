from bank import PokeBank

def moveChanger(pokeNum):
    global bank
    currPokemon = bank.allPokemon[pokeNum]
    print("The current moves of " + currPokemon.name + " are...")
    for i in range(0, 4):
        print("Move number " + str(i+1) + ": " + currPokemon.moves[i].name)
    print("")
    moveNum = input("Which move would you like to change?\n >>> ")
    newMove = input("What's the new move's name?\n >>> ")
    if moveNum == "quit" or newMove == "quit" or moveNum == "q" or newMove == "q":
        return None
    if currPokemon.changeMove(int(moveNum), newMove) == False:
        print("That wasn't a valid move (Did you misspell it?)")
        currPokemon = None
    return currPokemon

def statChanger(pokeNum, statToChange):
    global blank
    currPokemon = bank.allPokemon[pokeNum]
    if statToChange in {"hp", "atk", "def", "spd"}:
        pass
    else:
        print("The current stats of " + currPokemon.name + " are...")
        currPokemon = bank.allPokemon[pokeNum]
        print("HP: " + currPokemon.stats["hp"])
        print("ATK: " + currPokemon.stats["atk"])
        print("DEF: " + currPokemon.stats["def"])
        print("SPD: " + currPokemon.stats["spd"])
        print("")
        print("What stat would you like to change?")
        statToChange = input(">>> ")
    print("What value would you like to change it to?")
    newValue = input(">>> ")
    if statToChange == "quit" or newValue == "quit":
        currPokemon = None
    else:
        if currPokemon.changeStat(statToChange, newValue) == False:
            currPokemon = None
            print("That wasn't a valid stat name.")
    return currPokemon


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

    while(pokeNum != "quit"): #selecting pokemon, or quiting if user says quit
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
    pokeNum = pokeNum-1
    pokeData = bank.allPokemon[pokeNum]

    anythingElse = "y"
    while anythingElse != "n" and anythingElse != "no" and anythingElse != "quit":
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
        #changing various attributes based on user selection
        if dataToChange == "move" or dataToChange == "moves":
            pokeData = moveChanger(pokeNum)
        elif dataToChange in {"stats", "stat", "hp", "atk", "def", "spd", "attack", "defense", "speed"}:
            pokeData = statChanger(pokeNum, dataToChange)

        #Firetail, these are yours! ask the user for what they want to change the pokemone's data to.
        #For the name and species, after you get the input, just do pokeData.changeName(<new name variable>)
        #And  pokeData.changeSpecies(<the species variable>) to change species.
        #Becasue each pokemon can have up to two types, you'll have to ask the user for type1 and type2
        #then, when you have both types, do pokeData.changeType([newType1, newType2]) or whatever you named the variables
        #The [ ] are important, it won't work right without them!
        #I might add some error handling for the types later to make sure they're actually types and
        #not gibberish, but rn there is def nothing stopping you from entering fart type
        elif dataToChange == "name":
            pass#code for changing name
        elif dataToChange == "species":
            pass#code for changing species
        elif dataToChange == "type" or dataToChange == "types":
            pass #code to change type
        #Stop changing code past here

        else:
            print("That wasn't a valid option. (Did you misspell it?)")
            pokeData == None


        if pokeData == None:
            print("Change aborted.")
            break
        else:
            bank.allPokemon[pokeNum] = pokeData
            bank.saveBank()
        print("Anything else you want to change about that Pokemon?")
        anythingElse = input(">>> ")
    print("")



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
