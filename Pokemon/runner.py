from pokemonClass import Pokemon

def newPokemon():
    print ("Got it, create a new Pokeon.")
    newName = None
    species = None
    stats = [0, 0, 0, 0]
    type1 = None
    type2 = None
    moves = ["", "", "", ""]
    allCorrect = "n"

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

    print("Got all that! Your new Pokemon has been created.")
    print("")
    return




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
print("Great, see you again soon!")
